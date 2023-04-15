import datetime
import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Querybox
from tkinter import filedialog


def choose_date(title: str, start_date: datetime.date = datetime.date.today(), bootstyle: str = "primary", parent=None) -> datetime.date:
    """
    Let the user select a date from a date picker
    :param title: the title for the date picker windows
    :param start_date: the date at which the date picker will start at
    :param bootstyle: the ttkbootstyle style, e.g. primary, secondary etc.
    :param parent: the popup will appear to the bottom right of the parent widget, otherwise centered on the screen
    :return the chosen date
    """
    qbox = Querybox()
    start_date = datetime.datetime.combine(start_date, datetime.datetime.min.time())
    if parent is not None:
        chosen_datetime = qbox.get_date(parent=parent, title=title, firstweekday=0, startdate=start_date,
                                   bootstyle=bootstyle)
    else:
        chosen_datetime = qbox.get_date(title=title, firstweekday=0, startdate=start_date,
                                   bootstyle=bootstyle)
    
    return chosen_datetime


def ask_for_filename(parent: ttk.Window, title: str, initialdir: str, initialfile: str,
            defaultextension: str=".pdf") -> str:
    """
    Ask user for a file name to save a file
    :param parent: the window to place the dialog on top of
    :param initialdir: the directory that the dialog starts in
    :param initialfile: the file selected upton opening of the dialog
    :param defaultextension: default extension to append to file
    :return chosen file_name
    """

    file_name = filedialog.asksaveasfilename(parent=parent, title=title, initialdir=initialdir, initialfile=initialfile,
                                             defaultextension=defaultextension)
    
    return file_name