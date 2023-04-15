import datetime
import locale
import ttkbootstrap as ttk
from tkinter import ttk as tkinterttk

import database
import settings
import utils.navigation, utils.placement, utils.dialogs

MODULE_STYLE = "primary"
locale.setlocale(locale.LC_ALL, "de_DE")


class Matching(ttk.Frame):
    def __init__(self, app) -> None:
        super(Matching, self).__init__(master=app)
        self.app = app
        self.var_start_date = ttk.StringVar()
        self.var_end_date = ttk.StringVar()
        self.var_coach_name = ttk.StringVar()
        self.var_coach_description = ttk.StringVar()
        self.var_coach_web_link = ttk.StringVar()

        self.var_participant_first_name = ttk.StringVar()
        self.var_participant_last_name = ttk.StringVar()
        self.var_participant_first_name.trace("w", self._update_participant_full_name)
        self.var_participant_last_name.trace("w", self._update_participant_full_name)

        self.available_coaches = len(self.app.coaches)
        self.coach_index_pos = 0

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

        self.part_frame = ttk.Frame(self.bottom_frame)
        self.part_frame.grid(row=0, column=0, sticky="NSEW")
        # self.part_frame.grid_rowconfigure(0, weight=1)
        self.part_frame.grid_columnconfigure(0, weight=1)

        ttk.Separator(self.bottom_frame, orient="vertical").grid(
            row=0, column=1, sticky="NS", pady=75
        )
        self.start_frame = ttk.Frame(self.bottom_frame)
        self.start_frame.grid(row=0, column=2, sticky="NSEW")
        self.start_frame.grid_columnconfigure(0, weight=1)
        # self.start_frame.grid_rowconfigure(0, weight=1)
        ttk.Separator(self.bottom_frame, orient="vertical").grid(
            row=0, column=3, sticky="NS", pady=75
        )

        self.coach_frame = ttk.Frame(self.bottom_frame)
        self.coach_frame.grid(row=0, column=4, sticky="NSEW")
        self.coach_frame.grid_columnconfigure(0, weight=1)

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
        self._coaching_dates()
        self._coach()
        self._navigation(nav_style=navigation_style)

    def _title(self, title: str) -> None:
        """
        Place a title on the top frame
        :param title: the title for the page
        """
        title = ttk.Label(
            self.top_frame,
            text=title,
            bootstyle="inverse-primary",
            font=(settings.FONT, settings.FONT_SIZE_XL),
            justify="center",
        )
        title.grid(row=0, column=0)

    def _participant(self) -> None:
        """
        Create the possibility to enter participant details
        :return None
        """
        frame = ttk.Frame(self.part_frame)
        frame.grid(row=0, column=0, pady=(100, 0))

        # labels
        ttk.Label(
            frame, text="Teilnehmer:In", font=(settings.FONT, settings.FONT_SIZE_L), bootstyle=settings.HEADING_BOOTSTYLE
        ).grid(row=0, column=0, columnspan=2, pady=(0, 30), padx=0)
        ttk.Label(frame, text="Vorname").grid(
            row=1, column=0, sticky="W"
        )
        ttk.Label(frame, text="Nachname").grid(
            row=3, column=0, sticky="W"
        )
        ttk.Label(frame, text="E-Mail").grid(
            row=5, column=0, sticky="W"
        )
        ttk.Label(frame, text="Telefon").grid(
            row=7, column=0, sticky="W"
        )

        # entry widgets
        pady = (5, 20)
        first_name = ttk.Entry(frame, textvariable=self.var_participant_first_name)
        first_name.grid(row=2, column=0, pady=pady)
        last_name = ttk.Entry(frame, textvariable=self.var_participant_last_name)
        last_name.grid(row=4, column=0, pady=pady)
        email = ttk.Entry(frame, textvariable=self.app.var_participant_email)
        email.grid(row=6, column=0, pady=pady)
        phone = ttk.Entry(frame, textvariable=self.app.var_participant_phone)
        phone.grid(row=8, column=0, pady=pady, padx=0)

    def _coaching_dates(self) -> None:
        """
        Create the possibility to chose a start date for the coaching
        :return None
        """
        frame = ttk.Frame(self.start_frame)
        frame.grid(row=0, column=0, pady=(100, 0))

        header_start_date = ttk.Label(
            frame,
            text="Geplantes Startdatum",
            font=(settings.FONT, settings.FONT_SIZE_L),
            cursor="hand2",
            bootstyle=settings.HEADING_BOOTSTYLE
        )
        header_start_date.grid(row=0, column=0)
        header_start_date.bind(
            "<Button-1>",
            lambda event, parent=header_start_date: self._choose_date(parent),
        )

        start_date = ttk.Label(
            frame,
            textvariable=self.var_start_date,
            font=(settings.FONT, settings.FONT_SIZE_XL),
            cursor="hand2",
        )
        start_date.grid(row=1, column=0, pady=(40, 0))
        start_date.bind(
            "<Button-1>",
            lambda event, parent=header_start_date: self._choose_date(parent),
        )

        header_end_date = ttk.Label(
            frame, text="Geplantes Enddatum", font=(settings.FONT, settings.FONT_SIZE_S), bootstyle=settings.HEADING_BOOTSTYLE
        )
        header_end_date.grid(row=2, column=0, pady=(100, 0))

        end_date = ttk.Label(
            frame,
            textvariable=self.var_end_date,
            font=(settings.FONT, settings.FONT_SIZE_M),
        )
        end_date.grid(row=3, column=0, pady=(40, 0))

    def _choose_date(self, parent: ttk.Label) -> None:
        """
        Choose a coaching start date
        :param parent
        """
        start_date = utils.dialogs.choose_date(title="Wähle Datum", parent=parent)
        date_str_start_date = datetime.datetime.strftime(start_date, "%d. %B %Y")
        self.app.var_start_date.set(date_str_start_date)
        self.var_start_date.set(date_str_start_date)

        if self.app.chosen_package is not None:
            end_date = start_date + datetime.timedelta(
                weeks=self.app.chosen_package.duration_in_weeks
            )
            date_str_end_date = datetime.datetime.strftime(end_date, "%d. %B %Y")
            self.app.var_end_date.set(date_str_end_date)
            self.var_end_date.set(date_str_end_date)
        else:
            self.var_end_date.set("Bitte Paket auswählen")

    def _coach(self) -> None:
        """
        Create the possibility to select a coach
        :return None
        """
        frame = ttk.Frame(self.coach_frame)
        frame.grid(row=0, column=0, pady=(100, 0))

        header = ttk.Label(
            frame,
            text="Gewählter Coach",
            font=(settings.FONT, settings.FONT_SIZE_L),
            cursor="hand2",
            width=15,
            anchor="center",
            bootstyle=settings.HEADING_BOOTSTYLE
        )
        header.grid(row=0, column=1, pady=(0, 100))

        left = ttk.Label(
            frame, text="<<", cursor="hand2", font=(settings.FONT, settings.FONT_SIZE_S)
        )
        left.grid(row=1, column=0, padx=(0, 20), sticky="N")
        left.bind("<Button-1>", lambda event: self._change_coach(forward=False))

        # frame = ttk.Frame(frame)
        # frame.grid(row=1, column=1)

        self.var_coach_name.set("Bitte Coach auswählen")
        self.var_coach_description.set("")
        self.var_coach_web_link.set("")

        lbl_name = ttk.Label(
            frame,
            textvariable=self.var_coach_name,
            font=(settings.FONT, settings.FONT_SIZE_M),
        )
        lbl_name.grid(row=1, column=1, pady=(0, 30))

        lbl_description = ttk.Label(
            frame,
            textvariable=self.var_coach_description,
            wraplength=200,
            justify="center",
        )
        lbl_description.grid(row=2, column=1, pady=(0, 20))

        lbl_web_link = ttk.Label(frame, textvariable=self.var_coach_web_link)
        lbl_web_link.grid(row=3, column=1)

        right = ttk.Label(
            frame, text=">>", cursor="hand2", font=(settings.FONT, settings.FONT_SIZE_S)
        )
        right.grid(row=1, column=2, padx=(20, 0), sticky="N")
        right.bind("<Button-1>", lambda event: self._change_coach(forward=True))

    def _change_coach(self, forward: bool = True) -> None:
        """
        Change the coach displayed on the page by going to the next coach in the database
        :return None
        """
        if forward:
            self.coach_index_pos = (self.coach_index_pos + 1) % self.available_coaches
        else:
            self.coach_index_pos = (self.coach_index_pos - 1) % self.available_coaches

        coach = self.app.coaches[self.coach_index_pos]
        self.var_coach_name.set(f"{coach.first_name} {coach.last_name}")
        self.var_coach_description.set(coach.description)
        self.var_coach_web_link.set(coach.web_link)

        self.app.var_coach_name.set(self.var_coach_name.get())
        self.app.var_coach_description.set(self.var_coach_description.get())
        self.app.var_coach_web_link.set(self.var_coach_web_link.get())

    def _navigation(self, nav_style: str = "secondary") -> None:
        """
        Display naviagation elements
        :return None
        """
        style = f"inverse-{nav_style}"
        back = utils.navigation.NavToModulePicker(
            app=self.app, parent=self.nav_frame, style=style, forward=False
        )
        back.grid(row=0, column=0, sticky="W", padx=(20, 0))

        forward = utils.navigation.NavToParticipantNotes(
            app=self.app, parent=self.nav_frame, style=style, forward=True
        )
        forward.grid(row=0, column=1, sticky="E", padx=(0, 20))

    def _update_participant_full_name(self, a, b, c) -> None:
        """
        Update the full name of the participant if the first name or last name of the participant is changed on this page
        :return None
        """
        full_name = f"{self.var_participant_first_name.get()} {self.var_participant_last_name.get()}"
        self.app.var_participant_first_name.set(self.var_participant_first_name.get())
        self.app.var_participant_last_name.set(self.var_participant_last_name.get())
        self.app.var_participant_name.set(full_name)
