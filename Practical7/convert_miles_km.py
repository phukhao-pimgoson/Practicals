from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

KM_IN_MILES = 1.6  # There is 1.6 km in a mile


class ConvertMiles(App):
    def build(self):
        Window.size = (450, 300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def convert(self):
        value = self.valid_miles()
        result = value * KM_IN_MILES
        self.root.ids.output_label.text = str(result)

    def plus_minus_one(self, change):
        value = self.valid_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.convert()

    def valid_miles(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


ConvertMiles().run()
