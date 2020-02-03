from mycroft import MycroftSkill, intent_file_handler
import GPIO


#  https://github.com/MycroftAI/picroft_example_skill_gpio/blob/master/__init__.py
class LampsControl(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.lampa1 = "GPIO1"

    @intent_file_handler('start.lamps.intent')
    def handle_start_lamps(self, message):
        GPIO.set(self.lampa1, "On")
        self.speak_dialog('control.lamps')

    @intent_file_handler('stop.lamps.intent')
    def handle_stop_lamps(self, message):
        GPIO.set(self.lampa1, "Off")
        self.speak_dialog('control.lamps')


def create_skill():
    return LampsControl()

