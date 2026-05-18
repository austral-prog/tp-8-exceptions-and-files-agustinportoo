# Ejercicio 10 - Parser de archivos de log


def parse_log(filename):
    """
    Lee un archivo de log donde cada línea tiene el formato:

        NIVEL: mensaje

    y retorna un diccionario donde la clave es el nivel y el valor es una
    lista con todos los mensajes de ese nivel, en el orden en que aparecen.

    Reglas:
    - Los niveles no son fijos: cualquier string antes del primer ':'
      cuenta como nivel. El mensaje es todo lo que viene después del
      primer ':'.
    - Aplicar strip al nivel y al mensaje para eliminar espacios sobrantes.
    - Las líneas vacías (o con solo espacios) se ignoran: NO son inválidas.
    - Si alguna línea no vacía NO tiene ':', lanzar
      ValueError("invalid log line").
    - Si el archivo no existe, propagar FileNotFoundError.

    Args:
        filename: str - nombre del archivo a leer.

    Returns:
        dict[str, list[str]] - mensajes agrupados por nivel.

    Raises:
        FileNotFoundError: si el archivo no existe.
        ValueError: si alguna línea no vacía no tiene ':'.

    Ejemplo:
        # archivo contiene:
        # INFO: servidor iniciado
        # ERROR: no se puede conectar
        # INFO: reintentando
        # WARN: lento
        parse_log("server.log") -> {
            "INFO": ["servidor iniciado", "reintentando"],
            "ERROR": ["no se puede conectar"],
            "WARN": ["lento"],
        }
    """
    try:
        with open(filename, 'r') as archivo:
            contenido=archivo.read()
    except FileNotFoundError:
        raise FileNotFoundError
    listas=contenido.split("\n")
    diccionario={}
    for i in range(len(listas)):
        limpio = listas[i].strip()
        if listas[i]==[""] or limpio=="":
            continue
        if not ":" in listas[i]:
            raise ValueError("invalid log line")
        fila=listas[i]
        linea=fila.split(":",1)
        clave=linea[0].strip()
        mensaje=linea[1].strip()
        if clave in diccionario:
            diccionario[clave].append(mensaje)
        else:
            diccionario[clave]=[mensaje]
    return diccionario
