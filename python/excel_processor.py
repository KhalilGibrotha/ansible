#!/usr/bin/env python

import pandas as pd

class ExcelProcessor:
  def __init__(self, file_path):
    self.file_path = file_path

  def read_data(self):
    df = pd.read_excel(self.file_path)
    self.data = df.to_dict(orient="records")

  def process_data(self):
    self.processed_data = []
    for item in self.data:
      processed_item = {}
      for key, value in item.items():
        processed_key = str(key).lower().strip()
        processed_value = str(value).lower().strip()
        if processed_value == "":
          processed_value = None
        processed_item[processed_key] = processed_value
      self.processed_data.append(processed_item)