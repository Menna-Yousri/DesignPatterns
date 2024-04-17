# Command interface
class Command:
    def execute(self):
        pass

    def unexecute(self):
        pass

# Concrete command for turning a device on
class TurnOnCommand(Command):
    def __init__(self, device):
        self.device = device
        self.previous_state = None

    def execute(self):
        self.previous_state = self.device.get_state()
        self.device.turn_on()

    def unexecute(self):
        if self.previous_state:
            self.device.set_state(self.previous_state)

# Concrete command for turning a device off
class TurnOffCommand(Command):
    def __init__(self, device):
        self.device = device
        self.previous_state = None

    def execute(self):
        self.previous_state = self.device.get_state()
        self.device.turn_off()

    def unexecute(self):
        if self.previous_state:
            self.device.set_state(self.previous_state)

# Receiver interface
class Device:
    def turn_on(self):
        pass

    def turn_off(self):
        pass

    def get_state(self):
        pass

    def set_state(self, state):
        pass

# Concrete receiver for a TV
class TV(Device):
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        print("TV is now on")
        self.is_on = True

    def turn_off(self):
        print("TV is now off")
        self.is_on = False

    def get_state(self):
        return "on" if self.is_on else "off"

    def set_state(self, state):
        if state == "on":
            self.turn_on()
        else:
            self.turn_off()

# Concrete receiver for a stereo
class Stereo(Device):
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        print("Stereo is now on")
        self.is_on = True

    def turn_off(self):
        print("Stereo is now off")
        self.is_on = False

    def get_state(self):
        return "on" if self.is_on else "off"

    def set_state(self, state):
        if state == "on":
            self.turn_on()
        else:
            self.turn_off()

# Invoker
class RemoteControl:
    def __init__(self):
        self.on_commands = [None] * 4
        self.off_commands = [None] * 4
        self.undo_stack = []

    def set_command(self, slot, on_command, off_command):
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def press_on_button(self, slot):
        if self.on_commands[slot]:
            self.on_commands[slot].execute()
            self.undo_stack.append(self.on_commands[slot])

    def press_off_button(self, slot):
        if self.off_commands[slot]:
            self.off_commands[slot].execute()
            self.undo_stack.append(self.off_commands[slot])

    def press_undo_button(self):
        if self.undo_stack:
            last_command = self.undo_stack.pop()
            last_command.unexecute()

# Example usage with undo feature
if __name__ == "__main__":
    # Create devices
    tv = TV()
    stereo = Stereo()

    # Create command objects
    turn_on_tv_command = TurnOnCommand(tv)
    turn_off_tv_command = TurnOffCommand(tv)
    turn_on_stereo_command = TurnOnCommand(stereo)
    turn_off_stereo_command = TurnOffCommand(stereo)

    # Create remote control
    remote = RemoteControl()

    # Set commands for slots
    remote.set_command(0, turn_on_tv_command, turn_off_tv_command)
    remote.set_command(1, turn_on_stereo_command, turn_off_stereo_command)

    # Press buttons
    remote.press_on_button(0)  # Outputs: TV is now on
    remote.press_off_button(0)  # Outputs: TV is now off
    remote.press_on_button(1)  # Outputs: Stereo is now on
    remote.press_off_button(1)  # Outputs: Stereo is now off

    # Undo last action
    remote.press_undo_button()  # Outputs: Stereo is now on (undo last action)
    remote.press_undo_button()
    remote.press_undo_button()
    remote.press_undo_button()