from CleanManager import CleanManager
from basic_clean import *
from Stock_analysis.Src.config import DATA_PATHS

## 创建数据清理器
StockClean = StockClean()
## 创建清理数据管理器，传入数据和清理器
cleanmanager=CleanManager(StockClean)
df = pd.read_csv(DATA_PATHS["raw"])
data=cleanmanager.cleanData(df)
data.to_csv(DATA_PATHS["cleaned"],encoding='utf-8-sig',index=False)
print(df.head(20))