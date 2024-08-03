# Sistema para información básica de trabajadores
# Permite al usuario ingresar y mostrar datos como nombre, edad, salario y estado laboral.

# Definición de una función para ingresar datos del trabajador
def ingresar_trabajador():
    """
    Función para ingresar datos de un trabajador.

    Returns:
        dict: Un diccionario con los datos ingresados del trabajador.
    """
    print("Ingrese los datos del trabajador:")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    salario = float(input("Salario (en USD): "))
    activo = input("¿Está activo? (Sí/No): ").lower() == 'sí'

    trabajador = {
        'nombre': nombre,
        'edad': edad,
        'salario': salario,
        'activo': activo
    }

    return trabajador

# Función para mostrar los datos del trabajador
def mostrar_trabajador(trabajador):
    """
    Función para mostrar los datos de un trabajador.

    Args:
        empleado (dict): Diccionario con los datos del trabajador a mostrar.
    """
    print("\nDatos del trabajador:")
    print(f"Nombre: {trabajador['nombre']}")
    print(f"Edad: {trabajador['edad']} años")
    print(f"Salario: ${trabajador['salario']:.2f}")
    estado = "Activo" if trabajador['activo'] else "Inactivo"
    print(f"Estado: {estado}")

# Main code
if __name__ == "__main__":
    # Ingresar datos del trabajador
    empleado1 = ingresar_trabajador()

    # Mostrar los datos del trabajador ingresado
    mostrar_trabajador(trabajador1)