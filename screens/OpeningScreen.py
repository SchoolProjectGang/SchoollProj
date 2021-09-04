from kivy.uix.screenmanager import Screen


class OpeningScreen(Screen):
    def title_vap(self):
        self.ids.my_image.source = 'pictures/logo_pressed.jpg'

    def press_title(self):
        self.ids.my_image.source = 'pictures/logo.jpg'
