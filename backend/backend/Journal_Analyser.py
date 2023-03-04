import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

import pandas as pd
import csv

import math

text = 'flower happy, I am depressed and angry'

sia = SentimentIntensityAnalyzer()
sentiment_score = sia.polarity_scores(text)['compound']

sorted_list = pd.read_csv('Sorted_Database.csv', encoding='latin-1')

lowest_distance = 100
selected_id = ''
selected_title = ''
selected_artist = ''
selected_score = 0

low = 0
high = len(sorted_list)

index = int((high - low) / 2)

while abs(index - high) > 1 and abs(index - low) > 1:

    song_score = sorted_list.iloc[index][3]

    if song_score > sentiment_score:
        high = index
        index = int((high + low) / 2)

    elif song_score < sentiment_score:
        low = index
        index = int((high + low) / 2)

    else:
        break
