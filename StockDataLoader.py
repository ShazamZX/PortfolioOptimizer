import pandas as pd
import numpy as np
import pandas_datareader.data as web
import datetime

class StockDataLoader:
    def __init__(self, stock_list):
      self.stock_list= stock_list
      self.start_date= datetime.date.today() - datetime.timedelta(days=365)
      self.end_date= datetime.date.today() 
      self.df= pd.DataFrame(columns=['Date'])

    def get_date(self):
      self.df['Date']= web.DataReader("NIFTYBEES.NS","yahoo",self.start_date, self.end_date).index

    def add_stock(self,stock):
      stock_data= web.DataReader(f"{stock}.NS", "yahoo",self.start_date, self.end_date).reset_index()
      self.df= self.df.merge(stock_data[['Date','Close']], on= 'Date').rename(columns={'Close':stock})
      return
    
    def get_stock_data(self):
      self.get_date()
      for stock in self.stock_list:
        self.add_stock(stock)
      self.df.set_index('Date', inplace=True)
      return self.df