from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
import core.username

"""Screens"""
from screens.HistoryScreen import HistoryScreen
from screens.LoginScreen import LoginScreen
from screens.ListingsScreen import ListingsScreen
from screens.OpeningScreen import OpeningScreen
from screens.AccountCreation import AccountCreation
from screens.BuyingScreen import BuyingScreen
from screens.MarketScreen import MarketScreen

# stores username of user when logged in
core.username.global_username = ""


class WindowManager(ScreenManager):
    pass


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"
        return Builder.load_file('core/login.kv')


MainApp().run()
