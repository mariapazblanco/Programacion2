import sqlite3
from datetime import datetime

class Libreria:
    def __init__(self):
        self.conexion = Conexiones()
        self.conexion.abrirConexion()
        self.conexion.miCursor.execute("DROP TABLE IF EXISTS LIBROS")
        self.conexion.miCursor.execute("DROP TABLE IF EXISTS VENTAS")
        self.conexion.miCursor.execute("DROP TABLE IF EXISTS HISTORICO_LIBROS")
        self.conexion.miCursor.execute(
            "CREATE TABLE LIBROS (id_libro INTEGER PRIMARY KEY AUTOINCREMENT, isbn TEXT UNIQUE, titulo TEXT, autor TEXT, genero TEXT, precio REAL, fecha_ultimo_precio TEXT, cantidad_disponible INTEGER NOT NULL)"
        )
        self.conexion.miCursor.execute(
            "CREATE TABLE VENTAS (id_libro INTEGER, cantidad INTEGER, fecha TEXT)"
        )
        self.conexion.miCursor.execute(
            "CREATE TABLE HISTORICO_LIBROS (id_libro INTEGER, isbn TEXT, titulo TEXT, autor TEXT, genero TEXT, precio REAL, fecha_ultimo_precio TEXT, cantidad_disponible INTEGER NOT NULL)"
        )
        self.conexion.miConexion.commit()

    def agregar_libro(self, isbn, titulo, autor, genero, precio, cantidad_disponible):
        try:
            fecha_actual = datetime.now().strftime("%Y-%m-%d")
            self.conexion.miCursor.execute(
                "INSERT INTO LIBROS (isbn, titulo, autor, genero, precio, fecha_ultimo_precio, cantidad_disponible) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (isbn, titulo, autor, genero, precio, fecha_actual, cantidad_disponible)
            )
            self.conexion.miConexion.commit()
            print("Libro agregado exitosamente")
        except sqlite3.IntegrityError:
            print("ISBN ya existente. No se pudo agregar el libro.")
        except:
            print("Error al agregar un libro")

    def modificar_precio(self, id_libro, nuevo_precio):
        try:
            self.conexion.miCursor.execute(
                "UPDATE LIBROS SET precio = ? WHERE id_libro = ?",
                (nuevo_precio, id_libro)
            )
            self.conexion.miConexion.commit()
            print("Precio del libro modificado correctamente")
        except:
            print("Error al modificar el precio del libro")

    def borrar_libro(self, id_libro):
        try:
            self.conexion.miCursor.execute(
                "DELETE FROM LIBROS WHERE id_libro = ?",
                (id_libro,)
            )
            self.conexion.miConexion.commit()
            print("Libro eliminado correctamente")
        except:
            print("Error al eliminar el libro")

    def cargar_disponibilidad(self, id_libro, cantidad):
        try:
            self.conexion.miCursor.execute(
                "UPDATE LIBROS SET cantidad_disponible = cantidad_disponible + ? WHERE id_libro = ?",
                (cantidad, id_libro)
            )
            self.conexion.miConexion.commit()
            print("Disponibilidad actualizada correctamente")
        except:
            print("Error al cargar la disponibilidad")

    def listar_libros(self):
        try:
            self.conexion.miCursor.execute(
                "SELECT id_libro, autor, titulo FROM LIBROS ORDER BY id_libro, autor, titulo"
            )
            libros = self.conexion.miCursor.fetchall()
            print("Listado de Libros:")
            for libro in libros:
                print(f"ID: {libro[0]}, Autor: {libro[1]}, Título: {libro[2]}")
        except:
            print("Error al listar los libros")

    def ventas(self, id_libro, cantidad):
        try:
            self.conexion.miCursor.execute(
                "INSERT INTO VENTAS (id_libro, cantidad, fecha) VALUES (?, ?, ?)",
                (id_libro, cantidad, datetime.now().strftime("%Y-%m-%d"))
            )
            self.conexion.miCursor.execute(
                "UPDATE LIBROS SET cantidad_disponible = cantidad_disponible - ? WHERE id_libro = ?",
                (cantidad, id_libro)
            )
            self.conexion.miConexion.commit()
            print("Venta registrada correctamente")
        except:
            print("Error al realizar la venta")

    def actualizar_precios(self, porcentaje):
        try:
            self.conexion.miCursor.execute(
                "INSERT INTO HISTORICO_LIBROS SELECT * FROM LIBROS"
            )
            self.conexion.miCursor.execute(
                "UPDATE LIBROS SET precio = precio * (1 + ? / 100), fecha_ultimo_precio = ?",
                (porcentaje, datetime.now().strftime("%Y-%m-%d"))
            )
            self.conexion.miConexion.commit()
            print("Precios actualizados correctamente")
        except:
            print("Error al actualizar los precios")

    def mostrar_registros_anteriores(self, fecha):
        try:
            self.conexion.miCursor.execute(
                "SELECT * FROM LIBROS WHERE fecha_ultimo_precio < ?",
                (fecha,)
            )
            registros = self.conexion.miCursor.fetchall()
            print("Registros anteriores a la fecha especificada:")
            for registro in registros:
                print(registro)
        except:
            print("Error al mostrar los registros anteriores")

    def cerrar_libreria(self):
        self.conexion.cerrarConexion()


class Conexiones:
    def abrirConexion(self):
        self.miConexion = sqlite3.connect("Libreria.db")
        self.miCursor = self.miConexion.cursor()

    def cerrarConexion(self):
        self.miConexion.close()


libreria = Libreria()

while True:
    print("Menu de opciones Libreria")
    print("1- Cargar libro")
    print("2- Modificar precio de un libro")
    print("3- Borrar un libro")
    print("4- Cargar disponibilidad")
    print("5- Listado de libros")
    print("6- Ventas")
    print("7- Actualizar precios")
    print("8- Mostrar registros anteriores")
    print("0- Salir del menú")

    opcion = int(input("Por favor ingrese un número: "))

    if opcion == 1:
        isbn = input("Por favor ingrese el ISBN del libro: ")
        titulo = input("Por favor ingrese el título del libro: ")
        autor = input("Por favor ingrese el autor del libro: ")
        genero = input("Por favor ingrese el género del libro: ")
        precio = float(input("Por favor ingrese el precio del libro: "))
        cantidad_disponible = int(input("Por favor ingrese la cantidad disponible del libro: "))
        libreria.agregar_libro(isbn, titulo, autor, genero, precio, cantidad_disponible)
    elif opcion == 2:
        id_libro = int(input("Por favor ingrese el ID del libro a modificar: "))
        nuevo_precio = float(input("Por favor ingrese el nuevo precio del libro: "))
        libreria.modificar_precio(id_libro, nuevo_precio)
    elif opcion == 3:
        id_libro = int(input("Por favor ingrese el ID del libro a borrar: "))
        libreria.borrar_libro(id_libro)
    elif opcion == 4:
        id_libro = int(input("Por favor ingrese el ID del libro para cargar disponibilidad: "))
        cantidad = int(input("Por favor ingrese la cantidad para cargar disponibilidad: "))
        libreria.cargar_disponibilidad(id_libro, cantidad)
    elif opcion == 5:
        libreria.listar_libros()
    elif opcion == 6:
        id_libro = int(input("Por favor ingrese el ID del libro vendido: "))
        cantidad = int(input("Por favor ingrese la cantidad vendida: "))
        libreria.ventas(id_libro, cantidad)
    elif opcion == 7:
        porcentaje = float(input("Por favor ingrese el porcentaje de aumento de precios: "))
        libreria.actualizar_precios(porcentaje)
    elif opcion == 8:
        fecha = input("Por favor ingrese la fecha en formato YYYY-MM-DD: ")
        libreria.mostrar_registros_anteriores(fecha)
    elif opcion == 0:
        libreria.cerrar_libreria()
        break
    else:
        print("Opción inválida. Por favor ingrese un número válido.")
