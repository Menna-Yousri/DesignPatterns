from datetime import datetime

# Mediator interface
class Mediator:
    def get_time(self):
        pass

    def trigger_alarm(self):
        pass

    def prepare_coffee(self):
        pass

    def transport_robot(self):
        pass

    def open_window(self):
        pass

# Concrete mediator class
class HomeAutomation(Mediator):
    def __init__(self, my_calendar, alarm, coffee_machine, moving_robot, smart_window):
        self.my_calendar = my_calendar
        self.alarm = alarm
        self.coffee_machine = coffee_machine
        self.moving_robot = moving_robot
        self.smart_window = smart_window

    def get_time(self):
        return self.my_calendar.get_time()

    def trigger_alarm(self):
        self.alarm.ring()

    def prepare_coffee(self):
        self.coffee_machine.start()

    def transport_robot(self):
        self.moving_robot.transport()

    def open_window(self):
        self.smart_window.open()

# MyCalendar class
class MyCalendar:
    @staticmethod
    def get_time():
        return datetime.now().weekday() + 1  # Adding 1 to match Java's Calendar.DAY_OF_WEEK

class Alarm:
    def __init__(self, mediator):
        self.mediator = mediator

    def snooze(self):
        day = self.mediator.get_time()
        if day != 0 and day != 6:
            self.mediator.trigger_alarm()

    def ring(self):
        print("RINGGG..")

class CoffeeMachine:
    def __init__(self, mediator):
        self.mediator = mediator

    def start(self):
        print("Preparing Coffee")
        print("Finished Preparing Coffee")
        day = self.mediator.get_time()
        if day == 3:
            print("Adding Sugar!")
        self.mediator.transport_robot()

class MovingRobot:
    def __init__(self, mediator):
        self.mediator = mediator

    def transport(self):
        print("Robot Transporting!")
        print("Reached Destination!")
        self.mediator.open_window()

class SmartWindow:
    def open(self):
        print("Opening Window")

    def close(self):
        print("Closing Window")

if __name__ == "__main__":
    c = MyCalendar()
    window = SmartWindow()
    mr = MovingRobot(c)  # Since MovingRobot doesn't take any parameters in Java, passing None in Python
    cm = CoffeeMachine(c)  # Same as above
    mediator = HomeAutomation(c, Alarm(c), CoffeeMachine(c), MovingRobot(c), window)
    mediator.trigger_alarm()
