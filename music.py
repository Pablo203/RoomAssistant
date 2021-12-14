import json
import spotipy
import webbrowser

username = '31cvpctvdtoh57kzurnv3emafqja'
clientId = '9dad35d7cc144001b472518b9ac6d738'
clientSecret = '95bf4812e4af41d695850121273c9344'
redirectURI = 'https://google.com/'


class useSpotify:
    def __init__(self):
        self.username = '31cvpctvdtoh57kzurnv3emafqja'
        self.clientId = '9dad35d7cc144001b472518b9ac6d738'
        self.clientSecret = '95bf4812e4af41d695850121273c9344'
        self.redirectURI = 'https://google.com/'

    def getToken(self):
        # Create OAuth Object
        oauth_object = spotipy.SpotifyOAuth(clientId,clientSecret,redirectURI)
        #Create token
        token_dict = oauth_object.get_access_token()
        token = token_dict['access_token']

        #Create Spotify Object
        self.spotifyObject = spotipy.Spotify(auth=token)
        self.user = self.spotifyObject.current_user()

    def use(self):
        self.getToken()
        print("Welcome, " + self.user['display_name'])
        print("0 - Exit")
        print("1 - Search for a song")
        choice = int(input("Your choice: "))
        if(choice == 1):
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
        elif(choice == 0):
            return 0
        else:
            print("Enter valid choice")

x = useSpotify()
x.use()

#To print the response in readable format
#print(json.dumps(user,sort_keys=True, indent=4))

'''while True:
    print("Welcome, " + user['display_name'])
    print("0 - Exit")
    print("1 - Search for a song")
    choice = int(input("Your choice: "))
    if(choice == 1):
        #Get song name
        searchQuery = input("Enter Song Name: ")
        #Search for the song
        searchResults = spotifyObject.search(searchQuery,1,0,"track")
        #Get required data from JSON respone
        tracks_dict = searchResults['tracks']
        tracks_items = tracks_dict['items']
        song = tracks_items[0]['external_urls']['spotify']
        #Open the song in webbrowser
        webbrowser.open(song)
        print('Song has opened in your browser')
    elif(choice == 0):
        break
    else:
        print("Enter valid choice")'''