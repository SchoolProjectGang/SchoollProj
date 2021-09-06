from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.dialog import MDDialog
from core.setup import modify
from utils.check_mysql import check


class SetupScreen(Screen):
    dialog = None

    def update_creds(self):
        if self is None:
            return

        if self.auth():
            password = self.ids.password.text
            database = self.ids.database.text
            modify(password, database)
            self.ids.password.text = ""
            self.ids.database.text = ""
        else:
            self.ids.password.text = ""
            self.ids.database.text = ""
            self.show_alert_dialog()

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="[font=Exo-VariableFont_wght]Invalid Password Or Database[/font]",
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
        password = self.ids.password.text
        # print(username)
        database = self.ids.database.text
        return check(password, database)

        # modify()
    pass
