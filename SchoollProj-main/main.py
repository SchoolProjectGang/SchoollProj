from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivy.animation import Animation
from kivy.clock import Clock
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDRoundFlatButton
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivymd.uix.gridlayout import GridLayout
from core.MysqlClass import Mysql
import webbrowser


# class FirstScreen(Screen):
#     def __init__(self, **kwargs):
#         super(FirstScreen, self).__init__(**kwargs)
#         items = Mysql().get_game_list()
#         self.dialog = None
#         root = ScrollView()
#         layout = GridLayout(cols=1, size_hint_y=None)
#         for i in range(len(items)):
#             card = MDCard(
#                 size_hint=(None, None),
#                 size=(300, 200),
#                 pos_hint={'center_x': 1, 'center_y': 1},
#                 elevation=10,
#                 padding=25,
#                 spacing=25,
#                 orientation='vertical')
#             label = MDLabel(text=f"{items[i][1]}")
#             button = MDRoundFlatButton(
#                 text=f"buy for {items[i][2]}", on_release=self.show_alert_dialog)
#             print(button, i, items[i])
#             card.add_widget(label)
#             card.add_widget(button)
#             layout.add_widget(card)
#         root.add_widget(layout)
#         self.add_widget(root)
#
#     def show_alert_dialog(self, instance):
#         if not self.dialog:
#             print(instance)
#             self.dialog = MDDialog(
#                 title=f"do you want to buy {1} for {2}",
#                 buttons=[
#                     MDRoundFlatButton(
#                         text="yes", on_release=self.open
#                     ),
#                     MDRoundFlatButton(
#                         text="no", on_release=self.close_dialog
#                     ),
#                 ],
#             )
#         self.dialog.open()
#
#     def close_dialog(self, _):
#         if self.dialog is not None:
#             self.dialog.dismiss()
#
#     def open(self, _):
#         webbrowser.open('https://google.com')
#         self.close_dialog(_)


class OpeningScreen(Screen):
    def title_vap(self):
        self.ids.my_image.source = 'pictures/logo_pressed.jpg'

    def press_title(self):
        self.ids.my_image.source = 'pictures/logo.jpg'


class HistoryScreen(Screen):
    pass


class ListingsScreen(Screen):
    made = False
    dialog = None

    # function is called when user logs/signs in
    # sets up the listings screen and adds the buttons and games
    def cyka(self):
        if not self.made:
            self.made = True
            self.items = Mysql().get_game_list()
            for i in range(len(self.items)):
                card = MDCard(
                    size_hint=(None, None),
                    size=(300, 200),
                    pos_hint={'center_x': 1, 'center_y': 1},
                    elevation=10,
                    padding=25,
                    spacing=25,
                    orientation='vertical'
                )
                label = MDLabel(text=f"{self.items[i][2]}")
                button = MDRoundFlatButton(
                    text=f"buy {self.items[i][1]}", on_release=self.show_alert_dialog)
                card.add_widget(label)
                card.add_widget(button)
                self.ids['items'].add_widget(card)

    def show_alert_dialog(self, instance):
        name = " ".join(instance.text.split()[1::])
        self.dialog = MDDialog(
            title=f"do you want to buy {name} for {self.get_price(name)}",
            buttons=[
                MDRoundFlatButton(
                    text="yes", on_release=self.open
                ),
                MDRoundFlatButton(
                    text="no", on_release=self.close_dialog
                ),
            ],
        )
        self.dialog.open()

    def get_price(self, name):
        for i in self.items:
            if i[1] == name:
                return i[2]

    def close_dialog(self, _):
        if self.dialog is not None:
            self.dialog.dismiss()

    def open(self, _):
        webbrowser.open('https://google.com')
        self.close_dialog(_)


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
        return Builder.load_file('core/login.kv')


MainApp().run()
