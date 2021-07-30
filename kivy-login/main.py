from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
from kivy.uix.screenmanager import ScreenManager, Screen
# import MysqlClass
# from kivymd.uix.boxlayout import MDBoxLayout
# from kivy.uix.image import Image

class ListingsScreen(Screen):
    pass

class AccountCreation(Screen):
    def account_made_in_db(self):
        if self is None:
            return
        global new_user
        global new_pass
        new_user = self.ids.new_use.text
        new_pass = self.ids.new_password.text

        self.ids.new_use.text = ""
        self.ids.new_password.text = ""

class BuyingScreen(Screen):
    pass

class MarketScreen(Screen):
    pass

class LoginScreen(Screen):

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
        # print(username)
        password = self.ids.password.text

        self.ids.user.text = ""
        self.ids.password.text = ""

class WindowManager(ScreenManager):
    pass

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        return Builder.load_file('login.kv')


MainApp().run()
