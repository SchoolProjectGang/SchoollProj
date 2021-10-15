from kivy.uix.screenmanager import Screen
from core.setup import is_empty


class OpeningScreen(Screen):
    def title_vap(self):
        self.ids.my_image.source = "pictures/logo_pressed.jpg"

    def press_title(self):
        self.ids.my_image.source = "pictures/logo.jpg"

    def select_next_screen(self):
        if is_empty():
            return True
        else:
            return False
