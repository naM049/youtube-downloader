from pytube import YouTube
from os import strerror
import tkinter as tk
from tkinter import filedialog


def download_video(url, path=''):
    try:
        yt = YouTube(url)
        print(f"Downloading {yt.title}...")
        streams = yt.streams.filter(progressive=True, file_extension='mp4')
        highest_resolution = streams.get_highest_resolution()
        highest_resolution.download(output_path=path)
        print(f"{yt.title} has been downloaded successfully!")
    except Exception as e:
        print(f"An error occurred: {strerror(e.errno)}")


def open_file_dialog():
    path = filedialog.askdirectory()
    if path == '':
        print("No folder selected. Exiting...")
        exit()
    print(f"Selected folder: {path}")
    return path

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    url = input("Enter the video URL: ")
    path = open_file_dialog()
    download_video(url, path)