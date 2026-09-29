from abc import ABC, abstractmethod
from dotenv import load_dotenv
from supabase import create_client
import os
load_dotenv()
class Extraction(ABC):
    def __init__(self):
        self.bd_conection=Create_client(
            os.getenv("SUPABASE_URL"),
            os.getenv("SUPABASE_KEY")
        )
    @abstractmethod
    def extract(self, data):
        pass
    @abstractmethod
    def load(self,data):
        pass



class CSV_Train(Extraction):
    def extract(self, data):
        # Implement CSV extraction logic here
        pass

    def load(self, data):
        # Implement CSV loading logic here
        pass