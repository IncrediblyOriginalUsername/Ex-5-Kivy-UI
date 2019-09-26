import os

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from threading import Thread
from time import sleep
from pidev.MixPanel import MixPanel
from pidev.kivy.PassCodeScreen import PassCodeScreen
from pidev.kivy.PauseScreen import PauseScreen
from pidev.kivy import DPEAButton
from pidev.kivy import ImageButton
from kivy.properties import ObjectProperty
from kivy.uix.slider import Slider
from kivy.uix.image import Image
from kivy.animation import Animation
from pidev.Joystick import Joystick
from kivy.clock import Clock
import random
MIXPANEL_TOKEN = "x"
MIXPANEL = MixPanel("Project Name", MIXPANEL_TOKEN)

SCREEN_MANAGER = ScreenManager()
MAIN_SCREEN_NAME = 'main'
ADMIN_SCREEN_NAME = 'admin'
SIDE_SCREEN_NAME = 'side'
ANI_SCREEN_NAME = "anim"
JOY_SCREEN_NAME = 'joy'


class ProjectNameGUI(App):
    """
    Class to handle running the GUI Application
    """

    def build(self):
        """
        Build the application
        :return: Kivy Screen Manager instance
        """
        return SCREEN_MANAGER


Window.clearcolor = (1, .3, 1, 1)  # White


class JoyScreen(Screen):
    joystick = Joystick(0, False)
    nma = ObjectProperty(None)
    aer = ObjectProperty(None)
    arm = ObjectProperty(None)
    now = ObjectProperty(None)
    global event1
    global event2
    global event3
    global event4
    global ft
    ft = 2
    def startThread(self):
        print("Thread")
        Thread(target=self.threads).start()

    def threads(self):
        while SCREEN_MANAGER.current == JOY_SCREEN_NAME:
            self.callback(1)
            self.cords(1)
            self.combo(1)
            self.backroundc(1)
            sleep(.01)
        print("Thread ended")
    def callback(self,dt):
        if(self.joystick.get_button_state(1)==1):
            self.nma.text = "Button 1 on"
        else:
            self.nma.text = "Button 1 off"
    def cords(self,dt):
        self.arm.text = "x:%f y:%f" % (self.joystick.get_both_axes()[0],self.joystick.get_both_axes()[1])
        self.arm.x = self.joystick.get_both_axes()[0]*Window.size[0] * 1/2
        self.arm.y = -self.joystick.get_both_axes()[1]*Window.size[1] * 1/2
    def backroundc(self,dt):
        global ft
        random.seed(ft)
        if(self.joystick.get_button_state(0)==1):
            Window.clearcolor = (random.random(),random.random(),random.random(),1)
            s = self.aer.text
            self.aer.text = "A"
            self.aer.text = "%s" % s
            ft = self.joystick.get_both_axes()[0] + self.joystick.get_both_axes()[1]


    def combo(self,dt):
        list = [1,2,3]
        if(self.joystick.button_combo_check(list)==1):
            self.aer.text = "Combo of 123 active"
        else:
            self.aer.text = "Combo of 123 not active"
    def __init__(self, **kwargs):
        Builder.load_file('joyScreen.kv')
        super(JoyScreen, self).__init__(**kwargs)
    def hi(self,df):
        print("hi")
    def canceled(self):
        global event1
        global event2
        global event3
        global event4
        event1.cancel()
        event2.cancel()
        event3.cancel()
        event4.cancel()
        print("Clock Canceled")

    def events(self):
        print("Clock")
        global event1
        global event2
        global event3
        global event4
        event1 = Clock.schedule_interval(self.callback, 1/100)
        event2 = Clock.schedule_interval(self.combo, 1/100)
        event4 = Clock.schedule_interval(self.backroundc, 1 / 100)
        event3 = Clock.schedule_interval(self.cords, 1/100)
    def yes(self):
        self.canceled() # commit this out to switch to thread instead of clock.
        SCREEN_MANAGER.current = MAIN_SCREEN_NAME

class SideScreen(Screen):
        def __init__(self, **kwargs):
            Builder.load_file('side.kv')
            super(SideScreen, self).__init__(**kwargs)
        def ye(self):
            SCREEN_MANAGER.current = MAIN_SCREEN_NAME

class AnimationScreen(Screen):
        animr = ObjectProperty(None)
        def __init__(self, **kwargs):
            Builder.load_file("animation.kv")
            super(AnimationScreen, self).__init__(**kwargs)
            anit = Animation(x=0, y=0) + Animation(size=(1, 1)) + Animation(x=500, y=500) + Animation(
                size=(1000, 1000))
            anit.repeat = True
            anit.start(self.animr)
        def yet(self):
            SCREEN_MANAGER.current = MAIN_SCREEN_NAME
class MainScreen(Screen):
    """
    Class to handle the main screen and its associated touch events
    """
    egg = ObjectProperty(None)
    egt = ObjectProperty(None)
    lma = ObjectProperty(None)
    lmt = ObjectProperty(None)
    sli = ObjectProperty(None)
    asd = ObjectProperty(None)
    global fy
    global f
    global counter
    counter = 0
    fy = True
    f = True

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        ani = Animation(x=100, y=200) + Animation(size=(800,800))+ Animation(x= 500, y = 500) + Animation(size=(100,100))
        ani.repeat = True
        ani.start(self.asd)
    def up(self):
        self.lmt.text = "%d" % self.sli.value
    def fellow(self):
       # SCREEN_MANAGER.get_screen(JOY_SCREEN_NAME).events() remeber that you can do this, but the on_enter in the kv is better
        SCREEN_MANAGER.current = JOY_SCREEN_NAME
    def gamers(self):
        SCREEN_MANAGER.current = ANI_SCREEN_NAME
    def riseup(self):

        SCREEN_MANAGER.current = SIDE_SCREEN_NAME


    def Motor(self):
        global f
        if(f ==True):
            self.lma.text = " Motor Off"
            f = False
        else:
            self.lma.text = "Motor On"
            f = True
    def changeText(self):
        global fy
        if( fy == True):
            self.egg.text = "Off"
            fy = False
        else:
            self.egg.text = "On"
            fy = True
    def counterButton(self):
        global counter
        counter = counter+1
        self.egt.text = "%d" % counter



    def pressed(self):
        """
        Function called on button touch event for button with id: testButton
        :return: None
        """
        PauseScreen.pause(pause_scene_name='pauseScene', transition_back_scene='main', text="Test", pause_duration=5)

    def admin_action(self):
        """
        Hidden admin button touch event. Transitions to passCodeScreen.
        This method is called from pidev/kivy/PassCodeScreen.kv
        :return: None
        """
        SCREEN_MANAGER.current = 'passCode'


class AdminScreen(Screen):
    """
    Class to handle the AdminScreen and its functionality
    """

    def __init__(self, **kwargs):
        """
        Load the AdminScreen.kv file. Set the necessary names of the screens for the PassCodeScreen to transition to.
        Lastly super Screen's __init__
        :param kwargs: Normal kivy.uix.screenmanager.Screen attributes
        """
        Builder.load_file('AdminScreen.kv')

        PassCodeScreen.set_admin_events_screen(ADMIN_SCREEN_NAME)  # Specify screen name to transition to after correct password
        PassCodeScreen.set_transition_back_screen(MAIN_SCREEN_NAME)  # set screen name to transition to if "Back to Game is pressed"

        super(AdminScreen, self).__init__(**kwargs)

    @staticmethod
    def transition_back():
        """
        Transition back to the main screen
        :return:
        """
        SCREEN_MANAGER.current = MAIN_SCREEN_NAME

    @staticmethod
    def shutdown():
        """
        Shutdown the system. This should free all steppers and do any cleanup necessary
        :return: None
        """
        os.system("sudo shutdown now")

    @staticmethod
    def exit_program():
        """
        Quit the program. This should free all steppers and do any cleanup necessary
        :return: None
        """
        quit()
"""
Widget additions
"""

Builder.load_file('main.kv')
SCREEN_MANAGER.add_widget(MainScreen(name=MAIN_SCREEN_NAME))
SCREEN_MANAGER.add_widget(PassCodeScreen(name='passCode'))
SCREEN_MANAGER.add_widget(PauseScreen(name='pauseScene'))
SCREEN_MANAGER.add_widget(SideScreen(name=SIDE_SCREEN_NAME))
SCREEN_MANAGER.add_widget(AdminScreen(name=ADMIN_SCREEN_NAME))
SCREEN_MANAGER.add_widget(AnimationScreen(name=ANI_SCREEN_NAME))
SCREEN_MANAGER.add_widget(JoyScreen(name=JOY_SCREEN_NAME))

"""
MixPanel
"""


def send_event(event_name):
    """
    Send an event to MixPanel without properties
    :param event_name: Name of the event
    :return: None
    """
    global MIXPANEL

    MIXPANEL.set_event_name(event_name)
    MIXPANEL.send_event()


if __name__ == "__main__":
    # send_event("Project Initialized")
    # Window.fullscreen = 'auto'
    ProjectNameGUI().run()
