from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
import json

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

import pandas as pd
import csv
import math

class MusicAPI(APIView):
     def post(self, request, *args, **kwargs):
        text = request.data.get('text')
  
        try: 
            sia = SentimentIntensityAnalyzer()
            sentiment_score = sia.polarity_scores(text)['compound']

            sorted_list = pd.read_csv('Sorted_Database.csv', encoding='latin-1')

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

            id = sorted_list.iloc[0]
            title = sorted_list.iloc[1]
            artist = sorted_list.iloc[2]
            song_score = sorted_list.iloc[3]

            selected_id = id
            selected_artist = artist
            selected_title = title
            selected_score = song_score

            url = "https://open.spotify.com/track/" + str(selected_id)

            result = {"song_name": selected_title,
                      "artist": selected_artist,
                      "url": url,
                      "score": selected_score}
            
            response = HttpResponse(json.dumps(result), content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename=export.json'
            return response
        except:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

