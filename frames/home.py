import ttkbootstrap as ttk
from tkinter import ttk as tkinterttk
import tkinter as tk

import database
import frames
from PIL import Image, ImageTk
import settings
import utils.navigation, utils.placement


class Home(ttk.Frame):

    def __init__(self, app) -> None:
        super(Home, self).__init__(master=app)
        self.app = app

        self.style = ttk.Style()
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.top_frame = ttk.Frame(self, bootstyle=settings.HOME_BOOTSTYLE_BG)
        self.top_frame.grid(row=0, column=0, sticky="NSEW")
        self.top_frame.grid_rowconfigure(0, weight=1)
        self.top_frame.grid_columnconfigure(0, weight=1)

        self.top_frame.bind("<Button->", lambda event: self.app.show_page(frames.choose_package.PackagePicker))

        self._title(title="BeginnerLuft 1.0")
    
    def _title(self, title: str) -> None:
        """
        Place a title on the page
        :param title: the title for the page
        """

        title = ttk.Label(self.top_frame, text=title, bootstyle=settings.HOME_BOOTSTYLE_TITLE_FG, cursor="hand2",
                          font=(settings.FONT, settings.FONT_SIZE_XXXL), justify="center")
        title.grid(row=0, column=0)
        title.bind("<Button->", lambda event: self.app.show_page(frames.choose_package.PackagePicker))

        active_environment = ttk.Label(self.top_frame, text=f"- {self.app.active_environment} -", 
            bootstyle=settings.HOME_BOOTSTYLE_TITLE_FG, 
        font=(settings.FONT, settings.FONT_SIZE_S))
        active_environment.grid(row=1, column=0, pady=(0, 50))



