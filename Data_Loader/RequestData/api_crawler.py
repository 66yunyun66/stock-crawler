from datetime import time, datetime

# 对接Tushare/AKShare等数据接口[2]()
# 这里选用不收费的AkShare
import akshare as ak
import pandas as pd
from abc import ABC, abstractmethod
from typing import override

class DataCrawler(ABC):
    @abstractmethod
    def request_data(self)->pd.DataFrame:
        pass

## 实时数据
class stock_akshare(DataCrawler):
    # def __init__(self):
    # 获取所有A股实时数据
    @override
    def request_data(self)->pd.DataFrame:
        data = ak.stock_zh_a_spot_em()
        data["时间"] = datetime.now().strftime("%Y-%m-%d  %H:%M:%S")

        return data

## 获取历史数据--指定股票
class stock_akshare_history(DataCrawler):
    def __init__(self,symbol,period,start_date,end_date,adjust):
        self.symbol = symbol
        self.period = period
        self.start_date = start_date
        self.end_date = end_date
        self.adjust = adjust

    @override
    def request_data(self) -> pd.DataFrame:

        # 获取贵州茅台（代码600519）的日线后复权数据
        data_hist = ak.stock_zh_a_hist(symbol=self.symbol, period=self.period,
                                       start_date=self.start_date, end_date=self.end_date,
                                       adjust=self.adjust)

        return data_hist



## 财务数据--指定股票
class stock_akshare_financial(DataCrawler):
    def __init__(self,symbol):
        self.symbol = symbol
    # 获取所有A股财务数据
    @override
    def request_data(self)->pd.DataFrame:
        data_financial = ak.stock_financial_analysis_indicator(symbol=self.symbol)

        return data_financial

## 资金流数据--指定股票
class stock_akshare_individual(DataCrawler):
    def __init__(self,symbol):
        self.symbol = symbol
    # 获取所有A股财务数据
    @override
    def request_data(self)->pd.DataFrame:
        data_individual = ak.stock_individual_fund_flow(stock=self.symbol)

        return data_individual