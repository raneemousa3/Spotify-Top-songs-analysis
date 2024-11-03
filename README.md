# Spotify-Top-songs-analysis
Analyzing the users top songs and recommending new songs and artists



Spotify Music Analysis App
Overview
This application allows users to analyze their top songs on Spotify and discover new music recommendations based on audio features. It fetches the user's top tracks using the Spotify API, analyzes audio features such as danceability, energy, valence, and acousticness, and then provides personalized song and artist recommendations.

Features
Extracts user's top songs from Spotify, including audio features.
Visualizes audio features with bar charts.
Provides personalized song recommendations based on the user's music preferences.
Suggests artists based on the genres of the user's top songs.
Requirements
To run this application, you'll need:

Python 3.x
spotipy for Spotify API interactions
streamlit for the web interface
pandas for data manipulation
python-dotenv for environment variable management
You can install the required libraries using pip:

bash
Copy code
pip install spotipy streamlit pandas python-dotenv
Setup
Spotify API Credentials:

Create a Spotify Developer account and create an application to obtain your CLIENT_ID and CLIENT_SECRET.
Set the redirect URI to http://localhost:5100 in your Spotify Developer Dashboard.
Environment Variables:

Create a .env file in the project directory with the following content:
makefile
Copy code
CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
Dataset:

Place your dataset CSV file in the specified path (/Users/raneemmousa/Desktop/openavenues/Create playlist/dataset.csv). The CSV should contain the necessary columns, including track_name, artists, and track_genre.
Usage
Run the Application: Start the Streamlit app by running the following command in your terminal:

bash
Copy code
streamlit run app.py
Replace app.py with the name of your Python script.

Input Number of Songs:

Enter the number of top songs you want to analyze (between 1 and 20).
Analyze Your Top Songs:

The app will fetch your top songs, analyze their audio features, and display the results.
View Recommendations:

The app provides personalized song and artist recommendations based on your listening habits.
Code Explanation
Extract Users' Top Songs: The Extract_users_top_songs function retrieves the user's top tracks and their audio features using the Spotify API.

Create DataFrame: The create_Data_frame function constructs a DataFrame with the retrieved audio features and prepares a playlist of the top songs.

Analysis: The Analysis function calculates average audio features of the user's top songs and visualizes them using bar charts.

Recommendations:

song_recommendations provides song recommendations based on audio feature averages.
artist_recommendations suggests new artists based on the genres of songs the user listens to.
Web Interface: The create_webpage function sets up the Streamlit interface for user interaction.
