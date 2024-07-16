import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

URL = "https://www.billboard.com/charts/hot-100/"

date = input("Please enter a date for the songs in YYYY-MM-DD format\n")


response = requests.get(f"{URL}{date}/")

bb_web_page = response.text

soup = BeautifulSoup(bb_web_page, "html.parser")

songs = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in songs]
print(song_names)
#2023-05-06

return_url = "http://example.com"
client = "client"
secret_key = "secret_key"
display_name= "Display_name"

# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id= client,
#                                                client_secret=secret_key,
#                                                redirect_uri=return_url,
#                                                scope="user-library-read"))

# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=client,
        client_secret=secret_key,
        #show_dialog=True,
        cache_path="token.txt",
        username=display_name, 
    )
)
user_id = sp.current_user()["id"]
print(user_id)

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    #print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

print(song_uris)
#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 10", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)        