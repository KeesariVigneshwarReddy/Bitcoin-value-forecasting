import os
import sys

import warnings
warnings.filterwarnings('ignore')

import pandas as pd
from sqlalchemy import create_engine

from dataclasses import dataclass
@dataclass
class DataBaseConfig :
    db_username = ''
    db_password = ''
    db_host = 'localhost'
    db_port = '3306'
    db_name = 'bitcoin_value_forecasting'

class DataBaseOperations :

    def __init__(self):
        self.database_config = DataBaseConfig()
        self.db_engine = create_engine(f"mysql+mysqlconnector://{self.database_config.db_username}:{self.database_config.db_password}@{self.database_config.db_host}:{self.database_config.db_port}/{self.database_config.db_name}?ssl_disabled=True")

    def dataframe_to_sql_table(self, dataframe, table_name) :
        dataframe.to_sql(table_name, self.db_engine, if_exists='replace', index=False)