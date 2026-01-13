"""Módulo que modela una biblioteca y la gestión de libros."""


class Biblioteca:
    """Representa una biblioteca que contiene una colección de libros."""

    def __init__(self, name):
        """
        Inicializa la biblioteca.

        :param name: Nombre de la biblioteca
        """
        self.name = name
        self.libros = []

    def addb(self, book):
        """
        Agrega un libro a la biblioteca.

        :param book: Instancia de la clase Book
        """
        self.libros.append(book)

    def show(self):
        """Muestra la información de todos los libros disponibles."""
        for libro in self.libros:
            print(libro.titulo, libro.autor, libro.indice)


class Book:
    """Representa un libro y su estado de disponibilidad."""

    def __init__(self, titulo, autor, indice):
        """
        Inicializa un libro.

        :param titulo: Título del libro
        :param autor: Autor del libro
        :param indice: Identificador o índice del libro
        """
        self.titulo = titulo
        self.autor = autor
        self.indice = indice
        self.exist = True

    def lend(self):
        """
        Presta el libro si está disponible.

        :return: True si el préstamo fue exitoso, False en caso contrario
        """
        if self.exist:
            self.exist = False
            return True
        return False

    def back(self):
        """Devuelve el libro a la biblioteca."""
        self.exist = True
