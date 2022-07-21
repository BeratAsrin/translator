from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from googletrans import Translator

class SayHello(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1

        self.input_language_text = TextInput()
        self.window.add_widget(self.input_language_text)

        self.translate_button = Button(text="Click to Translate")
        self.translate_button.bind(on_press=self.button_clicked)
        self.window.add_widget(self.translate_button)

        self.translation_label = Label(text="Welcome :)")
        self.window.add_widget(self.translation_label)

        return self.window

    def button_clicked(self,event):
        translator = Translator()
        input_text = self.input_language_text.text
        self.translation_label.text = translator.translate(text=input_text, dest="tr").text


if __name__ == "__main__":
    SayHello().run()
