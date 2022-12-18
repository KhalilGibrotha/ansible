#!/usr/bin/env python

from excel_processor import ExcelProcessor

def main():
   # Create an instance of the ExcelProcessor class to read and process/
   #  the data from an Excel file
    processor = ExcelProcessor("path/to/file.xlsx")
    processor.read_data()
    processor.process_data()

    # The processed_data attribute of the processor object now contains the data
    # from the Excel file as a list of dictionaries, with all keys and values/
    # converted to lower case and leading and trailing whitespace removed

    if __name__ == "__main__":
      main()
