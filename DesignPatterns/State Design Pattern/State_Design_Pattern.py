from abc import *


class State(ABC):
    """
    Interface for States
    """
    @abstractmethod
    def push_up_btn(self):
        pass

    @abstractmethod
    def push_down_btn(self):
        pass


class GroundFloor(State):
    def push_up_btn(self):
        self.elevator.set_elevator(FirstFloor())
        print("You are going to first floor")

    def push_down_btn(self):
        print("You are already at ground floor")


class FirstFloor(State):
    def push_up_btn(self):
        self.elevator.set_elevator(SecondFloor())
        print("You are going to Second floor")

    def push_down_btn(self):
        self.elevator.set_elevator(GroundFloor())
        print("You are going to ground floor")


class SecondFloor(State):
    def push_up_btn(self):
        print("You are already at top floor")

    def push_down_btn(self):
        self.elevator.set_elevator(FirstFloor())
        print("You are going to first floor")


class Elevator(object):
    def __init__(self):
        self.set_elevator(GroundFloor())

    def set_elevator(self, state: State):
        self._state = state
        self._state.elevator = self

    def push_up(self):
        self._state.push_up_btn()

    def push_down(self):
        self._state.push_down_btn()

    def current_state(self):
        print(f"You are at {self._state.__class__.__name__}")


if __name__ == "__main__":
    elevator = Elevator()

    elevator.current_state()
    elevator.push_down()
    elevator.push_up()
    elevator.push_up()
    elevator.current_state()
    elevator.push_up()
    elevator.current_state()