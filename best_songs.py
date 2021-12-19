#!/usr/bin/env python3
from numpy import result_type
from pandas.core.algorithms import rank
import requests
import urllib.request as ureq
from bs4 import BeautifulSoup as bs
import pandas as pd
import re

def sort_tracks():
    best_songs_url = "https://pitchfork.com/features/lists-and-guides/best-songs-2021/"

    content = ureq.urlopen(best_songs_url).read()
    soup = bs(content, "html.parser")
    headers = soup.find_all('h2')

    sort_tracks.tracks = list(map(lambda h: h.text.strip(), headers))

def rank_list():
    global rank_artist_track_list
    
    list = pd.DataFrame(sort_tracks.tracks)
    clean_list = pd.DataFrame(list[0].str.split(':', expand=True).values, columns=['artist', 'track'])
    clean_list['track'] = clean_list['track'].map(lambda x: x[1:-1].replace('“', ''))

    result = []
    total_rank = len(clean_list)
    for row in clean_list['track']:
        rank = total_rank
        total_rank -= 1
        result.append(rank)
    clean_list['rank'] = result
    sort_list = clean_list[['rank','artist','track']]
    rank_artist_track_list = sort_list.values.tolist()
    
sort_tracks()
rank_list()