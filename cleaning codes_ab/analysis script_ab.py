import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time
from scipy.stats import linregress
import scipy.stats as stats
#open combined data of 11 countries
country_data = pd.read_csv("CSV_Output/11_country.csv")
del country_data['Unnamed: 0']

#-----------------------------------------------------#
#collecting stats for Danceability
danceability_mean_country = pd.DataFrame(country_data.groupby("Country")['Danceability'].mean())
danceability_median_country = pd.DataFrame(country_data.groupby("Country")['Danceability'].median())
danceability_min_country = pd.DataFrame(country_data.groupby("Country")['Danceability'].min())
danceability_max_country = pd.DataFrame(country_data.groupby("Country")['Danceability'].max())
#merge information to data frame for Danceability
danceability_mean_median = pd.merge(danceability_mean_country,danceability_median_country,on="Country")
danceability_max_min = pd.merge(danceability_max_country,danceability_min_country,on="Country")
danceability_stats = pd.merge(danceability_mean_median,danceability_max_min, on = "Country",how = "outer")
danceability_df = danceability_stats.rename(columns={
    "Danceability_x_x":"Mean Value Danceability",
    "Danceability_y_x":"Median Value Danceability",
    "Danceability_x_y":"Max Value Danceability",
    "Danceability_y_y":"Min Value Danceability"})
danceability_df.reset_index(level=0, inplace=True)
#save stat table to csv for Danceability
danceability_df.to_csv("Danceability_Stats.csv",index=False)
#plotting - kind = bar
x_axis = np.arange(len(danceability_df["Country"]))
tick_locations = [value+0.4 for value in x_axis]
plt.figure(figsize=(19.20,10.80))
plt.figure(figsize=(len(danceability_df["Country"]),4))
plt.bar(danceability_df["Country"],danceability_df["Mean Value Danceability"],alpha=0.5, align="edge")
plt.xticks(tick_locations,danceability_df["Country"], rotation=45)
plt.xlim(-0.25, len(danceability_df["Country"]))
plt.ylim(0.3, max(danceability_df["Mean Value Danceability"])+0.085)
plt.title("Danceability Value of Different Countries")
plt.ylabel("Mean of Danceability Value")
plt.savefig("Danceability_stats.png",bbox_inches = 'tight')

#-----------------------------------------------------#
#valence stats
valence_mean_country = pd.DataFrame(country_data.groupby("Country")['Valence'].mean())
valence_median_country = pd.DataFrame(country_data.groupby("Country")['Valence'].median())
valence_min_country = pd.DataFrame(country_data.groupby("Country")['Valence'].min())
valence_max_country = pd.DataFrame(country_data.groupby("Country")['Valence'].max())

valence_mean_median = pd.merge(valence_mean_country,valence_median_country,on="Country")
valence_max_min = pd.merge(valence_max_country,valence_min_country,on="Country")
valence_stats = pd.merge(valence_mean_median,valence_max_min, on = "Country",how = "outer")
valence_df = valence_stats.rename(columns={
    "Valence_x_x":"Mean Value Valence",
    "Valence_y_x":"Median Value Valence",
    "Valence_x_y":"Max Value Valence",
    "Valence_y_y":"Min Value Valence"
})
valence_df.reset_index(level=0,inplace=True)
#save stat table to csv for Valence
valence_df.to_csv("Valence_stats.csv",index=False)
#ploting - valence
plt.figure(figsize=(19.20,10.80))
plt.figure(figsize=(len(valence_df["Country"]),4))
plt.bar(valence_df["Country"],valence_df["Mean Value Valence"],alpha=0.75, align="edge",color='rosybrown')
plt.xticks(tick_locations,valence_df["Country"], rotation=45)
plt.xlim(-0.25, len(valence_df["Country"]))
plt.ylim(0, max(valence_df["Mean Value Valence"])+0.03)
plt.ylabel("Mean of Valence Value")
plt.title("Valence Value of Different Countries")
plt.savefig("Valence_stats.png", bbox_inches = 'tight')

#-----------------------------------------------------#
#Loudness group by country, get stats
loudness_mean_country = pd.DataFrame(country_data.groupby("Country")['Loudness'].mean())
loudness_median_country = pd.DataFrame(country_data.groupby("Country")['Loudness'].median())
loudness_min_country = pd.DataFrame(country_data.groupby("Country")['Loudness'].min())
loudness_max_country = pd.DataFrame(country_data.groupby("Country")['Loudness'].max())
loudness_mean_median = pd.merge(loudness_mean_country,loudness_median_country,on="Country")
loudness_max_min = pd.merge(loudness_max_country,loudness_min_country,on="Country")
loudness_stats = pd.merge(loudness_mean_median,loudness_max_min, on = "Country",how = "outer")
loudness_df = loudness_stats.rename(columns={
    "Loudness_x_x":"Mean Value Loudness",
    "Loudness_y_x":"Median Value Loudness",
    "Loudness_x_y":"Max Value Loudness",
    "Loudness_y_y":"Min Value Loudness"})
loudness_df.reset_index(level=0,inplace=True)
loudness_df.to_csv("Loudness_stats.csv",index=False)
#Bar ploting - loudness, kind = bar
plt.figure(figsize=(19.20,10.80))
plt.figure(figsize=(len(loudness_df["Country"]),4))
plt.bar(loudness_df["Country"],loudness_df["Mean Value Loudness"],alpha=0.75, align="edge",color='darkseagreen')
plt.xticks(tick_locations,loudness_df["Country"], rotation=45)
plt.xlim(-0.5, len(loudness_df["Country"]))
plt.ylim(max(loudness_df["Mean Value Loudness"])-4.5,0)
plt.ylabel("Mean of Loudness Value")
plt.title("Loudness Value of Different Countries")
plt.savefig("Loudness_stats.png", bbox_inches = 'tight')


#-----------------------------
#-----------------------
#---------------
#Analysis using boxplot
#-----------
#danceability
danceability_plot=country_data.boxplot("Danceability", by="Country", figsize=(20, 15),fontsize="15",patch_artist=True)
danceability_plot.set_title("Danceability by Country",fontsize="25")
plt.ylabel("Danceability Value",fontsize="15")
plt.xlabel("")
plt.savefig("Danceability Boxplot.png")
plt.show()
#energy
energy_plot=country_data.boxplot("Energy", by="Country", figsize=(20, 15),fontsize="15",patch_artist=True)
energy_plot.set_title("Energy by Country",fontsize="25")
plt.ylabel("Energy Value",fontsize="15")
plt.xlabel("")
plt.savefig("Energy Boxplot.png")
plt.show()
#tempo
tempo_plot=country_data.boxplot("Tempo", by="Country", figsize=(20, 15),fontsize="15",patch_artist=True)
tempo_plot.set_title("Tempo by Country",fontsize="25")
plt.ylabel("Tempo Value",fontsize="15")
plt.xlabel("")
plt.savefig("Tempo Boxplot.png")
plt.show()
#loudness
loudness_plot=country_data.boxplot("Loudness", by="Country", figsize=(20, 15),fontsize="15",patch_artist=True)
loudness_plot.set_title("Loudness by Country",fontsize="25")
plt.ylabel("Loudness Value",fontsize="15")
plt.xlabel("")
plt.savefig("Loudness Boxplot.png")
plt.show()
#acousticness
acousticness_plot=country_data.boxplot("Acousticness", by="Country", figsize=(20, 15),fontsize="15",patch_artist=True)
acousticness_plot.set_title("Acousticness by Country",fontsize="25")
plt.ylabel("Acousticness Value",fontsize="15")
plt.xlabel("")
plt.savefig("Acousticness Boxplot.png")
plt.show()