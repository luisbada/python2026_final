import pytest


# FUNCIÓN DE NEGOCIO (Algoritmo de Emisiones)

def calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4):
    if consumo_kwh < 0:
        raise ValueError("El consumo en kWh no puede ser negativo.")
    return consumo_kwh * factor_emision


# PUNTO A: Auditoría


def test_calculo_nominal_por_defecto():
    assert calcular_emisiones_carbono(100.0) == 40.0


def test_calculo_con_factor_personalizado():
    assert calcular_emisiones_carbono(250.0, factor_emision=0.5) == 125.0


def test_consumo_negativo_lanza_excepcion():
    with pytest.raises(ValueError):
        calcular_emisiones_carbono(-15.0)





# PUNTO B

def obtener_metricas_consumo(registros):
    if not registros:
        return {"total_global_emisiones": 0.0, "planta_mayor_consumo": "Ninguna"}

    total_global_emisiones = 0.0
    max_consumo = -1.0
    planta_mayor_consumo = ""

    for reg in registros:
        planta = reg["planta"]
        consumo = reg["consumo_kwh"]


        total_global_emisiones += calcular_emisiones_carbono(consumo)

        if consumo > max_consumo:
            max_consumo = consumo
            planta_mayor_consumo = planta

    return {
        "total_global_emisiones": total_global_emisiones,
        "planta_mayor_consumo": planta_mayor_consumo
    }


def vista_panel_sustentabilidad(request):
    from django.shortcuts import render

    registros_industriales = [
        {"planta": "Planta Industrial Norte", "consumo_kwh": 1500.0},
        {"planta": "Planta Procesadora Sur", "consumo_kwh": 850.5},
        {"planta": "Sede Logística Central", "consumo_kwh": 2200.0}
    ]

    metricas = obtener_metricas_consumo(registros_industriales)

    contexto = {
        "total_emisiones": metricas["total_global_emisiones"],
        "planta_critica": metricas["planta_mayor_consumo"],
        "lista_registros": registros_industriales
    }

    return render(request, 'sustentabilidad/panel.html', contexto)