
# 本地数据存储（CSV/SQLite）[3]()
from abc import ABC, abstractmethod
from typing import override
import pandas as pd
class LocalStorage(ABC):
    @abstractmethod
    def save_data(self, df: pd.DataFrame):
        pass


class CSVLocalStorage(LocalStorage):
    @override
    def save_data(self, df: pd.DataFrame):
        df.to_csv('data.csv',encoding="utf-8-sig")

# 历史数据
class CSVLocalStorageHistory(LocalStorage):
    @override
    def save_data(self, df: pd.DataFrame):
        df.to_csv('HistoryData.csv',encoding="utf-8-sig")

# 财务数据
class CSVLocalStorageFinancial(LocalStorage):
    @override
    def save_data(self, df: pd.DataFrame):
        df.to_csv('FinancialData.csv',encoding="utf-8-sig")


# 资金流数据
class CSVLocalStorageIndividual(LocalStorage):
    @override
    def save_data(self, df: pd.DataFrame):
        df.to_csv('IndividualData.csv',encoding="utf-8-sig")