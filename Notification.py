from flet import UserControl, SnackBar, Text, TextThemeStyle, DismissDirection, SnackBarBehavior

class Notification(UserControl):
    def __init__(self, page, message, color):
        super().__init__()
        self.page = page
        self.message = message
        self.color = color
        self.content = Text(value=message, color = color, style=TextThemeStyle.BODY_LARGE)
        self.snack_bar = SnackBar(
            content=self.content,
            elevation=10,
            duration=6000,
            show_close_icon=True,
            behavior=SnackBarBehavior.FLOATING,
            dismiss_direction=DismissDirection.END_TO_START
        )
    
    def show_message(self):
        self.page.snack_bar = self.snack_bar
        self.snack_bar.open = True
        self.page.update()