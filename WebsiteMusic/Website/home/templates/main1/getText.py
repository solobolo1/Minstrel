import requests
import bs4
import random
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import re
import os
import time
import datetime
import keyboard

f = open('../../static/home/environ.json')

vars = json.load(f)

os.environ['SPOTIPY_CLIENT_ID'] = vars['ID']
os.environ['SPOTIPY_CLIENT_SECRET'] = vars['SECRET']

def line_choose(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)

def to_char_ar(s):
    new = ""
    for x in s:
        new += x
    return new

def clean(input_string):
    pattern1 = r' ,|\[.*?\]|<.*?>'
    result = re.sub(pattern1, '', input_string)

    result = result[3:]
    result = result[:-2]

    char_ar = []
    char_ar.extend(result)

    n=0
    while n < len(char_ar):
        if char_ar[n] == ' ':
            if char_ar[n+1] == ',':
                char_ar[n] = ''
                char_ar[n+1] = ''
        n += 1

    return to_char_ar(char_ar)

def img_link_format(img_link):
    if 'jpg' in img_link:
        img_link = img[3]['src'].split('.jpg')
        img_link[0] += '.jpg'
    elif 'png' in img_link:
        img_link = img[3]['src'].split('.png')
        img_link[0] += '.png'

    sep = img_link[0].split('/')

    for word in sep:
        if word == 'thumb':
            sep.remove(word)

    return '/'.join(sep)

while True:

    name = line_choose('artists.txt')

    name_path = "../../static/main1/name.json"

    with open(name_path, "w") as file:
        json.dump(name, file)

    n = name.split()
    print(n)
    print(to_char_ar(name))

    ####

    link = 'https://en.wikipedia.org/wiki/'

    i = 0

    while i < len(n):
        link = link + n[i] + '_'
        i += 1

    print(link)
    r = requests.get(link)

    soup = bs4.BeautifulSoup(r.content, 'html.parser')

    content = soup.find_all('p', limit=3)

    content = str(content)

    content = clean(content)

    desc_path = "../../static/main1/desc.json"

    with open(desc_path, "w") as file:
        json.dump(content, file)

    img = soup.find_all('img')

    img_path = '../../static/main1/img.json'

    img_link_og = img[3]['src']

    img_link = img_link_format(img_link_og)

    with open(img_path, "w") as file:
        json.dump(img_link, file)

    print(img_link_og)
    print(img_link)

    ####
    
    spotipy = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

    results = spotipy.search(q='artist: ' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        artist = items[0]
        artist_id = artist['id']

    raw_tracks = spotipy.artist_top_tracks(artist_id, country='US')
    top_ids = [None] * 3

    for i in range(3):
        top_ids[i] = raw_tracks["tracks"][i]["id"]

    ids = {
        "id1": ""+top_ids[0],
        "id2": ""+top_ids[1],
        "id3": ""+top_ids[2]
    }

    song_path = "../../static/main2/ids.json"

    with open(song_path, "w") as file:
        json.dump(ids, file)

    restart_time = datetime.time(16, 0)

    while True:
        current_time = datetime.datetime.now().time()

        if current_time >= desired_restart_time:
            console.log('New Artist')
            break
        else if keyboard.is_pressed('e'):
            console.log('Force Quit')
            break
