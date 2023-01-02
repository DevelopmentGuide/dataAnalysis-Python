import pandas as pd

# Shape of the dataframe
print(df.shape)

# Column names
print(df.columns)

# Data types of each column
print(df.dtypes)

# First 5 rows
print(df.head())

# Last 5 rows
print(df.tail())

# Summary statistics
print(df.describe())

# Information about the dataframe
print(df.info())

# Mean of each column
print(df.mean())


# Mean - Average
print(df.temperature.mean())

# Median - Middle value
print(df.temperature.median())

# Mode - Most frequent value
print(df.temperature.mode())

# Standard Deviation - How much the values are spread out
print(df.temperature.std())

# Variance - How much the values are spread out
print(df.temperature.var())

# Min - Lowest value
print(df.temperature.min())

# Max - Highest value
print(df.temperature.max())

# Quantile - Value below which a given percentage of observations in a group of observations fall
print(df.temperature.quantile(0.25))

# Count - Number of non-null values
print(df.temperature.count())

# Sum - Total sum of values
print(df.temperature.sum())

# Cumulative Sum - Cumulative sum of values
print(df.temperature.cumsum())

# Cumulative Max - Cumulative maximum of values
print(df.temperature.cummax())

# Cumulative Min - Cumulative minimum of values
print(df.temperature.cummin())

# Cumulative Product - Cumulative product of values
print(df.temperature.cumprod())

# Unique - Unique values
print(df.temperature.unique())

# Value Counts - Number of times each unique value appears
print(df.temperature.value_counts())

# Replace - Replace values
print(df.temperature.replace(0, 100))


# **Reading** and **writing** CSV data

# Read CSV
df = pd.read_csv('climate.txt')
print(df)

# Create blank CSV
df = pd.DataFrame()
df.to_csv('new.csv')

# Add column
df['new'] = [1, 2, 3, 4, 5]
df.to_csv('new.csv')
print(df)

# Add row
df.loc[6] = [6]
df.to_csv('new.csv')
print(df)

# Delete column
df['col2del'] = [1, 2, 3, 4, 5, 6]
df.to_csv('new.csv')
print(df)
del df['col2del']
df.to_csv('new.csv')
print(df)

# Delete row
df = df.drop(6)
df.to_csv('new.csv')
print(df)

# Rename column
df = df.rename(columns={'new': 'new_col'})
df.to_csv('new.csv')
print(df)


df = pd.read_csv('climate.txt')

# Query
print(df.query('temperature > 90'))

# Filter
print(df[df.temperature > 90])

# Sort
print(df.sort_values(by='temperature', ascending=False))

# Indexing
print(df.temperature[0])

# Slicing
print(df.temperature[0:5])


# Groupby
print(df.groupby('temperature').mean())

# Aggregation
print(df.agg(['min', 'max', 'mean', 'median', 'std', 'var']))

# Apply
print(df.temperature.apply(lambda x: x * 2))

# Map
print(df.temperature.map(lambda x: x * 2))


# Merge
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                   index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                   index=[4, 5, 6, 7])


df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                   index=[8, 9, 10, 11])

frames = [df1, df2, df3]
result = pd.concat(frames)
print(result)

# Concat
df4 = pd.DataFrame({'B': ['B2', 'B3', 'B6', 'B7'],
                    'D': ['D2', 'D3', 'D6', 'D7'],
                    'F': ['F2', 'F3', 'F6', 'F7']},
                   index=[2, 3, 6, 7])

result = pd.concat([df1, df4], axis=1, sort=False)
print(result)

# Join
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['K0',
                              'K1',
                              'K2',
                              'K3'],
                      'C': ['C0',
                            'C1',
                            'C2',
                            'C3'],
                      'D': ['D0',
                            'D1',
                            'D2',
                            'D3']})

result = pd.merge(left, right, on='key')
print(result)
