#!/usr/bin/env python3
import requests
import urllib.request as ureq
from bs4 import BeautifulSoup as bs

best_songs_url = "https://pitchfork.com/features/lists-and-guides/best-songs-2021/"

content = ureq.urlopen(best_songs_url).read()

soup = bs(content, "html.parser")
headers = soup.find_all('h2')

titles = list(map(lambda h: h.text.strip(), headers))

total_rank = len(titles)

for rank, song in enumerate(titles):
    rank = total_rank
    total_rank -= 1
    print(rank, song)
