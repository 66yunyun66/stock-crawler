## 保存数据的客户端代码
## 将保存策略的功能调用进行封装
import pandas as pd


class SaveDataController:
    def __init__(self,LocalStorage):
        self.LocalStorage = LocalStorage

    def SaveData(self,df:pd.DataFrame):
        self.LocalStorage.save_data(df)






