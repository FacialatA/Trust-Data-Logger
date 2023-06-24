# Proyecto de Raspberry Pi Pico y Sensor BME280
## Requisitos

    Raspberry Pi Pico
    Sensor BME280 fabricado por Pimoroni
    Conexión a Internet (opcional)

## Conexión de pines

Conecta los pines de la Raspberry Pi Pico a los pines correspondientes del sensor BME280 de la siguiente manera:

    Pin SDA del sensor -> Pin GP14 de la Raspberry Pi Pico
    Pin SCL del sensor -> Pin GP15 de la Raspberry Pi Pico

![imagen](https://github.com/FacialatA/PicoDataLogger/assets/92767544/e2a02bd6-3e35-4fe6-bc84-bf2f59aeae7a)


Asegúrate de que la Raspberry Pi Pico esté conectada correctamente y los pines estén configurados según tus necesidades.


## Funcionamiento

El proyecto utiliza Raspberry Pi Pico y el sensor BME280 fabricado por Pimoroni para recopilar y almacenar información de temperatura, humedad y presión en la memoria interna de la Raspberry Pi Pico. Los datos se recogen cada 20 segundos y se guardan en archivos.

El código proporcionado configura la comunicación I2C con el sensor BME280 y realiza las siguientes tareas:

*    Genera un nombre de archivo único para almacenar los datos recopilados.
*    Abre un archivo en modo escritura para almacenar los datos.
*    Configura un LED en el pin 25 de la Raspberry Pi Pico y crea una función para que el LED parpadee.
*    Inicia un hilo para el parpadeo del LED.
*    En un bucle infinito, recopila los datos de temperatura, presión y humedad del sensor BME280.
*    Obtiene la hora local y los valores de los sensores.
*    Escribe los datos recopilados en el archivo abierto.
*    Espera 20 segundos y repite el ciclo.

Los datos recopilados se guardan en archivos en la memoria interna de la Raspberry Pi Pico. Cada archivo tiene un nombre único basado en la fecha y hora de creación. Los archivos se crean en el formato "bme_data_YYYYMMDDHHMMSS.txt" donde "YYYY" representa el año, "MM" el mes, "DD" el día, "HH" la hora, "MM" el minuto y "SS" el segundo en que se creó el archivo.

Recuerda ajustar la configuración de pines según tus conexiones específicas.

¡Disfruta de tu proyecto de Raspberry Pi Pico y Sensor BME280! Si tienes alguna pregunta, no dudes en consultar la documentación adicional o buscar ayuda en la comunidad de Raspberry Pi.
