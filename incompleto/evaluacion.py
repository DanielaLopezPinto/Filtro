import os
import traceback
import json
from camper import buscar_camper, guardar_camper

patch = "notas.json"
evaluacion = {}

try:
    with open(patch, "r") as f:
        evaluacion = json.load(f)
except FileNotFoundError:
    pass

def cargar_camper():
    global camper
    try:
        with open("camper.json", "r") as f:
            camper = json.load(f)
    except FileNotFoundError:
        pass

def filtros(camper_info=None):
    while True:
        cargar_camper()
        print("****************")
        print("*    FILTRO    *")
        print("****************")
        try:
            op = int(input("1. Filtro\n2. Atras\n"))
        except ValueError:
            print("\n---Ingrese un número---")
        
        if op == 1:
            try:
                if camper_info is None:
                    id = int(input("\nIngrese el documento del camper: "))
                    camper_info = buscar_camper(camper, id)

                if camper_info:
                    print(f"\n---El camper con documento {camper_info['Documento']} ya está registrado---")

                    nota_teorica = int(input("\nIngrese la nota teórica: "))
                    nota_practica = int(input("\nIngrese la nota práctica: "))
                    quiz=int(input("\nIngrese la nota del quiz: "))
                    trabajo=int(input("\nIngrese la nota del trabajo: "))
                    promedio = (nota_teorica*0.3)+(nota_teorica*0.6)+((quiz+trabajo)*0.1) / 3
                    
                    if id not in evaluacion:
                        evaluacion[id] = {"Documento": id, "Notas": {}}

                    evaluacion[id]["Notas"] = {
                        "Teorica": nota_teorica,
                        "Practica": nota_practica,
                        "Quiz": quiz,
                        "Trabajo":trabajo,
                        "Promedio": promedio
                        
                    }

                    if promedio >= 60:
                        print("\n----¡Felicidades has pasado el filtro!----")
                        print(f"---Con un promedio de {round(promedio)}---\n")
                        evaluacion[id]["Notas"] = {
                            "Teorica": nota_teorica,
                            "Practica": nota_practica,
                            "Quiz":quiz,
                            "Trabajo":trabajo,
                            "Promedio": promedio
                        }
                        input("Presiona Enter para salir al menú principal...")
                        break
                    else:
                        print("\n---Lo sentimos, has reprobado el filtro---")
                        print(f"---Con un promedio de {round(promedio)}---\n")

                else:
                    print(f"\n---El camper con documento {id} no está registrado.---")
                    opcion = input("¿Desea registrar el camper? (S/N): ").upper()

                    if opcion == 'S':
                        camper_info = guardar_camper()
                        filtros(camper_info)
                    else:
                        print("---Operación cancelada. No se registró el camper---")
                        input("Presione Enter para continuar")
                        os.system("clear")
                        return filtros
                    
            except Exception as Error:
                traceback_info = traceback.format_exc()
                os.system("clear")
                print(f"Excepción atrapada: {Error}")
                print(f"Información de la traza:\n{traceback_info}")
                print("\n---Ingrese nuevamente los datos---\n")
                return filtros()

        elif op == 2:
            os.system("clear")
            break

        else:
            print("\n---Ingrese un dato válido---\n")

filtros()