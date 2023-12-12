import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

birdy_uri = 'spotify:artist:13pwqHspIhcy1IcAooefso'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
results = spotify.artist_top_tracks(birdy_uri)

print(spotipy.artist_related_artists(birdy_uri))
