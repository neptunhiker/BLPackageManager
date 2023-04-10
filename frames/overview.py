import ttkbootstrap as ttk
from tkinter import ttk as tkinterttk

import database
import settings
import utils.navigation, utils.placement

MODULE_STYLE = "primary"

class Overview(ttk.Frame):

    def __init__(self, app) -> None:
        super(Overview, self).__init__(master=app)
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
        self.bottom_frame.grid_columnconfigure(2, weight=1)
        self.bottom_frame.grid_columnconfigure(4, weight=1)
        self.bottom_frame.grid_rowconfigure(0, weight=1)
        self.bottom_frame.grid_rowconfigure(2, weight=1)

        self.frame_01 = ttk.Frame(self.bottom_frame, bootstyle="seondary")
        self.frame_01.grid(row=0, column=0, sticky="NSEW")
        ttk.Separator(self.bottom_frame, orient="vertical").grid(row=0, column=1, rowspan=3, sticky="NS", pady=20)
        self.frame_02 = ttk.Frame(self.bottom_frame, bootstyle="seondary")
        self.frame_02.grid(row=0, column=2, sticky="NSEW")
        ttk.Separator(self.bottom_frame, orient="vertical").grid(row=0, column=3, rowspan=3, sticky="NS", pady=20)
        self.frame_03 = ttk.Frame(self.bottom_frame, bootstyle="seondary")
        self.frame_03.grid(row=0, column=4, sticky="NSEW")
        ttk.Separator(self.bottom_frame, orient="horizontal").grid(row=1, column=0, columnspan=5, sticky="EW", padx=20)
        self.frame_04 = ttk.Frame(self.bottom_frame, bootstyle="seondary")
        self.frame_04.grid(row=2, column=0, sticky="NSEW")
        self.frame_05 = ttk.Frame(self.bottom_frame, bootstyle="seondary")
        self.frame_05.grid(row=2, column=2, sticky="NSEW")
        self.frame_06 = ttk.Frame(self.bottom_frame, bootstyle="seondary")
        self.frame_06.grid(row=2, column=4, sticky="NSEW")

        frames = [self.frame_01, self.frame_02, self.frame_03, self.frame_04, self.frame_05, self.frame_06]
        for frame in frames:
            frame.grid_columnconfigure(0, weight=1)
            frame.grid_propagate(False)
        self.bottom_frame.grid_propagate(False)

        # navigation frame
        navigation_style = "secondary"
        self.nav_frame = ttk.Frame(self, bootstyle=navigation_style)
        self.nav_frame.grid(row=2, column=0, sticky="NSEW")
        self.nav_frame.grid_rowconfigure(0, weight=1)
        for i in range(2):
            self.nav_frame.grid_columnconfigure(i, weight=1)

        # create content
        self._title(title="Coaching-Überblick")
        self._package()
        self._coaching_period()
        self._modules()
        self._coach()
        self._participant()
        self._notes()
        self._navigation(nav_style=navigation_style)
    
    def _package(self) -> None:
        """
        Display details about the chosen package
        :return None
        """
        header = ttk.Label(self.frame_01, text="Coaching-Paket", font=(settings.FONT, settings.FONT_SIZE_L), bootstyle="secondary")
        header.grid(row=0, column=0, pady=20)

        test = ttk.Label(self.frame_01, text="hi")
        test.grid(row=1, column=0)

    def _coaching_period(self) -> None:
        """
        Display details about the chosen choaching period
        :return None
        """
        header = ttk.Label(self.frame_02, text="Coaching-Zeitraum", font=(settings.FONT, settings.FONT_SIZE_L), bootstyle="secondary")
        header.grid(row=0, column=0, pady=20)

    def _modules(self) -> None:
        """
        Display details about the chosen modules
        :return None
        """
        header = ttk.Label(self.frame_03, text="BeginnerLuft Service", font=(settings.FONT, settings.FONT_SIZE_L), bootstyle="secondary")
        header.grid(row=0, column=0, pady=20)

    def _coach(self) -> None:
        """
        Display details about the chosen coach
        :return None
        """
        header = ttk.Label(self.frame_04, text="Coach", font=(settings.FONT, settings.FONT_SIZE_L), bootstyle="secondary")
        header.grid(row=0, column=0, pady=20)

    def _participant(self) -> None:
        """
        Display details about the chosen participant
        :return None
        """
        header = ttk.Label(self.frame_05, text="Teilnehmer:In", font=(settings.FONT, settings.FONT_SIZE_L), bootstyle="secondary")
        header.grid(row=0, column=0, pady=20)

    def _notes(self) -> None:
        """
        Display the notes taken about the participant and the planned coaching
        :return None
        """
        header = ttk.Label(self.frame_06, text="Notizen", font=(settings.FONT, settings.FONT_SIZE_L), bootstyle="secondary")
        header.grid(row=0, column=0, pady=20)

    def _title(self, title: str) -> None:
        """
        Place a title on the top frame
        :param title: the title for the page
        """
        title = ttk.Label(self.top_frame, text=title, bootstyle="inverse-primary",
                          font=(settings.FONT, settings.FONT_SIZE_XL), justify="center")
        title.grid(row=0, column=0)

    def _navigation(self, nav_style: str = "secondary") -> None:
        """
        Display naviagation elements
        :return None
        """
        style = f"inverse-{nav_style}"
        back = utils.navigation.NavToParticipantNotes(app=self.app, parent=self.nav_frame, style=style, forward=False)
        back.grid(row=0, column=0, sticky="W", padx=(20, 0))
