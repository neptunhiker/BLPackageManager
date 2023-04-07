import ttkbootstrap as ttk

import settings

class PackagePicker(ttk.Frame):

    def __init__(self, app) -> None:
        super(PackagePicker, self).__init__(master=app)
        self.app = app
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=2)
        self.grid_rowconfigure(1, weight=12)
        self.grid_rowconfigure(2, weight=2)
        
        self.top_frame = ttk.Frame(self, bootstyle="primary")
        self.top_frame.grid(row=0, column=0, sticky="NSEW")
        self.top_frame.grid_rowconfigure(0, weight=1)
        self.top_frame.grid_columnconfigure(0, weight=1)

        self.bottom_frame = ttk.Frame(self)
        self.bottom_frame.grid(row=1, column=0, sticky="NSEW")
        # self.bottom_frame.grid_rowconfigure(0, weight=1)
        for i in range(4):
            self.bottom_frame.grid_columnconfigure(i, weight=1)

        # self.bottom_frame.grid_propagate(False)

        navigation_style = "secondary"
        self.nav_frame = ttk.Frame(self, bootstyle=navigation_style)
        self.nav_frame.grid(row=2, column=0, sticky="NSEW")
        self.nav_frame.grid_rowconfigure(0, weight=1)
        for i in range(2):
            self.nav_frame.grid_columnconfigure(i, weight=1)

        self._title(title="Coaching Pakete")
        self._packages()
        self._navigation(nav_style=navigation_style)
    
    def _title(self, title: str) -> None:
        """
        Place a title on the top frame
        :param title: the title for the page
        """
        title = ttk.Label(self.top_frame, text=title, bootstyle="inverse-primary",
                          font=(settings.FONT, settings.FONT_SIZE_XL), justify="center")
        title.grid(row=0, column=0)

    def _packages(self) -> None:
        """
        Display available packages
        :return None
        """

        packages = self.app.db.get_packages()
        package_titles = [package.name for package in packages]
        durations_in_weeks = [package.duration_in_weeks for package in packages]
        ues_per_week = [package.ues_per_week for package in packages]
        sessions_per_week = [package.sessions_per_week for package in packages]
        ues_coach = [package.ues_coach for package in packages]
        ues_bl = [package.ues_bl for package in packages]
        ues_total = [package.ues for package in packages]

        column_counter = 0
        for package, duration, ues, sessions, coach_ues, bl_ues, total_ues in zip(package_titles, durations_in_weeks, ues_per_week, sessions_per_week, ues_coach, ues_bl, ues_total):
            lbl = ttk.Label(self.bottom_frame, text=package, 
                            font=(settings.FONT, settings.FONT_SIZE_L))
            lbl.grid(row=0, column=column_counter, pady=(100, 20))

            lbl = ttk.Label(self.bottom_frame, text=f"Dauer in Wochen: {duration}")
            lbl.grid(row=1, column=column_counter)

            lbl = ttk.Label(self.bottom_frame, text=f"UEs pro Woche: {ues}")
            lbl.grid(row=2, column=column_counter)

            lbl = ttk.Label(self.bottom_frame, text=f"Termine pro Woche: {sessions}")
            lbl.grid(row=3, column=column_counter)

            lbl = ttk.Label(self.bottom_frame, text=f"UEs vom Coach: {coach_ues}")
            lbl.grid(row=4, column=column_counter)

            lbl = ttk.Label(self.bottom_frame, text=f"UEs von BeginnerLuft: {bl_ues}")
            lbl.grid(row=5, column=column_counter)

            lbl = ttk.Label(self.bottom_frame, text=f"UEs insgesamt: {total_ues}")
            lbl.grid(row=6, column=column_counter)

            column_counter += 1

    def _navigation(self, nav_style: str = "secondary") -> None:
        """
        Display naviagation elements
        :return None
        """
        style = f"inverse-{nav_style}"
        back = ttk.Label(self.nav_frame, text="<-- zurück", bootstyle=style,
                         font=(settings.FONT, settings.FONT_SIZE_M))
        back.grid(row=0, column=0, sticky="W", padx=(20, 0))

        advance = ttk.Label(self.nav_frame, text="vor -->", bootstyle=style,
                            font=(settings.FONT, settings.FONT_SIZE_M))
        advance.grid(row=0, column=1, sticky="E", padx=(0, 20))