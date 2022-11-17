#!/APSshare/anaconda3/x86_64/bin/python

import pandas as pd
import plotly.express as px

# Define the columns in the camonitor log
headers = ["pv", "date", "time", "value"]
dtypes = {"pv":"str", "date":"str", "time":"str", "value":"float"}
date_cols= ["date", "time"]
# Read the camonitor log
df = pd.read_csv('data.txt', delim_whitespace=True, header=None, names=headers, dtype=dtypes, parse_dates=date_cols)

# Drop the date column, which still has string values in it
df.drop('date', axis=1, inplace=True)
# Rename the time column to datetime
df.rename(columns={'time':'datetime'}, inplace=True)

# Create the plot
#!fig = px.bar(df, x="datetime", y="value")
fig = px.line(df, x="datetime", y="value")
fig.show()
