from src.lyrics import *

scope = 'user-read-currently-playing'
username = 'danya.scout'
client_id = 'e9e3e856adaa497fa671f3fa8c9996ff'
client_secret = '233d79463dd040228ea5f98d3e19eb01'
redirect_uri = 'http://localhost:8888/callback/'
client_access_token = 'wIRZZio3TmJHGS2KMluqh0Y8ncwKatMf1EGn8-n2Nw7UrPRdcxJ-ZLU3g3GGUIWA'

get_lyrics(scope, username, client_id, client_secret, redirect_uri, client_access_token)

with open('lyrics.json', 'r') as openfile:
    lyrics = json.load(openfile)['lyrics']

print(f'\n{lyrics}\n')
