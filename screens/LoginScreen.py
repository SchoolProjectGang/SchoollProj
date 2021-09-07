from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRoundFlatButton
from kivy.uix.screenmanager import Screen
from core.MysqlClass import Mysql
import cache.username


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

        if username := self.auth():
            cache.username.global_username = username
            print(cache.username.global_username)
            self.ids.user.text = ""
            self.ids.password.text = ""
        else:
            self.ids.user.text = ""
            self.ids.password.text = ""
            self.show_alert_dialog()

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="[font=Exo-VariableFont_wght]Invalid Username Or Password[/font]",
                buttons=[
                    MDRoundFlatButton(
                        text="[font=Exo-VariableFont_wght]GO BACK[/font]", on_release=self.close_dialog
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
