
# Punto A: Normalización de Lecturas

registro_raw = {
    "sensor_id": " SENSOR-001 ",
    "temperatura": "24.5C",
    "ubicacion": " Planta Norte "
    }

  

def limpiar_registro_sensor(registro_raw):

    registro_limpio = {}

    registro_limpio["sensor_id"] = registro_raw["sensor_id"].strip()
    registro_limpio["temperatura"] = float(registro_raw["temperatura"].replace("C",""))
    registro_limpio["ubicacion"] = registro_raw["ubicacion"].strip()
    if registro_raw["ubicacion"] == None:
        registro_limpio["ubicacion"] = "centro"
    else:
       registro_limpio["ubicacion"] = registro_raw["ubicacion"]
    
    return registro_limpio


print(limpiar_registro_sensor(registro_raw))




#Punto B: Monitoreo y Mapeo Estadístico

# registro de sensonres de ejemplo
registro_raw = [
    {
    "sensor_id": " SENSOR-001 ",
    "temperatura": "24.5C",
    "ubicacion": " Planta Norte "
    },

    {
    "sensor_id": " SENSOR-002 ",
    "temperatura": "31.0C",
    "ubicacion": " Planta Norte "
    },

    {
    "sensor_id": " SENSOR-003 ",
    "temperatura": "22.3C",
    "ubicacion": " Planta Norte "
    },

    {
    "sensor_id": " SENSOR-004 ",
    "temperatura": "32.4C",
    "ubicacion": " Planta Norte "
    }
    ]

#funcion iterable para limpiar todos los registros de sensores en la lista

def generar_lista_limpia(lista_raw):
    sensores_limpios = []

    for sensor in lista_raw:
        sensores_limpios.append(limpiar_registro_sensor(sensor))

    return sensores_limpios

lista_sensores_limpios = generar_lista_limpia(registro_raw)

print(lista_sensores_limpios)
    


#funcion para generar un resumen de los sensores que superan un umbral de temperatura y el promedio de temperatura

def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura):
    
    lista_sensores_alerta = []
   
    promedio_temperatura = 0

    for sensor in lista_sensores_limpios:
        
        promedio_temperatura += sensor["temperatura"]/len(lista_sensores_limpios)

        if sensor["temperatura"] >= umbral_temperatura:
            lista_sensores_alerta.append(sensor["sensor_id"])
    return (lista_sensores_alerta, promedio_temperatura)  

print(generar_resumen_sensores(lista_sensores_limpios, 29))
