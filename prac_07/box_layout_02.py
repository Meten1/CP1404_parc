from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout_02.kv')
        Window.size = (700, 200)
        return self.root


    def handle_greet(self):
        print("test")
        self.root.ids.output_label.text = "Hello"
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

    def clear_textbox(self):
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = 'Enter your name'


BoxLayoutDemo().run()
