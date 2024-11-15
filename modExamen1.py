import random
import json

f = "playlist2.txt"
filejson = "playlistjson.json"

# Formato json:
#[
#    {
#       "Nombre": "valueNombre",
#       "Artista": "valueArtista",
#       "Género": "valueGenero"
#    },
#
#    {
#       "Nombre": "valueNombre",
#       "Artista": "valueArtista",
#       "Género": "valueGenero"
#    },
#]

# Leer archivo.

def cargar_lista(f):
    listCanciones = []

    try:
        with open(f, "r") as archivo:
            fallo = False
            for linea in archivo:
                # Eliminamos cualquier espacio extra y saltos de línea, y dividimos línea en función de los " - ", creando una lista.
                # values es una lista de los elementos de línea.
                values = linea.strip().split(" - ")
                # Si values comprende 3 elementos entrará en el if.
                if len(values) ==3:
                    # Tomamos los valores de nombre, artista y género en función de los elementos de values.
                    nombre, artista, genero = values
                    # Cada canción (dict) tendrá sus respectivos Nombre, Artista y Género.
                    cancion = {
                        "Nombre": nombre,
                        "Artista": artista, 
                        "Género": genero
                    }
                    # Finalmente añadimos la canción a la lista de canciones.
                    listCanciones.append(cancion)
                else:
                    fallo = True
            if fallo:
                print("\nEl archivo proporcionado tiene errores en el formato.")
                print("\nVerifica que el formato de cada línea es: NombreCanción - Artista - Género\n")
    except FileNotFoundError:
        print(f"\nEl archivo {f} no se pudo encontrar.\n")
    except IOError:
        print(f"\nHubo un error al leer el archivo {f}.\n")
        
    return listCanciones

# Opción 1

def agregar_cancion(listCanciones, nuevaCancion, artista, genero):
                        # Recorremos la lista. Si ya existe la canción, no la añadiremos.
                        #for cancion in listCanciones:
                        #    if nuevaCancion == cancion["Nombre"]:
                        #        print("La canción ya existe en la lista.")
                        #        # Salimos de la función si ya existe
                        #        return
                        # Si no existe, la canción se añadirá.
                        #cancion = {
                        #    "Nombre": nuevaCancion,
                        #    "Artista": artista,
                        #    "Género": genero
                        #}
                        #listCanciones.append(cancion)
                        #print("Canción añadida con éxito.")

    # Forma 2 de hacerlo

    # Recorremos la lista gracias a la función buscar_imagen(), obteniendo un boolean que nos dirá 
    # si existe o no el elemento deseado.
    numCancion, exito = buscar_cancion(listCanciones, nuevaCancion) # en este caso numCancion no es necesario.
    if exito:
        print("La canción ya existe en la lista.")
    else:
        cancion = {
            "Nombre": nuevaCancion,
            "Artista": artista,
            "Género": genero
        }
        listCanciones.append(cancion)
        print("Canción añadida con éxito.")

# Opción 2

def eliminar_cancion(listCanciones, tituloCancion):
                        # Recorremos la lista. Si existe la canción la eliminaremos.
                        #for cancion in listCanciones:
                        #    if tituloCancion == cancion["Nombre"]:
                        #        listCanciones.remove(cancion)
                        #        print(f"La canción {tituloCancion} ha sido eliminada.")
                        #        return
                        # Si no existe la canción pondremos el siguiente mensaje.
                        #print("No se ha encontrado la canción.")

    # Forma 2 de hacerlo

    numCancion, exito = buscar_cancion(listCanciones, tituloCancion)
    if exito:
        del listCanciones[numCancion]
        print(f"La canción {tituloCancion} ha sido eliminada.")
    else:
        print("No se ha encontrado la canción.")

# Opción 3

def buscar_cancion(listCanciones, nombreCancion):
    # for i, cancion in ennumerate(playlist):
    for i, cancion in enumerate(listCanciones):
        if nombreCancion == cancion["Nombre"]:
            return i, True
    return i, False
    # Otra forma de hacerlo es que solo devuelva i. 
    # Si i es positivo significa que el valor se encontró y la propia i es la posición en la lista de este valor.
    # Si i es negativo (-1) significa que el valor no se encontró.

# Opción 4

def guardar_lista(listCanciones, f):
    try:
        with open(f,"w") as archivo:
            for cancion in listCanciones:
                archivo.write(f"{cancion['Nombre']} - {cancion['Artista']} - {cancion['Género']}\n")
    except FileNotFoundError:
        print(f"\nEl archivo {f} no se pudo encontrar.\n")
    except IOError:
        print(f"\nHubo un error al leer el archivo {f}.\n")

# Leer JSON

def cargar_json(filejson):
    with open (filejson, "r", encoding='utf-8') as archivo:
        # json.load(<file name> (Str)) --> List / Dict
        return json.load(archivo)

# Escribir JSON

def escribir_json(filejson, contenido):
    with open (filejson, "w", encoding='utf-8') as archivo:
        # json.dump(List / Dict, archivo) --> Str
        json.dump(contenido, archivo, indent=4, ensure_ascii=False)
        # json.dumps(List / Dict) --> Str
        #archivo.write(json.dumps(contenido, indent=4, ensure_ascii=False))
        


# Vamos a crear un menú de opciones para el usuario.

def mostrar_menu():
    print("\nRegistro de canciones:\n")
    print("1. Agregar Canción a Lista de Música.")
    print("2. Eliminar Canción de Lista de Música.")
    print("3. Buscar Canción de Lista de Música.")
    print("4. Guardar Lista de Reproducción en Archivo.")  
    print("5. Salir.") 

# Implementamos una funcion main para controlar todas las decisiones del usuario

def main():

    listCanciones = cargar_lista(f)
    #listCanciones = cargar_json(filejson)

    if not listCanciones:
        return
    else:

        exit = False

        while not exit:
            mostrar_menu()
            opcion = input("\nSeleccione una opción (1-5):").strip()
            if opcion == "1":
                # Agregar Canción a Lista de Música.
                nuevaCancion = input("Introduce una nueva canción:").strip()
                artista = input("Introduce el artista de la canción a implementar:").strip()
                genero = input("Introduce el género de la canción a implementar:").strip()

                agregar_cancion(listCanciones, nuevaCancion, artista, genero)

            elif opcion == "2":
                # Eliminar Canción de Lista de Música.
                tituloCancion = input("Introduce la canción a eliminar:").strip()
                eliminar_cancion(listCanciones, tituloCancion)

            elif opcion == "3":
                # Buscar Canción de Lista de Música.
                nombreCancion = input("Introduce la canción a buscar:").strip()
                exito = buscar_cancion(listCanciones, nombreCancion)
                if exito:
                    print("Se encontró la canción con éxito.")
                else:
                    print("No se encontró la canción en la lista.")

            elif opcion == "4":
                # Guardar Lista de Reproducción en Archivo.
                guardar_lista(listCanciones, f)
                escribir_json(filejson, listCanciones)
                print("Datos guardados correctamente.")

            elif opcion == "5":
                # Salir
                print("Saliendo del programa...")
                exit = True
            else:
                print("Opción no válida. Inténtelo de nuevo.")


# Hacemos que el main se inicie automáticamente al iniciar el proyecto.

if __name__ == "__main__":
    main()


# Investigación

# 1. Try - except                                       Done
# 2. Comprobar nº valores fichero (3)                   Done
# 3. Crear función buscar canción (lista, nombre)       
# 4. JSON                                               