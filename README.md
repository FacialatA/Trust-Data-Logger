![Logo](https://github.com/FacialatA/Trust-Data-Logger/assets/92767544/3131dc2d-5edb-4105-937b-13e8f3cfa82d)

# PROYECTO TRUST: Data logger
## Requisitos

* Raspberry Pi Pico
* Sensor BME280 fabricado por Pimoroni

## Conexión de pines

Conecta los pines de la Raspberry Pi Pico a los pines correspondientes del sensor BME280 de la siguiente manera:

    Pin SDA del sensor -> Pin GP14 de la Raspberry Pi Pico
    Pin SCL del sensor -> Pin GP15 de la Raspberry Pi Pico

![imagen](https://github.com/FacialatA/PicoDataLogger/assets/92767544/e2a02bd6-3e35-4fe6-bc84-bf2f59aeae7a)


Asegúrate de que la Raspberry Pi Pico esté conectada correctamente y los pines estén configurados según tus necesidades.


## Funcionamiento

El proyecto utiliza Raspberry Pi Pico y el sensor BME280 fabricado por Pimoroni para recopilar y almacenar información de temperatura, humedad y presión en la memoria interna de la Raspberry Pi Pico. Los datos se recogen cada 20 minutos y se guardan en archivos sin extension.

El código proporcionado configura la comunicación I2C con el sensor BME280 y realiza las siguientes tareas:

*    Genera un nombre de archivo único para almacenar los datos recopilados.
*    Abre un archivo en modo escritura para almacenar los datos.
*    Configura un LED en el pin 25 de la Raspberry Pi Pico y crea una función para que el LED parpadee.
*    Inicia un hilo para el parpadeo del LED.
*    En un bucle infinito, recopila los datos de temperatura, presión y humedad del sensor BME280.
*    Obtiene la hora local y los valores de los sensores.
*    Escribe los datos recopilados en el archivo abierto.
*    Espera 20 segundos y repite el ciclo.

Los datos recopilados se guardan en archivos en la memoria interna de la Raspberry Pi Pico. C

Recuerda ajustar la configuración de pines según tus conexiones específicas, y cambiar los strings correspondientes a la fecha y lugar (ubicacion del logger) en el codigo!

¡Disfruta de tu proyecto de Raspberry Pi Pico y Sensor BME280! Si tienes alguna pregunta, no dudes en consultar la documentación adicional o buscar ayuda en la comunidad de Raspberry Pi.

## Preparacion
1- Conecta tu Pico a la PC en modo Boot e instala el firmware de MicroPython.
2- Vuelve a conectar tu dispositivo y carga en el el archivo main.py en el directorio raiz. Para esto puedes ayudarte del IDE Thonny.
3- Con la ayuda de Thonny, instala las librerias para el correcto funcionamiento del sensor. Para ello, ve a Herramientas > Gestionar Paquetes... e instala el paquete "micropython-bme280".
4- Opcional: en el archivo main.py cambia los valores de los strings "fecha" y "lugar".
5- Listo! El dispositivo ya esta preparado para usar. La proxima vez que lo enchufes (a una PC o a corriente) comenzara a registrar en un nuevo archivo, y el LED del microcontrolador parpadeara cada un segundo como testigo de ello.

## Disclaimer

La RPi Pico si no esta conectada a una PC tomara "epoch" como la hora local, por lo que los datos estaran emparejados a fechas no correspondientes.
Se recomienda descartar siempre el/los primer/os valor/es registrados para disminuir el error.

![Poster 2](https://github.com/user-attachments/assets/f0042399-ea29-411a-a43b-8fa7bdf2030e)

