from machine import Pin, I2C
import utime
import uos
import bme280
import _thread

i2c = I2C(1, scl=Pin(15), sda=Pin(14))

bme = bme280.BME280(i2c=i2c)

#ESTABLECER FECHA Y LUGAR
lugar = "incubadora prospeccion"
fecha = str(20230630)
fecha_anio = fecha[0:4]
fecha_mes = fecha[4:6]
fecha_dia =fecha[6:]

# Genero un nombre base para el archivo
nombre_base = fecha + "_" + lugar

# Verificar si existe un archivo con el nombre base
contador = 0
while nombre_base + str(contador) in uos.listdir():
    contador += 1

# Generar un nuevo nombre de archivo con el número de contador
nombredearchivo = nombre_base + str(contador) + ".csv"

# Generar un archivo y abrirlo en modo escritura
doc = open(nombredearchivo, "w")

#Grabar una primer linea con la fecha establecida
#doc.write(fecha_anio + " ")
#doc.write(fecha_mes + " ")
#doc.write(fecha_dia + " ")
#doc.write(lugar + "\n")

# Creo una variable para el led de la pi pico y una función para que parpadee
led = Pin(25, Pin.OUT)

def parpadeo():
    while True:
        led.on()
        utime.sleep(1)
        led.off()
        utime.sleep(1)

# Iniciar el hilo para el parpadeo del LED
_thread.start_new_thread(parpadeo, ())


while True:
    # Recojo los datos en variables
    temp = bme.values[0]
    pres = bme.values[1]
    hum = bme.values[2]
    hora_local = utime.localtime()
    hora = str(hora_local[3])
    minuto = str(hora_local[4])
    segundo = str(hora_local[5])
    
    # Escribo los datos que recogí en el archivo que abrí
    doc.write(hora + " ")
    doc.write(minuto + " ")
    doc.write(segundo + " ")
    doc.write(str(temp) + " ")
    doc.write(str(pres) + " ")
    doc.write(str(hum) + "\n")

    
    doc.flush()
    
    # Espero 20 segundos para repetir el ciclo
    utime.sleep(1200)
