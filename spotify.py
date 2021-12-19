#!/usr/bin/env python3
from numpy import empty
import spotipy as sp
from spotipy.oauth2 import SpotifyClientCredentials
from best_songs import rank_artist_track_list
from dotenv import load_dotenv
load_dotenv()

spotify = sp.Spotify(client_credentials_manager=SpotifyClientCredentials())

def get_spotify_id():
    get_track_id = []
    for rank, artist, track in rank_artist_track_list:
        get_track_id = spotify.search(q='artist:' + artist + ' track:' + track, type='track', limit=1)
        if not get_track_id['tracks']['items']:
            continue
        track_id = (rank, artist, track, ("https://open.spotify.com/track/" + get_track_id['tracks']['items'][0]['id']))
        print(track_id)
        
get_spotify_id()
