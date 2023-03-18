'''
Author: tansen
Date: 2023-03-05 12:55:27
LastEditors: Please set LastEditors
LastEditTime: 2023-03-05 13:11:05
'''
import numpy as np
import pandas as pd
from pandas.core.frame import DataFrame

class JournalLedgerDA:
    def __init__(self, df: DataFrame) -> None:
        self.df = df

    @staticmethod
    def test4(
        df: DataFrame,
        entity: str = "Entity",
        journalNumber: str = "Journal Number",
        accountNumber: str = "Account Number"
    ) -> None:
        pt = pd.pivot_table(df, index=[accountNumber, entity, journalNumber])
        
