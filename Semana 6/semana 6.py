# Definición de la clase base Empleado
class Empleado:
    def __init__(self, nombre, salario):
        self.__nombre = nombre  # Encapsulación del atributo nombre
        self.__salario = salario  # Encapsulación del atributo salario

    def obtener_nombre(self):
        return self.__nombre

    def obtener_salario(self):
        return self.__salario

    def descripcion(self):
        return f"Soy un empleado llamado {self.__nombre} y mi salario es ${self.__salario:.2f}"


# Definición de la clase derivada Gerente
class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.__departamento = departamento

    def obtener_departamento(self):
        return self.__departamento

    def descripcion(self):  # Polimorfismo: método sobrescrito
        return f"Soy un gerente llamado {self.obtener_nombre()}, trabajo en el departamento {self.__departamento} y mi salario es ${self.obtener_salario():.2f}"


# Creación de objetos y prueba del programa
if __name__ == "__main__":
    # Crear un objeto Empleado
    empleado1 = Empleado("Omar", 1800)
    print(empleado1.descripcion())

    # Crear un objeto Gerente
    gerente1 = Gerente("Lucia", 2500, "Ventas")
    print(gerente1.descripcion())