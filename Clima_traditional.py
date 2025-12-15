# ==========================================
# Nombre del Archivo: clima_tradicional.py
# ==========================================

def ingresar_temperaturas_diarias():
    """
    Función encargada de solicitar al usuario las temperaturas
    de los 7 días de la semana.
    Retorna: Una lista con números flotantes.
    """
    temperaturas = []
    print("--- Ingreso de Temperaturas Semanales (Tradicional) ---")

    for i in range(7):
        while True:
            try:
                # Solicitamos la temperatura del día i+1
                temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
                temperaturas.append(temp)
                break  # Rompe el ciclo while si el dato es correcto
            except ValueError:
                print("Error: Por favor, ingrese un número válido.")

    return temperaturas


def calcular_promedio_semanal(lista_temperaturas):
    """
    Recibe una lista de temperaturas y calcula el promedio.
    Retorna: El promedio en formato float.
    """
    if not lista_temperaturas:  # Validación por si la lista está vacía
        return 0.0

    suma_total = sum(lista_temperaturas)
    promedio = suma_total / len(lista_temperaturas)
    return promedio


def main():
    """
    Función principal que orquesta la lógica del programa.
    """
    # 1. Entrada de datos
    datos_clima = ingresar_temperaturas_diarias()

    # 2. Cálculo
    promedio = calcular_promedio_semanal(datos_clima)

    # 3. Salida de información
    print(f"\nResultados:")
    print(f"Temperaturas ingresadas: {datos_clima}")
    print(f"El promedio semanal de temperatura es: {promedio:.2f}°C")


# Bloque para ejecutar el script
if __name__ == "__main__":
    main()