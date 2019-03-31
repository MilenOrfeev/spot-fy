import sys
import spotipy
import spotipy.util as util
from read_microbit import scanVariable, tooFar

#scope = 'user-library-read' 

def doSpotify():
    if token:
        temperature, light = scanVariable()
        if temperature == -1:
            raise Exception("Couldn't read temperature")
        if  light == -1:
            raise Exception("Couldn't read temperature")
        if temperature>=20 and light>=220:
            category = 'Minions'
        elif temperature<=10 and light>=220:
            category = 'Beauty and the beast'
        elif temperature>=20 and light>144 and light<=220:
            category = 'Rainy'
        elif temperature>=10 and temperature<=20 and light>=144 and light<220:
            category ='Brave'
        elif temperature>=20 and light<=144:
            category='Netflix and chill'
        else:
            category = 'Frozen'
        print ("Choosing playlist for:")
        print ("Temp: {0}, light: {1}, cat: {2}".format(temperature, light, category))
    
        
        sp = spotipy.Spotify(auth=token)
        #results = sp.current_user_saved_tracks()
        playlists = sp.user_playlists(username)
        while playlists:
            for i, playlist in enumerate(playlists['items']):
                if playlist['name'] == category:
                    result = playlist['uri']
                    sp.start_playback(context_uri= result)
                    break
    
            if playlists['next']:
                playlists = sp.next(playlists)
            else:
                playlists = None
    else:
        print ("Can't get token for", username)
    
    isTooFar = tooFar()
    if isTooFar:
        print ("User too far")
        sp.pause_playback()

# START OF CODE
scope = 'user-modify-playback-state'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print ("Usage: {0} username".format(sys.argv[0]))
    sys.exit()

token = util.prompt_for_user_token(username,scope,client_id='004d2df4a7004057b7bb25de5d0f16d4',client_secret='da8ccb946f524db2b2e8862482399995',redirect_uri='http://localhost:8888/callback')
    
while True:
    doSpotify()
