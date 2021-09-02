from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivymd.uix.card import MDCard
# from kivy.animation import Animation
# from kivy.clock import Clock
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDRoundFlatButton
from kivy.uix.screenmanager import ScreenManager, Screen
from core.MysqlClass import Mysql
from core.new import password_maker
from core.User_buy import UserData

# stores username of user when logged in
global_username = ""


class OpeningScreen(Screen):
    def title_vap(self):
        self.ids.my_image.source = 'pictures/logo_pressed.jpg'

    def press_title(self):
        self.ids.my_image.source = 'pictures/logo.jpg'


class HistoryScreen(Screen):
    made = False

    def printing_out(self):
        if not self.made:
            self.made = True
            self.items = UserData(global_username).reading()
            if self.items == []:
                return
            for i in range(len(self.items)):
                card = MDCard(
                    size_hint=(None, None),
                    size=(1000, 25),
                    pos_hint={'center_x': 1, 'center_y': 1},
                    elevation=10,
                    padding=25,
                    spacing=25,
                    orientation='vertical'
                )
                label = MDLabel(text=f"{self.items[i]}")
                card.add_widget(label)
                self.ids['items'].add_widget(card)


class ListingsScreen(Screen):
    made = False
    dialog = None

    # function is called when user logs/signs in
    # sets up the listings screen and adds the buttons and games
    def button_setter(self):
        if not self.made:
            self.made = True
            self.items = Mysql().get_game_list()
            for i in range(len(self.items)):
                card = MDCard(
                    size_hint=(None, None),
                    size=(700, 200),
                    pos_hint={'center_x': 1, 'center_y': 1},
                    elevation=10,
                    padding=25,
                    spacing=25,
                    orientation='vertical'
                )
                label = MDLabel(text=f"{self.items[i][2]}")
                button = MDRoundFlatButton(
                    text=f"buy {self.items[i][1]}", on_release=self.show_alert_dialog)
                card.add_widget(button)
                card.add_widget(label)

                self.ids['items'].add_widget(card)

    def show_alert_dialog(self, instance):
        self.game_name = " ".join(instance.text.split()[1::])
        self.dialog = MDDialog(
            title=f"do you want to buy {self.game_name} for {self.get_price(self.game_name)}",
            buttons=[
                MDRoundFlatButton(
                    text="yes", on_release=lambda instance: self.open(self.game_name, instance)
                ),
                MDRoundFlatButton(
                    text="no", on_release=self.close_dialog
                ),
            ],
        )
        self.dialog.open()

    def show_transaction_complete_dialog(self, _):
        self.dialog = MDDialog(
            title=f"transaction complete!",
            buttons=[
                MDRoundFlatButton(
                    text="close", on_release=self.close_dialog,
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
            UserData(global_username).writing(self.name)
            self.dialog.dismiss()

    def open(self, name, _):
        x = Mysql()
        x.add_game(name, global_username)
        self.close_dialog(_)
        self.show_transaction_complete_dialog(_)


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

        global global_username
        if self.auth():
            global_username = self.username
            print(global_username)
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
                text=f"[font=Exo-VariableFont_wght]{self.password_made()}[/font]",
                buttons=[
                    MDRoundFlatButton(
                        text="[font=Exo-VariableFont_wght]GO BACK[/font]", on_release=self.close_dialog
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

        global global_username
        if username := self.auth():
            global_username = username
            print(global_username)
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
        return Builder.load_file('core/login.kv')


MainApp().run()
