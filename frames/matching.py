import ttkbootstrap as ttk
from tkinter import ttk as tkinterttk

import database
import settings
import utils.navigation, utils.placement

MODULE_STYLE = "primary"

class Matching(ttk.Frame):

    def __init__(self, app) -> None:
        super(Matching, self).__init__(master=app)
        self.app = app

        self.var_first_name = ttk.StringVar()
        self.var_last_name = ttk.StringVar()
        self.var_email = ttk.StringVar()
        self.var_phone = ttk.StringVar()

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
        for i in range(3):
            self.bottom_frame.grid_columnconfigure(i, weight=1)
        self.bottom_frame.grid_rowconfigure(0, weight=1)

        self.part_frame = ttk.Frame(self.bottom_frame, bootstyle="danger")
        self.part_frame.grid(row=0, column=0, sticky="NSEW")
        self.part_frame.grid_rowconfigure(0, weight=1)
        self.part_frame.grid_columnconfigure(0, weight=1)

        self.start_frame = ttk.Frame(self.bottom_frame, bootstyle="warning")
        self.start_frame.grid(row=0, column=1, sticky="NSEW")

        self.coach_frame = ttk.Frame(self.bottom_frame, bootstyle="danger")
        self.coach_frame.grid(row=0, column=2, sticky="NSEW")

        self.bottom_frame.grid_propagate(False)
        self.part_frame.grid_propagate(False)
        self.start_frame.grid_propagate(False)
        self.coach_frame.grid_propagate(False)

        # navigation frame
        navigation_style = "secondary"
        self.nav_frame = ttk.Frame(self, bootstyle=navigation_style)
        self.nav_frame.grid(row=2, column=0, sticky="NSEW")
        self.nav_frame.grid_rowconfigure(0, weight=1)
        for i in range(2):
            self.nav_frame.grid_columnconfigure(i, weight=1)

        # create content
        self._title(title="Matching")
        self._participant()
        self._navigation(nav_style=navigation_style)
    
    def _title(self, title: str) -> None:
        """
        Place a title on the top frame
        :param title: the title for the page
        """
        title = ttk.Label(self.top_frame, text=title, bootstyle="inverse-primary",
                          font=(settings.FONT, settings.FONT_SIZE_XL), justify="center")
        title.grid(row=0, column=0)

    def _participant(self) -> None:
        """
        Create the possibility to enter participant details
        :return None
        """
        frame = ttk.Frame(self.part_frame)
        frame.grid(row=0, column=0)

        # labels
        ttk.Label(frame, text="Teilnehmer:In", font=(settings.FONT, settings.FONT_SIZE_L)).grid(row=0, column=0, columnspan=2, pady=(0, 30), padx=0)
        ttk.Label(frame, text="Vorname").grid(row=1, column=0, sticky="W")
        ttk.Label(frame, text="Nachname").grid(row=3, column=0, sticky="W")
        ttk.Label(frame, text="E-Mail").grid(row=5, column=0, sticky="W")
        ttk.Label(frame, text="Telefon").grid(row=7, column=0, sticky="W")

        # entry widgets
        pady = (5, 20)
        first_name = ttk.Entry(frame, textvariable=self.var_first_name)
        first_name.grid(row=2, column=0, pady=pady)
        last_name = ttk.Entry(frame, textvariable=self.var_last_name)
        last_name.grid(row=4, column=0, pady=pady)
        email = ttk.Entry(frame, textvariable=self.var_email)
        email.grid(row=6, column=0, pady=pady)
        phone = ttk.Entry(frame, textvariable=self.var_phone)
        phone.grid(row=8, column=0, pady=pady, padx=0)

        btn = ttk.Button(frame, text="click me", command=lambda: print(self.var_phone.get()))
        btn.grid(row=9, column=0, columnspan=2)

    def _navigation(self, nav_style: str = "secondary") -> None:
        """
        Display naviagation elements
        :return None
        """
        style = f"inverse-{nav_style}"
        back = utils.navigation.NavToModulePicker(app=self.app, parent=self.nav_frame, style=style, forward=False)
        back.grid(row=0, column=0, sticky="W", padx=(20, 0))

        forward = utils.navigation.NavToParticipantNotes(app=self.app, parent=self.nav_frame, style=style, forward=True)
        forward.grid(row=0, column=1, sticky="E", padx=(0, 20))