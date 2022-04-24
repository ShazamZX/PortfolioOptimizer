from turtle import width
import streamlit as st
import pandas as pd
from optimustock import PortfolioOptimizer
from optimustock.StockDataLoader import StockDataLoader
from optimustock.PortfolioOptimizer import MarkowitzPortfolioOptimizer
from stockList import StockSectors as sc
import numpy as np
import json
import seaborn as sns
import matplotlib.pyplot as plt
st.title("Markowitz Portfolio  Optimization")

fig = plt.figure(figsize=(15, 10))

sector_list = sc.get_sector_list()
dropdown_sectors = st.multiselect('Select Sector ', sector_list)
tickers = list()
if dropdown_sectors:
    for item in dropdown_sectors:
        if item == 'Auto':
            auto_list = sc.get_sector_stocks(item)
            tickers = tickers + auto_list

        elif item == 'Banking':
            banking_list = sc.get_sector_stocks(item)
            tickers = tickers + banking_list

        elif item == 'Finance':
            finance_list = sc.get_sector_stocks(item)
            tickers = tickers + finance_list

        elif item == 'IT':
            it_list = sc.get_sector_stocks(item)
            tickers = tickers + it_list

        elif item == 'FMCG':
            fmcg_list = sc.get_sector_stocks(item)
            tickers = tickers + fmcg_list

dropdown = st.multiselect('Select Tickers', tickers)

obj = StockDataLoader(dropdown)
option = st.select_slider(
    'Select your preferred portfolio return ',


    options=[str(i)+"%" for i in range(100)])
st.write('Chosen Return  Value is :', option)
return_expected = float(option[:-1])/100
capital = st.number_input('Choose your Investment Amount in Rs. ')
load_flag = st.button("Calculate")
if (len(dropdown) > 0) and return_expected > 0 and capital > 0 and load_flag:
    df = obj.get_stock_data()
    markowitzer = MarkowitzPortfolioOptimizer(df)
    fit_data = markowitzer.fit()
    model_data = json.loads(fit_data)
    user_portfolio = markowitzer.get_portfolio(return_expected, capital)
    mvp_portfolio = markowitzer.get_least_volatility_portfolio(capital)
    SrMax_portfolio = markowitzer.get_SRmax_portfolio(capital)

    st.subheader(f'Portfolio to achieve {option} return:')
    user_ptf = {"Stocks": dropdown,
                "Investment Amount(In Rs.)": user_portfolio['Amount']}
    user_ptf_df = pd.DataFrame(user_ptf).astype(str)
    st.write("Expected Return: ", option)
    st.write("Sharpe Ratio: ", np.round(user_portfolio['SR'], 2))
    st.dataframe(user_ptf_df)

    st.subheader('Portfolio with Minimum Risk(Volatility)')
    mvp_ptf = {"Stocks": dropdown,
               "Investment Amount(In Rs.)": mvp_portfolio['Amount']}
    mvp_ptf_df = pd.DataFrame(mvp_ptf).astype(str)
    st.write("Expected Return: ", str(mvp_portfolio['return']*100)+"%")
    st.write("Sharpe Ratio: ", np.round(mvp_portfolio['SR'], 2))
    st.dataframe(mvp_ptf_df)

    st.subheader('Portfolio with Maximum Sharpe Ratio')
    SrMax_ptf = {"Stocks": dropdown,
                 "Investment Amount(In Rs.)": SrMax_portfolio['Amount']}
    SrMax_ptf_df = pd.DataFrame(SrMax_ptf).astype(str)
    st.write("Expected Return: ", str(SrMax_portfolio['return']*100)+"%")
    st.write("Sharpe Ratio: ", np.round(SrMax_portfolio['SR'], 2))
    st.dataframe(SrMax_ptf_df)

    st.subheader('Markowitz Efficient Frontier')

    plt.plot(model_data['volatility'], model_data['returns'])
    plt.xlabel("Expected Volatility")
    plt.ylabel("Expected Retuns")

    plt.scatter(user_portfolio["volatility"],
                user_portfolio["return"], c='black')
    plt.scatter(mvp_portfolio["volatility"],
                mvp_portfolio["return"], c='black')
    plt.scatter(SrMax_portfolio["volatility"],
                SrMax_portfolio["return"], c='black')

    plt.colorbar(label="SR")

    st.pyplot(fig)
