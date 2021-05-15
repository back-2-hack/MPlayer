from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton,MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from helpers import *
import os
import pygame
from control import *
from crawler import bcrawler
import sys
try:
    os.system('python3 server.py & ')
except:
    try:
        os.system('python server.py & ')
    except:
        print('MPlayer was unable to find python compiler in ur computer...')
        p_path = input('Enter the path where ur python compiler is stored :- ')
        cmd = f'{p_path} server.py & '
        try:
            os.system(cmd)
        except:
            print(f"Didn't found python compiler at {p_path}\nExiting...\n")
            sys.exit()
count = 0
current_song = ''
ftime=True
temp_songs = bcrawler.crawl('/var/www/html/python/Projects/MPlayer/musics')
songs = []
for i in temp_songs:
    x = i.split('/')
    for j in x:
        if j ==x[-1]:
            if j.split('.')[-1]=='mp3':
                songs.append(i)

bnr = '''
<MyTile@SmartTileWithLabel>
    size_hint_y: None
    height: "240dp"


ScrollView:

    MDGridLayout:
        cols: 3
        adaptive_height: True
        padding: dp(4), dp(4)
        spacing: dp(4)
        MyTile:
            source: "icons/msic.png"
            text: "[size=26][color=#ffffff]Cat 3[/color][/size]\n[size=14]cat-3.jpg[/size]"
            tile_text_color: app.theme_cls.accent_color
'''

class MPlayer(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Pink"
        self.theme_cls.theme_style='Dark'

        self.screen = Screen()

        self.play_btn=Builder.load_string(pause)
        self.play_btn.bind(on_press = self.paused)

        self.pause_btn=Builder.load_string(play)
        self.pause_btn.bind(on_press = self.play)

        self.forward=Builder.load_string(forward)
        self.forward.bind(on_press = self.next)
        self.backward=Builder.load_string(backward)
        self.backward.bind(on_press = self.back)
        self.msi=Builder.load_string(msi)

        self.screen.add_widget(self.pause_btn)
        self.screen.add_widget(self.forward)
        self.screen.add_widget(self.backward)
        self.screen.add_widget(self.msi)

        return self.screen

    def play(self,event):
        self.screen.remove_widget(self.pause_btn)
        self.screen.add_widget(self.play_btn)
        print('playing')
        global count
        global current_song
        global ftime
        if ftime==True:
            
            print(songs)
            control(f'play {songs[count]}')
            current_song=songs[count]
            ftime=False
            count = count+1
        else:
            control('unpause')
        return ''

    def paused(self,event):
        self.screen.remove_widget(self.play_btn)
        self.screen.add_widget(self.pause_btn)
        control('pause')
        print('paused')

    def next(self,event):
        global count
        global current_song
        control('stop')
        x = songs.index(current_song)-1
        control(f'play {songs[x]}')
        current_song = songs[x]
        print(songs[x])
        count = count+1
        try:
            self.screen.remove_widget(self.pause_btn)
            self.screen.add_widget(self.play_btn)
        except:
            pass
    def back(self,event):
        global count
        global current_song

        control('stop')

        x = songs.index(current_song)-1
        control('play '+songs[x])

        print('back(2) :-',songs[x])
        current_song = songs[x]
        print('back() :-',songs[x])
        try:
            self.screen.remove_widget(self.pause_btn)
            self.screen.add_widget(self.play_btn)
        except:
            pass

MPlayer().run()