import os
from threading import Thread
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFlatButton
from kivy.uix.screenmanager import Screen
from core.User_buy import UserData
import cache.username


class HistoryScreen(Screen):
    made = False

    def printing_out(self):
        if not self.made:
            self.made = True
            self.items = UserData(cache.username.global_username).reading()
            if self.items == []:
                return
            for i in range(len(self.items)):
                card = MDCard(
                    size_hint=(None, None),
                    size=(1000, 50),
                    pos_hint={"center_x": 1, "center_y": 1},
                    elevation=10,
                    padding=25,
                    spacing=25,
                    orientation="vertical",
                )
                label = MDFlatButton(
                    text=f"{self.items[i]}", on_release=self.show_game_starting
                )
                card.add_widget(label)
                self.ids["items"].add_widget(card)

    def show_game_starting(self, instance):
        new_thread = Thread(target=game_start, args=[])
        new_thread.start()


def game_start():
    os.system("gnome-mahjongg")
