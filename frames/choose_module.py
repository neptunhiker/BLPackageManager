import ttkbootstrap as ttk
from tkinter import ttk as tkinterttk

import database
import settings

# class SelectableFrame:

#     def __init__(self, parent: ttk.Frame, package: database.Package) -> None:
#         self.package = package
#         self.active = False
#         self.frame = tkinterttk.Frame(parent, cursor="hand2")


class ModulePicker(ttk.Frame):

    def __init__(self, app) -> None:
        super(ModulePicker, self).__init__(master=app)
        self.app = app

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=12)
        self.grid_rowconfigure(2, weight=1)
        
        self.top_frame = ttk.Frame(self, bootstyle="primary")
        self.top_frame.grid(row=0, column=0, sticky="NSEW")
        self.top_frame.grid_rowconfigure(0, weight=1)
        self.top_frame.grid_columnconfigure(0, weight=1)

        self.bottom_frame = ttk.Frame(self, bootstyle="danger")
        self.bottom_frame.grid(row=1, column=0, sticky="NSEW")
        self.bottom_frame.grid_columnconfigure(0, weight=2)
        self.bottom_frame.grid_columnconfigure(1, weight=1)
        self.bottom_frame.grid_rowconfigure(0, weight=1)

        self.module_frame = ttk.Frame(self.bottom_frame, bootstyle="success")
        self.module_frame.grid(row=0, column=0, sticky="NSEW")
        self.doc_frame = ttk.Frame(self.bottom_frame, bootstyle="warning")
        self.doc_frame.grid(row=0, column=1, sticky="NSEW")


        self.bottom_frame.grid_propagate(False)

        # navigation frame
        navigation_style = "secondary"
        self.nav_frame = ttk.Frame(self, bootstyle=navigation_style)
        self.nav_frame.grid(row=2, column=0, sticky="NSEW")
        self.nav_frame.grid_rowconfigure(0, weight=1)
        for i in range(2):
            self.nav_frame.grid_columnconfigure(i, weight=1)

        # create content
        self._title(title="BeginnerLuft Zusatzmodule")

        self._navigation(nav_style=navigation_style)
    
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
        back = ttk.Label(self.nav_frame, text="<-- zurück", bootstyle=style,
                         font=(settings.FONT, settings.FONT_SIZE_M))
        back.grid(row=0, column=0, sticky="W", padx=(20, 0))

        advance = ttk.Label(self.nav_frame, text="vor -->", bootstyle=style,
                            font=(settings.FONT, settings.FONT_SIZE_M))
        advance.grid(row=0, column=1, sticky="E", padx=(0, 20))