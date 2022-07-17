# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os, re
import datetime as datetime
from datetime import timedelta
import pathlib

import numpy as np

from utils.ticket_analysis import ticket_utils as tu

import pandas as pd

class TicketAnalysis:
    def __init__(self, source_file):
        self.ticket_utils = tu.Utils(source_file)
        self.source_file = source_file

    def preprocess_snow_data(self):
        base = '/Users/jayantkaushal/Data/POC/SummaHealth/SR'
        listdir = os.listdir(base)
        # listdir = ['sumo-logic-Nutanix-Holodeck-Combined-system-error.json']
        # listdir = ['search-results-2021-11-17T00_20_16.614-0800.csv']
        excel_sheet_name = 'Data'
        new_relic_dataframe = pd.DataFrame()
        time_p = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d%H%M%S")
        for file in listdir:
            stem = pathlib.Path(file).stem
            audit_log_file = os.path.join(base, file)
            # newfile = audit_log_file.replace('.xlsx', '_new.xlsx')
            new_results = self.ticket_utils.retrieve_dataframe(file_name=audit_log_file, sheet_name=excel_sheet_name,
                                                               encoding='latin1')
            new_results1 = new_results.rename(columns={'Request #': 'RequestNumber'})
            new_results1.update(
                new_results1.select_dtypes('datetime').apply(lambda x: x.dt.strftime("%Y-%m-%d %H:%M:%S")))
            file_name  = self.ticket_utils.write_to_file(new_results1,
                                                         custom_file_extension='.json',
                                                         custom_output_file_name=stem,
                                                         custom_dir= '/Users/jayantkaushal/Data/Repo/AiOps/AiOpsDataPreprocessor/data/Summa/' + time_p,
                                                         source_file=self.source_file,
                                                         sheet_name=excel_sheet_name)
            print(file_name)

    def preprocess_svb_data(self):
        base = '/Users/jayantkaushal/Data/POC/SVB/tasks'
        listdir = os.listdir(base)
        # listdir = ['sumo-logic-Nutanix-Holodeck-Combined-system-error.json']
        # listdir = ['search-results-2021-11-17T00_20_16.614-0800.csv']
        excel_sheet_name = 'sc_task'
        new_relic_dataframe = pd.DataFrame()
        time_p = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d%H%M%S")
        for file in listdir:
            stem = pathlib.Path(file).stem
            audit_log_file = os.path.join(base, file)
            # newfile = audit_log_file.replace('.xlsx', '_new.xlsx')

            new_results = self.ticket_utils.retrieve_dataframe(file_name=audit_log_file, sheet_name=excel_sheet_name,
                                                               encoding='latin1')
            new_results = new_results.astype(object).replace(np.nan, 'None')
            self.ticket_utils.print_unique_values_in_columns(new_results,"State")
            new_results['Created'] = new_results['Created'].apply(lambda x: pd.to_datetime(x).strftime('%Y-%m-%d %H:%M:%S'))

            new_results.update(
                new_results.select_dtypes('datetime').apply(lambda x: x.dt.strftime("%Y-%m-%d %H:%M:%S")))
            # new_results["Description"] = new_results['Primary application'].astype(str) + "-" + new_results["Short description"]
            # print(self.ticket_utils.print_unique_values_in_columns(new_results,"Status"))

            file_name  = self.ticket_utils.write_to_file(new_results.head(5),
                                                         custom_file_extension='.json',
                                                         custom_output_file_name=stem,
                                                         custom_dir= '/Users/jayantkaushal/Data/Repo/AiOps/AiOpsDataPreprocessor/data/SVB/' + time_p,
                                                         source_file=self.source_file,
                                                         sheet_name=excel_sheet_name)
            print(file_name)

    def preprocess_af_group_data(self):
        base = '/Users/jayantkaushal/Data/POC/AFGroup/t4'
        listdir = os.listdir(base)
        # listdir = ['sumo-logic-Nutanix-Holodeck-Combined-system-error.json']
        # listdir = ['search-results-2021-11-17T00_20_16.614-0800.csv']
        excel_sheet_name = 'Aisera Data for Previous 12 Mon'
        new_relic_dataframe = pd.DataFrame()
        time_p = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d%H%M%S")
        for file in listdir:
            stem = pathlib.Path(file).stem
            audit_log_file = os.path.join(base, file)
            print(audit_log_file)
            # newfile = audit_log_file.replace('.xlsx', '_new.xlsx')

            new_results = self.ticket_utils.retrieve_dataframe(file_name=audit_log_file, sheet_name=excel_sheet_name,
                                                               encoding='latin1')


            # new_results = new_results1.rename(columns={'ï»¿Incident ID': 'Incident ID'})

            new_results.update(
                new_results.select_dtypes('datetime').apply(lambda x: x.dt.strftime("%Y-%m-%d %H:%M:%S")))
            print(self.ticket_utils.print_unique_values_in_columns(new_results,"Status"))
            # new_results.update(
            #     new_results.select_dtypes('datetime').apply(lambda x: x.dt.strftime("%Y-%m-%d %H:%M:%S")))
            #


            # new_results['Created Date Time'] = new_results['Created Date Time'].apply(lambda x: pd.to_datetime(x).strftime('%Y-%m-%d %H:%M:%S'))
            # self.ticket_utils.print_columns_in_datasource(new_results)
            # new_results['Created Date Time'] = new_results['Created Date Time'].apply(lambda x: pd.to_datetime(x).strftime('%Y-%m-%d %H:%M:%S'))
            # print(new_results['Created Date Time'])
            # new_results["Description"] = new_results['Primary application'].astype(str) + "-" + new_results["Short description"]
            # print(self.ticket_utils.print_unique_values_in_columns(new_results,"Status"))
            # new_results['Created Date Time'] = new_results['Created Date Time'].apply(lambda x: pd.to_datetime(x).strftime('%Y-%m-%d %H:%M:%S'))
            # print(new_results.head(5))
            # new_results = new_results.astype(object).replace(np.nan, 'None')
            # new_results['Created Date Time'] = [datetime.strptime(date[0:10], '%Y-%m-%d').date() for date in
            #                    new_results['Created Date Time']]

            file_name  = self.ticket_utils.write_to_file(new_results,
                                                         custom_file_extension='.json',
                                                         custom_output_file_name=stem,
                                                         custom_dir= '/Users/jayantkaushal/Data/Repo/AiOps/AiOpsDataPreprocessor/data/AFG/' + time_p,
                                                         source_file=self.source_file,
                                                         sheet_name=excel_sheet_name)
            print(file_name)
    def preprocess_varkada_data(self):
        base = '/Users/jayantkaushal/Data/POC/Varkada/tickets'
        listdir = os.listdir(base)
        # listdir = ['sumo-logic-Nutanix-Holodeck-Combined-system-error.json']
        # listdir = ['search-results-2021-11-17T00_20_16.614-0800.csv']
        excel_sheet_name = 'Aisera Data for Previous 12 Mon'
        new_relic_dataframe = pd.DataFrame()
        time_p = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d%H%M%S")
        for file in listdir:
            stem = pathlib.Path(file).stem
            audit_log_file = os.path.join(base, file)
            print(audit_log_file)
            # df = pd.read_json(audit_log_file, lines=True)
            # newfile = audit_log_file.replace('.xlsx', '_new.xlsx')

            new_results = self.ticket_utils.retrieve_dataframe(file_name=audit_log_file, sheet_name=excel_sheet_name,
                                                               encoding='latin1')
            self.ticket_utils.print_columns_in_datasource(new_results)

            # new_results = new_results1.rename(columns={'ï»¿Incident ID': 'Incident ID'})

            # new_results.update(
            #     new_results.select_dtypes('datetime').apply(lambda x: x.dt.strftime("%Y-%m-%d %H:%M:%S")))
            # print(self.ticket_utils.print_unique_values_in_columns(new_results,"Status"))
            # new_results.update(
            #     new_results.select_dtypes('datetime').apply(lambda x: x.dt.strftime("%Y-%m-%d %H:%M:%S")))
            #


            # new_results['Created Date Time'] = new_results['Created Date Time'].apply(lambda x: pd.to_datetime(x).strftime('%Y-%m-%d %H:%M:%S'))
            # self.ticket_utils.print_columns_in_datasource(new_results)
            # new_results['Created Date Time'] = new_results['Created Date Time'].apply(lambda x: pd.to_datetime(x).strftime('%Y-%m-%d %H:%M:%S'))
            # print(new_results['Created Date Time'])
            # new_results["Description"] = new_results['Primary application'].astype(str) + "-" + new_results["Short description"]
            # print(self.ticket_utils.print_unique_values_in_columns(new_results,"Status"))
            # new_results['Created Date Time'] = new_results['Created Date Time'].apply(lambda x: pd.to_datetime(x).strftime('%Y-%m-%d %H:%M:%S'))
            # print(new_results.head(5))
            # new_results = new_results.astype(object).replace(np.nan, 'None')
            # new_results['Created Date Time'] = [datetime.strptime(date[0:10], '%Y-%m-%d').date() for date in
            #                    new_results['Created Date Time']]

            file_name  = self.ticket_utils.write_to_file(new_results.head(5),
                                                         custom_file_extension='.json',
                                                         custom_output_file_name=stem,
                                                         custom_dir= '/Users/jayantkaushal/Data/Repo/AiOps/AiOpsDataPreprocessor/data/Varkada/' + time_p,
                                                         source_file=self.source_file,
                                                         sheet_name=excel_sheet_name)
            print(file_name)