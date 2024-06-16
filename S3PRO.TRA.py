# Función para ingresar temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal de las temperaturas
def calcular_promedio_semanal(temperaturas):
    if len(temperaturas) == 0:
        return 0
    return sum(temperaturas) / len(temperaturas)

def main():
    # Entrada de datos
    temperaturas = ingresar_temperaturas()

    # Cálculo del promedio semanal
    promedio = calcular_promedio_semanal(temperaturas)

    # Presentación del resultado
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f}")

# Ejecución del programa
if __name__ == "__main__":
    main()