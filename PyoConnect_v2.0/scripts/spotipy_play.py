from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import spotipy.util as util


scope = 'user-read-currently-playing user-library-read user-read-playback-state user-modify-playback-state'
token = util.prompt_for_user_token("o4w0bk3lbch42k64adwkjeu6m",scope,client_id='004d2df4a7004057b7bb25de5d0f16d4',client_secret='da8ccb946f524db2b2e8862482399995',redirect_uri='http://localhost:8888/callback')

connecteed = False

sp = None   
if token:
    sp = spotipy.Spotify(auth=token)
else:
    print("Can't get token for")


def onPoseEdge(pose, edge):
    if connected:
        print "Another command executing"
        pass
    if pose == 'waveIn':
        print "Hello"
        sp.previous_track()
    elif pose == 'waveOut':
        print "Bye"
        sp.next_track()
    elif pose == 'doubleTap':
        sp.pause_playback()
    connnected = False

    
