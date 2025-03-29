import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

client_credentials_manager = SpotifyClientCredentials(client_id="25dc74bf43dc49fd9e569d92b4430a39", client_secret="af744f45cda04d338da5f1edeb2ddbae")

sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF?si=1333723a6eff4b7f"

playlist_URI = playlist_link.split("/")[-1].split('?')[0]

data = sp.playlist_tracks(playlist_URI)

data['items']

