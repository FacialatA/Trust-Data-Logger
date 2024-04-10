import utime
import _thread
import sensor
import led

# Calibro el sensor
led.led.on()
sensor.calibracion_sensor()
led.led.off()


#Espero
utime.sleep(1)

# Registro los datos en el archivo mientras en otro hilo parpadea el led
_thread.start_new_thread(led.parpadeo, ())
while True:
    sensor.escribir_datos_sensor()




