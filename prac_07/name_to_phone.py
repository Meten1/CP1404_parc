
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class NPdisplay(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name_to_phone = {"Bob Brown": "0414144411", "Cat Cyan": "0441411211", "Oren Ochre": "0432123456"}

    def build(self):
        self.title = "Name -- Phone Display"
        self.root = Builder.load_file('name_to_phone.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name, phone in self.name_to_phone.items():
            out_label = Label(text = "{}'s phone number is {}".format(name, phone))
            self.root.ids.main.add_widget(out_label)




NPdisplay().run()

