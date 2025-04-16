from Data_Loader.RequestData.api_crawler import *
from Data_Loader.RequestData.LoadDataController import *
from Data_Loader.SaveData.SaveDataController import *
from Data_Loader.SaveData.local_storage import *
## 创建读取AKShare实时数据接口的实例化对象
stock_akshare = stock_akshare()
## csv格式实时数据保存器对象
CSVLocalStorage = CSVLocalStorage()
## 创建读取AKShare历史数据接口的实例化对象
stock_akshare_history = stock_akshare_history("600519","daily","20200101","20250416","hfq")
## csv格式历史数据保存器对象
CSVLocalStorageHistory = CSVLocalStorageHistory()
## 创建读取AKShare财务数据接口的实例化对象
stock_akshare_financial = stock_akshare_financial("300605")
## csv格式财务数据保存器对象
CSVLocalStorageFinancial = CSVLocalStorageFinancial()

## 创建读取AKShare资金流数据接口的实例化对象
stock_akshare_individual = stock_akshare_individual("600519")
## csv格式资金流数据保存器对象
CSVLocalStorageIndividual = CSVLocalStorageIndividual()

"""

手动切换策略
"""


## 创建读取策略管理器对象
loadDataController = LoadData(stock_akshare_financial)
## 数据保存控制器对象
saveDatacontroller = SaveDataController(CSVLocalStorageFinancial)



data = loadDataController.ReadData()
# 保存
saveDatacontroller.SaveData(data)
print(data)
