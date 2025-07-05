import utime
import bme280
import utime
from machine import Pin, I2C
import config_file
import generarnombrearchivo

i2c = I2C(1, scl=Pin(15), sda=Pin(14))
bme = bme280.BME280(i2c=i2c)

# Funcion para calibracion del sensor
def calibracion_sensor():
        print(bme.values)
        utime.sleep(1)
        print(bme.values)
        utime.sleep(1)
        print(bme.values)
        utime.sleep(1)
        print(bme.values)
        utime.sleep(1)
        print(bme.values)
        utime.sleep(1)
    

# Abro el archivo CSV y defino la funcion para guardar los datos    

doc = open(generarnombrearchivo.nombredearchivo, "w")
# Escribo los datos que recogí en el archivo que abrí
def escribir_datos_sensor():
    # Recojo los datos en variables
    temp = (bme.values[0][:-1].replace(".", ","))
    pres = (bme.values[1][:-3].replace(".", ","))
    hum = (bme.values[2][:-1].replace(".", ","))
    hora_local = utime.localtime()
    hora = hora_local[3]
    minuto = hora_local[4]
    segundo = hora_local[5]
    
    # Abro el archivo en modo escritura
    doc.write(str(hora) + " ")
    doc.write(str(minuto) + " ")
    doc.write(str(segundo) + " ")
    doc.write(str(temp) + " ")
    doc.write(str(pres) + " ")
    doc.write(str(hum) + "\n")
    
    # Guardo la informacion en el archivo
    doc.flush()
    
    # Espero 20 minutos para repetir el ciclo
    utime.sleep(config_file.demora)