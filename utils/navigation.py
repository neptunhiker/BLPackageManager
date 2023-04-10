import ttkbootstrap as ttk

from frames import choose_package, choose_module
import settings



class NavLabel(ttk.Label):

    BACKWARD_LABEL = "<-- Zurück"
    FORWARD_LABEL = "Vor -->"

    def __init__(self, app: ttk.Window, parent: ttk.Frame, style: str, forward: bool=True):
        if forward:
            self.text_for_label = self.FORWARD_LABEL
        else:
            self.text_for_label = self.BACKWARD_LABEL
        super().__init__(parent, text=self.text_for_label,
                    font=(settings.FONT, settings.FONT_SIZE_M),
                    bootstyle=style,
                    cursor="hand2")
        self.bind("<Enter>", lambda event, label=self: self.on_enter(label))
        self.bind("<Leave>", lambda event, label=self: self.on_leave(label))

    def on_enter(self, label: ttk.Label) -> None:
        """
        Hover effect when entering the label
        """
        try:
            size = int(str(label.cget("font")).split()[-1])
        except ValueError:
            size = int(str(label.cget("font")).split()[-2])
        label.config(font=(settings.FONT, size, "bold"))

    def on_leave(self, label: ttk.Label) -> None:
        """
        Eeffect when leaving the label
        """
        try:
            size = int(str(label.cget("font")).split()[-1])
        except ValueError:
            size = int(str(label.cget("font")).split()[-2])
        label.config(font=(settings.FONT, size))

class NavToModulePicker(NavLabel):

    def __init__(self, app: ttk.Window, parent: ttk.Frame, style: str, forward: bool = True):
        super().__init__(app, parent, style, forward)
        self.bind("<Button-1>", lambda event: app.show_page(choose_module.ModulePicker))

class NavToPackagePicker(NavLabel):

    def __init__(self, app: ttk.Window, parent: ttk.Frame, style: str, forward: bool = True):
        super().__init__(app, parent, style, forward)
        self.bind("<Button-1>", lambda event: app.show_page(choose_package.PackagePicker))