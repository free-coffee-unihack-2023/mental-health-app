# import nltk
# from nltk.sentiment import SentimentIntensityAnalyzer

# # nltk.download('vader_lexicon')

import pandas as pd
import csv

songs = pd.read_csv('Song_Database.csv')
database = songs[:60000]

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
    def __init__(self, title, artist, id, dance, energy, loudness, speech, acoustic, instrument, liveness, valence, tempo):
        self.f_score = \
            dance * danceability_multiplier + \
            energy * energy_multiplier + \
            loudness * loudness_multiplier + \
            speech * speechiness_multiplier + \
            acoustic * acousticness_multiplier + \
            instrument * instrumentalness_multiplier + \
            liveness * liveness_multiplier + \
            valence * valence_multiplier + \
            tempo * tempo_multiplier
        self.normalized_f_score = -1
        self.id = id
        self.title = title
        self.artist = artist

# Min/max values 
min_f = 1000
max_f = -1000

validCharacters = "1234567890qwertyuiopasdfghjklzxcvbnm,./?\;:'QWERTYUIOPLKJHGFDSAZXCVBNM"

def isValidName(testString):
    for value in testString:
        if value not in validCharacters:
            return False
    return True

# F-value
for index, row in database.iterrows():

    # if (row['artists'].isalnum() and row['track_name'].isalnum()):
    if (isValidName(row['artists']) and isValidName(row['track_name'])):
        new_song = Song(
            row['track_name'],
            row['artists'],
            row['track_id'],
            row['danceability'],
            row['energy'],
            row['loudness'],
            row['speechiness'],
            row['acousticness'],
            row['instrumentalness'],
            row['liveness'],
            row['valence'],
            row['tempo']
        )

        if new_song.f_score > max_f:
            max_f = new_song.f_score

        elif new_song.f_score < min_f:
            min_f = new_song.f_score

        trained_database.append(new_song)

for entry in trained_database:
    entry.normalized_f_score = 2 * (entry.f_score - min_f) / (max_f - min_f) - 1

trained_database.sort(key=lambda x: x.normalized_f_score)

for i, song in enumerate(trained_database):
    song1 = trained_database[i]

f = open('Sorted_Database.csv', 'w', newline='')

writer = csv.writer(f)

for song in trained_database:
    list_for_append = []
    list_for_append.append(song.id)
    list_for_append.append(song.title)
    list_for_append.append(song.artist)
    list_for_append.append(song.normalized_f_score)

    try:
        writer.writerow(list_for_append)
    except:
        1#print("lol")

f.close()

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