class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Usamos una tupla para título y autor, que son atributos inmutables
        self.informacion = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"'{self.informacion[0]}' por {self.informacion[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, isbn):
        for libro in self.libros_prestados:
            if libro.isbn == isbn:
                self.libros_prestados.remove(libro)
                return libro
        return None

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"


class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario con ISBN como clave y objeto Libro como valor
        self.usuarios_registrados = set()  # Conjunto para IDs únicos de usuarios
        self.usuarios = {}  # Diccionario para almacenar objetos Usuario por ID

    # Funcionalidades de gestión de libros
    def agregar_libro(self, libro):
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro añadido: {libro}")
        else:
            print(f"El libro con ISBN {libro.isbn} ya existe.")

    def eliminar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            libro_eliminado = self.libros_disponibles.pop(isbn)
            print(f"Libro eliminado: {libro_eliminado}")
        else:
            print(f"No se encontró un libro con ISBN {isbn}.")

    # Funcionalidades de gestión de usuarios
    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios_registrados:
            self.usuarios_registrados.add(usuario.id_usuario)
            self.usuarios[usuario.id_usuario] = usuario
            print(f"Usuario registrado: {usuario}")
        else:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")

    def dar_de_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            self.usuarios_registrados.remove(id_usuario)
            usuario_baja = self.usuarios.pop(id_usuario)
            print(f"Usuario dado de baja: {usuario_baja}")
        else:
            print(f"No se encontró un usuario con ID {id_usuario}.")

    # Funcionalidades de préstamo de libros
    def prestar_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios_registrados:
            print(f"Usuario con ID {id_usuario} no registrado.")
            return
        if isbn not in self.libros_disponibles:
            print(f"Libro con ISBN {isbn} no disponible.")
            return

        libro = self.libros_disponibles.pop(isbn)
        self.usuarios[id_usuario].prestar_libro(libro)
        print(f"Libro '{libro.informacion[0]}' prestado a {self.usuarios[id_usuario].nombre}.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios_registrados:
            print(f"Usuario con ID {id_usuario} no registrado.")
            return

        libro = self.usuarios[id_usuario].devolver_libro(isbn)
        if libro:
            self.libros_disponibles[isbn] = libro
            print(f"Libro devuelto: {libro}")
        else:
            print(f"El usuario con ID {id_usuario} no tiene un libro con ISBN {isbn} prestado.")

    # Funcionalidades de búsqueda
    def buscar_libro(self, criterio, valor):
        resultados = []
        for libro in self.libros_disponibles.values():
            if criterio == "titulo" and libro.informacion[0].lower() == valor.lower():
                resultados.append(libro)
            elif criterio == "autor" and libro.informacion[1].lower() == valor.lower():
                resultados.append(libro)
            elif criterio == "categoria" and libro.categoria.lower() == valor.lower():
                resultados.append(libro)

        if resultados:
            print("Libros encontrados:")
            for libro in resultados:
                print(f" - {libro}")
        else:
            print(f"No se encontraron libros con {criterio}: '{valor}'.")

    # Funcionalidad para listar libros prestados por un usuario
    def listar_libros_prestados(self, id_usuario):
        if id_usuario not in self.usuarios_registrados:
            print(f"Usuario con ID {id_usuario} no registrado.")
            return

        usuario = self.usuarios[id_usuario]
        if usuario.libros_prestados:
            print(f"Libros prestados por {usuario.nombre}:")
            for libro in usuario.libros_prestados:
                print(f" - {libro}")
        else:
            print(f"El usuario {usuario.nombre} no tiene libros prestados.")


# Ejemplo de uso
biblioteca = Biblioteca()

# Crear libros
libro1 = Libro("El Quijote", "Miguel de Cervantes", "Novela", "12345")
libro2 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", "67890")

# Agregar libros a la biblioteca
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Registrar usuarios
usuario1 = Usuario("Omar Morales", 1)
biblioteca.registrar_usuario(usuario1)

# Prestar libro
biblioteca.prestar_libro(1, "12345")

# Listar libros prestados
biblioteca.listar_libros_prestados(1)

# Devolver libro
biblioteca.devolver_libro(1, "12345")

# Buscar libros
biblioteca.buscar_libro("titulo", "El Quijote")
biblioteca.buscar_libro("autor", "Gabriel García Márquez")
biblioteca.buscar_libro("categoria", "Novela")