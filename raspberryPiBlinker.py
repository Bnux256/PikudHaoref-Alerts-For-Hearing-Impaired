import os
from time import sleep
from gpiozero import LED


def gpioAlert():
    # defining gpio pins
    led_pin = LED(4)
    buzzer_pin = LED(17)
    motor_pin = LED(27)
    i = 0
    while i < 50:
        # running 10 seconds
        led_pin.on()  # giving 3.3V to the Led for 0.1 seconds - making it blink
        buzzer_pin.on()  # turning buzzer on
        motor_pin.on() # turning on vibrating motor
        sleep(.100)
        led_pin.off()  # turning LED off
        # alert sound is 3 seconds. we don't want it so start while it is already playing
        if i % 17 == 0:
            os.system("omxplayer --no-keys -o both tts.mp3 &")  # playing alert sound
        sleep(.100)
        i += 1
