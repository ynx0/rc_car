import RPi.GPIO as GPIO
import time
from enum import Enum

motor_pin1 = 13
motor_pin2 = 12
turn_pin1 = 23
turn_pin2 = 24

pwm_freq = 20  # hz, allows for more granular speed control than say, 300hz
turn_freq = 10

min_speed = 20  # duty cycle
max_speed = 35  # can actually go higher, like 100% duty cycle, but eh

turn_duty = 30
turn_slp_interval = 0.125



class Direction(Enum):
    ABSOLUTE_LEFT = 0
    MID_LEFT = 1
    MIDDLE = 2
    MID_RIGHT = 3
    ABSOLUTE_RIGHT = 4

    GENERAL_LEFT = 5
    GENERAL_RIGHT = 6
    
    global current_direction
    def __init__(self, *args):
    	current_direction = MIDDLE

    def validateDirection(direction):
        if not isinstance(Direction):
            raise TypeError('Invalid parameter to normalize in direction')

    # todo add print statements
    def adjDirection(direction):
        validateDirection(direction)

        # edge cases
        if direction == Direction.ABSOLUTE_LEFT:
            current_direction = Direction.ABSOLUTE_LEFT

        elif direction == Direction.ABSOLUTE_RIGHT:
            current_direction = Direction.ABSOLUTE_RIGHT

        elif direction == Direction.GENERAL_RIGHT:
        # from the middle, going right gets greater
        # see python enum docs as to why this works
            current_direction = Direction(current_direction.value + 1)

        elif direction == Direction.GENERAL_LEFT:
            current_direction = Direction(current_direction.value - 1)


# start in middle


def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(motor_pin1, GPIO.OUT)
    GPIO.setup(motor_pin2, GPIO.OUT)
    GPIO.setup(turn_pin1, GPIO.OUT)
    GPIO.setup(turn_pin2, GPIO.OUT)
    # https://electronics.stackexchange.com/a/80154/161902 for now going to
    # use 300hz
    global motor1
    global motor2
    global turn1
    global turn2
    motor1 = GPIO.PWM(motor_pin1, pwm_freq)
    motor2 = GPIO.PWM(motor_pin2, pwm_freq)
    turn1 = GPIO.PWM(turn_pin1, turn_freq)
    turn2 = GPIO.PWM(turn_pin2, turn_freq)
    motor1.start(0)
    motor2.start(0)
    turn1.start(0)
    turn2.start(0)



def stop(pwm):
    pwm.ChangeDutyCycle(0)


def stopBoth():
    stop(motor1)
    stop(motor2)


def normalize(speed):
    if speed > max_speed:
        speed = max_speed

    if speed < min_speed:
        speed = min_speed

    return speed


def forward(speed=min_speed):
    speed = normalize(speed)
    motor1.ChangeDutyCycle(speed)
    motor2.ChangeDutyCycle(0)


def backward(speed=min_speed):
    speed = normalize(speed)
    motor2.ChangeDutyCycle(speed)
    motor1.ChangeDutyCycle(0)


def smoothStop():
    pass


def smoothForward():
    pass


def smoothBackward(speed_ceil):
    pass


def resetTurnPWMS():
    turn1.ChangeDutyCycle(0)
    turn2.ChangeDutyCycle(0)


# simply turn, don't care about tracking direction in this method
def turn(pwm_turn):
    resetTurnPWMS()
    pwm_turn.ChangeDutyCycle(turn_duty)
    time.sleep(turn_slp_interval)
    pwm_turn.ChangeDutyCycle(0)


def turnLeft():
    turn(pwm1)
    if:
        pass


def turnRight():
    resetTurnPWMS()
    turn2.ChangeDutyCycle(turn_duty)
    turn


def turnToDirection(direction):
	pass

def main():
    setup()
    forward(30)
    time.sleep(10)
    stopBoth()
    time.sleep(5)
    backward(30)
    time.sleep(10)
    stopBoth()
    print('Finished :) Exitting')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
        print('\nExitting')
