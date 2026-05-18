# Ejercicio 1 - Leer líneas de un archivo


def read_lines(filename):
    """
    Lee un archivo de texto y retorna una lista con sus líneas.

    Reglas:
    - Cada línea debe venir sin el salto de línea final y sin espacios
      al principio o al final (strip).
    - Las líneas vacías (o con solo espacios) se ignoran.
    - Si el archivo no existe, se debe propagar FileNotFoundError.
    - Si el archivo está vacío, retornar [].

    Args:
        filename: str - nombre (o ruta) del archivo a leer.

    Returns:
        list[str] - lista de líneas no vacías, en el orden del archivo.

    Raises:
        FileNotFoundError: si el archivo no existe.

    Ejemplo:
        # archivo contiene: "manzana\n  banana\npera\n"
        read_lines("datos.txt") -> ["manzana", "banana", "pera"]
    """
    try:
        with open(filename, 'r') as archivo:
            contenido=archivo.read()
    except FileNotFoundError:
        raise FileNotFoundError

    lista = contenido.split('\n')
    resultado = []

    for i in range(len(lista)):
        elemento = lista[i].strip()
        if elemento != "":
            resultado.append(elemento)

    return resultado
