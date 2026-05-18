# Ejercicio 5 - CSV a lista de diccionarios


def csv_to_dict(filename):
    """
    Lee un archivo CSV con header "name,age,city" y retorna una lista de
    diccionarios, uno por fila.

    Reglas:
    - La primera línea es siempre el header.
    - Las claves del diccionario se toman del header.
    - El campo "age" se convierte a int. "name" y "city" quedan como str.
    - Se deben hacer strip a los valores para eliminar espacios sobrantes.
    - Si el archivo está vacío o solo tiene header, retornar [].
    - Si el archivo no existe, propagar FileNotFoundError.
    - No se permite usar el módulo csv.

    Args:
        filename: str - nombre del archivo a leer.

    Returns:
        list[dict] - lista de diccionarios por fila del CSV.

    Raises:
        FileNotFoundError: si el archivo no existe.

    Ejemplo:
        # archivo contiene:
        # name,age,city
        # Alice,30,Buenos Aires
        # Bob,25,Rosario
        csv_to_dict("people.csv") -> [
            {"name": "Alice", "age": 30, "city": "Buenos Aires"},
            {"name": "Bob", "age": 25, "city": "Rosario"},
        ]
    """
    import csv
    try:
        with open(filename,'r') as archivo:
            lector=csv.reader(archivo)
            lista = list(lector)
    except FileNotFoundError:
        raise FileNotFoundError
    if lista==[]:
        return[]
    super_lista=[]
    for fila in range(len(lista)):
        diccionario = {}
        if fila==0 and len(lista) == 1:
            return []
        if fila == 0:
            continue
        for i in range(len(lista[0])):
            clave=lista[0][i].strip()
            valor=lista[fila][i].strip()
            if fila!=0 and i==1:
                valor=int(valor)
            diccionario[clave] = valor
        super_lista.append(diccionario)
    return super_lista
