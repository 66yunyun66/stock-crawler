from basic_clean import *


class CleanManager:
    def __init__(self,cleanStrategy):
        self.cleanStrategy = cleanStrategy

    def cleanData(self,table)->pd.DataFrame:
       data = self.cleanStrategy.clean(table)
       return data