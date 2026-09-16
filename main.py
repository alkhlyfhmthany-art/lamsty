from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class LamstyApp(App):
    def build(self):
        box = BoxLayout(orientation='vertical', padding=20, spacing=20)
        box.add_widget(Label(text="Lamsty Store", font_size=32))
        box.add_widget(Label(text="متجر لمستي", font_size=24))
        box.add_widget(Button(text="ابدأ التسوق"))
        return box

LamstyApp().run()
