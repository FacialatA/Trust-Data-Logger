import establecer_fecha
import uos

# Genero un nombre base para el archivo
nombre_base = establecer_fecha.fecha + "_" + establecer_fecha.lugar

# Verificar si existe un archivo con el nombre base
contador = 0
while nombre_base + str(contador) in uos.listdir():
    contador += 1

# Generar un nuevo nombre de archivo con el número de contador
nombredearchivo = nombre_base + str(contador)
