import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

import pandas as pd
import csv

import math

text = 'I had an extremely happy day'

sia = SentimentIntensityAnalyzer()
sentiment_score = sia.polarity_scores(text)['compound']

sorted_list = pd.read_csv('Sorted_Database.csv', encoding='latin-1')

lowest_distance = 100
selected_id = ''
selected_title = ''
selected_artist = ''
selected_score = 0

for index, row in sorted_list.iterrows():
    id = row[0]
    title = row[1]
    artist = row[2]
    song_score = row[3]

    if (math.pow(math.pow(sentiment_score - song_score, 2), 0.5)) < lowest_distance:
        lowest_distance = sentiment_score - song_score
        selected_id = id
        selected_artist = artist
        selected_title = title
        selected_score = song_score

print(selected_title, selected_score, selected_id)