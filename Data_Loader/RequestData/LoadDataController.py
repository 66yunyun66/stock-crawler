import pandas as pd

from Data_Loader.RequestData.api_crawler import DataCrawler

"""
在线数据获取策略的管理类，在这个类中封装了在线数据获取的接口，
实现在客户端只需要调用ReadData函数就能获取到数据

"""
class LoadData:
    def __init__(self,dataCrawler:DataCrawler):
        self.dataCrawler = dataCrawler

    def ReadData(self)->pd.DataFrame:
        data = self.dataCrawler.request_data()
        return data


