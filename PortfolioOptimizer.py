import pandas as pd
import numpy as np
from scipy.optimize import minimize
def __init__(self, data):
    self.data = data
    self.returns = np.linspace(0,1,10000)
    self.volatility = np.zeros(len(self.returns))
    self.stock_count = len(data.columns)
    daily_returns = (self.data - self.data.shift(1))/self.data.shift(1)
    mean_daily_returns = daily_returns.mean()
    self.expected_annual_return = ((mean_daily_returns+1)**252) - 1
    self.Sigma = daily_returns.cov()
    self.weights = weights = np.zeros((10000,self.stock_count))



def portfolio_optimizer_positive_weights(self):
    w0 = np.full(self.stock_count, 0.25)
    bounds = [(0,1)] * self.stock_count
    for rt in self.returns:
        constraints2 = ({'type':'eq', 'fun':lambda w: np.sum(w)-1},
               {'type':'eq', 'fun': lambda w: self.getReturn(w) - rt})
        optimalvol = minimize(self.get_volatility,w0, bounds=bounds, constraints=constraints2, method="SLSQP")
        self.volatility.append(optimalvol['fun'])
        self.weights.append(optimalvol.x)

def lagrange_solver(Sigma,Pbar,r_min):
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

def get_max_sharpe_ratio(self):
    return np.argmax(self.returns/self.volatility)

def get_mvp(self):
    return np.argmin(self.volatility)