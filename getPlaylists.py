import spotifyInit as spi 
import pandas as pd
import numpy as np
import seaborn as sns
import bokeh as bk 
import json 
import itertools

sp= spi.genAuth()


spo = sp[0]
username = sp[1]
playlists = spo.user_playlists(username)

playlistarray=[]
for playlist in playlists['items']:
	playname=playlist['name']
	results = spo.user_playlist(username,playlist['id'],fields="tracks,next")
	tracks=results['tracks']
	x=spi.show_tracks(playname,tracks)
	playlistarray.append(x)

merged=list(itertools.chain(*playlistarray))

colloquialFrame=pd.DataFrame(data=merged,columns=['Playlist','Artist','Album','Trackname'])

 