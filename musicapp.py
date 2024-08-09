import tkinter
import customtkinter
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from pygame import mixer
from customtkinter import filedialog
import os
import tkinter.messagebox as messagebox
mixer.init()
root = customtkinter.CTk()
root.title("Music player")
root.geometry("650x500+350+100")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
root.resizable(0, 0)
current_song_index = 0
path = ""
def browse():
    global path
    path = filedialog.askdirectory()
    if path:
        browse_btn.pack_forget() 
        os.chdir(path)
        songlist.delete(0, END)
        songs = os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                songlist.insert(END, song)
        browse_after_btn.place(relx=0.5, rely=0.67, anchor=tkinter.CENTER)     
                
#function to play music
def playmusic(event=None):
    global path
    global current_song_index
    if songlist.size()>0:
        music_name = songlist.selection_get()
        mixer.music.load(music_name)
        mixer.music.play()
        current_song_index = songlist.curselection()[0] 
        play_btn.place_forget()
        pause_btn.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    else:
        messagebox.showwarning("No Music", "Please select a music folder first.")
        
#function to stop music
def stopmusic():
    mixer.music.stop()
    pause_btn.place_forget()
    play_btn.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    
#function to pause music
def pausemusic():
    mixer.music.pause()
    pause_btn.place_forget()
    play_btn.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    
#function to play next
def nextmusic():
    global current_song_index
    current_song_index += 1
    if current_song_index >= songlist.size():
        current_song_index = 0
    songlist.selection_clear(0, END)
    songlist.selection_set(current_song_index)
    playmusic()
    
#function to play previous
def previousmusic():
    global current_song_index
    current_song_index -= 1
    if current_song_index < 0:
        current_song_index = songlist.size() - 1
    songlist.selection_clear(0, END)
    songlist.selection_set(current_song_index)
    playmusic()

img = ImageTk.PhotoImage(Image.open("assets/bg.jpg").resize((650, 500), Image.Resampling.LANCZOS))
background_image = customtkinter.CTkLabel(root, text="", image=img)
background_image.pack()

main_label = customtkinter.CTkLabel(background_image, font=('Courier New', 40, 'bold'), text="Music Player", padx=10, text_color="Yellow3")
main_label.place(relx=0.5, y=50, anchor=tkinter.CENTER)

songframe = customtkinter.CTkFrame(background_image, width=400, height=200)
songframe.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)

Scroll = Scrollbar(songframe)
Scroll.pack(side=RIGHT, fill=Y)

songlist = tk.Listbox(songframe, yscrollcommand=Scroll.set, selectbackground="blue", width=60, height=10, font=('Times New Roman', 10, 'bold'))
songlist.pack(side=LEFT, fill=BOTH)

Scroll.config(command=songlist.yview)

browse_btn = customtkinter.CTkButton(songlist, text="Browse Music", cursor="hand2", height=80, font=('Courier New', 30, 'bold'), fg_color="Yellow3", text_color="black", command=browse)
browse_btn.pack()

songlist.bind("<<ListboxSelect>>", playmusic)

browse_after_btn = customtkinter.CTkButton(background_image, text="Browse Music", font=('Courier New', 20, 'bold'), height=40, command=browse)
browse_after_btn.place_forget()

button_frame = customtkinter.CTkFrame(root, width=450, height=100, fg_color="transparent")
button_frame.place(relx=0.5, rely=0.83, anchor=tkinter.CENTER)

play = ImageTk.PhotoImage(Image.open("assets/play.png").resize((50, 50), Image.Resampling.LANCZOS))
pause = ImageTk.PhotoImage(Image.open("assets/pause.png").resize((50, 50), Image.Resampling.LANCZOS))
next = ImageTk.PhotoImage(Image.open("assets/next.png").resize((50, 50), Image.Resampling.LANCZOS))
prev = ImageTk.PhotoImage(Image.open("assets/previous.png").resize((50, 50), Image.Resampling.LANCZOS))

play_btn = customtkinter.CTkLabel(button_frame, image=play, text="", cursor="hand2")
play_btn.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
play_btn.bind("<Button-1>", lambda e: stopmusic() if mixer.music.get_busy() else playmusic())

pause_btn = customtkinter.CTkLabel(button_frame, image=pause, text="", cursor="hand2")
pause_btn.place_forget()  # Initially hide the pause button
pause_btn.bind("<Button-1>", lambda e: pausemusic())

prev_btn = customtkinter.CTkLabel(button_frame, image=prev, text="", cursor="hand2")
prev_btn.place(relx=0.35, rely=0.5, anchor=tkinter.CENTER)
prev_btn.bind("<Button-1>", lambda e: previousmusic())

next_btn = customtkinter.CTkLabel(button_frame, image=next, text="", cursor="hand2")
next_btn.place(relx=0.65, rely=0.5, anchor=tkinter.CENTER)
next_btn.bind("<Button-1>", lambda e: nextmusic())

root.mainloop()
