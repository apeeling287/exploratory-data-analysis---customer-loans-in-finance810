import yaml
from sqlalchemy import create_engine
from sqlalchemy import text
import pandas as pd


def load_yaml(yaml_file):
    '''loads RDS credentials as a dict'''
    with open(yaml_file, "r") as f:
        credentials_dict = yaml.load(f, Loader=yaml.SafeLoader)
    print(credentials_dict)
    return credentials_dict


class RDSDatabaseConnector:
    '''
    class containing methods to extract data from RDS database 
    '''
    def __init__(self, my_dict):
        self.my_dict = my_dict  
        self.engine = None

    def SQL_alchemy_connection(self):
        #initialise SQLAlchemy engine 
        self.engine = create_engine(f"{self.my_dict['DATABASE_TYPE']}+{self.my_dict['DBAPI']}://{self.my_dict['RDS_USER']}:{self.my_dict['RDS_PASSWORD']}@{self.my_dict['RDS_HOST']}:{self.my_dict['RDS_PORT']}/{self.my_dict['RDS_DATABASE']}")
        print("Database connected")

    def extract_data(self):
        #extracts data and returns it as a pandas dataframe 
        # with self.engine.execution_options(isolation_level="AUTOCOMMIT").connect() as conn:
        #     loan_payments = pd.read_sql_table("loan_payments", self.engine)
        #     loan_payments.head()
        # with self.engine.connect() as conn:
        #     result = conn.execute(text("select 'hello world'"))
        #     print(result.all())
        with self.engine.connect() as conn:
            df = pd.read_sql_table('loan_payments', conn)
            df.head()
            print(df)


credentials = load_yaml("credentials.yaml")

my_database = RDSDatabaseConnector(credentials)
my_database.SQL_alchemy_connection()
my_database.extract_data()
