class FileManager:
    def __init__(self, filename):
        """
        Constructor de la clase FileManager.
        Inicializa el nombre del archivo y abre el archivo en modo lectura.

        :param filename: Nombre del archivo a abrir.
        """
        self.filename = filename
        self.file = None
        try:
            self.file = open(self.filename, 'r')
            print(f"Archivo '{self.filename}' abierto correctamente.")
        except IOError as e:
            print(f"Error al abrir el archivo '{self.filename}': {e}")

    def read_file(self):
        """
        Método para leer el contenido del archivo.

        :return: Contenido del archivo como una cadena de texto.
        """
        if self.file:
            return self.file.read()
        else:
            return "El archivo no está abierto."

    def __del__(self):
        """
        Destructor de la clase FileManager.
        Cierra el archivo si está abierto.
        """
        if self.file:
            self.file.close()
            print(f"Archivo '{self.filename}' cerrado correctamente.")
        else:
            print("No hay ningún archivo abierto para cerrar.")


# Uso de la clase FileManager
if __name__ == "__main__":
    # Crear una instancia de FileManager
    file_manager = FileManager("example.txt")

    # Leer el contenido del archivo
    content = file_manager.read_file()
    print("Contenido del archivo:")
    print(content)

    # El objeto file_manager será destruido al final del programa o cuando se llame explícitamente a del file_manager
    del file_manager6