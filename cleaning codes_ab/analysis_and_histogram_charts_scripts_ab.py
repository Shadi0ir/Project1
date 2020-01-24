import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time
from scipy.stats import linregress
import scipy.stats as stats

country_data = pd.read_csv("CSV_Output/11_country.csv")
del country_data['Unnamed: 0']
global_data = pd.read_csv("CSV_Output/Global_top_50_songs.csv")
del global_data['Unnamed: 0']

danceability_allcountry = country_data["Danceability"]
daneability_global = global_data["Danceability"]
energy_allcountry = country_data["Energy"]
energy_global = global_data["Energy"]
valence_allcountry = country_data["Valence"]
valence_global = global_data["Valence"]
loudness_allcountry=country_data["Loudness"]
loudness_global=global_data["Loudness"]
acousticness_allcountry=country_data["Acousticness"]
acousticness_global=global_data["Acousticness"]
instramentalness_allcountry=country_data["Instramentalness"]
instramentalness_global=global_data["Instramentalness"]
time_allcountry =country_data["Time Signature"]
time_global = global_data["Time Signature"]
tempo_allcountry = country_data["Tempo"]
tempo_global = global_data["Tempo"]
#one way stats_________________________
stats_danceability = stats.f_oneway(danceability_allcountry,daneability_global)
stats_energy = stats.f_oneway(energy_allcountry,energy_global)
stats_valence = stats.f_oneway(valence_allcountry,valence_global)
stats_loudness = stats.f_oneway(loudness_allcountry,loudness_global)
stats_tempo = stats.f_oneway (tempo_allcountry,tempo_global)
stats_time = stats.f_oneway(time_allcountry,time_global)
stats_instramentalness=stats.f_oneway(instramentalness_allcountry,instramentalness_global)
stats_acousticness=stats.f_oneway(acousticness_allcountry,acousticness_global)
#creating dataframe to collect values for 1-way statistic
stats_df = pd.DataFrame({
    "1-way Stats":["Statistic","p-value"],
    "Danceability":stats_danceability,
    "Energy":stats_energy,
    "Valence":stats_valence,
    "Loudness":stats_loudness,
    "Tempo":stats_tempo,
    "Time Signature":stats_time,
    "Instramentalness":stats_instramentalness,
    "Acousticness":stats_acousticness})
stats_df.to_csv("1way_statistic on 11 country data vs global result.csv", index =False)

#2-way statistic, ttest
danceability_ttest = stats.ttest_1samp(global_data["Danceability"], country_data["Danceability"].mean())
energy_ttest = stats.ttest_1samp(global_data["Energy"], country_data["Energy"].mean())
valence_ttest = stats.ttest_1samp(global_data["Valence"], country_data["Valence"].mean())
loudness_ttest = stats.ttest_1samp(global_data["Loudness"], country_data["Loudness"].mean())
tempo_ttest = stats.ttest_1samp(global_data["Tempo"], country_data["Tempo"].mean())
time_ttest = stats.ttest_1samp(global_data["Time Signature"], country_data["Time Signature"].mean())
instramental_ttest = stats.ttest_1samp(global_data["Instramentalness"], country_data["Instramentalness"].mean())
acoustic_ttest=stats.ttest_1samp(global_data["Acousticness"], country_data["Acousticness"].mean())
twoway_stats_df =pd.DataFrame({
    "2-way Stats":["Statistic","p-value"],
    "Danceability":danceability_ttest,
    "Energy":energy_ttest,
    "Valence":valence_ttest,
    "Loudness":loudness_ttest,
    "Tempo":tempo_ttest,
    "Time Signature":time_ttest,
    "Instramentalness":instramental_ttest,
    "Acousticness":acoustic_ttest
})

#generating histogram - time signature
plt.figure(figsize=(19.20,10.80))
plt.subplot(2, 1, 2)
plt.hist(country_data["Time Signature"], 50, density=True, alpha=0.7, label="All Countries in Study")
plt.hist(global_data["Time Signature"], 50, density=True, alpha=0.7, label="Global")
plt.axvline(country_data["Time Signature"].mean(), color='blue', linestyle='dashed', linewidth=1)
plt.axvline(global_data["Time Signature"].mean(), color='orange', linestyle='dashed', linewidth=1)
plt.legend(loc='upper left',fontsize=12)  
plt.title("Time Signature Histogram",fontsize=14)
plt.xlabel("Time Signature Value",fontsize=12)
   
plt.savefig("Time_Signature_countries_vs_global.png")
plt.show()

#generating histogram - energy
plt.figure(figsize=(19.20,10.80))
plt.subplot(2, 1, 2)
plt.hist(country_data["Energy"], 50, density=True, alpha=0.7, label="All Countries in Study")
plt.hist(global_data["Energy"], 50, density=True, alpha=0.7, label="Global")
plt.axvline(country_data["Energy"].mean(), color='blue', linestyle='dashed', linewidth=1)
plt.axvline(global_data["Energy"].mean(), color='orange', linestyle='dashed', linewidth=1)
plt.legend(loc='upper left',fontsize=12)  
plt.title("Energy Histogram",fontsize=14)
plt.xlabel("Energy Value",fontsize=12)
   
plt.savefig("Energy_countries_vs_global.png")
plt.show()

#generating histogram - valence
plt.figure(figsize=(19.20,10.80))
plt.subplot(2, 1, 2)
plt.hist(country_data["Valence"],50 , density=True, alpha=0.7, label="All Countries in Study")
plt.hist(global_data["Valence"], 50, density=True, alpha=0.7, label="Global")
plt.axvline(country_data["Valence"].mean(), color='blue', linestyle='dashed', linewidth=1)
plt.axvline(global_data["Valence"].mean(), color='orange', linestyle='dashed', linewidth=1)
plt.legend(loc='upper left',fontsize=12)  
plt.title("Valence Histogram",fontsize=14)
plt.xlabel("Valence Value",fontsize=12)
   
plt.savefig("Valence_countries_vs_global.png")
plt.show()

#generating histogram - loudness
plt.figure(figsize=(19.20,10.80))
plt.subplot(2, 1, 2)
plt.hist(country_data["Loudness"],50 , density=True, alpha=0.7, label="All Countries in Study")
plt.hist(global_data["Loudness"], 50, density=True, alpha=0.7, label="Global")
plt.axvline(country_data["Loudness"].mean(), color='blue', linestyle='dashed', linewidth=1)
plt.axvline(global_data["Loudness"].mean(), color='orange', linestyle='dashed', linewidth=1)
plt.legend(loc='upper left',fontsize=12)  
plt.title("Loudness Histogram",fontsize=14)
plt.xlabel("Loudness Value (dB)",fontsize=12)
    
plt.savefig("Loudness_countries_vs_global.png")
plt.show()

#generating histogram - danceability
plt.figure(figsize=(19.20,10.80))
plt.subplot(2, 1, 2)
plt.hist(country_data["Danceability"],50 , density=True, alpha=0.7, label="All Countries in Study")
plt.hist(global_data["Danceability"], 50, density=True, alpha=0.7, label="Global")
plt.axvline(country_data["Danceability"].mean(), color='blue', linestyle='dashed', linewidth=1)
plt.axvline(global_data["Danceability"].mean(), color='orange', linestyle='dashed', linewidth=1)
plt.legend(loc='upper left',fontsize=12)  
plt.title("Danceability Histogram",fontsize=14)
plt.xlabel("Danceability Value",fontsize=12)
   
plt.savefig("Danceability_countries_vs_global.png")
plt.show()

##generating histogram - tempo
plt.figure(figsize=(19.20,10.80))
plt.subplot(2, 1, 2)
plt.hist(country_data["Tempo"],50 , density=True, alpha=0.7, label="All Countries in Study")
plt.hist(global_data["Tempo"], 50, density=True, alpha=0.7, label="Global")
plt.axvline(country_data["Tempo"].mean(), color='blue', linestyle='dashed', linewidth=1)
plt.axvline(global_data["Tempo"].mean(), color='orange', linestyle='dashed', linewidth=1)
plt.legend(loc='upper left',fontsize=12)  
plt.title("Tempo Histogram",fontsize=14)
plt.xlabel("Tempo Value (BPM)",fontsize=12)
   
plt.savefig("Tempo_countries_vs_global.png")
plt.show()

#generating histogram - acousticness
plt.figure(figsize=(19.20,10.80))
plt.subplot(2, 1, 2)
plt.hist(country_data["Acousticness"],40 , density=True, alpha=0.7, label="All Countries in Study")
plt.hist(global_data["Acousticness"],40, density=True, alpha=0.7, label="Global")
plt.axvline(country_data["Acousticness"].mean(), color='blue', linestyle='dashed', linewidth=1)
plt.axvline(global_data["Acousticness"].mean(), color='orange', linestyle='dashed', linewidth=1)
plt.legend(loc='upper left',fontsize=12)  
plt.title("Acousticness Histogram",fontsize=14)
plt.xlabel("Acousticness Value",fontsize=12)
plt.savefig("Acousticness_countries_vs_global.png")
plt.show()

#generating histogram - instramentalness
plt.figure(figsize=(19.20,10.80))
plt.subplot(2, 1, 2)
plt.hist(country_data["Instramentalness"], 50, density=True, alpha=0.7, label="All Countries in Study")
plt.hist(global_data["Instramentalness"], 50, density=True, alpha=0.7, label="Global")
plt.axvline(country_data["Instramentalness"].mean(), color='blue', linestyle='dashed', linewidth=1)
plt.axvline(global_data["Instramentalness"].mean(), color='orange', linestyle='dashed', linewidth=1)
plt.legend(loc='upper right',fontsize=12)  
plt.title("Instramentalness Histogram",fontsize=14)
plt.xlabel("Instramentalness Value",fontsize=12)
   
plt.savefig("Instramentalness_countries_vs_global.png")
plt.show()

