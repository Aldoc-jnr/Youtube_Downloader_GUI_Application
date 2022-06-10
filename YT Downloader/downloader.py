from os import path
from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube

import shutil

# external modules needed:
# pip install moviepy
# pip install pytube

# Function 1: A function to allow user to select file path from file explorer/finder
def specify_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)

# Function 2: A function that downloads the video
def download_file():
    # fetch video link
    get_link = link_field.get()
    # fetch selected file path
    user_path = path_label.cget("text")

    # Download video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    screen.title('Downloading Video... Please wait!')
    # Assign a file name
    jet_vid = VideoFileClip(mp4_video)
    jet_vid.close()
    # Send file to specified directory/path
    shutil.move(mp4_video, user_path)
    screen.title('Download Complete!')



screen = Tk()
title = screen.title('JetM YouTube Downloader')
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

# logo image
logo_img = PhotoImage(file='yt.png')

# resize image to suitable dimension
logo_img = logo_img.subsample(2, 2)
canvas.create_image(250, 80, image=logo_img)

# Video link capture field
link_field = Entry(screen, width=60)
link_label = Label(screen, text="Paste video link here! ", font=('Poppins', 16))

# Specify download file path
path_label = Label(screen, text="Specify save location ", font=('Poppins', 16))
specify_btn = Button(screen, text="Specify", command=specify_path)

# Add Download Buttons
download_btn = Button(screen, text="Download Video", command=download_file)

# Add the link field widget to the canvas
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 200, window=link_field)

# Add the file path widget to the canvas
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 315, window=specify_btn)

# Add the download btn widget to the canvas
canvas.create_window(250, 390, window=download_btn)



screen.mainloop()