import RPi.GPIO as GPIO
import time

pwm_pin1 = 13
pwm_pin2 = 12
turn_pin1 = 23
turn_pin2 = 24

pwm_freq = 20  # hz, allows for more granular speed control than say, 300hz
turn_freq = 10

min_speed = 20  # duty cycle
max_speed = 35  # can actually go higher, like 100% duty cycle, but eh

turn_duty = 30
turn_slp_interval = 0.125

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pwm_pin1, GPIO.OUT)
    GPIO.setup(pwm_pin2, GPIO.OUT)
    GPIO.setup(turn_pin1, GPIO.OUT)
    GPIO.setup(turn_pin2, GPIO.OUT)
    # https://electronics.stackexchange.com/a/80154/161902 for now going to
    # use 300hz
    global pwm1
    global pwm2
    global turn1
    global turn2
    pwm1 = GPIO.PWM(pwm_pin1, pwm_freq)
    pwm2 = GPIO.PWM(pwm_pin2, pwm_freq)
    turn1 = GPIO.PWM(turn_pin1, turn_freq)
    turn2 = GPIO.PWM(turn_pin2, turn_freq)
    pwm1.start(0)
    pwm2.start(0)
    turn1.start(0)
    turn2.start(0)


def stop(pwm):
    pwm.ChangeDutyCycle(0)

def stopBoth():
    stop(pwm1)
    stop(pwm2)

def normalize(speed):
	if speed > max_speed:
		speed = max_speed

	if speed < min_speed:
		speed = min_speed

	return speed

def forward(speed=min_speed):
    speed = normalize(speed)
    pwm1.ChangeDutyCycle(speed)
    pwm2.ChangeDutyCycle(0)


def backward(speed=min_speed):
    speed = normalize(speed)
    pwm2.ChangeDutyCycle(speed)
    pwm1.ChangeDutyCycle(0)

def smoothStop():
	pass

def smoothForward():
	pass

def smoothBackward(speed_ceil):
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

