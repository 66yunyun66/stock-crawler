# 基础清洗逻辑

from abc import ABC, abstractmethod
from typing import override

import pandas as pd


class BasicClean(ABC):
    ## 基础清洗的基类
    ## 定义一个抽象方法，供父调用子的方法
    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        pass

## 清洗实时数据
class StockClean(BasicClean):
    @override
    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        threshold = int(df.shape[1] * 0.5)  # 计算允许的最小非空列数
        clean_data = df.dropna(thresh=threshold)
        # 动态计算市场平均涨跌幅（作为参考阈值）
        market_avg = clean_data["涨跌幅"].mean()
        # 静态阈值：常规股票单日涨跌幅不应超过10%
        cleaned_df = clean_data[(clean_data['涨跌幅'].abs() <= 10) |
                        (clean_data['名称'].str.contains(' 科创板'))]  # 科创板股票特殊处理

        # 动态阈值：过滤超过市场均值3倍标准差的数据
        std_threshold = market_avg + 3 * df['涨跌幅'].std()
        cleaned_df = cleaned_df[cleaned_df['涨跌幅'].abs() <= std_threshold]

        return cleaned_df


    ## 清洗历史数据
class HistoryDataClean(BasicClean):
    @override
    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        pass