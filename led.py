from machine import Pin, I2C
import utime
import sensor

led = Pin(25, Pin.OUT)

# Funcion "parpadeo" para que el Led integrado de la Pico parpadee cada 1 segundo
def parpadeo():
    while True:
        led.on()
        utime.sleep(1)
        led.off()
        utime.sleep(1)

