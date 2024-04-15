from songclass import Song
class Playlist:
    """Playlist represents a Spotify playlist."""

    def __init__(self, name):
        """
     Playlist name
     playlist
        """
        self.name = name
        self.playlist=[]

    def __str__(self):
        '''Playlist Name'''
        return f"Playlist: {self.name}"