#Aqui se configura el dispositivo
#Ingresar año, mes y dia en formato string (entre parentesis)
#siguiendo el formato DD/MM/AAAA

titulo_del_archivo = "database"
año = "2024"
mes = "00"
dia = "00"
fecha = str(año + mes + dia)

#La variable demora es numerica integer, almacena (en segundos)
#cuanto tiempo pasa entre cada registro de datos
#por defecto es 1200, una medicion cada 1200 segundos
#o lo mismo es, una medicion cada 20 minutos
demora = 1200

