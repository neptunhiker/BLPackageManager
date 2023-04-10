from PIL import ImageGrab
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

        self.bind("<Enter>", lambda event: self._update())
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
        self.frame_01.grid_columnconfigure(1, weight=1)
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
        header.grid(row=0, column=0, pady=20, columnspan=2)

        name = ttk.Label(self.frame_01, textvariable=self.app.var_package_name, font=(settings.FONT, settings.FONT_SIZE_M))
        name.grid(row=1, column=0, columnspan=2, pady=(0, 20))

        # sub-headers
        labels = ["UE  1:1 Coaching", "Termin(e) pro Woche", "Coaching-Wochen", "Termine insgesamt"]
        for i, label in enumerate(labels):
            ttk.Label(self.frame_01, text=label, font=(settings.FONT, settings.FONT_SIZE_S)).grid(row=i+2, column=1, sticky="W")

        ues_coach = ttk.Label(self.frame_01, textvariable=self.app.var_ues_coach, font=(settings.FONT, settings.FONT_SIZE_S))
        ues_coach.grid(row=2, column=0, sticky="E")

        sessions_per_week = ttk.Label(self.frame_01, textvariable=self.app.var_sessions_per_week, font=(settings.FONT, settings.FONT_SIZE_S))
        sessions_per_week.grid(row=3, column=0, sticky="E")

        duration_in_weeks = ttk.Label(self.frame_01, textvariable=self.app.var_duration_in_weeks, font=(settings.FONT, settings.FONT_SIZE_S))
        duration_in_weeks.grid(row=4, column=0, sticky="E")

        sessions_with_coach = ttk.Label(self.frame_01, textvariable=self.app.var_sessions_with_coach, font=(settings.FONT, settings.FONT_SIZE_S))
        sessions_with_coach.grid(row=5, column=0, sticky="E")

        plus = ttk.Label(self.frame_01, text="+", font=(settings.FONT, settings.FONT_SIZE_S))
        plus.grid(row=6, column=0, columnspan=2)

        bl_service = ttk.Label(self.frame_01, text="BeginnerLuft Service", font=(settings.FONT, settings.FONT_SIZE_S))
        bl_service.grid(row=7, column=0, columnspan=2)

    def _coaching_period(self) -> None:
        """
        Display details about the chosen choaching period
        :return None
        """
        header = ttk.Label(self.frame_02, text="Coaching-Zeitraum", font=(settings.FONT, settings.FONT_SIZE_L), bootstyle="secondary")
        header.grid(row=0, column=0, pady=(20, 50))

        start_date = ttk.Label(self.frame_02, textvariable=self.app.var_start_date, font=(settings.FONT, settings.FONT_SIZE_M))
        start_date.grid(row=2, column=0)

        until = ttk.Label(self.frame_02, text="-", font=(settings.FONT, settings.FONT_SIZE_M))
        until.grid(row=3, column=0)

        end_date = ttk.Label(self.frame_02, textvariable=self.app.var_end_date, font=(settings.FONT, settings.FONT_SIZE_M))
        end_date.grid(row=4, column=0)

    def _modules(self) -> None:
        """
        Display details about the chosen modules
        :return None
        """
        for widget in self.frame_03.winfo_children():
            widget.destroy()

        header = ttk.Label(self.frame_03, text="BeginnerLuft Service", font=(settings.FONT, settings.FONT_SIZE_L), bootstyle="secondary")
        header.grid(row=0, column=0, pady=20)

        modules_names = []
        for module, activated in self.app.chosen_modules.items():
            if activated:
                modules_names.append(module.name)

        sorted_modules = sorted(modules_names)

        rows_in_col_zero = utils.placement.module_place_overview(nr_of_modules=len(sorted_modules))[0]
        rows_in_col_one = utils.placement.module_place_overview(nr_of_modules=len(sorted_modules))[1]

        if rows_in_col_one == 0:
            row_counter = 1
            for module_name in sorted_modules:
                ttk.Label(self.frame_03, text=module_name, font=(settings.FONT, settings.FONT_SIZE_S)).grid(row=row_counter, column=0)
                row_counter += 1
        else:
            frame = ttk.Frame(self.frame_03)
            frame.grid(row=1, column=0)
            # first elements in col 0
            row_counter = 0
            for module_name in sorted_modules[0:rows_in_col_zero]:
                lbl = ttk.Label(frame, text=f"- {module_name}", font=(settings.FONT, settings.FONT_SIZE_S))
                lbl.grid(row=row_counter, column=0, sticky="W", padx=(0, 10))
                row_counter += 1
            # remaining elements in col 1
            row_counter = 0
            for module_name in sorted_modules[rows_in_col_zero:]:
                lbl = ttk.Label(frame, text=f"- {module_name}", font=(settings.FONT, settings.FONT_SIZE_S))
                lbl.grid(row=row_counter, column=1, sticky="W")
                row_counter += 1


    def _coach(self) -> None:
        """
        Display details about the chosen coach
        :return None
        """
        header = ttk.Label(self.frame_04, text="Coach", font=(settings.FONT, settings.FONT_SIZE_L), bootstyle="secondary")
        header.grid(row=0, column=0, pady=20)

        name = ttk.Label(self.frame_04, textvariable=self.app.var_coach_name, font=(settings.FONT, settings.FONT_SIZE_M))
        name.grid(row=1, column=0, pady=(0, 20))

        description = ttk.Label(self.frame_04, textvariable=self.app.var_coach_description, wraplength=200, justify="center")
        description.grid(row=2, column=0, pady=(0, 10))

        web_link = ttk.Label(self.frame_04, textvariable=self.app.var_coach_web_link)
        web_link.grid(row=3, column=0)

    def _participant(self) -> None:
        """
        Display details about the chosen participant
        :return None
        """
        header = ttk.Label(self.frame_05, text="Teilnehmer:In", font=(settings.FONT, settings.FONT_SIZE_L), bootstyle="secondary")
        header.grid(row=0, column=0, pady=20)

        name = ttk.Label(self.frame_05, textvariable=self.app.var_participant_name, font=(settings.FONT, settings.FONT_SIZE_M))
        name.grid(row=1, column=0, pady=(0, 20))

        email = ttk.Label(self.frame_05, textvariable=self.app.var_participant_email, wraplength=200, justify="center")
        email.grid(row=2, column=0, pady=(0, 10))

        phone = ttk.Label(self.frame_05, textvariable=self.app.var_participant_phone)
        phone.grid(row=3, column=0)

    def _notes(self) -> None:
        """
        Display the notes taken about the participant and the planned coaching
        :return None
        """
        for widget in self.frame_06.winfo_children():
            widget.destroy()
        
        header = ttk.Label(self.frame_06, text="Weitere Infos", font=(settings.FONT, settings.FONT_SIZE_L), bootstyle="secondary")
        header.grid(row=0, column=0, pady=(20, 10))

        header_wishes = ttk.Label(self.frame_06, text="Besondere Wünsche", font=(settings.FONT, settings.FONT_SIZE_S), bootstyle="secondary")
        header_wishes.grid(row=1, column=0, pady=(0, 5))
        if self.app.notes_wishes is not None:
            wishes = ttk.Label(self.frame_06, text=self.app.notes_wishes.get("1.0", ttk.END), 
                               font=(settings.FONT, settings.FONT_SIZE_XS), wraplength=450, justify="center")
            wishes.grid(row=2, column=0)

        header_other = ttk.Label(self.frame_06, text="Sonstige Besonderheiten", font=(settings.FONT, settings.FONT_SIZE_S), bootstyle="secondary")
        header_other.grid(row=3, column=0, pady=(0, 5))
        if self.app.notes_other is not None:
            wishes = ttk.Label(self.frame_06, text=self.app.notes_other.get("1.0", ttk.END), 
                               font=(settings.FONT, settings.FONT_SIZE_XS), wraplength=450, justify="center")
            wishes.grid(row=4, column=0)

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

        btn = ttk.Button(self.nav_frame, text="Als .png speichern", command= lambda: self._save_as_jpeg(), cursor="hand2")
        btn.grid(row=0, column=1, sticky="E", padx=(0, 20))

    def _save_as_jpeg(self) -> None:
        """
        Save the screen to a jpeg file
        """
        geometry = self.app.winfo_geometry()

        # Split the string into a list of four strings
        geometry = geometry.split("+")
        width, height, left, top = map(int, geometry[0].split("x") + geometry[1:])

        image = ImageGrab.grab(bbox=(left, top, width, height + top))
        file_name = f"Coaching - {self.app.var_participant_name.get()}.png"
        image.save(file_name)

    def _update(self) -> None:
        """
        Update the chosen modules and the notes
        :return None
        """
        self._modules()
        self._notes()