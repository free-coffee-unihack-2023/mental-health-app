import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

import pandas as pd
import csv

import math

text = 'the happiest day ever'

sia = SentimentIntensityAnalyzer()
sentiment_score_dict = sia.polarity_scores(text)
sentiment_score = sentiment_score_dict['compound']

sorted_list = pd.read_csv('Sorted_Database.csv', encoding='latin-1')

lowest_distance = 100
selected_id = ''
selected_title = ''
selected_artist = ''
selected_score = 0

low = 0
high = len(sorted_list)

index = int(high / 2)

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

id = sorted_list.iloc[index][0]
title = sorted_list.iloc[index][1]
artist = sorted_list.iloc[index][2]
song_score = sorted_list.iloc[index][3]

selected_id = id
selected_artist = artist
selected_title = title
selected_score = song_score

url = "https://open.spotify.com/track/" + str(selected_id)

def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

g1 = int(sentiment_score_dict['pos'] * 255)
b1 = int(sentiment_score_dict['neg'] * 255)

# r is either matching other two colours to make it neutral or 0 to make it vibrant
r1 = 10
r2 = 60
if sentiment_score_dict['neu'] > 0.5:
    r1 = int(min(255, (g1 + b1) / 2 + 25))
    r2 = int(min(255, (g1 + b1) / 2 - 25))

hexcode1 = rgb_to_hex(r1,g1,b1)
hexcode2 = rgb_to_hex(r2,g1,b1)

# print(hexcode1, hexcode2)

from datetime import *

hour = datetime.now().hour
minute = datetime.now().minute

type = "AM"

if 24 > hour > 11:
    type = "PM"

hour = hour % 12

if hour == 0:
    hour += 12

minute_string = ""

if minute < 10:
    minute_string += "0"

minute_string += str(minute)

return_time = str(hour) + ":" + str(minute_string) + " " + type

print(return_time)
