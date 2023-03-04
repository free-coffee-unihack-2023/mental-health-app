# import nltk
# from nltk.sentiment import SentimentIntensityAnalyzer

# # nltk.download('vader_lexicon')

import pandas as pd

songs = pd.read_csv('Song_Database.csv')
database = songs[:2]

trained_database = []

# Python values
tempo_multiplier = 0.8
valence_multiplier = 1
liveness_multiplier = 0
instrumentalness_multiplier = -1
acousticness_multiplier = 0
speechiness_multiplier = 0
loudness_multiplier = 1
energy_multiplier = 0.2
danceability_multiplier = -0.4

class Song:
    def __init__(self, id, dance, energy, loudness, speech, acoustic, instrument, liveness, valence, tempo):
        self.f_score = 0.1
        self.id = id

# F-value
for index in range(0,database.count()):
    row = database.iloc[index]

# # text = 'I was asked to sign a third party contract a week out from stay. If it wasn\'t an 8 person group that took a lot of wrangling I would have cancelled the booking straight away. Bathrooms - there are no stand alone bathrooms. Please consider this - you have to clear out the main bedroom to use that bathroom. Other option is you walk through a different bedroom to get to its en-suite. Signs all over the apartment - there are signs everywhere - some helpful - some telling you rules. Perhaps some people like this but It negatively affected our enjoyment of the accommodation. Stairs - lots of them - some had slightly bending wood which caused a minor injury.'
# happy_text = 'i had a great day'
# sad_text = 'i did not have the greatest, most happy day ever'

# sia = SentimentIntensityAnalyzer()
# happy_results = sia.polarity_scores(happy_text)
# sad_results = sia.polarity_scores(sad_text)

# print("\n")
# print("Happy:", happy_results['compound'])
# print("Sad:", sad_results['compound'])

# print("\nAll results")
# print("Happy:", happy_results)
# print("Sad:", sad_results)