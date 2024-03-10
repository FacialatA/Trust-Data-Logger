from machine import Pin, I2C
import utime
import uos
import bme280
import _thread
import generarnombrearchivo
import sensor
import led

# Calibro el sensor
led.led.on()
sensor.calibracion_sensor()
led.led.off()


#Espero
#utime.sleep(10)

# Registro los datos en el archivo
_thread.start_new_thread(led.parpadeo, ())
while True:
    sensor.escribir_datos_sensor()




