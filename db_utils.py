import yaml
from sqlalchemy import create_engine
import pandas as pd


def load_yaml(yaml_file):
    '''
    loads RDS credentials as a dict from credentials.yaml file
    '''
    with open(yaml_file, "r") as f:
        credentials_dict = yaml.load(f, Loader=yaml.SafeLoader)
    print(credentials_dict)
    return credentials_dict

def df_to_csv(df):
    '''
    converts dataframe to csv file
    '''
    df.to_csv("loan_payments.csv")
    print("exporting to csv")


class RDSDatabaseConnector:
    '''
    class containing methods to extract data from RDS database 
    '''
    def __init__(self, my_dict):
        self.my_dict = my_dict  

    def SQL_alchemy_connection(self):
        '''
        initialise SQLAlchemy engine 
        '''
        self.engine = create_engine(f"{self.my_dict['DATABASE_TYPE']}+{self.my_dict['DBAPI']}://{self.my_dict['RDS_USER']}:{self.my_dict['RDS_PASSWORD']}@{self.my_dict['RDS_HOST']}:{self.my_dict['RDS_PORT']}/{self.my_dict['RDS_DATABASE']}")
        print("Database connected")

    def extract_data(self, sql_table):
        '''
        extract data from database and return it as a dataframe
        '''
        with self.engine.connect() as conn:
            df = pd.read_sql_table(sql_table, conn)
            print(df.head()) 
            return df

credentials = load_yaml("credentials.yaml")
my_database = RDSDatabaseConnector(credentials)
my_database.SQL_alchemy_connection()
loan_payments_df = my_database.extract_data('loan_payments')

df_to_csv(loan_payments_df)