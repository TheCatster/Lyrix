import spotipy
import spotipy.util as util
import lyricsgenius
import json


def get_lyrics(scope, username, client_id, client_secret, redirect_uri, client_access_token):
    genius = lyricsgenius.Genius(client_access_token=client_access_token)
    token = util.prompt_for_user_token(username=username, scope=scope, client_id=client_id, client_secret=client_secret,
                                       redirect_uri=redirect_uri)

    spotify = spotipy.Spotify(auth=token)
    current_track = spotify.current_user_playing_track()

    artist = current_track['item']['artists'][0]['name']
    name = current_track['item']['name']

    song = genius.search_song(title=name, artist=artist)

    lyrics = {'lyrics': song.lyrics}

    json_object = json.dumps(lyrics, indent=4)

    with open('lyrics.json', 'w') as outfile:
        outfile.write(json_object)
