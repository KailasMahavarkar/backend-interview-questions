from abc import ABC, abstractmethod

class DataProcessor(ABC):
    def process(self):
        self.read_data()
        self.process_data()
        self.save_data()
    
    @abstractmethod
    def read_data(self):
        pass
    
    @abstractmethod
    def process_data(self):
        pass
    
    def save_data(self):
        print("Saving data (common implementation)")

class CSVProcessor(DataProcessor):
    def read_data(self):
        print("Reading CSV data")
    
    def process_data(self):
        print("Processing CSV data")

class JSONProcessor(DataProcessor):
    def read_data(self):
        print("Reading JSON data")
    
    def process_data(self):
        print("Processing JSON data")

# Usage
csv_processor = CSVProcessor()
csv_processor.process()