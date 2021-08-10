from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivymd.uix.card import MDCard
# from kivy.animation import Animation
# from kivy.clock import Clock
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDRoundFlatButton
from kivy.uix.screenmanager import ScreenManager, Screen
from MysqlClass import Mysql
from new import password_maker
import webbrowser


class OpeningScreen(Screen):
    def title_vap(self):
        self.ids.my_image.source = 'pictures/logo_pressed.jpg'

    def press_title(self):
        self.ids.my_image.source = 'pictures/logo.jpg'


class HistoryScreen(Screen):
    pass


class ListingsScreen(Screen):
    made = False

    def cyka(self):
        if not self.made:
            self.made = True
            for i in range(10):
                card = MDCard(
                    size_hint=(None, None),
                    size=(200, 100),
                    pos_hint={'center_x': 1, 'center_y': 1},
                    elevation=10,
                    padding=25,
                    spacing=25,
                    orientation='vertical'
                )
                button = MDRoundFlatButton(
                    text=f"button {i}", on_release=self.open)
                card.add_widget(button)
                self.ids['items'].add_widget(card)

    def open(self, _):
        webbrowser.open('https://google.com')


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
                text= f"[font=Exo-VariableFont_wght]{self.password_made()}[/font]",
                buttons=[
                    MDRoundFlatButton(
                        text= "[font=Exo-VariableFont_wght]GO BACK[/font]", on_release = self.close_dialog
                    )
                ]
            )
        self.dialog.open()


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


class WindowManager(ScreenManager):
    pass


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"
        return Builder.load_file('login.kv')


MainApp().run()
