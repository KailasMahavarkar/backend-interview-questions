from abc import ABC, abstractmethod

# ============================================
# COMMAND INTERFACE
# ============================================
class Command(ABC):
    """All commands must have an execute method"""
    @abstractmethod
    def execute(self):
        pass


# ============================================
# DEVICES (Receivers)
# ============================================
class Fan:
    """A ceiling fan"""

    def turn_on(self):
        return "🌀 Fan is spinning"

    def turn_off(self):
        return "🛑 Fan stopped"


class TV:
    """A television"""

    def turn_on(self):
        return "📺 TV is ON"

    def turn_off(self):
        return "⬛ TV is OFF"


# ============================================
# COMMANDS (Instructions)
# ============================================
class FanOnCommand(Command):
    def __init__(self, fan):
        self.fan = fan

    def execute(self):
        return self.fan.turn_on()


class FanOffCommand(Command):
    def __init__(self, fan):
        self.fan = fan

    def execute(self):
        return self.fan.turn_off()


class TVOnCommand(Command):
    def __init__(self, tv):
        self.tv = tv

    def execute(self):
        return self.tv.turn_on()


# ============================================
# REMOTE CONTROL (Invoker)
# ============================================
class RemoteControl:
    """Universal remote that can execute any command"""

    def __init__(self):
        self.command = None

    def set_command(self, command):
        """Program a button with a command"""
        self.command = command

    def press_button(self):
        """Execute the programmed command"""
        if self.command:
            return self.command.execute()
        return "No command set!"



if __name__ == "__main__":
    fan = Fan()
    tv = TV()

    remote = RemoteControl()
    remote.set_command(FanOnCommand(fan))
    print(remote.press_button())

    remote.set_command(FanOffCommand(fan))
    print(remote.press_button())