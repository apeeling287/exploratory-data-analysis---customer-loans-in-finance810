import yaml
from sqlalchemy import create_engine
import pandas as pd
from scipy.stats import normaltest


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
    print("exporting to csv...")

def csv_to_df(csv):
    print("importing csv to pandas dataframe...")
    df = pd.read_csv(csv, index_col=0)
    df.shape
    df.info
    return df


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
        print("Database connected...")

    def extract_data(self, sql_table):
        '''
        extract data from database and return it as a dataframe
        '''
        with self.engine.connect() as conn:
            df = pd.read_sql_table(sql_table, conn)
            print(df.head()) 
            return df


class DataTransform:
    '''
    handles conversions of columns to different data formats
    '''
    def __init__(self, df):
        self.df = df

    def convert_to_date(self, columns):
        print("converting columns to date format...")
        self.df[columns] = self.df[columns].apply(pd.to_datetime, format="%b-%Y", errors='coerce')
        return self.df

    def convert_to_str(self, columns):
        print("converting columns to string format...")
        self.df[columns] = self.df[columns].astype(str)
        return self.df

    def convert_to_numeric(self, columns):
        print("converting columns to numeric format...")
        self.df[columns] = self.df[columns].apply(pd.to_numeric, errors='raise')
        return self.df

       
class DataFrameInfo:
    '''
    gives information about dataframe: data types, statistical values, 
    distinct values, shape, count of Nulls 
    '''
    def __init__(self, df):
        self.df = df
    
    def describe_df(self):
        print("column data types: ")
        return self.df.info()

    def statistical_values(self):
        print("column statistical values: mean, median, std")
        return self.df.describe(include="all")

    def unique_values(self):
        print("unique values per column:")
        self.df = self.df.nunique().to_frame().reset_index()
        self.df.columns = ["Variable", "DistinctCount"]
        return self.df
    
    def df_shape(self):
        print("Shape of the df: ")
        return self.df.shape
    
    def count_of_nulls(self):
        null_count = self.df.isnull().sum()
        print("percentage and count of missing values: ")
        percent_missing = round(self.df.isnull().sum() * 100 / len(self.df), 2)
        missing_values_df = pd.DataFrame({"percentage_missing":percent_missing,
                                          "null_count": null_count
                                          })
        missing_values_df = missing_values_df.reset_index()
        return missing_values_df
 

class Plotter:
    '''
    visualises insights from the data
    '''
    def __init__(self):
        pass


class DataFrameTransform(DataFrameInfo):
    '''
    perform EDA transformations
    '''
    def __init__(self, df):
        self.df = df

    def count_of_nulls(self):
        return super().count_of_nulls()

    def drop_columns(self, columns_to_drop):
        self.df = self.df.drop(self.df.columns[columns_to_drop], axis=1)
        return self.df
    
    def drop_rows_with_NaN(self, *args):
        self.df = self.df.dropna(subset=args)
        return self.df
    
    def normaltest(self, columns_to_impute):
        data = self.df[columns_to_impute]
        stat, p = normaltest(data, nan_policy='omit')
        print("Statistics=%.3f, p=%.3f" % (stat, p))

    def impute_median(self, *args):
        for col in args:
            self.df[col] = self.df[col].fillna(self.df[col].median())




if __name__ == "__main__":

    credentials = load_yaml("credentials.yaml")     #create credentials variable
    my_database = RDSDatabaseConnector(credentials) #initialise the class
    my_database.SQL_alchemy_connection()        #call method to connect to database
    loan_payments_df = my_database.extract_data('loan_payments')  ##call method to extract data from database
    df_to_csv(loan_payments_df) #convert dataframe to csv 
    loan_payments_df_v2 = csv_to_df("loan_payments.csv")  #converts local csv file to dataframe
    transformed_df = DataTransform(loan_payments_df_v2)
    columns = ["last_payment_date", "next_payment_date", "last_credit_pull_date"]
    transformed_df.convert_to_date(columns)
    print(transformed_df)
    df_info = DataFrameInfo(transformed_df)
    df_info.describe_df()
