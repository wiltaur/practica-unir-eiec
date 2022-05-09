"""
License: Apache
Organization: UNIR
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False


def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"No puede ordenar {type(items)}")

    return sorted(items, reverse=(not ascending))


def remove_duplicates_from_list(items):
    return list(set(items))


if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
    else:
        print("Se debe indicar el fichero como primer argumento")
        print("El segundo argumento indica si se quieren eliminar duplicados")
        sys.exit(1)

    print(f"Se leerán las palabras del fichero {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        #se agrega una variable que va a contar la cantidad de items que se encontraron en el fichero
        #se inicia en 0 porque inicialmente esta vacía
        word_count_ini = 0
        word_count_fin = 0
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
        word_count_ini = len(word_list)
    else:
        print(f"El fichero {filename} no existe")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)
        word_count_fin = len(word_list)
    
    print(f"El fichero {filename} tenía {word_count_ini} palabras")
    print(f"Se encontraron {word_count_ini} - {word_count_fin} palabras duplicadas")
    print(sort_list(word_list))
    