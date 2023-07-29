import kivy
import math
kivy.require('2.0.0')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.base import EventLoop
from kivy.config import Config


class Container_CalculatorApp(App):

    def build(self):    
        Window.clearcolor = "7cf57b"
        Window.size = (275, 400)

        # Create the main layout
        layout = BoxLayout(orientation='vertical', padding=(dp(100), dp(10)))

        # Create the labels
        title = Label(text='SQUARE ROOTS', bold = True, size_hint = (1, 0.3), font_size = 32, color="016251", padding=(dp(10), dp(0)), pos_hint={'center_x': 0.5})
        label_containers = Label(text='Number of Containers:', size_hint = (1, 0.2), color="016251", valign= "bottom", padding=(dp(10), dp(0)))
        label_germination = Label(text='Germination Rate:', size_hint = (1, 0.2), color="016251", valign= "bottom", padding=(dp(10), dp(0)))
        label_extra_plugs = Label(text='Minimum Extra\nPlugs per Container:', size_hint = (1, 0.4), color="016251", valign= "bottom", padding=(dp(10), dp(0)))
        spacing_label1 = Label(text='', size_hint = (0.2, 0.2), padding=(dp(0), dp(0)))
        spacing_label2 = Label(text='', size_hint = (0.2, 0.2), padding=(dp(0), dp(0)))
        spacing_label3 = Label(text='', size_hint = (0.2, 0.2), padding=(dp(0), dp(0)))

        # Create the input fields
        self.container_input = TextInput(write_tab=False, multiline=False, cursor_color = "016251", size_hint = (None, None), size = (dp(150), dp(40)), pos_hint={'center_x': 0.5}, input_filter='int', padding=(dp(10), dp(5)))
        self.germination_input = TextInput(write_tab=False, multiline=False, cursor_color = "016251", size_hint = (None, None), size = (dp(150), dp(40)), pos_hint={'center_x': 0.5}, input_filter='int', padding=(dp(10), dp(5)))
        self.extra_plugs_input = TextInput(write_tab=False, multiline=False, cursor_color = "016251", size_hint = (None, None), size = (dp(150), dp(40)), pos_hint={'center_x': 0.5}, input_filter='int', padding=(dp(10), dp(5)))

        # Create the button
        button = Button(text='Calculate', on_press=self.on_button_press, disabled= False, background_color="016251",
                        size_hint=(None, None), size=(dp(150), dp(40)), pos_hint={'center_x': 0.5})

        # Create the result label
        self.result_label = Label(text='Result:', size_hint = (1, 0.2), color="016251", padding=(dp(10), dp(5)))

        # Define the focus behavior when Tab key is pressed
        self.container_input.focus_next = self.germination_input
        self.container_input.focus_previous = self.extra_plugs_input
        self.germination_input.focus_next = self.extra_plugs_input
        self.germination_input.focus_previous = self.container_input
        self.extra_plugs_input.focus_next = self.container_input
        self.extra_plugs_input.focus_previous = self.germination_input
        
        # Add the widgets to the layout
        layout.add_widget(title)
        layout.add_widget(label_containers)
        layout.add_widget(self.container_input)
        layout.add_widget(label_germination)
        layout.add_widget(self.germination_input)
        layout.add_widget(label_extra_plugs)
        layout.add_widget(self.extra_plugs_input)
        layout.add_widget(spacing_label1)
        layout.add_widget(button)
        layout.add_widget(spacing_label2)
        layout.add_widget(self.result_label)
        layout.add_widget(spacing_label3)

        return layout


    def on_start(self):
        # Configure the Tab key behavior
        Config.set('kivy', 'keyboard_mode', 'systemandmulti')
        
        # Set the initial focus on the first input field
        self.container_input.focus = True
        EventLoop.focus = self.container_input


    def on_button_press(self, button):
        # Get the input values
        container_value = self.container_input.text
        germination_value = self.germination_input.text
        extra_plugs_value = self.extra_plugs_input.text

        # Validate the input values
        # If number of containers is left blank, prompt user to enter a value
        if not container_value:
            self.result_label.text = 'Please enter the number of\ncontainers you wish to fill.'
            return
        
        # If germination rate is left blank, assume it is 100%
        if not germination_value.isdigit():
            germination_value = 100

        # If extra plugs is left blank, assume it is 0
        if not extra_plugs_value.isdigit():
            extra_plugs_value = 0

        # Perform calculations based on the input values
        print(f"{container_value = }")
        print(f"{germination_value = }")

        extra_plugs = int(extra_plugs_value) * int(container_value)
        print(f"{extra_plugs = }")

        plugs_needed_no_extras = math.ceil((int(container_value) * 146) / (int(germination_value) / 100))
        print(f"{plugs_needed_no_extras = }")

        plugs_needed = plugs_needed_no_extras + extra_plugs
        print(f"{plugs_needed = }")

        flats_162 = plugs_needed / 162
        print(f"{flats_162 = }")

        rounded_flats = math.ceil(flats_162)
        print(f"{rounded_flats = }")

        total_plugs_seeded = rounded_flats * 162
        print(f"{total_plugs_seeded = }")

        plug_remainder = total_plugs_seeded - plugs_needed_no_extras
        print(f"{plug_remainder = }")

        plug_remainder_per_container = plug_remainder/int(container_value)
        print(f"{plug_remainder_per_container = }\n")

        # Update the result label
        self.result_label.text = f"Flats to seed: {rounded_flats}\nTotal leftover plugs: {round(plug_remainder, 2)}\nLeftover plugs per container: {round(plug_remainder_per_container, 2)}"


if __name__ == '__main__':

    Container_CalculatorApp().run()