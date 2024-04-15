
import urllib.request
class Song():
    """Track represents a piece of music."""

    def __init__(self, name, song_id, danceability,energy,valence,acousticness,artist,image_path):
        """
        :param name (str): Track name
        :param id (int): Spotify track id
        :param artist (str): Artist who created the track
        """
        self.name = name
        self.id = song_id
        self.artist = artist
        self.danceability=danceability
        self.energy=energy
        self.valence=valence
        self.acousticness=acousticness
        self.imagepath=image_path
        

    def create_spotify_image_path(self,i):
        urllib.request.urlretrieve(self.imagepath, f'image{i}.jpg')
       
    def song_analysis(self):
        return f'danceability of song:{self.danceability} /n,energy of song: {self.energy}/n,song positvity: {self.valence}/n,song acousticness: {self.acousticness}'

    def __str__(self):
        return self.name + " by " + self.artist
    

   
               



