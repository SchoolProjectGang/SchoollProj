# from pip._internal import main as pip_installer
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
import cache.username

# These are screen imports can be found in screens folder
from screens.SetupScreen import SetupScreen
from screens.HistoryScreen import HistoryScreen
from screens.LoginScreen import LoginScreen
from screens.ListingsScreen import ListingsScreen
from screens.OpeningScreen import OpeningScreen
from screens.AccountCreation import AccountCreation
from screens.BuyingScreen import BuyingScreen

# to install all the packages
# pip_installer(["install", "kivy"])

# stores username of user when logged in
cache.username.global_username = ""


class WindowManager(ScreenManager):
    pass


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"
        return Builder.load_file("core/login.kv")


MainApp().run()
