import customtkinter as ctk


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.geometry('600x400')
        self.title('Video Downloader')

        title_label = ctk.CTkLabel(self, text='Video Downloader',
                                   text_color='#fff', font=("Calibri", 24, "bold"))
        title_label.pack(pady=20)

        entry_link = ctk.CTkEntry(self, width=500)
        entry_link.pack(pady=15)

        button_add = ctk.CTkButton(self, text='Adicionar a fila',
                                   height=50, width=200,)
        button_down = ctk.CTkButton(self, text='Download',
                                    height=50, width=200,)
        button_add.pack(pady=10)
        button_down.pack(pady=10)


if __name__ == '__main__':
    app = App()
    app.mainloop()
