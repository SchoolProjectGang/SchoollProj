from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import Screen
from core.User_buy import UserData
import core.username


class HistoryScreen(Screen):
    made = False

    def printing_out(self):
        if not self.made:
            self.made = True
            self.items = UserData(core.username.global_username).reading()
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
