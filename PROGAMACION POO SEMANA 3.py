class ClimaDiario:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperatura(self, temp):
        self.temperaturas.append(temp)

    def calcular_promedio_semanal(self):
        if len(self.temperaturas) == 0:
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)


def main():
    clima = ClimaDiario()

    # Entrada de datos
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        clima.ingresar_temperatura(temp)

    # Cálculo del promedio semanal
    promedio = clima.calcular_promedio_semanal()

    # Presentación del resultado
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f}")


# Ejecución del programa
if __name__ == "__main__":
    main()