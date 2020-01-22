import pandas as pd
import csv
import numpy as np

AU_df = pd.read_csv("CSV_Output/Australia_top_50_songs.csv")
IN_df = pd.read_csv("CSV_Output/India_top_50_songs.csv")
BA_df = pd.read_csv("CSV_Output/Brazil_top_50_songs.csv")
FR_df = pd.read_csv("CSV_Output/France_top_50_songs.csv")
HO_df = pd.read_csv("CSV_Output/Hong Kong_top_50_songs.csv")
JA_df = pd.read_csv("CSV_Output/Japan_top_50_songs.csv")
MA_df = pd.read_csv("CSV_Output/Malaysia_top_50_songs.csv")
SA_df = pd.read_csv("CSV_Output/South Africa_top_50_songs.csv")
TA_df = pd.read_csv("CSV_Output/Taiwan_top_50_songs.csv")
UK_df = pd.read_csv("CSV_Output/UK_top_50_songs.csv")
US_df = pd.read_csv("CSV_Output/US_top_50_songs.csv")
#removing index column
del AU_df["Unnamed: 0"]
del IN_df["Unnamed: 0"]
del BA_df["Unnamed: 0"]
del FR_df["Unnamed: 0"]
del HO_df["Unnamed: 0"]
del JA_df["Unnamed: 0"]
del MA_df["Unnamed: 0"]
del SA_df["Unnamed: 0"]
del TA_df["Unnamed: 0"]
del UK_df["Unnamed: 0"]
del US_df["Unnamed: 0"]

#insert columns with country names
AU_df.loc[:, 'Country'] = "Australia"
IN_df.loc[:, 'Country'] = "India"
BA_df.loc[:, 'Country'] = "Brazil"
FR_df.loc[:, 'Country'] = "France"
HO_df.loc[:, 'Country'] = "HongKong"
JA_df.loc[:, 'Country'] = "Japan"
MA_df.loc[:, 'Country'] = "Malaysia"
SA_df.loc[:, 'Country'] = "South Africa"
TA_df.loc[:, 'Country'] = "Taiwan"
UK_df.loc[:, 'Country'] = "UK"
US_df.loc[:, 'Country'] = "US"

#merge dataframes
#by groups of two countries
AU_IN = pd.merge(AU_df,IN_df,how ='outer')
BA_FR = pd.merge(BA_df,FR_df,how ='outer')
HO_JA = pd.merge(HO_df,JA_df,how ='outer')
MA_SA = pd.merge(MA_df,SA_df,how ='outer')
TA_UK = pd.merge(TA_df,UK_df,how ='outer')

US_group1 = pd.merge(AU_IN,US_df,how ='outer')
group2 = pd.merge(US_group1,BA_FR,how ='outer')
group3= pd.merge(HO_JA,MA_SA,how ='outer')
group2_3 = pd.merge(group2,group3,how ='outer')
TA_UK_group_2_3 = pd.merge(TA_UK,group2_3,how ='outer')
TA_UK_group_2_3["Country"].value_counts()
#export to csv of the final group of dataframes
TA_UK_group_2_3.to_csv("CSV_Output/11_country.csv")