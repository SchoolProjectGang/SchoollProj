from kivymd.uix.card import MDCard
# from kivy.animation import Animation
# from kivy.clock import Clock
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRoundFlatButton
from kivy.uix.screenmanager import Screen
from core.MysqlClass import Mysql
from core.User_buy import UserData
import core.username


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
                    text=f"Buy {self.items[i][1]}", on_release=self.show_alert_dialog)
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
            UserData(core.username.global_username).writing(self.game_name)
            self.dialog.dismiss()

    def open(self, name, _):
        x = Mysql()
        x.add_game(name, core.username.global_username)
        self.close_dialog(_)
        self.show_transaction_complete_dialog(_)
