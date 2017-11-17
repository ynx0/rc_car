from enum import Enum, unique

@unique
class Turn(Enum):
    ABS_LEFT = -2
    MID_LEFT = -1
    CENTER = 0
    MID_RIGHT = 1
    ABSOLUTE_RIGHT = 2

    def __str__(self):
        return self.name

    def is_left(self):
        return self.value < 0

    def is_right(self):
        return self.value > 0

    def is_center(self):
        return self.value == 0


@unique
class Motion(Enum):
    FORWARD = 1
    BACKWARD = -1
    STOPPED = 0

    def __str__(self):
        return self.name

    def is_going_forward(self):
        return self.value == 1

    def is_going_backwards(self):
        return self.value == -1

    def is_stopped(self):
        return self.value == 0