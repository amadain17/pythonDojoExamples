import pygame as pg
import os
import tkinter as tk
from tkinter import ttk

class MusicPlayer():
    def __init__(self, musicdir="/home/mfmdevine/Music/music", volume=0.8):
        self.musicdir=musicdir
        self.volume=volume
        self.musicFiles=self.getMusicFiles()
        self.pg=pg.mixer
        self.pg.init(44100, -16, 2, 2048)


    def play_music(self):
        music_file=self.musicdir+"/"+self.musicFiles[self.entryNum.get()]

        self.pg.music.set_volume(self.volume)
        clock = pg.time.Clock()
        try:
            self.pg.music.load(music_file)
            print("Music file {} loaded!".format(music_file))
        except pg.error:
            print("File {} not found! ({})".format(music_file, pg.get_error()))
            return
        print("Playing " + music_file.split('/')[-1])
        self.pg.music.play()
        while self.pg.music.get_busy():
            clock.tick(12000)
        print("finished")

    def stop_music(self):
        self.pg.music.stop()

    def getMusicFiles(self):
        musicDict={}
        for file in os.listdir(self.musicdir):
            if file.endswith("mp3"):
                key=file.replace("_", " ").split(".")[0]
                musicDict[key]=file
        return musicDict

    def startApp(self):
        root = tk.Tk()
        root.geometry('500x100+100+200')
        root.title('Rathdrum Dojo Music Player')
        gui_style = ttk.Style()
        gui_style.theme_use('clam')
        self.innerFrame(root)
        root.mainloop()

    def innerFrame(self, root):
        frm = ttk.Frame(root)
        frm.pack(expand=True, fill='both')

        labelTitle = ttk.Label(frm, text="Pick a song to play:").grid(row=0, column=2)
        labelNum = ttk.Label(frm, text="  SongList", width=10).grid(row=1, column=0)

        self.entryNum = ttk.Combobox(frm, values=list(self.musicFiles.keys()), width=40)
        self.entryNum.grid(row=1, column=2)
        self.entryNum.current(0)

        buttonPlay = ttk.Button(frm, text="Play", command=self.play_music).grid(row=4, column=2)
        #buttonStop = ttk.Button(frm, text="Stop", command=self.stop_music).grid(row=5, column=2)


if __name__=="__main__":
    MusicPlayer().startApp()
