class ClimaSemanal:
    """
    Clase que representa la información diaria del clima de una semana.
    Utiliza POO para gestionar los datos y cálculos.
    """

    def __init__(self):
        # Atributo privado (Encapsulamiento) para almacenar las temperaturas
        # Se usa guion bajo doble (__) para indicar que es privado.
        self.__temperaturas = []

    def ingresar_datos_diarios(self, temperatura):
        """
        Método para agregar una temperatura diaria a la lista.
        Parámetro temperatura: valor flotante del clima.
        """
        self.__temperaturas.append(temperatura)

    def calcular_promedio_semanal(self):
        """
        Método que calcula el promedio de las temperaturas almacenadas.
        Retorna: Promedio (float) o 0.0 si no hay datos.
        """
        if not self.__temperaturas:
            return 0.0

        suma = sum(self.__temperaturas)
        return suma / len(self.__temperaturas)

    def obtener_datos(self):
        """
        Método getter para ver los datos (ya que el atributo es privado).
        """
        return self.__temperaturas


def main():
    # Instanciamos el objeto de la clase ClimaSemanal
    clima_semana = ClimaSemanal()

    print("--- Ingreso de Temperaturas Semanales (POO) ---")

    # Ciclo para solicitar los 7 días
    for i in range(7):
        while True:
            try:
                temp_input = float(input(f"Ingrese la temperatura del día {i + 1}: "))
                # Llamamos al método del objeto para guardar el dato
                clima_semana.ingresar_datos_diarios(temp_input)
                break
            except ValueError:
                print("Error: Ingrese un valor numérico.")

    # El objeto calcula su propio promedio
    promedio = clima_semana.calcular_promedio_semanal()

    print(f"\nResultados Objeto:")
    # Accedemos a los datos a través del método público (getter)
    print(f"Temperaturas registradas: {clima_semana.obtener_datos()}")
    print(f"El promedio semanal es: {promedio:.2f}°C")


if __name__ == "__main__":
    main()