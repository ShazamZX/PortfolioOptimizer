import pandas as pd
import numpy as np
from scipy.optimize import minimize
import json

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

class MarkowitzPortfolioOptimizer:
  
    def __init__(self, data):
        self.data = data
        self.returns = np.arange(0,1,0.01)
        self.volatility = []
        self.stock_count = len(self.data.columns)
        # self.data = np.log(self.data)
        daily_returns = (self.data/self.data.shift(1))-1
        # daily_returns = np.log(self.data/self.data.shift(1))
        mean_daily_returns = daily_returns.mean()
        # self.expected_annual_return = ((mean_daily_returns+1)**365) - 1
        self.expected_annual_return = mean_daily_returns*365
        self.Sigma = daily_returns.cov()
        self.weights = weights = []



    def portfolio_optimizer_positive_weights(self):
        w0 = np.full(self.stock_count, 0.25)
        bounds = [(0,1)] * self.stock_count
        for rt in self.returns:
            constraints2 = ({'type':'eq', 'fun':lambda w: np.sum(w)-1},
                  {'type':'eq', 'fun': lambda w: self.get_return(w) - rt})
            optimalvol = minimize(self.get_volatility,w0, bounds=bounds, constraints=constraints2, method="SLSQP")
            self.volatility.append(optimalvol['fun'])
            self.weights.append(optimalvol.x)

    def lagrange_solver(self,Sigma,Pbar,r_min):
        N = len(Sigma)
        o = np.ones(N)
        Sigma_inv = np.linalg.inv(Sigma)
        a = np.dot(Pbar.T,np.dot(Sigma_inv,Pbar))
        b = np.dot(Pbar.T,np.dot(Sigma_inv,o))
        c = np.dot(o.T,np.dot(Sigma_inv,o))
        return (1/(a*c - b**2)) * np.dot(Sigma_inv,((c*r_min -b)*Pbar + (a - b*r_min)*o))

    def portfolio_optimizer_generalized(self):
        for rt in self.returns:
            wt = self.lagrange_solver(self.Sigma, self.expected_annual_return, rt)
            v = self.get_volatility(wt)
            self.volatility.append(v)
            self.weights.append(wt)

    def get_return(self,w):
        w = np.array(w)
        R = np.sum(w * self.expected_annual_return)
        return R

    def get_volatility(self,w):
        w = np.array(w)
        V = np.sqrt(np.dot(w.T, np.dot(self.Sigma ,w)))
        return V

    def get_sharpe_ratio(self):
        pass

    def get_SRmax_portfolio(self, amt= 1.00):
        idx = np.argmax(self.returns/self.volatility)
        R = self.returns[idx]
        V = self.volatility[idx]
        SR = R/V
        Amount = np.round((self.weights[idx] * amt),2)
        return dict({"return":R, "volatility":V, "SR":SR, "Amount":Amount})
    
    def get_least_volatility_portfolio(self, amt = 1.00):
        idx = np.argmin(self.volatility)
        R = self.returns[idx]
        V = self.volatility[idx]
        SR = R/V
        Amount = np.round((self.weights[idx] * amt),2)
        return dict({"return":R, "volatility":V, "SR":SR, "Amount":Amount})


    def get_mvp(self):
        return np.argmin(self.volatility)
    
    def get_portfolio(self, R, amt= 1.00):
        idx_n, = np.where(self.returns==R)
        idx = idx_n[0]
        R = self.returns[idx]
        V = self.volatility[idx]
        SR = R/V
        Amount = np.round((self.weights[idx] * amt),2)
        return dict({"return":R, "volatility":V, "SR":SR, "Amount":Amount})




    def fit(self, short_selling = False):
        if short_selling:
            self.portfolio_optimizer_generalized()
        else:
            self.portfolio_optimizer_positive_weights()
        volatility= self.volatility
        weights= np.round(self.weights, 4)
        returns = self.returns
        output= dict({"volatility": volatility, "weights": weights, "returns": returns})
        return json.dumps(output, indent=2, cls= NumpyEncoder)
