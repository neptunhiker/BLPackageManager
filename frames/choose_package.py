import ttkbootstrap as ttk
from tkinter import ttk as tkinterttk

import database
import utils.navigation
import settings

class SelectableFrame:

    def __init__(self, parent: ttk.Frame, package: database.Package) -> None:
        self.package = package
        self.active = False
        self.frame = tkinterttk.Frame(parent, cursor="hand2")


class PackagePicker(ttk.Frame):

    def __init__(self, app) -> None:
        super(PackagePicker, self).__init__(master=app)
        self.app = app

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
        self.packages_frame = ttk.Frame(self.bottom_frame)
        self.packages_frame.grid(row=0, column=0)
        self.var_package_description = ttk.StringVar()
        package_description = ttk.Label(self.bottom_frame, 
                                        textvariable=self.var_package_description,
                                        justify="center", bootstyle="secondary",
                                        font=(settings.FONT, settings.FONT_SIZE_S))
        package_description.grid(row=1, column=0, ipady=20)

        self.bottom_frame.grid_propagate(False)

        # navigation frame
        navigation_style = "secondary"
        self.nav_frame = ttk.Frame(self, bootstyle=navigation_style)
        self.nav_frame.grid(row=2, column=0, sticky="NSEW")
        self.nav_frame.grid_rowconfigure(0, weight=1)
        for i in range(2):
            self.nav_frame.grid_columnconfigure(i, weight=1)

        # create content
        self._title(title="Coaching Pakete")
        self.selectable_frames = [SelectableFrame(parent=self.packages_frame, package=package) 
                                  for package in self.app.packages]

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

        for i, selec_frame in enumerate(self.selectable_frames):
            frame = selec_frame.frame
            frame.grid(row=0, column=i, padx=10, pady=30, ipadx=20)
            frame.grid_columnconfigure(0, weight=1)
            frame.grid_columnconfigure(1, weight=1)
            frame.bind("<Button-1>", lambda event, 
                       selec_frame=selec_frame: self._highlight_frame(selec_frame))
            frame.bind("<Enter>", lambda event, selec_frame=selec_frame: self._on_enter(selec_frame, "secondary"))
            frame.bind("<Leave>", lambda event, selec_frame=selec_frame: self._on_leave(selec_frame))

            package = selec_frame.package

            if package.name == "Paket Flex":
                flex_adjuster = "~"
            else:
                flex_adjuster = ""
            justify = "center"

            lbl = ttk.Label(frame, text=package.name, justify=justify,
                            font=(settings.FONT, settings.FONT_SIZE_L))
            lbl.grid(row=0, column=0, pady=30, columnspan=2)

            lbl = ttk.Label(frame, text=package.ues_coach,
                            font=(settings.FONT, settings.FONT_SIZE_L))
            lbl.grid(row=2, column=0, sticky="E")
            lbl = ttk.Label(frame, text="UE  1:1 Coaching",
                font=(settings.FONT, settings.FONT_SIZE_S))
            lbl.grid(row=2, column=1, sticky="W")

            if package.sessions_per_week > 1:
                text = "Termine pro Woche"
            else:
                text = "Termin pro Woche"
            lbl = ttk.Label(frame, text=f"{flex_adjuster}{package.sessions_per_week}",
                            font=(settings.FONT, settings.FONT_SIZE_L))
            lbl.grid(row=3, column=0, sticky="E")
            lbl = ttk.Label(frame, text=text,
                font=(settings.FONT, settings.FONT_SIZE_S))
            lbl.grid(row=3, column=1, sticky="W")

            lbl = ttk.Label(frame, text=f"{flex_adjuster}{package.duration_in_weeks}",
                            font=(settings.FONT, settings.FONT_SIZE_L))
            lbl.grid(row=4, column=0, sticky="E")
            lbl = ttk.Label(frame, text="Coaching-Wochen",
                font=(settings.FONT, settings.FONT_SIZE_S))
            lbl.grid(row=4, column=1, sticky="W")

            sessions_with_coach = str(package.duration_in_weeks * package.sessions_per_week),
            lbl = ttk.Label(frame, text=f"{flex_adjuster}{sessions_with_coach[0]}",
                            font=(settings.FONT, settings.FONT_SIZE_L))
            lbl.grid(row=5, column=0, sticky="E")
            lbl = ttk.Label(frame, text="Termine insgesamt",
                font=(settings.FONT, settings.FONT_SIZE_S))
            lbl.grid(row=5, column=1, sticky="W")

            lbl = ttk.Label(frame, text="+",
                            font=(settings.FONT, settings.FONT_SIZE_L))
            lbl.grid(row=6, column=0, columnspan=2)
            lbl = ttk.Label(frame, text="BeginnerLuft Service",
                font=(settings.FONT, settings.FONT_SIZE_M))
            lbl.grid(row=7, column=0, columnspan=2, pady=(10, 30))

            for widget in frame.winfo_children():
                widget.bind("<Button-1>", lambda event, 
                       selec_frame=selec_frame: self._highlight_frame(selec_frame))

    def _highlight_frame(self, selec_frame: SelectableFrame) -> None:
        """
        Highlight the frame passed as an argument
        :param selec_frame: the selectable frame object that contains the frame to be highlighted
        :param labels: a list of labels within the frame
        :return None
        """
        activation_status = selec_frame.active

        # deactivate all frames and remove highlight
        self.app.chosen_package = None
        for selectable_frame in self.selectable_frames:
            selectable_frame.active = False
            selectable_frame.frame.config(style="TFrame")
            for label in selectable_frame.frame.winfo_children():
                label.config(style="TLabel")

        # activate this frame and highlight it
        if activation_status == False:
            selec_frame.active = True
            self.app.chosen_package = selec_frame.package
            selec_frame.frame.config(bootstyle="success")
            for label in selec_frame.frame.winfo_children():
                label.config(bootstyle="inverse-success")

    def _on_enter(self, selec_frame: ttk.Frame, ttkbootstyle: str = "secondary") -> None:
        """
        Change the background color of the frame
        :param selec_frame: the selectable frame object that contains the frame to be highlighted
        :param ttkbootstyle: the style to be used for the highlighting
        : return None
        """
        if selec_frame.active:
            pass
        else:
            selec_frame.frame.config(bootstyle=ttkbootstyle)
            for label in selec_frame.frame.winfo_children():
                label.config(bootstyle=f"inverse-{ttkbootstyle}")

        self.var_package_description.set(f"{selec_frame.package.name}\n\n{selec_frame.package.description}")

    def _on_leave(self, selec_frame: ttk.Frame) -> None:
        """
        Change the background color of the frame back to default
        :param selec_frame: the selectable frame object that contains the frame to be highlighted
        : return None
        """
        if selec_frame.active:
            pass
        else:
            selec_frame.frame.config(style="TFrame")
            for label in selec_frame.frame.winfo_children():
                label.config(style="TLabel")
    
        self.var_package_description.set("")


    def _navigation(self, nav_style: str = "secondary") -> None:
        """
        Display naviagation elements
        :return None
        """
        style = f"inverse-{nav_style}"
        advance = utils.navigation.NavToModulePicker(app=self.app, parent=self.nav_frame, style=style, forward=True)
        advance.grid(row=0, column=1, sticky="E", padx=(0, 20))