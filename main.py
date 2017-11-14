__author__ = 'Abhi Gupta'

import pafy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy
import time
import sys


# can get duration of video using video.duration

# url = "https://www.youtube.com/watch?v=kfVsfOSbJY0"
# video = pafy.new(url)

# audiostreams = video.audiostreams
# for currAudio in audiostreams:
#     print("{} {} {} ".format(currAudio.bitrate, currAudio.extension, currAudio.get_filesize()))
# print(video.title)


class Downloader:
    def __init__(self):
        pass

    def search(self):
        sp = spotipy.Spotify()
        results = sp.search(q='weezer', limit=20)
        for i, t in enumerate(results['tracks']['items']):
            # print(' ', i, t['name'])
            print("{} {}".format(i, t['name']))
            return


if __name__ == "__main__":
    # Downloader().search()
    spotify = spotipy.Spotify()

    if len(sys.argv) > 1:
        name = ' '.join(sys.argv[1:])
    else:
        name = 'Radiohead'

    results = spotify.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        artist = items[0]
        print(artist['name'], artist['images'][0]['url'])
