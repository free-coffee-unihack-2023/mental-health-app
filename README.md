# Mind The Music
This repo consists of two parts:
- A mobile applicaiton developed in Flutter.
- A Django backend which performs sentimental analysis and accordingly recommends a song

## Flutter App
Setup Instructions:
- Install Flutter: https://docs.flutter.dev/get-started/install
- Install Android Studio: https://developer.android.com/studio
- Install an Android Emulator: https://developer.android.com/studio/run/emulator
- Open the flutter_app directory in Android Studio and run the app.

## Django Backend
Background:

  The algorithm works by comparing sentiment analysis from nltk with our custom formula, which assesses how appropriate a song would be for a person depending on their mood. A song with a score of 1 is appropriate for an extremely happy mood, whilst -1 is appropriate for someone feeling down. For efficiency reasons, this function is precomputed by the Testing.py script, for ~100k songs, which are stored into the csv file Sorted_Database.csv. This allows fast search on the fly to find the song which most closely fits the analysis from nltk of the journal entry, which is called by the Django backend.
   The algorithm also creates a custom hex code, which appears on the flutter ui page. This hex code reflects the mood of the song as well.
   
Setup Instructions:
- Install Python 3.8: https://www.python.org/downloads/release/python-380/
- We recommend that you use a virtual environment to run the backend. https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/
- In the terminal, change directory to the backend directory:
```
cd backend
```
- Run the server using the following code: 
```
python manage.py runserver
```
