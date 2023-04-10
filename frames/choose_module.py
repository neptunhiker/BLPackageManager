import ttkbootstrap as ttk
from tkinter import ttk as tkinterttk

import database
import settings
import utils.navigation, utils.placement

MODULE_STYLE = "primary"

class SelectableFrame:

    def __init__(self, parent: ttk.Frame, module: database.Module) -> None:
        self.module = module
        self.active = False
        self.frame = ttk.Frame(parent, cursor="hand2", bootstyle=MODULE_STYLE)


class ModulePicker(ttk.Frame):

    def __init__(self, app) -> None:
        super(ModulePicker, self).__init__(master=app)
        self.app = app
        self.var_module_name = ttk.StringVar()
        self.var_module_default = ttk.StringVar()
        self.var_module_description = ttk.StringVar()
        self.default_services = {1: "Standardservice", 0: "Zusatzmodul"}

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
        self.bottom_frame.grid_columnconfigure(0, weight=2)
        self.bottom_frame.grid_columnconfigure(1, weight=1)
        self.bottom_frame.grid_rowconfigure(0, weight=1)

        self.module_frame = ttk.Frame(self.bottom_frame)
        self.module_frame.grid(row=0, column=0, sticky="NSEW")
        self.module_frame_center = ttk.Frame(self.module_frame)
        self.module_frame_center.grid(row=1, column=0)
        self.module_frame.grid_columnconfigure(0, weight=1)
        self.module_frame.grid_rowconfigure(1, weight=1)

        self.doc_frame = ttk.Frame(self.bottom_frame)
        self.doc_frame.grid(row=0, column=1, sticky="NSEW")
        self.doc_frame.grid_columnconfigure(1, weight=1)
        self.doc_frame.grid_rowconfigure(0, weight=1)


        self.bottom_frame.grid_propagate(False)
        self.module_frame.grid_propagate(False)
        self.doc_frame.grid_propagate(False)

        # navigation frame
        navigation_style = "secondary"
        self.nav_frame = ttk.Frame(self, bootstyle=navigation_style)
        self.nav_frame.grid(row=2, column=0, sticky="NSEW")
        self.nav_frame.grid_rowconfigure(0, weight=1)
        for i in range(2):
            self.nav_frame.grid_columnconfigure(i, weight=1)

        # create content
        self._title(title="BeginnerLuft Service")
        self._modules()
        self._documentation()
        self._navigation(nav_style=navigation_style)
    
    def _title(self, title: str) -> None:
        """
        Place a title on the top frame
        :param title: the title for the page
        """
        title = ttk.Label(self.top_frame, text=title, bootstyle="inverse-primary",
                          font=(settings.FONT, settings.FONT_SIZE_XL), justify="center")
        title.grid(row=0, column=0)

    def _modules(self) -> None:
        """
        Place modules for selection on the page
        :return None
        """

        label = ttk.Label(self.module_frame, text="Verfügbare Module", font=(settings.FONT, settings.FONT_SIZE_L), bootstyle="light")
        label.grid(row=0, column=0, pady=(100, 0))

        nr_of_modules = len(self.app.modules)
        modules = self.app.modules.copy()
        grid_system = utils.placement.module_placement(nr_of_modules)

        # frames
        frame_row_0 = ttk.Frame(self.module_frame_center)
        frame_row_0.grid(row=0, column=0, pady=(0, 20))
        if sum(grid_system.values()) > 5:
            frame_row_1 = ttk.Frame(self.module_frame_center)
            frame_row_1.grid(row=1, column=0, pady=20)
        if sum(grid_system.values()) > 10:
            frame_row_2 = ttk.Frame(self.module_frame_center)
            frame_row_2.grid(row=2, column=0, pady=20)

        # label settings
        padx = 10
        pady = 5
        anchor = "center"
        width = 20
        font_up = (settings.FONT, settings.FONT_SIZE_S)
        font_down = (settings.FONT, settings.FONT_SIZE_XS)

        def create_frame_and_modules(parent: ttk.Frame):
            module = modules.pop(0)
            selectable_mini_frame = SelectableFrame(parent, module=module)
            selectable_mini_frame.frame.grid(row=0, column=col, padx=padx, pady=pady)
            label = ttk.Label(selectable_mini_frame.frame, text=module.name, width=width, anchor=anchor, font=font_up, cursor="hand2", 
                              bootstyle=f"inverse-{MODULE_STYLE}")
            label.grid(row=0, column=0, pady=(pady, 0))
            label = ttk.Label(selectable_mini_frame.frame, text=self.default_services[module.default], width=width, anchor=anchor, 
                              font=font_down, cursor="hand2", bootstyle=f"inverse-{MODULE_STYLE}")
            label.grid(row=1, column=0, pady=pady)
            selectable_mini_frame.frame.bind("<Button-1>", lambda event, frame=selectable_mini_frame: self._highlight_frame(frame))
            selectable_mini_frame.frame.bind("<Enter>", lambda event, frame=selectable_mini_frame: self._on_enter(frame))
            selectable_mini_frame.frame.bind("<Leave>", lambda event, frame=selectable_mini_frame: self._on_leave(frame))

            for widget in selectable_mini_frame.frame.winfo_children():
                widget.bind("<Button-1>", lambda event, 
                       selec_frame=selectable_mini_frame: self._highlight_frame(selec_frame))
                
            # activate if it is a standard service
            if module.default == 1:
                self._highlight_frame(selec_frame=selectable_mini_frame)

        # row 0 frame and modules
        for col in range(grid_system[0]):
            create_frame_and_modules(parent=frame_row_0)

        # row 1 frame and modules
        for col in range(grid_system[1]):
            create_frame_and_modules(parent=frame_row_1)

        # row 2 frame and modules
        for col in range(grid_system[2]):
            create_frame_and_modules(parent=frame_row_2)

    
    def _documentation(self) -> None:
        """
        A frame to describe the modules in more detail
        """
        ttk.Separator(self.doc_frame, orient="vertical").grid(row=0, column=0, pady=80, sticky="NSW")
        frame = ttk.Frame(self.doc_frame)
        frame.grid(row=0, column=1)

        name = ttk.Label(frame, textvariable=self.var_module_name, font=(settings.FONT, settings.FONT_SIZE_L), bootstyle="secondary")
        name.grid(row=0, column=1, pady=(0, 50))
        
        default = ttk.Label(frame, textvariable=self.var_module_default, font=(settings.FONT, settings.FONT_SIZE_M))
        default.grid(row=1, column=1, pady=(0, 20))

        description = ttk.Label(frame, textvariable=self.var_module_description, wraplength=200, justify="center")
        description.grid(row=2, column=1)


    def _navigation(self, nav_style: str = "secondary") -> None:
        """
        Display naviagation elements
        :return None
        """
        style = f"inverse-{nav_style}"
        back = utils.navigation.NavToPackagePicker(app=self.app, parent=self.nav_frame, style=style, forward=False)
        back.grid(row=0, column=0, sticky="W", padx=(20, 0))

        forward = utils.navigation.NavToMatching(app=self.app, parent=self.nav_frame, style=style, forward=True)
        forward.grid(row=0, column=1, sticky="E", padx=(0, 20))

    def _highlight_frame(self, selec_frame: SelectableFrame) -> None:
        """
        Highlight the frame passed as an argument
        :param selec_frame: the selectable frame object that contains the frame to be highlighted
        :param labels: a list of labels within the frame
        :return None
        """
        activation_status = selec_frame.active

        # activate this frame and highlight it
        if activation_status == False:
            selec_frame.active = True
            self.app.chosen_modules[selec_frame.module] = selec_frame.active
            selec_frame.frame.config(bootstyle="success")
            for label in selec_frame.frame.winfo_children():
                label.config(bootstyle="inverse-success")
        else:
            selec_frame.active = False
            self.app.chosen_modules[selec_frame.module] = selec_frame.active
            selec_frame.frame.config(bootstyle=MODULE_STYLE)
            for label in selec_frame.frame.winfo_children():
                label.config(bootstyle=f"inverse-{MODULE_STYLE}")


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

        self.var_module_name.set(selec_frame.module.name)
        self.var_module_default.set(self.default_services[selec_frame.module.default])
        self.var_module_description.set(selec_frame.module.description)

    def _on_leave(self, selec_frame: ttk.Frame) -> None:
        """
        Change the background color of the frame back to default
        :param selec_frame: the selectable frame object that contains the frame to be highlighted
        : return None
        """
        if selec_frame.active:
            pass
        else:
            # selec_frame.frame.config(style="TFrame")
            selec_frame.frame.config(bootstyle=MODULE_STYLE)
            for label in selec_frame.frame.winfo_children():
                # label.config(style="TLabel")
                label.config(bootstyle=f"inverse-{MODULE_STYLE}")
    
        self.var_module_name.set("")
        self.var_module_default.set("")
        self.var_module_description.set("")