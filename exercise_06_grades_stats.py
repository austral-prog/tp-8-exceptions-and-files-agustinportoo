# Ejercicio 6 - Estadísticas de notas por estudiante


def grades_stats(filename):
    """
    Lee un archivo donde cada línea tiene el formato:

        estudiante:nota1,nota2,nota3,...

    y retorna un diccionario donde la clave es el nombre del estudiante y
    el valor es una TUPLA (promedio, maximo, minimo) con los tres valores
    como float.

    Reglas:
    - El promedio se calcula con todas las notas de la línea.
    - Las líneas vacías se ignoran.
    - Se garantiza que todas las notas son números válidos.
    - Si el archivo no existe, propagar FileNotFoundError.

    Args:
        filename: str - nombre del archivo a leer.

    Returns:
        dict[str, tuple[float, float, float]] - estadísticas por estudiante.

    Raises:
        FileNotFoundError: si el archivo no existe.

    Ejemplo:
        # archivo contiene: "Ana:8,9,7\nBeto:5,5,10\nCami:10\n"
        grades_stats("notas.txt") -> {
            "Ana": (8.0, 9.0, 7.0),
            "Beto": (6.666666666666667, 10.0, 5.0),
            "Cami": (10.0, 10.0, 10.0),
        }
    """
    try:
        with open(filename, 'r') as archivo:
            contenido=archivo.read()
    except FileNotFoundError:
        raise FileNotFoundError
    listas=contenido.split('\n')
    diccionario = {}
    for i in range(len(listas)):
        filas = listas[i].split(':')
        if listas[i] == "":
            continue
        nombres = filas[0]
        notas=filas[1].split(',')
        maximo=0
        minimo=10
        suma=0
        for n in notas:
            numero=int(n)
            suma+=numero
            if maximo<numero:
                maximo=numero
            elif minimo>numero:
                minimo=numero
        promedio=suma/len(notas)
        diccionario[nombres]=(float(promedio),float(maximo),float(minimo))
    return diccionario
