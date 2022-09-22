
import pandas as pd

df = pd.read_csv('data/train.csv')

df2 = pd.read_csv('data/test.csv')

# print(df.dtypes)

# print(df2.dtypes)

# print(F"test df shape: {df2.shape}")

# print(F"train df shape: {df.shape}")

print(df['class'].nunique())

print(df2['class'].value_counts())