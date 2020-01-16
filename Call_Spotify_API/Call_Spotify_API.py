#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import dependencies and Client keys
import pandas as pd
import spotipy
import matplotlib.pyplot as plt
from keys import client_id, client_secret
from spotipy.oauth2 import SpotifyClientCredentials
import top_50_playlists


# In[3]:


#Set Credentials
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#Call api for data from top 50 US tracks
playlists = sp.user_playlist_tracks('spotify', top_50_playlists.top_50_US, market = 'US')


# In[43]:


#Loop through each song to get name and URI, saved to empty list. Ignore the first 14 characters in each URI
top_song_names = []
top_songs_uri = []
for index in range(0, 50):
    top_song_names.append(playlists['items'][index]['track']['name'])
    top_songs_uri.append(playlists['items'][index]['track']['uri'][14:])


# In[42]:


#List of each feature for generationg dataframe
audio_feature_names = ['Song Name', 'Danceability', 'Energy', 'Key', 'Loudness', 'Mode', 'Speechiness', 'Acousticness', 'Instramentalness',
                 'Liveness', 'Valence', 'Tempo', 'Type', 'ID', 'URI', 'Track Href', 'Analysis URL', 'Duration (ms)', 'Time Signature']

#Tag to hold the name of each audio feature to reference from json object
audio_features_tags = list(sp.audio_features(top_songs_uri[0])[0].keys())

#List of lists to hold actual features of each song in a list
audio_features_array = [[] for x in range(0,19)]


# In[44]:


#create a list of strings for the different audio features
list(sp.audio_features(top_songs_uri[0])[0].keys())

#loop to find audio features for each song in playlist
for index in range(0,50):
    #Call api for features of each individual song
    print(index)
    features = sp.audio_features(top_songs_uri[index])
    audio_features_array[0].append(top_song_names[index])
    #loop to append each feature to a list in the audio_features_array list of lists
    for i in range(0,18):      
        audio_features_array[i+1].append(features[0][audio_features_tags[i]])
        


# In[46]:


features_dict = {audio_feature_names[i] : audio_features_array[i] for i in range(0, len(audio_feature_names))}
pd.DataFrame(features_dict)


# In[26]:


jupyter nbconvert --to script 'Call Spotify API'.ipynb


# In[6]:


# # A bunch of OAuth2.0 stuff that we skipped thanks to SciPy
# spotipy.util.prompt_for_user_token('famousafu','user-library-read',client_id=client_id,client_secret=client_id, redirect_uri='https://github.com/')

# lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

# spotify = spotipy.Spotify()
# results = spotify.artist_top_tracks(lz_uri)

# for track in results['tracks'][:10]:
#     print('track    : ' + track['name'])
#     print('audio    : ' + track['preview_url'])
#     print('cover art: ' + track['album']['images'][0]['url'])
#     print()


# In[26]:


# #get oauth token
# auth_url = 'https://accounts.spotify.com/authorize'
# params = {
#     'grant_type': 'password',
#     'client_id' : client_id,
#     'response_type' : 'code',
#     'redirect_uri': 'https://www.google.com'
# }

# auth_response = requests.get(auth_url, params = params)
# type(auth_response)
# # token_url = 'https://accounts.spotify.com/api/token'
# # params = {
# #     'grant_type' : 'authorization_code',
# #     'code': auth_response,
# #     'redirect_uri': 'https://www.google.com'
# # }

# # access_token_response = requests.post(token_url, params=params, verify=False, allow_redirects=False, auth=(client_id, client_secret))
# # access_token_response

