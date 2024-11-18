ChatGPT
🎧 Spotify Top Songs Analysis
🌟 Overview
Spotify Top Songs Analysis is a web application that helps users analyze their favorite Spotify tracks and discover personalized recommendations for songs and artists. Using the Spotify API, the app visualizes audio features like danceability, energy, and valence, enabling users to explore their musical preferences and find new favorites!

✨ Features
🎵 Retrieve and visualize your top Spotify tracks and audio features.
🧠 Personalized Recommendations for songs based on your preferences.
🎤 Discover Artists tailored to the genres of your favorite tracks.
🛠️ Technologies
Backend: Python, Spotipy (Spotify API)
Frontend: Streamlit
Data Processing: Pandas
Environment Management: Python-dotenv
⚙️ Requirements
To run this application, you'll need:

Python 3.x
Required Libraries:
bash
Copy code
pip install spotipy streamlit pandas python-dotenv
🚀 Setup
1️⃣ Spotify API Credentials
Create a Spotify Developer account and set up an application.
Obtain your CLIENT_ID and CLIENT_SECRET.
Set the redirect URI in your Spotify Developer Dashboard to:
arduino
Copy code
http://localhost:5100
2️⃣ Environment Variables
Create a .env file in the project directory.
Add the following credentials to the .env file:
plaintext
Copy code
CLIENT_ID=your_client_id  
CLIENT_SECRET=your_client_secret  
📝 Usage
▶️ Run the Application
Start the Streamlit app by running:

bash
Copy code
streamlit run app.py
🎶 Analyze Songs
Enter the number of top songs you want to analyze (between 1 and 20).
The app will fetch your top songs and display their audio features.
🎧 Get Recommendations
View song recommendations based on audio features.
Discover new artists based on the genres of your favorite tracks.
💡 Code Highlights
🎼 Top Song Extraction
Fetches the user's top tracks and their audio features via the Spotify API.
📊 Data Visualization
Displays average audio features using bar charts for better insights.
🔍 Recommendations
Songs: Suggested based on average audio features like danceability and energy.
Artists: Recommended based on genres in the user's top tracks.
🖥️ Interactive Web Interface
Built with Streamlit for a dynamic and user-friendly experience.
🤝 Contributing
💡 Feel free to fork the repository, open issues, or submit pull requests to enhance the project.

📜 License
This project is open-source and licensed under the MIT License.

🎵 Explore your favorite music and discover new tracks that match your vibe! 🎶







You’ve
