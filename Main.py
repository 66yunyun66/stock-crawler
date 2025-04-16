# 主程序入口
import akshare as ak
stock_zh_a_spot_df = ak.stock_zh_a_spot_em()
print(stock_zh_a_spot_df[['代码', '名称', '最新价', '涨跌幅']].head())

        # 筛选特定股票（如贵州茅台）
maotai = stock_zh_a_spot_df[stock_zh_a_spot_df['代码'] == '600519']
print(maotai)