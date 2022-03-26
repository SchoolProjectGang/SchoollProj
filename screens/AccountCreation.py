from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRoundFlatButton
from kivy.uix.screenmanager import Screen
from core.MysqlClass import Mysql
from core.new import password_maker
import cache.username


class AccountCreation(Screen):
    dialog = None
    username, password = "", ""
    k = ""

    def account_made_in_db(self):
        if self is None:
            return True

        self.username = self.ids.new_use.text
        self.password = self.ids.new_password.text

        x = Mysql()

        if self.auth():
            cache.username.global_username = self.username
            print(cache.username.global_username)
            self.ids.new_use.text = ""
            self.ids.new_password.text = ""
            x.add_userdata(self.username, self.password)
            with open(f"./core/critcalfiles/{self.username}_data.txt", "w"):
                pass
        else:
            self.ids.new_use.text = ""
            self.ids.new_password.text = ""
            self.show_alert_dialog()

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="[font=Exo-VariableFont_wght]Invalid Username Or Password[/font]",
                buttons=[
                    MDRoundFlatButton(
                        text="[font=Exo-VariableFont_wght]GO BACK[/font]",
                        on_release=self.close_dialog,
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

    def password_made(self):
        class_holder = password_maker(6)
        self.k = class_holder.generator()
        return self.k

    def show_password_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="[font=Exo-VariableFont_wght]Your Password is[/font]",
                text=f"[font=Exo-VariableFont_wght]{self.password_made()}[/font]",
                buttons=[
                    MDRoundFlatButton(
                        text="[font=Exo-VariableFont_wght]GO BACK[/font]",
                        on_release=self.close_dialog,
                    )
                ],
            )
        self.dialog.open()
