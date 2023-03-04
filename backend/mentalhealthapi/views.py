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

