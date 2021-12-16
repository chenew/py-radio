#!/usr/bin/env python3
import requests
import urllib.request as ureq
from bs4 import BeautifulSoup as bs
import pandas as pd

def sort_tracks():
    best_songs_url = "https://pitchfork.com/features/lists-and-guides/best-songs-2021/"

    content = ureq.urlopen(best_songs_url).read()
    soup = bs(content, "html.parser")
    headers = soup.find_all('h2')

    sort_tracks.tracks = list(map(lambda h: h.text.strip(), headers))

    total_rank = len(sort_tracks.tracks)

    for rank, track in enumerate(sort_tracks.tracks):
        rank = total_rank
        total_rank -= 1
        print(rank, track)

def dataframe():
    df = pd.DataFrame(sort_tracks.tracks)
    df2 = pd.DataFrame(df[0].str.split(':', expand=True).values, columns=['artist', 'track'])
    print(df2)

sort_tracks()
dataframe()