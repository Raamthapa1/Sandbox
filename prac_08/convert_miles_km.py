from kivy.app import App
from kivy.lang import Builder


class ConvertMilesToKm(App):
    """ convert miles to km is a kivy add to convert the input miles to kilometers"""

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Miles to Kilometers converter"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def calculation(self):
