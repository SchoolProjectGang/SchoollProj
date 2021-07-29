from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
# from kivymd.uix.boxlayout import MDBoxLayout
# from kivy.uix.image import Image


class SchoolProjApp(MDApp):
    dialog = None

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        return Builder.load_file('login.kv')

    def loggerchecker(self):
        if self.root is not None:
            self.root.ids.welcome_label.text = f'Sup {self.root.ids.user.text}!'

    def clearchecker(self):
        if self.root is not None:
            self.root.ids.welcome_label.text = "WELCOME"
            self.root.ids.user.text = ""
            self.root.ids.password.text = ""

    def show_alert_dialog(self):
        if self.root is None:
            return
        if not self.dialog:
            self.dialog = MDDialog(
                title="LOGGED IN",
                text=f"you have logged in {self.root.ids.user.text} ",
                buttons=[
                    MDFlatButton(
                        text="Cancel", on_release=self.close_dialog
                    ),
                    MDRectangleFlatButton(
                        text="Continue", on_release=self.continue_dialog
                    )
                ],

            )

        self.dialog.open()

    def close_dialog(self, obj):
        if self.dialog is None:
            return
        self.dialog.dismiss()

    def continue_dialog(self, obj):
        if self.dialog is None or self.root is None:
            return
        self.dialog.dismiss()
        self.root.ids.welcome_label.text = "You have logged out"
        self.root.ids.welcome_label.font_size = 20


SchoolProjApp().run()
