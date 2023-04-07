import ttkbootstrap as ttk

import frames
import settings


class App(ttk.Window):

    def __init__(self):
        super(App, self).__init__(themename=settings.THEMENAME)
        self._full_screen_window()
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.pages = {}

        self.add_page(page_class=frames.choose_package.PackagePicker)

        # starting page
        self.show_page(frames.choose_package.PackagePicker)
    
    def add_page(self, page_class: ttk.Frame) -> None:
        """
        Add a page to the app
        :param page: a page/frame
        :return None
        """
        # place page onto app
        page = page_class(self)
        page.grid(row=0, column=0, sticky="NSEW")

        # add page to dictionary of pages
        self.pages[page_class] = page

    
    def _full_screen_window(self) -> None:
        """
        Sets the screen to full size
        :return None
        """
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w, h))  # sets screen to full size
        self.state('zoomed')

    def show_page(self, page) -> None:
        """
        Lift a particular page to the foreground to make it visible
        :param page: the page to be shown
        :return None
        """
        self.pages[page].tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()