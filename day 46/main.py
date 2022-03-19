
from bs4 import BeautifulSoup
import requests

WELCOME_TEXT = "Musical Time Machine"
PROMPT = "In which year would you like to travel? Enter a date in the form YYYY-DD-MM"
print(f"\n{WELCOME_TEXT}\n\n")
user_input = input(f"{PROMPT}: ")
response = requests.get(url=f"https://billboard.com/charts/hot-100/{user_input}/")
board = response.text
soup = BeautifulSoup(board, "html.parser")

# Get billboard top 100 table
table = soup.find_all("div", class_="o-chart-results-list-row-container")
top100 = [item.find("h3").getText().strip("\n") for item in table]

# print first 100

import spotipy
Client_ID = "769f8e8fa99b4528abc47de035dc18f7"
Client_Secret = "891ebf4dd8c74305beb100b757412680"
redirected_uri = "http://example.com"
scope = "playlist-modify-private"
token_id = "BQABIbfAnnyw5VxiU_5_Y0srYT5gWLsdIUFeUxW-dWLKLXcc8sRFxAtTMOJ7cXXOaBJZQeeOwBKS8ECgcL9452jtEcpB68SBop4_K6huuANwLUUzKE0IGBr3ebNv1vtKA-mDlzrmqFiwziT1gTxEBgEvFI7hEwWr5PqzyXpToZrdpxcg0kWEGfVGuF3EFgg9tywrUQ"
#Spotify Authentication
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=scope,
        redirect_uri="http://example.com",
        client_id=Client_ID,
        client_secret=Client_Secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
#Searching Spotify for songs by title

year = user_input.split('-')[0]
song_uri = []
for track in top100:
    result = sp.search(f"track:{track} year:{year}",type="track")
    try:
        uri = result['tracks']['items'][0]["uri"]
        song_uri.append(uri)
    except:
        print("Not found song on spotify skiping!")
#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{user_input} Billboard {len(song_uri)}",
                        public=False)

#Adding playlist
sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist["id"], tracks = song_uri)
