from kivy.app import App
from kivy.app import Widget
from kivy import Config


# Create a custom derived Kivy App class
class HelloWorld(App):
    def build(self):
        self.title = "Hello Kivy"
        self.root = Widget()
        return self.root  # build() should always return a widget object


# create a custom App object and start it running
# set window size
Config.set('graphics', 'width', 800)
Config.set('graphics', 'height', 600)
HelloWorld().run()
