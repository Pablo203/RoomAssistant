import spotipy
import webbrowser
import os

class useSpotify:
    def __init__(self):
        self.username = '31cvpctvdtoh57kzurnv3emafqja'
        self.clientId = '9dad35d7cc144001b472518b9ac6d738'
        self.clientSecret = '95bf4812e4af41d695850121273c9344'
        self.redirectURI = 'https://google.com/'

    def getToken(self):
        # Create OAuth Object
        oauth_object = spotipy.SpotifyOAuth(self.clientId, self.clientSecret, self.redirectURI)
        #Create token
        token_dict = oauth_object.get_access_token()
        token = token_dict['access_token']

        #Create Spotify Object
        self.spotifyObject = spotipy.Spotify(auth=token)
        self.user = self.spotifyObject.current_user()

    def use(self):
        self.getToken()
        print("Welcome, " + self.user['display_name'])
        #Get song name
        searchQuery = input("Enter Song Name: ")
        #Search for the song
        searchResults = self.spotifyObject.search(searchQuery,1,0,"track")
        #Get required data from JSON respone
        tracks_dict = searchResults['tracks']
        tracks_items = tracks_dict['items']
        song = tracks_items[0]['external_urls']['spotify']
        #Open the song in webbrowser
        webbrowser.open(song)
        print('Song has opened in your browser')

    def closeMusic(self, name):
        os.system("killall -9 " + name)