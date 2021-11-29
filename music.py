import os

songsList = {
    'Watch Dogs': ['Attak', 'Shanghaied', 'On My Own', 'Barricade', 'Black and Yellow', 'One for the Money', 'Riot', 'Oi'],
    'Dave Winkler': ['Numb', 'Zombie', 'One More Light', 'Im with you', 'Wonderwall', 'What Ive done', 'Torn', 'The Scientist', 'Radioactive', 'New Divide', 'Lullaby', 'Human', 'Crawling'],
    'Favs' : ['Scream', 'White Wolf', 'Without wounds', 'Not today', 'El Dinero', 'Last party', 'In the end', 'See me fall', 'Whats the matter', 'Fuck junks', 'Bench', 'Record of decade', 'Youre gonna go far kid', 'Everytime we touch', 'Shots & squats', 'Lost within']
}

class Music:
    def __init__(self, name):
        self.name = name

    def playSong(self):
        os.system("aplay Audio/Songs")

    def playPlaylist(self):
        #os.system("aplay Audio/Songs")
        for i in songsList[self.name]:
            print(i)

temp = Music("Watch Dogs")
temp.playPlaylist()