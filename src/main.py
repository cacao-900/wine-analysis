import numpy as np
import pandas as pd
import matplotlib

df = pd.read_csv('data/wine.csv')

print(df.info())
print(df.describe())
print(df.head())
