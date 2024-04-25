

from datetime import datetime
class MyCalendar:
    def get_time(self):
        cal = datetime.now()
        day_of_week = cal.weekday()  # Monday is 0 and Sunday is 6
        return day_of_week

class Mediator:
    def __init__(self, my_calendar, alarm, coffee_machine, moving_robot, smart_window=None):
        self.my_calendar = my_calendar
        self.alarm = alarm
        self.coffee_machine = coffee_machine
        self.moving_robot = moving_robot
        self.smart_window = smart_window

    def trigger_alarm(self):
        self.alarm.ring()

    def prepare_coffee(self):
        self.coffee_machine.start()

    def transport_robot(self):
        self.moving_robot.transport()

    def open_window(self):
        if self.smart_window:
            self.smart_window.open()


class Alarm:
    def __init__(self, mediator):
        self.mediator = mediator

    def snooze(self):
        day = self.mediator.my_calendar.get_time()
        if day != 5 and day != 6:  # Assuming Monday is 0 and Sunday is 6
            self.mediator.prepare_coffee()


    def ring(self):
        print("RINGGG..")


class CoffeeMachine:
    def __init__(self, mediator):
        self.mediator = mediator

    def start(self):
        print("Preparing Coffee")
        print("Finished Preparing Coffee")
        day = self.mediator.my_calendar.get_time()
        if day == 2:  # Assuming Wednesday is 2
            print("Adding Sugar!")
        self.mediator.transport_robot()


class MovingRobot:
    def __init__(self, mediator):
        self.mediator = mediator

    def transport(self):
        print("Robot Transporting!")
        print("Reached Destination!")
        self.mediator.trigger_alarm()
        self.mediator.open_window()


class SmartWindow:
    def open(self):
        print("Opening Window")

    def close(self):
        print("Closing Window")


class MediatorTester:
    @staticmethod
    def main():
        c = MyCalendar()
        window = SmartWindow()
        alarm = Alarm(c)
        mr = MovingRobot(c)
        cm = CoffeeMachine(c)
        mediator = Mediator(c, alarm, cm, mr, window)
        alarm.mediator = mediator
        mr.mediator = mediator
        cm.mediator = mediator
        alarm.snooze()


if __name__ == "__main__":
    MediatorTester.main()
