from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
from kivy.uix.screenmanager import ScreenManager, Screen
# from kivymd.uix.boxlayout import MDBoxLayout
# from kivy.uix.image import Image

class BuyingScreen(Screen):
    pass

class MarketScreen(Screen):
    pass


class LoginScreen(Screen):
    pass



class WindowManager(ScreenManager):
    pass


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        return Builder.load_file('login.kv')


MainApp().run()