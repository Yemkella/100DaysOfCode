import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

SPOTIFY_ID = os.environ["SPOTIFY_ID"]
SPOTIFY_SECRET = os.environ["SPOTIFY_SECRET"]
SPOTIFY_DISPLAY_NAME = os.environ["SPOTIFY_DISPLAY_NAME"]

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"
date = input("What date do you want to travel to? Format YYYY-MM-DD: ")
url_selection = f"{BILLBOARD_URL}{date}/"
response = requests.get(url_selection)
website = response.text
soup = BeautifulSoup(website, "html.parser")
songs = soup.select("li ul li h3")
song_titles = [song.getText() for song in songs]
stripped_titles = [song.strip() for song in song_titles]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:3000",
        client_id=SPOTIFY_ID,
        client_secret=SPOTIFY_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username=SPOTIFY_DISPLAY_NAME, 
    )
)
user_id = sp.current_user()["id"]

year = date.split("-")[0]

song_uris = []
for song in stripped_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=SPOTIFY_DISPLAY_NAME, name=f"{date} Billboard 100", public=False)
print(playlist)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)