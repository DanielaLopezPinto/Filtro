import os
import traceback
import json
from camper import buscar_camper, guardar_camper

patch = "notas.json"
notas = {}

try:
    with open(patch, "r") as f:
        notas = json.load(f)
except FileNotFoundError:   #Excepcion por si el archivo no existe
    pass

def cargar_camper():
    global camper
    try:
        with open("camper.json", "r") as f:
            camper = json.load(f)
    except FileNotFoundError:
        pass

#funcion que borra los datos del camper y las notas si no paso la prueba inicial
def borrar_camper_y_notas(camper_id):
    global notas
    global camper
    if camper_id in notas:
        del notas[camper_id]
        with open(patch, "w") as f:
            json.dump(notas, f, indent=4)

    if camper_id in camper:
        del camper[camper_id]
        with open("camper.json", "w") as f:
            json.dump(camper, f, indent=4)

def prueba_inicial(camper_info=None):
    while True:
        cargar_camper()
        print("****************************")
        print("*     PRUEBA DE INGRESO    *")
        print("****************************")
        try:
            op = int(input("1. Prueba de ingreso\n2. Atras\n"))
        except ValueError:
            print("\n---Ingrese un número---")
        
        if op == 1:
            try:
                if camper_info is None:
                    id = int(input("\nIngrese el documento del camper: "))
                    camper_info = buscar_camper(camper, id)

                if camper_info:
                    print(f"\n---El camper con documento {camper_info['Documento']} ya está registrado---")

                    nota_teoria = int(input("\nIngrese la nota teórica: "))
                    nota_practica = int(input("\nIngrese la nota práctica: "))
                    promedio = (nota_teoria + nota_practica) / 2

                    if id not in notas:
                        notas[id] = {"Documento": id, "Notas": {}}

                    notas[id]["Notas"] = {
                        "Teorica": nota_teoria,
                        "Practica": nota_practica,
                        "Promedio": promedio
                    }

                    if promedio >= 60:
                        print("\n----¡Bienvenido a CampusLands!----\n")
                        notas[id]["Notas"] = {
                            "Teorica": nota_teoria,
                            "Practica": nota_practica,
                            "Promedio": promedio
                        }
                        input("Presiona Enter para salir al menú principal...")
                        break

                    else:
                        print("\n----Lo sentimos, no pasaste la prueba----\n")
                        borrar_camper_y_notas(str(id))
                        input("Presiona Enter para salir al menú principal...")
                        break

                else:
                    print(f"\n---El camper con documento {id} no está registrado.---")
                    opcion = input("¿Desea registrar el camper? (S/N): ").upper()

                    if opcion == 'S':
                        camper_info = guardar_camper()
                        prueba_inicial(camper_info)
                    else:
                        print("---Operación cancelada. No se registró el camper---")
                        input("Presione Enter para continuar")
                        os.system("clear")
                        return prueba_inicial
                    
            except Exception as Error:
                traceback_info = traceback.format_exc()
                os.system("clear")
                print(f"Excepción atrapada: {Error}")
                print(f"Información de la traza:\n{traceback_info}")
                print("\n---Ingrese nuevamente los datos---\n")
                return prueba_inicial()

        elif op == 2:
            os.system("clear")
            break

        else:
            print("\n---Ingrese un dato válido---\n")

# Llama a la función prueba_inicial para comenzar el proceso
#prueba_inicial()

            
            
            
            
            