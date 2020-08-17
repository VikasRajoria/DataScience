import pandas as pd

# below command of pandas_profiling will analysis the data and it will also prepare the report by it's own 
# (automatically anlyzer and report generator)
#  
from pandas_profiling import ProfileReport

df= pd.read_csv('housing.csv')
print(df)

# Generate a Report

profile = ProfileReport(df)
profile.to_file(output_file="housing.html")