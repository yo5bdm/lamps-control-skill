from mycroft import MycroftSkill, intent_file_handler


class LampsControl(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('control.lamps.intent')
    def handle_control_lamps(self, message):
        self.speak_dialog('control.lamps')


def create_skill():
    return LampsControl()

