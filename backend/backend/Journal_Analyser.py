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

# for index, row in sorted_list.iterrows():
#     song_score = row[3]

#     if (math.pow(math.pow(sentiment_score - song_score, 2), 0.5)) < lowest_distance:

#         id = row[0]
#         title = row[1]
#         artist = row[2]

#         lowest_distance = sentiment_score - song_score
#         selected_id = id
#         selected_artist = artist
#         selected_title = title
#         selected_score = song_score

# url = "https://open.spotify.com/track/" + str(selected_id)

# print(selected_title, selected_score, selected_artist)