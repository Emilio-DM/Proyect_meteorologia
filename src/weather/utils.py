def celsius_to_fahrenheit(temp_c: float) -> float:
    """Convert a temperature from Celsius to Fahrenheit.

    Args:
        temp_c: The temperature in degrees Celsius.

    Returns:
        The temperature in degrees Fahrenheit.
    """
    return (temp_c * 9 / 5) + 32




def comprobar_altitud(altitud_or:float , altitud_ac:float):
    """Una funcion que comprueba si la altitud se ha desplazado o no. Las estaciones que tenemos son estaticas por lo que no tiene sentido recibir cambios en esta variable

    Args:
        Las dos altitudes, la original y la que se le ha aportado ese dia

    Returns:
        altitud_ac si tira bien y si no la altitud_ac
    """

    if altitud_or == altitud_or:
        return 1
    else: return 0

def comprobar_indicativo(indicativo_or:float , indicativo_ac:float):
    """Una funcion que comprueba que seguimos probando con el mismo indicativo, que no estamos cambiando de serie 

    Args:
        Las dos altitudes, la original y la que se le ha aportado ese dia

    Returns:
        altitud_ac si tira bien y si no la altitud_ac
    """

    if indicativo_or == indicativo_ac:
        return 1
    else: return 0


def comprobar_temperatura(tmp:float):
    """Hace una comprobacion para ver si tenemos datos veridicos

    Args:
        El dato de la temperatura

    Returns:
        BNos devuelve 1 si es un dato veridico
    """

    if tmp < -20 or tmp > 80:
        return 0
    return 1

def comprobar_precipitacion(pre:float):
    """Hace una comprobacion para ver si tenemos datos veridicos

    Args:
        El dato de la temperatura

    Returns:
        BNos devuelve 1 si es un dato veridico
    """

    if pre < 0 or pre > 2000:
        return 0
    return 1



class Ola_de_Calor:

    """Una clase para guardar la informacion relevante de si hay una ola de calor respecto a los terminos de la AEMET.
    
    Se toma en consideracion que se tiene que superar el percentil del 95% de su serie de temperaturas
    máximas diarias de los meses de julio y agosto del periodo 1971-2000. En este caso es 33 """


    def __init__(self):
        self.count = 0
        self._max = 0.0
        self._umbral = 33
        self._dia_inicio="2025-01-01"
        self._dia_final="2025-01-01"
        self._true=0
        self._contador=0

    def update(self, value: float) -> None:
        """
        Hace una comprobacion para ver si tenemos datos de una ola de calor o si ha terminado
        
        Args:
        El dato de la temperatura

        Returns:
        Primero hace la comprobacion de si la temperatura a aumentado la temperatura umbral. Despues si no la supera comprueba si se ha sufrido
        una ola de calor para guardar los valores en un diccionario. Esto se hace viendo si el contador ha superado o igualado los 3 dias.

        Si la temperatura a aumentado el umbral se actualizan valores. Si contador esta en 0 se ajusta la el dia inicial si no lo esta se actualiza el dia final
        se calcula el dia maximo. Se aumenta en 1 el contador
        """


        if float(value["tmax"].replace(',', '.')) > self._umbral:
            if self._contador==0:

                self._dia_inicio=value["fecha"]
                self._contador += 1
                self._max=float(value["tmax"].replace(',', '.'))

            else:
                self._dia_final=value["fecha"]
                self._contador += 1

                if float(value["tmax"].replace(',', '.')) > self._max:
                    self._max=float(value["tmax"].replace(',', '.'))
        
        else:
            if self._contador > 2:
                self._true=1
            else: 
                self._contador=0
                self._max=0
        
    def guardar_ola(self) -> None:
        """
        Si hemos detectado una ola de calor nos devuelve los datos de la ola de calor
        
        Args:
        El propio self

        Returns:
        Si self._true == 1 Se nos ha indicado que ha habido una ola de calor y guardaremos los valores en un diccionario 
        """


        if self._true==1:

            self._true=0
            duracion=self._contador
            self._contador=0      

            return {
                    "Duracion":duracion,
                    "Dia_inic":self._dia_inicio,
                    "Dia_final":self._dia_final,
                    "Maximo":self._max,
                    "anomalia":self._max-self._umbral
                }
        
        else:
            if self._contador > 2:
                self._true=1
            self._contador=0



        

class WelfordStats:
    """
    Una clase para obtener la media sin tener que hacer el calculo con toda la base de datos. Esta bien porque la base de datos la separamos cada 6 meses
    pero vamos que para mi pues sunica sunica

    
    Examples:
        >>> ws = WelfordStats()
        >>> ws.update(10.0)
        >>> ws.update(20.0)
        >>> ws.mean()
        15.0
        >>> ws.variance(sample=True)
        50.0
    """
    def __init__(self):
        self.count = 0
        self._mean = 0.0
        self._m2 = 0.0

    def update(self, value: float) -> None:
        """
        Calcular la media
        
        Args:
            value (float): The new numerical value from the stream.
        """
        #primero actualizamos self.count
        self.count =self.count +  1


        delta= value -self._mean

        #Actualizamos la media
        self._mean = self._mean  +    delta / self.count

        #sacamos el valor de delta2
        delta2 = value - self._mean

        #Sacamos el valor del M2 nuevo

        self._m2 = self._m2 +  delta * delta2


    def mean(self) -> float:
        """
        Nos devuelva la media
        
        Returns:
            float: Pues nos devuelve la media. Si no hay valores nos devuelve un 0
        """

        return float(self._mean)

    def variance(self, sample: bool = True) -> float:
        """
        Devuelve la varianza
        
        Args:
            sample (bool): Si es cierto que nos devuelva la cuasivarianza y si no la varianza
                           
        Returns:
            float: Primero hace dos comprobaciones de si hay 0 elementos y si no nos devuelve toda la base de datos en general
        """
        if self.count == 0:
            return 0.0
        
        if self.count==1:
            return 0.0

        if sample == True:
            return self._m2 / (self.count - 1)
        else: return self._m2 / (self.count)


    def std(self, sample: bool = True) -> float:
        """
        Nos devuelve la desviacion tipica

        Args:
            sample (bool): Si es cierto que use la cusivarianza y si es falso la varianza

        Returns:
            float: Nos devuelve la desviacion tipica
        """

        if sample == True:
            return (self._m2/(self.count - 1))**(1/2)
        else: return (self._m2 / self.count)**(1/2)

