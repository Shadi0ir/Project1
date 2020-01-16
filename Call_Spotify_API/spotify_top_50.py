def top_50_stats(top_50_playlist):
    #import dependencies and Client keys
    import pandas as pd
    import spotipy
    import matplotlib.pyplot as plt
    from keys import client_id, client_secret
    from spotipy.oauth2 import SpotifyClientCredentials


    #Set Credentials
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    #Call api for data from top 50 US tracks
    playlists = sp.user_playlist_tracks('spotify', playlist_id = top_50_playlist, market = 'US', limit=50)

    #Loop through each song to get name and URI, saved to empty list. Ignore the first 14 characters in each URI
    top_song_names = []
    top_songs_uri = []
    for index in range(0, 50):
        top_song_names.append(playlists['items'][index]['track']['name'])
        top_songs_uri.append(playlists['items'][index]['track']['uri'][14:])

    #List of each feature for generationg dataframe
    audio_feature_names = ['Song Name', 'Danceability', 'Energy', 'Key', 'Loudness', 'Mode', 'Speechiness', 'Acousticness', 'Instramentalness',
                    'Liveness', 'Valence', 'Tempo', 'Type', 'ID', 'URI', 'Track Href', 'Analysis URL', 'Duration (ms)', 'Time Signature']

    #Tag to hold the name of each audio feature to reference from json object
    audio_features_tags = list(sp.audio_features(top_songs_uri[0])[0].keys())

    #List of lists to hold actual features of each song in a list
    audio_features_array = [[] for x in range(0,19)]

    #create a list of strings for the different audio features
    list(sp.audio_features(top_songs_uri[0])[0].keys())

    #loop to find audio features for each song in playlist
    for index in range(0,50):
        #Call api for features of each individual song
        print(f'Calling song {index}')
        features = sp.audio_features(top_songs_uri[index])
        audio_features_array[0].append(top_song_names[index])
        #loop to append each feature to a list in the audio_features_array list of lists
        for i in range(0,18):      
            audio_features_array[i+1].append(features[0][audio_features_tags[i]])
    
    #dictionary interpretation to generate dictionary of lists containing all song names and features 
    features_dict = {audio_feature_names[i] : audio_features_array[i] for i in range(0, len(audio_feature_names))}
    
    #generate dataframe from features_dict
    return pd.DataFrame(features_dict)