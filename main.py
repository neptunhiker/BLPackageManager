import ttkbootstrap as ttk


import settings


class App(ttk.Window):

    def __init__(self):
        super(App, self).__init__(themename=settings.THEMENAME)
        self._full_screen_window()
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    
    def _full_screen_window(self) -> None:
        """
        Sets the screen to full size
        :return None
        """
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w, h))  # sets screen to full size
        self.state('zoomed')

if __name__ == "__main__":
    app = App()
    app.mainloop()