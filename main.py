#encoding:utf-8

import urllib2
import sys
import re
import random
import os
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import zipfile

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

def descargar(videoId, playlistId, songName):
    url = "https://youtubemp3api.com/es/@api/button/mp3/" + videoId
    
    browser = webdriver.PhantomJS()
    browser.get(url)
    
    time.sleep(20)
    
    html = browser.page_source
    
    soup = BeautifulSoup(html, 'html.parser')
    
    download_link = soup.find('a',{'class':'download-mp3-url btn audio q320'})['href']

    mp3file = urllib2.urlopen(download_link)
    with open('./files/'+str(playlistId)+'/'+songName+'.mp3','wb') as output:
        output.write(mp3file.read())

def ejecutar():
    songs = sys.argv[1]
    ids = []
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
    playlistId = random.getrandbits(16)
    songs = songs.split('\n')
    numero = len(songs)
    
    for i, song in enumerate(songs):
        print song
        progreso = str(i * 100 / numero) + "% (" + str(i) + "/" + str(numero) + ")"
        print progreso
        
        if not os.path.exists("files"):
            os.mkdir("files")
        if not os.path.exists("files/"+str(playlistId)):
            os.mkdir("files/"+str(playlistId))
        with open('./files/'+str(playlistId)+'/log', "wb") as f:
            f.write(progreso)
            
        req = urllib2.Request("https://www.googleapis.com/youtube/v3/search?part=snippet&q="+song.replace(" ","+")+"&type=video&key=AIzaSyAfGR_cKX3hrd59oLofgLPT9dx9_wy7wzM", headers=headers)
        response = urllib2.urlopen(req)
        html = response.read()
        songYouTubeVideoId = re.findall(r'"videoId": "(.+)"',html)[0]
        ids.append(songYouTubeVideoId)
        descargar(songYouTubeVideoId, playlistId, song)
    
    zipf = zipfile.ZipFile(str(playlistId) + '.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir('./files/'+str(playlistId)+'/', zipf)
    zipf.close()
    
    with open('./files/'+str(playlistId)+'/log', "wb") as f:
        f.write("http://188.226.183.56/StreamMusic/" + str(playlistId) + ".zip")
        
    return (playlistId, ids)


if __name__ == "__main__":
    print ejecutar()