import datetime
from ttkbootstrap.dialogs import Querybox

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