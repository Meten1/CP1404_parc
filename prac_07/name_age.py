from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class NameAge(App):
    output_information = StringProperty()

    def __init__(self):
        super().__init__()
        self.name_to_age = {"Bob Brown": "16", "Cat Cyan": "17", "Oren Ochre": "18",
                            "June": "19", "Smith": "20"}

    def build(self):
        self.title = "Name -- Age display"
        self.root = Builder.load_file("name_age.kv")
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.name_to_age:
            temp_button = Button(text=name)
            temp_button.bind(on_release=self.press_entry)
            self.root.ids.entries_box.add_widget(temp_button)

    def press_entry(self, instance):
        name = instance.text
        self.output_information = "{}'s age is {}".format(name, self.name_to_age[name])

    def clear_all(self):
        """Clear all of the widgets that are children of the "entries_box" layout widget."""
        self.root.ids.entries_box.clear_widgets()


NameAge().run()
