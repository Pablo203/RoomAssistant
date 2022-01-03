import spotipy
import webbrowser
import os
import speech
import talk


import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class useSpotify:
    def __init__(self):
        self.username = 'SPOTIFY_API_USERNAME'
        self.clientId = 'SPOTIFY_CLIENT_ID'
        self.clientSecret = 'SPOTIFY_SECRET_CLIENT_ID'
        self.redirectURI = 'SPOTIFY_REDIRECT_URI'

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
        recognition = speech.Recognize()
        
        try:
            recognized = recognition.recognize()
            #Get song name
            searchQuery = recognized
            #Search for the song
            searchResults = self.spotifyObject.search(searchQuery,1,0,"track")
            #Get required data from JSON respone
            tracks_dict = searchResults['tracks']
            tracks_items = tracks_dict['items']
            song = tracks_items[0]['external_urls']['spotify']
            #Open the song in webbrowser
            #webbrowser.open(song)
            driver = webdriver.Chrome()
            driver.get(song)
            #driver.switch_to_window(driver.window_handles[0])
            elem = driver.find_elements_by_xpath("/html/body/div[4]/div/div[2]/div[1]/header/div[4]/button[2]")
            print(elem)
            elem[0].click()
            #driver.close()
            print('Song has opened in your browser')
        except IndexError:
            talk.tellSentence("Podałeś złą nazwę piosenki")


    def closeMusic(self, name):
        os.system("killall -9 " + name)