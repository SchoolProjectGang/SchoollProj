from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
from kivy.uix.screenmanager import ScreenManager, Screen
# from kivymd.uix.boxlayout import MDBoxLayout
# from kivy.uix.image import Image

# the username and password we will use to authenticate
username = ""
password = ""


# screen for market
class MarketScreen(Screen):
    pass


# login screen that will be shown once app is started
class LoginScreen(Screen):
    dialog = None

    # show input fields
    def clearchecker(self):
        if self is not None:
            self.ids.welcome_label.text = "WELCOME"
            self.ids.user.text = ""
            self.ids.password.text = ""

    # login button, will update username and password and authenticate
    def login_to_db(self):
        if self is None:
            return
        global username
        global password
        username = self.ids.user.text
        password = self.ids.password.text


class WindowManager(ScreenManager):
    pass


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        return Builder.load_file('login.kv')


MainApp().run()
