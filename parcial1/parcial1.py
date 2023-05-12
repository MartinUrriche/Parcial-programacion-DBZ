
import re
import random
import json
#1
def obtener_csv_como_lista():
    with open("parcial1\DBZ (1).csv", 'r',encoding = 'UTF-8') as archivo:
        personajes = []
        for linea in archivo:
            columna = re.split(",|\n",linea)
            id = int(columna[0])
            nombre = columna[1]
            nombre = nombre.strip()
            #posicion = raza.find("-H")
            if( columna[2] == "Shin-jin" or  columna[2] == "Three-Eyed People"):
                columna[2] = columna[2].replace("-"," ")
            raza = re.split(r"-", columna[2])
            poder_pelea = int(columna[3])
            poder_ataque = int(columna[4])
            habilidades = re.split(r"[|$%]+",columna[5])
            #print(habilidades)
            personajes.append({
                'ID': id,
                'nombres': nombre,
                'raza': raza,
                'poder_pelea': poder_pelea,
                'poder_ataque': poder_ataque,
                'habilidades': habilidades,   
                })
            
    return personajes

lista_personajes = obtener_csv_como_lista()

#2
def cantidad_personajes_por_raza(raza: str , lista_personajes: list)-> list:
    '''
    Brief:
        Calcula y imprime la cantidad de personajes por raza
    Parameters: 
        raza: es un dato de tipo str que se usa para buscar valores en la lista
        lista_personajes: la lista con todos los diccionarios que contienen los dartos de los personajes
    Return:
        La funcion retorna una lista con los distintos valores contados
    '''
    lista_raza = {}
    for personaje in(lista_personajes):
        raza_actual = personaje[raza]
        for clave in raza_actual:
            if(clave in lista_raza):
                lista_raza[clave] += 1
            else :
                lista_raza[clave] = 1
    return lista_raza
#3
def mostrar_datos_personaje_por_raza(clave:str ,  lista_personajes:list):
    lista_raza = cantidad_personajes_por_raza (clave, lista_personajes)
    for tipo in lista_raza :
        print(f"La {clave} es {tipo}")
        for personaje in lista_personajes:
            if(tipo in personaje[clave]):
                print(f"El nombre es: {personaje['nombres']} , y su poder de ataque es: {personaje['poder_ataque']} ")
        print()
#4
def datos_pesonaje_por_habilidad (clave: str, lista:list):
    descripcion_habilidad = str(input("Ingrese una descripcion de la habilidad: "))
    print(f"La habilidad es: ", descripcion_habilidad)
    print("La habilidad pertenece a los siguientes personajes: ")
    for personaje in lista_personajes:
        if(descripcion_habilidad in personaje[clave]):
            poder_de_ataque_actual = int(personaje['poder_ataque'])
            poder_de_pelea_actual = int(personaje['poder_pelea'])
            promedio_poder_ataque_y_pelea = float((poder_de_ataque_actual + poder_de_pelea_actual)/2)
            print(f"{personaje['nombres']} y su raza es: {personaje['raza']}",
                "y el promedio entre su poder de pelea y ataque es de: ", promedio_poder_ataque_y_pelea)  

#5
def mostrar_lista_de_personajes(lista:list):
    '''
        Brief:
            Calcula y imprime la cantidad de personajes por raza
        Parameters: 
            raza: es un dato de tipo str que se usa para buscar valores en la lista
            lista_personajes: la lista con todos los diccionarios que contienen los dartos de los personajes
        Return:
            La funcion retorna una lista con los distintos valores contados
        '''
    for personaje in lista_personajes:
        id = personaje['ID']
        nombre = personaje['nombres']
        raza = personaje['raza']
        #if (personaje['raza'] != "Shin-jin" and personaje['raza'] != "Three-Eyed People" ):
        #    raza = re.split("-", personaje['raza'])
        poder_pelea = personaje['poder_pelea']
        poder_ataque = personaje['poder_ataque']
        habilidades = personaje['habilidades']
        print(f"ID: {id}")
        print(f"Nombre: {nombre}")
        print(f"Raza: {raza}")
        print(f"Poder de pelea: {poder_pelea}")
        print(f"Poder de ataque: {poder_ataque}")
        print(f"Habilidades: {habilidades}\n")
mostrar_lista_de_personajes(lista_personajes)


def elegi_un_personaje(lista:list,clave_id:int):
    lista_personajes
    eleccion_personaje = int(input("Elegi el numero del personaje que quieras usar: "))
    for personaje in lista_personajes:
        if(eleccion_personaje == personaje[clave_id]):
            nombre_personaje_elegido = personaje['nombres']
            raza_personaje_elegido = personaje['raza']
            poder_ataque_personaje_elegido = personaje['poder_ataque']
    return nombre_personaje_elegido, raza_personaje_elegido, poder_ataque_personaje_elegido


def personaje_random(clave:int):
    id_personaje_que_eligio = random.randint(0,36)
    for personaje in lista_personajes:
        if(id_personaje_que_eligio == personaje[clave]):
            nombre_personaje_random = personaje['nombres']
            raza_personaje_random = personaje['raza']
            poder_ataque_personaje_random =personaje['poder_ataque']
    return nombre_personaje_random,raza_personaje_random,poder_ataque_personaje_random,


def jugar_batalla(): 
    nombre_pj_elegido,raza_pj_elegido,poder_ataque_pj_elegido= elegi_un_personaje(lista_personajes,'ID')
    print("")
    print(f"El personaje que elgiste es: ",nombre_pj_elegido,raza_pj_elegido,poder_ataque_pj_elegido)
    personaje_random('ID')
    nombre_pj_random,raza_pj_random,poder_ataque_pj_random= personaje_random('ID')
    print(" ")
    print(f"El personaje random es: ",nombre_pj_random,raza_pj_random,poder_ataque_pj_random)
    print("")
    if(poder_ataque_pj_elegido > poder_ataque_pj_random):
        print(f"El personaje ganador es: ", nombre_pj_elegido,raza_pj_elegido,poder_ataque_pj_elegido)
    else:
        print("El personaje ganador es: ", nombre_pj_random,raza_pj_random,poder_ataque_pj_random)
    return nombre_pj_elegido, nombre_pj_random


def crear_archivo_txt():
    
guardar_duelos_txt()

def menu_opciones():
    print('''
    1:Listar cantidad por raza
    2:Listar personajes por raza
    3:Listar personajes por habilidad
    4:Jugar batalla
    5:Guardar Json
    6:Leer Json
    7:Salir
    ''')

def respuestas_menu():
    menu_opciones
    respuestas_validas = {1, 2, 3, 4, 5, 6, 7}
    respuesta = int(input("Ingrese una opcion: "))
    while (respuesta not in respuestas_validas):
        respuesta = int(input("Ingrese una opcion valida: "))
    return respuesta


def app_DBZ(lista):
    respuesta = respuestas_menu()
    match respuesta :
        case 1:
            lista_raza = cantidad_personajes_por_raza('raza', lista)
            for tipo in(lista_raza): 
                print(f"{tipo}: {lista_raza[tipo]}")
        case 2: 
            mostrar_datos_personaje_por_raza('raza', lista_personajes)
        case 3:
            datos_pesonaje_por_habilidad('habilidades', lista_personajes)
        #case 4:
            
        #case 5:
            


app_DBZ(lista_personajes)
