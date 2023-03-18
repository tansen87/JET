'''
Author: XiaZeCheng, tansen
Date: 2023-03-02 20:01:08
LastEditors: Please set LastEditors
LastEditTime: 2023-03-18 19:01:47
'''

import re
import warnings
from typing import Union

import numpy as np
import pandas as pd
from rich.progress import track
from pypinyin import pinyin, Style
from pandas.core.frame import DataFrame

from utils.log import Log

warnings.filterwarnings("ignore")


class JournalsTemplate():
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def insert_column(
        df: DataFrame
    ) -> DataFrame:
        """ insert column """
        try:
            # read template column name
            with open("config/columnName.txt", "r", encoding="utf-8") as fp:
                column_names = fp.readlines()
            list_cs = [column_name.strip("\n") for column_name in column_names]
            # insert column
            for value in list_cs:
                df[value] = None
            Log.info("insert column successfully.")
            return df
        except Exception as e:
            Log.error(e)
    
    @staticmethod
    def reset_column(
        df: DataFrame,
        entity: str = "Entity",
        companyName: str = "Company Name",
        journalNumber: str = "Journal Number",
        spotlightType: str = "Spotlight Type",
        dateEntered: str = "Date Entered",
        timeEntered: str = "Time Entered",
        dateUpdated: str = "Date Updated",
        timeUpdated: str = "Time Updated",
        userIDEntered: str = "UserID Entered",
        nameOfUserEntered: str = "Name of User Entered",
        userIDUpdated: str = "UserID Updated",
        nameOfUserUpdated: str = "Name of User Updated",
        dateEffective: str = "Date Effective",
        dateOfJournal: str = "Date of Journal",
        financialPeriod: str = "Financial Period",
        journalType: str = "Journal Type",
        journalTypeDescription: str = "Journal Type Description",
        autoManualOrInterface: str = "Auto Manual or Interface",
        journalDescription: str = "Journal Description",
        lineNumber: str = "Line Number",
        lineDescription: str = "Line Description",
        currency: str = "Currency",
        entityCurrencyEC: str = "Entity Currency (EC)",
        exchangeRate: str = "Exchange Rate",
        dcIndicator: str = "DC Indicator",
        signedJournalAmount: str = "Signed Journal Amount",
        unsignedDebitAmount: str = "Unsigned Debit Amount",
        unsignedCreditAmount: str = "Unsigned Credit Amount",
        signedAmountEC: str = "Signed Amount EC",
        unsignedDebitAmountEC: str = "Unsigned Debit Amount EC",
        unsignedCreditAmountEC: str = "Unsigned Credit Amount EC",
        accountNumber: str = "Account Number",
        accountDescription: str = "Account Description",
        controllingAreaForCostAndProfitCentre: str = "Controlling Area for Cost and Profit Centre",
        costCentre: str = "Cost Centre",
        costCentreDescription: str = "Cost Centre Description",
        profitCentre: str = "Profit Centre",
        profitCentreDescription: str = "Profit Centre Description",
        sourceActivityOrTransactionCode: str = "Source Activity or Transaction Code"
    ) -> DataFrame:
        df["Entity"] = df[entity]
        df["Company Name"] = df[companyName]
        df["Journal Number"] = df[journalNumber]
        df["Spotlight Type"] = df[spotlightType]
        df["Date Entered"] = df[dateEntered]
        df["Time Entered"] = df[timeEntered]
        df["Date Updated"] = df[dateUpdated]
        df["Time Updated"] = df[timeUpdated]
        df["UserID Entered"] = df[userIDEntered]
        df["Name of User Entered"] = df[nameOfUserEntered]
        df["UserID Updated"] = df[userIDUpdated]
        df["Name of User Updated"] = df[nameOfUserUpdated]
        df["Date Effective"] = df[dateEffective]
        df["Date of Journal"] = df[dateOfJournal]
        df["Financial Period"] = df[financialPeriod]
        df["Journal Type"] = df[journalType]
        df["Journal Type Description"] = df[journalTypeDescription]
        df["Auto Manual or Interface"] = df[autoManualOrInterface]
        df["Journal Description"] = df[journalDescription]
        df["Line Number"] = df[lineNumber]
        df["Line Description"] = df[lineDescription]
        df["Currency"] = df[currency]
        df["Entity Currency (EC)"] = df[entityCurrencyEC]
        df["Exchange Rate"] = df[exchangeRate]
        df["DC Indicator"] = df[dcIndicator]
        df["Signed Journal Amount"] = df[signedJournalAmount]
        df["Unsigned Debit Amount"] = df[unsignedDebitAmount]
        df["Unsigned Credit Amount"] = df[unsignedCreditAmount]
        df["Signed Amount EC"] = df[signedAmountEC]
        df["Unsigned Debit Amount EC"] = df[unsignedDebitAmountEC]
        df["Unsigned Credit Amount EC"] = df[unsignedCreditAmountEC]
        df["Account Number"] = df[accountNumber]
        df["Account Description"] = df[accountDescription]
        df["Controlling Area for Cost and Profit Centre"] = df[controllingAreaForCostAndProfitCentre]
        df["Cost Centre"] = df[costCentre]
        df["Cost Centre Description"] = df[costCentreDescription]
        df["Profit Centre"] = df[profitCentre]
        df["Profit Centre Description"] = df[profitCentreDescription]
        df["Source Activity or Transaction Code"] = df[sourceActivityOrTransactionCode]
        return df
    
    @staticmethod
    def get(
        df: DataFrame
    ) -> DataFrame:
        """ get standard templates """
        try:
            # read template column name
            with open("config/columnName.txt", "r", encoding="utf-8") as fp:
                column_names = fp.readlines()
            list_cs = [column_name.strip("\n") for column_name in column_names]
            Log.info("get columns successfully.")
            return df.loc[:, list_cs]
        except Exception as e:
            Log.error(e)
    
    @staticmethod
    def convert_date(
        df: DataFrame,
        dateEffective: str = "Date Effective",
        dateEntered: str = "Date Entered",
    ) -> DataFrame:
        """ convert date format to dd/mm/yyyy """
        try:
            df[dateEffective] = pd.to_datetime(df[dateEffective])
            df[dateEffective] = pd.to_datetime(df[dateEffective]).dt.strftime("%d/%m/%Y")
            df[dateEntered] = pd.to_datetime(df[dateEntered])
            df[dateEntered] = pd.to_datetime(df[dateEntered]).dt.strftime("%d/%m/%Y")
            Log.info("convert date format successfully.")
            return df
        except Exception as e:
            Log.error(e)

    @staticmethod
    def convert_number(
        df: DataFrame,
    ) -> DataFrame:
        """" retain 2 decimals """
        try:
            df = df.round({'Unsigned Debit Amount': 2, 'Unsigned Credit Amount': 2, "Signed Journal Amount": 2,
                        "Unsigned Debit Amount EC": 2, "Unsigned Credit Amount EC": 2, "Signed Amount EC": 2})
            Log.info("retain 2 decimals successfully.")
            return df
        except Exception as e:
            Log.error(e)

    @staticmethod
    def convert_string(
        df: DataFrame,
        lineDescription: str = "Line Description"
    ) -> DataFrame:
        """ clear special symbols and limits string length """
        try:
            df[lineDescription] = df[lineDescription].astype(str)
            df[lineDescription] = df[lineDescription].apply(lambda x: re.sub("\W", "", x))
            df[lineDescription] = df[lineDescription].apply(lambda x: x[: 200])
            Log.info("clear special symbols and limits string length successfully.")
            return df
        except Exception:
            Log.error("'Line Description' column is null.")
    
    @staticmethod
    def convert_chinese(
        df: DataFrame,
        journalNumber: str = "Journal Number",
        py_type: str = "upper",  # upper, lower, captial, abbre
    ) -> DataFrame:
        """ convert chinese to pinyin """
        try:
            df[journalNumber] = df[journalNumber].astype(str)
            for value in df[journalNumber]:
                py_single = pinyin(value, style=Style.NORMAL)
                py_mutiple = [value[0] for value in py_single]
                if py_type == "upper":
                    py_result = ''.join([i.upper() for i in py_mutiple])
                if py_type == "lower":
                    py_result = ''.join([i.lower() for i in py_mutiple])
                if py_type == "captial":
                    py_result = py_mutiple[0].capitalize(
                    ) + ''.join(py_mutiple[1:])
                if py_type == "abbre":
                    py_result = ''.join([i[0].upper() for i in py_mutiple])
                df.replace(value, py_result, inplace=True)
            Log.info("convert pinyin successfully.")
            return df
        except Exception:
            Log.error("'Journal Number' column is null.")
    
    @staticmethod
    def pivot(
        df: DataFrame,
        index: Union[str, list[str], None] = None,
        values: Union[str, list[str], None] = None,
        save_path: str = "saveFile",
        is_pivot: bool = True,  # export pivot table -> default(yes)
        is_net2zero: bool = True  # export net 2 zero table -> default(yes)
    ) -> None:
        """ get pivot table and net 2 zero table """
        try:
            pt = pd.pivot_table(df, index=index, values=values, aggfunc=np.sum)
            pt.reset_index(inplace=True)
            if is_pivot:
                pt.to_excel(f"{save_path}/pivot.xlsx", index=False)
                Log.info(f"pivot save file path: {save_path}\\pivot.xlsx")
            if is_net2zero:
                pt.to_excel(f"{save_path}/net2zero.xlsx", index=False)
                Log.info(f"net2zero save file path: {save_path}\\net2zero.xlsx")
        except Exception as e:
            Log.error(e)
    
    @staticmethod
    def calculation_sum(
        df: DataFrame,
        debit: str = "Unsigned Debit Amount EC",
        credit: str = "Unsigned Credit Amount EC",
        amount: str = "Signed Amount EC"
    ) -> None:
        """ calculation of summation """
        try:
            df[debit] = df[debit].astype(float)
            df[credit] = df[credit].astype(float)
            df[amount] = df[amount].astype(float)
            Log.info(f"Debit -> {df[debit].sum()}")
            Log.info(f"Credit -> {df[credit].sum()}")
            Log.info(f"Amount -> {df[amount].sum()}")
        except Exception as e:
            Log.error(e)
    
    @staticmethod
    def sort(
        df: DataFrame,
        journalNumber: str = "Journal Number",
        ascending: bool = True,
    ) -> DataFrame:
        """ sort values """
        try:
            df = df.sort_values(by=journalNumber, ascending=ascending, ignore_index=True)
            Log.info("sort value successfully.")
            return df
        except Exception as e:
            Log.error(e)
    
    @staticmethod
    def add_number(
        df: DataFrame,
        journalNumber: str = "Journal Number",
        lineNumber: str = "Line Number"
    ) -> DataFrame:
        """ add Line Number """
        try:
            df[lineNumber] = int(1)
            for value in track(range(1, len(df))):
                if df[journalNumber][value] == df[journalNumber][value-1]:
                    df[lineNumber][value] = df[lineNumber][value-1] + 1
                else:
                    df[lineNumber][value] = 1
            Log.info("add Line Number successfully.")
            return df
        except Exception:
            Log.error("'Line Number' column is null.")
    
    @staticmethod
    def add_month(
        df: DataFrame,
        financialPeriod: str = "Financial Period",
    ) -> DataFrame:
        """ add Financial Period """
        try:
            df[financialPeriod] = df["Date Effective"].str.split("/")[1]
            df[financialPeriod] = df[financialPeriod].astype("uint8")
            Log.info("add Financial Period successfully.")
            return df
        except Exception:
            Log.error("'Date Effective' column is null.")

    @staticmethod
    def add_direction(
        df: DataFrame,
        amount: str = "Signed Amount EC",
        dcIndicator: str = "DC Indicator",
    ) -> DataFrame:
        """ adjust 'DC Indicator' direction """
        try:
            df[amount] = df[amount].astype(float)
            df[dcIndicator] = np.where(df[amount] >= 0, "D", "C")
            Log.info("adjust dc direction successfully.")
            return df
        except Exception as e:
            Log.error(e)

    @staticmethod
    def add_dc(
        df: DataFrame,
        amount: str = "Signed Amount EC",
        debit: str = "Unsigned Debit Amount EC",
        credit: str = "Unsigned Credit Amount EC",
    ) -> DataFrame:
        """ calculation dc values """
        try:
            df[debit] = np.where(df[amount] > 0, df[amount], 0)
            df[credit] = np.where(df[amount] < 0, df[amount]*-1, 0)
            Log.info("calculation dc values successfully.")
            return df
        except Exception as e:
            Log.error(e)
    
    @staticmethod
    def get_last_account(
        df: DataFrame,
        location: int = 0,  # entity_accountCode loaction
        entity_account: str = "enacc",  # entity_accountCode column
    ) -> list:
        """ get end-level account """
        cell = 0
        last_acc: list = []
        try:
            while cell < len(df)-1:
                try:
                    if df.iloc[cell, location-1] == df.iloc[cell+1, location-1][:len(df.iloc[cell, location-1])]:
                        pass
                    else:
                        last_acc.append(df.iloc[cell, df.columns.get_loc(entity_account)])
                    cell += 1
                except:
                    break
            last_acc.append(df.iloc[len(df)-1, location-1])
            Log.info("get end-level account successfully.")
            return last_acc
        except Exception as e:
            Log.error(e)
    
    @staticmethod
    def screen(
        df: DataFrame,
        entity_account: str = "enacc",  # entity_accountCode column
        screen_condition: Union[str, list[str], None] = None  # screening conditions
    ) -> DataFrame:
        """ screen data """
        list_screen: list = []
        try:
            for condition in screen_condition:
                df_screen = df.loc[df[entity_account] == condition]
                list_screen.append(df_screen)
            df = pd.concat(list_screen, axis=0, ignore_index=True)
            Log.info("screen data successfully.")
            return df
        except Exception as e:
            Log.error(e)
    
    @staticmethod
    def write(
        df: DataFrame,
        path: str = "saveFile/handleGL.txt"
    ) -> None:
        df.to_csv(path, index=False, encoding="utf-16le", sep="|")
        Log.info(f"save path -> {path}.")
    
    @staticmethod
    def check(
        df: DataFrame,
        entity: str = "Entity",
        currency: str = "Currency",
        currencyEC: str = "Entity Currency (EC)",
        amount: str = "Signed Amount EC",
        debit: str = "Unsigned Debit Amount EC",
        credit: str = "Unsigned Credit Amount EC",
        mi: str = "Auto Manual or Interface",
        fp: str = "Financial Period",
        is_equal: bool = True,  # check debit credit and amount column
        is_mi: bool = True,  # check auto manual or interface column
        is_negative: bool = True,  # check negative number
        is_month: bool = True,  # check Financial Period
        is_entity: bool = True,  # check entity
        is_currency: bool = True,  # check currency
    ) -> DataFrame:
        try:
            if is_equal:
                debit_sum = df[debit].sum()
                credit_sum = df[credit].sum()
                amount_sum = df[amount].sum()
                if debit_sum == credit_sum and amount_sum == float(0):
                    Log.info("debit credit amount is correct.")
                else:
                    Log.error("please check debit credit and amount column.")
            if is_mi:
                ami = df[mi].unique().tolist()
                if pd.isna(ami):
                    Log.error("[Auto Manual or Interface] column is null.")
                else:
                    Log.info(f"[Auto Manual or Interface] -> {ami}")
            if is_negative:
                uni_d = df[debit].unique().tolist()
                uni_c = df[credit].unique().tolist()
                neg_d = [value for value in uni_d if value < 0]
                neg_c = [value for value in uni_c if value < 0]
                if len(neg_d) == 0 and len(neg_c) == 0:
                    Log.info("no negative number.")
                else:
                    Log.error("there are negative numbers.")
            if is_month:
                month = df[fp].unique().tolist()
                if pd.isna(month):
                    Log.error("[Financial Period] column is null.")
                else:
                    Log.info(f"[Financial Period] -> {month}")
            if is_entity:
                ent = df[entity].unique().tolist()
                if pd.isna(ent):
                    Log.error("[Entity] column is null.")
                else:
                    Log.info(f"[Entity] -> {ent}")
            if is_currency:
                curr = df[currency].unique().tolist()
                curr_ec = df[currencyEC].unique().tolist()
                if pd.isna(curr) or pd.isna(curr_ec):
                    Log.error("[Currency] or [Currency EC] column is null.")
                else:
                    Log.info(f"[currency] -> {curr}\n[Currency EC] -> {curr_ec}")
        except Exception as e:
            Log.error(e)


if __name__ == "__main__":
    jet = JournalsTemplate()
    jet.check()
