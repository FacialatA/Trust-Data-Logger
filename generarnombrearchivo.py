import config_file
import uos

# Genero un nombre base para el archivo
nombre_base = config_file.fecha + "_" + config_file.lugar

# Verificar si existe un archivo con el nombre base
contador = 0
while nombre_base + str(contador) in uos.listdir():
    contador += 1

# Generar un nuevo nombre de archivo con el número de contador
nombredearchivo = nombre_base + str(contador)
