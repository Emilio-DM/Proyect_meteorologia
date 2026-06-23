from weather.utils import celsius_to_fahrenheit
from weather.utils import comprobar_altitud
from weather.utils import comprobar_temperatura

from weather.utils import comprobar_precipitacion,comprobar_indicativo
from weather.utils import Ola_de_Calor
from weather.utils import WelfordStats
import json


with open ("data/JALANCE_VAL_1.json") as archivo:
    datos = json.load(archivo)

altitud = datos[0]["altitud"]
indicativo= datos[0]["indicativo"]

ola_calor=Ola_de_Calor()
olas_calor=[]

def test_prueba_ola_calor(path="data/JALANCE_VAL_1.json"):
    with open (path) as archivo:
        datos = json.load(archivo)

    for dia in datos:
        assert 1 == comprobar_altitud(altitud,dia["altitud"])

        assert 1 == comprobar_precipitacion(float(dia["prec"].replace(',', '.')))
        assert 1 == comprobar_temperatura(float(dia["tmed"].replace(',', '.')))
        assert 1 == comprobar_temperatura(float(dia["tmax"].replace(',', '.')))
        assert 1 == comprobar_indicativo(dia["indicativo"],indicativo)



        ola_calor.update(dia)
        if ola_calor._true != 0:
            olas_calor.append(ola_calor.guardar_ola)
        
    
    

assert "2025-01-01" == datos[0]["fecha"]





class TestCelsiusToFahrenheit:
    def test_freezing_point(self):
        assert celsius_to_fahrenheit(0) == 32.0

    def test_boiling_point(self):
        assert celsius_to_fahrenheit(100) == 212.0

    def test_negative_forty_is_equal_in_both_scales(self):
        assert celsius_to_fahrenheit(-40) == -40.0



