from pytube import YouTube
import customtkinter as ctk
from tkinter.filedialog import askdirectory
import asyncio


class Download:

    def __init__(self, instance) -> None:
        self.video_queue = []
        self.instance = instance

    def add_video_in_queue(self, entry_link: ctk.CTkEntry):
        print('teste')
        if len(entry_link.get()) == 0:
            return
        link = entry_link.get()

        try:
            yt = YouTube(link)
            video_title = yt.title
            video_time = self.get_video_duration(yt)

            if link not in self.video_queue:
                self.video_queue.append(link)
                self.getText_and_time(video_title, video_time)
                print(self.video_queue)
        except:
            entry_link.delete(0, 'end')
            return

        entry_link.delete(0, 'end')

    def download_queue(self):
        print('teste')
        if len(self.video_queue) == 0:
            return
        path = askdirectory(title='Selecione o diretório para salvar os videos')
        for i in self.video_queue:
            yt = YouTube(i)
            yt = yt.streams.get_highest_resolution()
            yt.download(path)
        self.video_queue.clear()

    def getText_and_time(self, title, time):
        label_video_title = ctk.CTkLabel(
            self.instance, text=f"{len(self.video_queue)} - {title} - ({time})", text_color='#fff')
        return label_video_title.pack()

    def get_video_duration(self, yt_class: YouTube):
        try:
            yt = yt_class

            duration_in_seconds = yt.length

            duration_formatted = f'{str(int(duration_in_seconds // 3600))}:{str(int((duration_in_seconds % 3600) // 60))}:{str(int(duration_in_seconds % 60))}'

            return duration_formatted

        except:
            return
