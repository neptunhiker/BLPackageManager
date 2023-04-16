from ttkbootstrap import toast


class MessageBox(toast.ToastNotification):

    def __init__(self, title: str, message: str, duration_in_seconds: int) -> None:
        super(MessageBox, self).__init__(title=title, message=message, duration=duration_in_seconds*1000)

    def show_message(self) -> None:
        """
        Show the message box
        :return None
        """
        self.show_toast()
