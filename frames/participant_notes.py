import ttkbootstrap as ttk
from tkinter import ttk as tkinterttk

import database
import settings
import utils.navigation, utils.placement

MODULE_STYLE = "primary"

class Notes(ttk.Frame):

    def __init__(self, app) -> None:
        super(Notes, self).__init__(master=app)
        self.app = app

        self.style = ttk.Style()

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=12)
        self.grid_rowconfigure(2, weight=1)
        
        self.top_frame = ttk.Frame(self, bootstyle="primary")
        self.top_frame.grid(row=0, column=0, sticky="NSEW")
        self.top_frame.grid_rowconfigure(0, weight=1)
        self.top_frame.grid_columnconfigure(0, weight=1)

        self.bottom_frame = ttk.Frame(self)
        self.bottom_frame.grid(row=1, column=0, sticky="NSEW")
        self.bottom_frame.grid_columnconfigure(0, weight=1)

        self.bottom_frame.grid_propagate(False)

        # navigation frame
        navigation_style = "secondary"
        self.nav_frame = ttk.Frame(self, bootstyle=navigation_style)
        self.nav_frame.grid(row=2, column=0, sticky="NSEW")
        self.nav_frame.grid_rowconfigure(0, weight=1)
        for i in range(2):
            self.nav_frame.grid_columnconfigure(i, weight=1)

        # create content
        self._title(title="Coaching-Notizen")
        self._notes()
        self._navigation(nav_style=navigation_style)
    
    def _title(self, title: str) -> None:
        """
        Place a title on the top frame
        :param title: the title for the page
        """
        title = ttk.Label(self.top_frame, text=title, bootstyle="inverse-primary",
                          font=(settings.FONT, settings.FONT_SIZE_XL), justify="center")
        title.grid(row=0, column=0)

    def _notes(self) -> None:
        """
        Allow for text entry into two fields
        """
        frame = ttk.Frame(self.bottom_frame)
        frame.grid(row=0, column=0)

        header_wishes = ttk.Label(frame, text="Besondere Wünsche", font=(settings.FONT, settings.FONT_SIZE_L), bootstyle="secondary")
        header_wishes.grid(row=0, column=0, pady=(150, 0))
        header_other = ttk.Label(frame, text="Sonstige Besonderheiten", font=(settings.FONT, settings.FONT_SIZE_L), bootstyle="secondary")
        header_other.grid(row=0, column=1, pady=(150, 0))

        notes_wishes = ttk.Text(frame, height=7, width=40)
        notes_wishes.grid(row=1, column=0, pady=(20, 0), padx=(0, 30))
        self.app.notes_wishes = notes_wishes

        notes_other = ttk.Text(frame, height=7, width=40)
        notes_other.grid(row=1, column=1, pady=(20, 0))
        self.app.notes_other = notes_other


    def _navigation(self, nav_style: str = "secondary") -> None:
        """
        Display naviagation elements
        :return None
        """
        style = f"inverse-{nav_style}"
        back = utils.navigation.NavToMatching(app=self.app, parent=self.nav_frame, style=style, forward=False)
        back.grid(row=0, column=0, sticky="W", padx=(20, 0))

        forward = utils.navigation.NavToOverview(app=self.app, parent=self.nav_frame, style=style, forward=True)
        forward.grid(row=0, column=1, sticky="E", padx=(0, 20))
