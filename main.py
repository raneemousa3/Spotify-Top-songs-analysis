import spotipy 
from spotipy.oauth2 import SpotifyOAuth
import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
from songclass import Song
from playlist import Playlist
import urllib.request



from SPOTIFYtoken import get_artist
import time
load_dotenv()

ds=pd.read_csv("/Users/raneemmousa/Desktop/openavenues/Create playlist/dataset.csv")
#print(len(ds))
def Extract_users_top_songs(num):
    """
    Extracts the user's top songs along with their audio features.

    Parameters:
    Number of top songs to retrieve.

    Returns:
    audiofeature: Dictionary containing audio features of the user's top songs, 
    song_id: List of IDs of the user's top songs and top_songs: Dictionary containing
    information about the user's top songs.
    """
    client_id = os.environ.get('CLIENT_ID')
    client_secret= os.getenv("CLIENT_SECRET")

    redirect_uri='http://localhost:5100'
    sp=spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                client_secret=client_secret,
                                                redirect_uri=redirect_uri,
                                                scope='user-top-read,playlist-modify-private ,playlist-modify-public'))
    
    top_songs=sp.current_user_top_tracks(time_range='short_term',limit=num)
    song_id=[song['id'] for song in top_songs['items']]
    song_images_url=[song['album']['images'][0]['url'] for song in top_songs['items']]
    print(song_images_url)
    #print(top_songs['items'][0]['album']['images'][1]['url'])
    audiofeature=sp.audio_features(song_id)
    return audiofeature,song_id,top_songs,song_images_url
def create_Data_frame(audiofeature,song_id,top_songs,image_url):
    """
    Creates a DataFrame containing audio features of songs and a playlist of recommended songs.

    Parameters:
    audiofeature-Dictionary containing audio features of songs
    song_id: List of song IDs.
    top_songs: Dictionary containing top songs information.

    Returns:
    - DataFrame: DataFrame containing audio features of songs and Playlist object containing top songs I listen to.
    """
    df=pd.DataFrame(audiofeature)
    artistsname=pd.DataFrame()
    df['song_name']=[song['name'] for song in top_songs['items']]
    artistsname['artist']=[song['album']['artists'][0]['name'] for song in top_songs['items']]
    df=df[['song_name','danceability','energy','valence','acousticness']]
    recommended_playlist=Playlist("Song Recommendations")
    for i in range(len(df)):
        s=Song(df['song_name'][i],song_id[i],df['danceability'][i],df['energy'][i],df['valence'][i],df['acousticness'][i],artistsname['artist'][i],image_url[i])
        recommended_playlist.playlist.append(s)
    df.set_index('song_name',inplace=True)
    return df,recommended_playlist

def create_webpage():
    st.set_page_config(page_title='top songs analysis', page_icon=':muciscal_note:')
    #st.title("<h5 style='text-align: center;font-family: sans-serif;font-size: small;'>Analysis for your top songs</h5>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: grey;'>Analysis for your top songs</h1>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color: white;'>Learn More about what music interests you</h5>", unsafe_allow_html=True)

  
    num_songs=st.number_input('How many songs would you like to analyse, pick a number between 1-20',1,20,12)
    return num_songs
#print(song_id)
#print(audiofeature)
#print(df)
#df.set_index('song_name',inplace=True)
#print(df['song_name'])
#print(df)
def Analysis(df,recommendedplaylist):
    """
    Analyzes the audio features of a DataFrame of songs and provides recommendations based on those features.

    Parameters:
    - df: DataFrame containing audio features of songs
    - recommendedplaylist: List of songs person listens to.
    - numsong: Number of songs to be analysed

    Returns:
    - dataframe containing average danceability, acousticness, energy, and valence of the analyzed songs.
    """
  

    total_energy=0
    for energy in df['energy']:
        total_energy+=energy
    avg_energy=total_energy/len(df)
    total_acousticness=0
    for acousticness in df['acousticness']:
        total_acousticness+=acousticness
    avg_acouticness=total_acousticness/len(df)
    total_danceability=0
    for danceability in df['danceability']:
        total_danceability+=danceability
    avg_danceability=total_danceability/len(df)
    total_valence=0
    for valence in df['valence']:
        total_valence+=valence
    avg_valence=total_valence/len(df)
    st.subheader('Audio features for your top songs')
    st.bar_chart(df, height=500)
    songs=song_recommendations(avg_valence, avg_danceability, avg_acouticness, avg_energy)
    #Artists=artist_recommendations(recommendedplaylist)
    i=0

    images={}
    
    for song in recommendedplaylist.playlist:
       song.create_spotify_image_path(i)
       images[f'image{i}.jpg']=song.name
       i=i+1
    #st.image(images,width=250, caption=[images[f'image{i}.jpg']] * len(images))
    imageskeys=list(images.keys())
    groups=[]
    for i in range(0,len(images),4):
       groups.append(imageskeys[i:i+4])
    cols=st.columns(4)
    j=0
    for group in groups:
       for i, image in enumerate(group):
          cols[i].image(image)
          cols[i].write("<h5 style='text-align: center;font-family: sans-serif;font-size: small; '>"+images[image]+"</h5>", unsafe_allow_html=True)
       j=j+1

          
    with st.expander("More about the type of songs you listen too:"):
        st.write("<ul>"+f'Average energy: {format(avg_energy, ".2f")} \n Average Danceability: {format(avg_danceability, ".2f")} \n Average Valence: {format(avg_valence, ".2f")} \n Average Acousticness: {format(avg_acouticness, ".2f")}'+ "</ul>" , unsafe_allow_html=True)
        st.write(df)
    with st.expander("Here are songs you might like:"):
        st.write(songs)
   #with st.expander("Here are Artists you should check out:"):
        #st.write(Artists)
    return(avg_danceability,avg_acouticness,avg_energy,avg_valence)
   
    


def song_recommendations(average_valence, average_danceability, average_acousticness, average_energy):
    """
    Provides personalized song recommendations based on specified average values of musical attributes.

    Parameters:
    - takes in average_valence,average_danceability average_acousticness and  average_energy of my top songs.
   
    Returns:
    - recommended_songs: A DataFrame containing recommended songs, along with their artists and genres.
    """
  
    recommended_songs = pd.DataFrame(columns=['song_name', 'artist','Genre'])
   

    # Filter songs based on the given criteria
    for i in range(len(ds)):
     
     if isinstance(ds['danceability'][i],float):
        absdance=abs((ds['danceability'][i] - average_danceability)/average_danceability)
        absvalence=abs((ds['valence'][i] - average_valence)/average_valence)
        absenergy=abs((ds['energy'][i] - average_energy)/average_energy)
        absacouticness=abs((ds['acousticness'][i] - average_acousticness)/average_acousticness)
      

        if absdance < 0.11 and absvalence <0.11 and absacouticness < 0.11 and absenergy<0.11:
          
          if ds['track_name'][i] not in recommended_songs['song_name'].values:
           
            recommended_songs = recommended_songs._append({
                'song_name': ds['track_name'][i],
                'artist': ds['artists'][i],
                'Genre' : ds['track_genre'][i]
            }, ignore_index=True)
  
    return recommended_songs

def artist_recommendations(recommended_playlist):
   

    """
    Recommend artists based on genre I listen to, checks the genre 
    of artists I listen to and gives me artists recommendations based on that

    Parameter: 
    Takes in the persons top songs list

    Returns 
    Artist recommendation and their genre
    """
    x=ds.sample(frac=1, ignore_index=True)
    recommended_artists = pd.DataFrame(columns=['Artist','Genre'])

    # Filter songs based on the given criteria
  #  #print(songs_recommended['Genre']
    
    for song in recommended_playlist.playlist:
        for i in range(100):
            art=get_artist(song.artist) #reds from get_artist function in spotifytoken.py
            artist_genres=art['artists']['items'][0]['genres']
            for artist_genre in artist_genres:
             if artist_genre == x['track_genre'][i]:
                artist = x['artists'][i]
                genre = x['track_genre'][i]
                # Check if artist already exists in recommended_artists
                if artist not in recommended_artists['Artist'].values:
                  if len(recommended_artists)<50:
                    recommended_artists = recommended_artists._append({'Artist': artist, 'Genre': [genre]}, ignore_index=True)
                  else:
                      break
                else:
                    # Update genres for existing artist
                    index = recommended_artists.index[recommended_artists['Artist'] == artist][0]
                    if genre not in recommended_artists.at[index, 'Genre']:
                        recommended_artists.at[index, 'Genre'].append(genre)
            

    return recommended_artists

# Example usage:
    
def main():
    """
    Call functions for streamlit exectution
    """
    num=create_webpage()
    st.balloons ()
    with st.spinner( 'Wait for it...'):
        time.sleep(10)
    audiofeatures,songid,topsongs,song_image_path=Extract_users_top_songs(num)
    df,recommended_playlist=create_Data_frame(audiofeatures,songid,topsongs,song_image_path)
    Analysis(df,recommended_playlist)
main()






