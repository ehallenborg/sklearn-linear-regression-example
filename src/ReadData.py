import numpy as np
import pandas as pd
FILE_PATH = "other\london_data\data"

filenames = {
    'year': "housing_in_london_yearly_variables.csv",
    'month': "housing_in_london_monthly_variables.csv"
}

def read_data(filename):
    data = pd.read_csv(f'{FILE_PATH}\{filenames.get(filename)}')
    data = data.fillna(0)
    return data

def read_city_data(city, filename):
    data = pd.read_csv(f'{FILE_PATH}\{filenames.get(filename)}')
    data = data.fillna(0)
    data = data.loc[data['area']==city]
    return data

def test():
    read_city_data("city of london", "housing_in_london_monthly_variables.csv")
    read_data("housing_in_london_monthly_variables.csv")


