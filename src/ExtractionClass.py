from abc import ABC, abstractmethod
from dotenv import load_dotenv
from supabase import create_client
import os
import csv
from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine
load_dotenv()
class Extraction(ABC):
    def __init__(self):
        self.bd_conection=Create_client(
            os.getenv("SUPABASE_URL"),
            os.getenv("SUPABASE_KEY")
        )
    @abstractmethod
    def Extract(self, data):
        pass
    @abstractmethod
    def Load(self,data):    
        pass



class CSV_Train(Extraction):
    def __init__(self):
        self.data=None
        self.path=Path(__file__).resolve().parent.parent /"dataset" /"tarin.csv"
    def Extract(self):
        try:
            with open(self.path,'r') as file:
                file_data=DictReader(file)
                self.data=list(file_data)
            print(f"Data extracted from {self.path}")
        except FileNotFoundError:
            print(f"File not found: {self.path}")
        except Exception as e:
            raise e
    def Load(self, data):
        try:
            if not self.data:
                raise Exception("There isnt data to load")
            response=self.bd_conection.table("train_data").upsert(self.data).execute()
            if not response or response.status_code!=201:
                raise Exception("failed to load data into the DB")
            print("data loaded into the DB")
        except Exception as e:
            raise e


class CSV_Test(Extraction):
    def __init__(self):
        self.path=Path(__file__).resolve().parent.parent /"dataset" /"teste.csv"
        self.data=None

    def Extract(self):
        try:
            with open(self.path,'r') as file:
                file_data=DictReader(file)
                self.data=list(file_data)
            print("Extract finisehd sucessfuly")    
        except Exception as e:
            raise Exception(f"error during extract the test data from {self.path}")
    def Load(self):
        try:
            if  not self.data:
                raise Exception("There isnt data to load")
            response=bd_conection.table("test_data").upsert(self.data).execute()
            if not response or response.status_code!=201:
                raise Exception(f"error to load data into DB PATH:{self.path}")
        except Exception as e:
            raise Exception("error loading data into the DB")  




class CSV_Complaiment(Extraction):
    def __init__(self):
        self.data=None
        self.path=Path(__file__).resolve().parent.parent /"dataset" /"chief_complaints.csv"

    def Extract(self):
        try:
            with opne(self.path,'r') as file:
                file_data=DictReader(file)
                self.data=list(file_data)
            print(f"extraction comleted  from:{self.path}")
        except Exception as e:
            raise Exception("ERROR tring to extract chief_colmplaiments")

    def Load(self):
        try:

            if not self.data:
                raise Exception("there isnt data")
            response=bd_conection.table("chief_complaints").upsert(self.data).execute()
            if not resposne or response.status_code!=201:
                 raise Exception("Errro druing load complaiment into the db")
            print(f"Load completed from {self.path}")
        except Exception as e:
            raise Exception("Errro druing load complaiment into the db")



class CSV_Patinet_history(Extraction):
    def __init__(self):
        self.data=None
        self.path=Path(__file__).resolve().parent.parent /"dataset" / "patient_history.csv"
    def Extract(self):
        try:
            with opne(self.path,'r') as file:
                file_data=DictReader(file)
                self.data=list(file_data)
            print(f"extraction comleted  from:{self.path}")
        except Exception as e:
            raise Exception("ERROR tring to extract chief_colmplaiments")

    def Load(self):
        try:

            if not self.data:
                raise Exception("there isnt data")
            response=bd_conection.table("patient_history").upsert(self.data).execute()
            if not resposne or response.status_code!=201:
                 raise Exception("Errro druing load complaiment into the db")
            print(f"Load completed from {self.path}")
        except Exception as e:
            raise Exception("Errro druing load complaiment into the db")

