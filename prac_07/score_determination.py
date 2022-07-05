from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class ScoreDetermination(App):
    def build(self):
        self.title = "Score determination"
        self.root = Builder.load_file('score_determination.kv')
        Window.size = (700, 300)
        return self.root

    def clear_textbox(self):
        self.root.ids.input_score.text = ''
        self.root.ids.output_label.text = 'Enter your score'

    def determine_score(self):
        if int(self.root.ids.input_score.text) >= 50:
            pass_or_fail = "Pass"
        else:
            pass_or_fail = "Fail"
        if int(self.root.ids.input_score.text) >= 85:
            grade = "HD"
        elif int(self.root.ids.input_score.text) >= 75:
            grade = "D"
        elif int(self.root.ids.input_score.text) >= 65:
            grade = "C"
        elif int(self.root.ids.input_score.text) >= 50:
            grade = "P"
        else:
            grade = "N"
        self.root.ids.output_label.text = "Your grade is {}, you {}!".format(grade, pass_or_fail)

ScoreDetermination().run()