import ttkbootstrap as ttk

import database
import frames
import settings
import utils.sorting
import config_database

from ttkcreator import __main__


class App(ttk.Window):

    def __init__(self, database, active_environment: str):
        super(App, self).__init__(themename=settings.THEMENAME, title="BeginnerLuft")
        self.db = database
        self.active_environment = active_environment
        self.coaches = db.get_coaches()
        self.chosen_coach = None
        self.modules = utils.sorting.sort_modules(self.db.get_modules())
        self.chosen_modules = {}

        # package
        self.packages = sorted(self.db.get_packages(), key=lambda obj: obj.id)
        self.chosen_package = None
        self.var_package_name = ttk.StringVar(value="Bitte Plan auswählen")
        self.var_ues_coach = ttk.IntVar(value="")
        self.var_sessions_per_week = ttk.IntVar(value="")
        self.var_duration_in_weeks = ttk.IntVar(value="")
        self.var_total_sessions = ttk.IntVar(value="")

        # coach
        self.var_coach_name = ttk.StringVar()
        self.var_coach_description = ttk.StringVar()
        self.var_coach_web_link = ttk.StringVar()

        # participant
        self.var_participant_name = ttk.StringVar()
        self.var_participant_first_name = ttk.StringVar()
        self.var_participant_last_name = ttk.StringVar()
        self.var_participant_email = ttk.StringVar()
        self.var_participant_phone = ttk.StringVar()
        self.var_start_date = ttk.StringVar()
        self.var_end_date = ttk.StringVar()

        # notes
        self.notes_wishes = None
        self.notes_other = None
        
        style = ttk.Style()
        style.configure("Custom.TFrame", bordercolor="red")

        self._full_screen_window()
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.pages = {}
        self.add_page(page_class=frames.matching.Matching)
        self.add_page(page_class=frames.choose_module.ModulePicker)
        self.add_page(page_class=frames.overview.Overview)
        self.add_page(page_class=frames.choose_package.PackagePicker)
        self.add_page(page_class=frames.participant_notes.Notes)
        self.add_page(page_class=frames.home.Home)

        # starting page
        # self.show_page(frames.choose_package.PackagePicker)
        # self.show_page(frames.choose_module.ModulePicker)
        # self.show_page(frames.matching.Matching)
        # self.show_page(frames.overview.Overview)
        self.show_page(frames.home.Home)

        self._menu()
            
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

    def _menu(self) -> None:
        # Create a menu
        menu = ttk.Menu(self)

        # Create a sub-menu for "Package"
        package_menu = ttk.Menu(menu, tearoff=0)
        package_menu.add_command(label="Coaching-Pläne", command= lambda: self.show_page(frames.choose_package.PackagePicker))
        package_menu.add_command(label="BeginnerLuft Service", command= lambda: self.show_page(frames.choose_module.ModulePicker))
        package_menu.add_command(label="Matching", command= lambda: self.show_page(frames.matching.Matching))
        package_menu.add_command(label="Coaching-Notizen", command= lambda: self.show_page(frames.participant_notes.Notes))
        package_menu.add_command(label="Coaching-Überblick", command= lambda: self.show_page(frames.overview.Overview))
        menu.add_cascade(label="Coaching Menü", menu=package_menu)

        # Attach the menu to the window
        self.config(menu=menu)

    def show_page(self, page) -> None:
        """
        Lift a particular page to the foreground to make it visible
        :param page: the page to be shown
        :return None
        """
        self.pages[page].tkraise()

    def _trace_package(self) -> None:
        """
        Trace the variable for chosen package
        :return None
        """

        

if __name__ == "__main__":
    config_database = config_database.ConfigDataBase()
    database_name = config_database.get_database_info()["database name"]
    environment = config_database.get_database_info()["environment"]

    db = database.DataBase(path=database_name)
    app = App(database=db, active_environment=environment)
    app.mainloop()