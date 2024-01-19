import customtkinter as ctk
from download import Download


class App(ctk.CTk):

    def __init__(self) -> None:
        super().__init__()

        self.download_instance = Download(self)

        self.geometry('600x400')
        self.title('Video Downloader')

        title_label = ctk.CTkLabel(self, text='Video Downloader',
                                   text_color='#fff', font=("Calibri", 24, "bold"))
        title_label.pack(pady=20)

        entry_link = ctk.CTkEntry(self, width=500)
        entry_link.pack(pady=15)

        button_add_video_in_queue = ctk.CTkButton(self, text='Adicionar a fila',
                                                  height=50, width=200, command=lambda: self.download_instance.add_video_in_queue(entry_link))
        button_download_queue = ctk.CTkButton(self, text='Download',
                                              height=50, width=200, command=self.download_instance.download_queue)
        button_add_video_in_queue.pack(pady=10)
        button_download_queue.pack(pady=10)


if __name__ == '__main__':
    app = App()
    app.mainloop()
