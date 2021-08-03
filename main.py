from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDRoundFlatButton
from kivy.uix.screenmanager import ScreenManager, Screen
from MysqlClass import Mysql

class OpeningScreen(Screen):
    pass
    # def title_vap(self):
      #  self.ids.my_image.source = 'pictures/logo_pressed.jpg'
    #def press_title(self):
     #   self.ids.my_image.source = 'pictures/logo.jpg'
    


class HistoryScreen(Screen):
    pass


class ListingsScreen(Screen):
    pass


class AccountCreation(Screen):
    dialog = None
    username, password = "", ""

    def account_made_in_db(self):
        if self is None:
            return True

        self.username = self.ids.new_use.text
        self.password = self.ids.new_password.text

        x = Mysql()

        if self.auth():
            self.ids.new_use.text = ""
            self.ids.new_password.text = ""
            x.add_userdata(self.username, self.password)
        else:
            self.ids.new_use.text = ""
            self.ids.new_password.text = ""
            self.show_alert_dialog()

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Invalid Username Or Password",
                buttons=[
                    MDRoundFlatButton(
                        text="Go Back To Create Account", on_release=self.close_dialog
                    ),
                ],
            )
        self.dialog.open()

    def close_dialog(self, obj):
        if self.dialog is not None:
            self.dialog.dismiss()

    def auth(self):
        self.username = self.ids.new_use.text
        self.password = self.ids.new_password.text
        return Mysql().check_first_letter(self.username, self.password)


class BuyingScreen(Screen):
    pass


class MarketScreen(Screen):
    pass


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

        if self.auth():
            self.ids.user.text = ""
            self.ids.password.text = ""
        else:
            self.ids.user.text = ""
            self.ids.password.text = ""
            self.show_alert_dialog()

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Invalid Username Or Password",
                buttons=[
                    MDRoundFlatButton(
                        text="Go Back To Login Screen", on_release=self.close_dialog
                    ),
                ],
            )
        self.dialog.open()

    def close_dialog(self, obj):
        if self.dialog is not None:
            self.dialog.dismiss()

    def auth(self):
        username = self.ids.user.text
        # print(username)
        password = self.ids.password.text
        return Mysql().check_creds(username, password)


class WindowManager(ScreenManager):
    pass


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"
        return Builder.load_file('login.kv')


MainApp().run()
