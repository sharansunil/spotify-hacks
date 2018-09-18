import spotifyInit as spi 
import pandas as pd
import numpy as np
import itertools


def init():
	sp= spi.genAuth()
	spo = sp[0]
	username = sp[1]
	return spo,username

def generateRefSet(init):
	username=init[1]
	sp=init[0]
	playlists=sp.user_playlists(username)
	playlistarray=[]
	for playlist in playlists['items']:
		playname=playlist['name']
		playid=playlist['id']
		results = sp.user_playlist(username,playlist['id'],fields="tracks,next")
		tracks=results['tracks']
		x=spi.show_tracks(playname,playid,tracks)
		playlistarray.append(x)
	plArray=list(itertools.chain(*playlistarray))

	referenceDataset=pd.DataFrame(data=plArray,columns=['Playlist','PlaylistID','Artist','ArtistID','Album','AlbumID','Trackname','TrackID'])
	referenceDataset.index.name = 'ID'
	return referenceDataset


def sliceRefSet(df,segment):
	df1=df[[segment[0],segment[1]]]
	return df1


def generateFeatureSet(df):
    df['Features'] = df.iloc[:, -1]
    sp = spi.genAuth()
    sp = sp[0]
    features = df.iloc[:, -1].apply(sp.audio_features)
    chain = list(itertools.chain(*features))
    featdf = pd.DataFrame(chain)
    trackSet2 = pd.concat(
    	[df.iloc[:, 0:2], featdf], axis=1, join='outer')
    return trackSet2
