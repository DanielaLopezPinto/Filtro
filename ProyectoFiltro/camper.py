import traceback
import json
import os

patch = "camper.json"
camper = {}

def buscar_camper(data: dict, clave):
    return data.get(str(clave))

with open(patch, "r") as f:
    camper = json.load(f)

def guardar_camper() -> str:
    while True:
        print("****************************")
        print("*      REGISTRO CAMPER     *")
        print("****************************")
        
        try:
            op=int(input("1. Registrar camper\n2. Atras\n"))
        except ValueError:
            print("\n---Ingrese un número---")
        
        if op==1:
            global camper
            try:
                cc = int(input("\nIngrese el número de documento del camper: "))
                #print("Camper antes de buscar_camper:", camper)
                camper_info = buscar_camper(camper, cc)
                #print("Camper después de buscar_camper:", camper)

                if camper_info:
                    
                    print("\n      ---El camper ya está inscrito---        ")
                    print(f"---Información del camper con documento {cc}---")
                    for key, value in camper_info.items():
                        if isinstance(value, dict):
                            print(f"{key}:")
                            for subkey, subvalue in value.items():
                                print(f"  {subkey}: {subvalue}")
                        else:
                            print(f"{key}: {value}")
                    print("\n---Ingrese un camper nuevo---\n")        
                    return guardar_camper()
                else:
                    print(f"\n---El camper con documento {cc} no está registrado---\n")

                tipo = int(input("Ingrese el tipo de documento:\n\t1. CC\n\t2. TI\n\t3. CE\n"))

                camper[cc] = {          
                    "Documento": cc,
                    "Nombre": str(input("\nIngrese el nombre del camper: ")),
                    "Apellido": str(input("\nIngrese el apellido del camper: ")),
                    "Direccion": str(input("\nIngrese la dirección del camper: ")),
                    "Acudiente": (),
                    "Telefonos": [],
                    "Estado": "Inscrito"
                }

                if tipo == 1 or tipo == 3:
                    print("\n---Ya estás grande para tener acudiente---")
                else:
                    acudiente = input("\nIngrese el acudiente del camper: ")  
                    camper[cc]["Acudiente"] = acudiente       

                bandera2 = True
                while(bandera2):
                    colTel = {}
                    opc = int(input("\nSeleccione el número de contacto\n\t1. Celular\n\t2. Fijo\n"))
                    if opc - 1: 
                        tel = str(input("\nIngrese el número: "))
                        colTel["Fijo"] = tel
                        camper[cc]["Telefonos"].append(colTel)
                        opc = int(input("\n¿Deseas ingresar otro número de contacto?\n\t1. SI\n\t2. NO\n"))
                        if opc - 1:
                            bandera2 = False
                    else:
                        cel = str(input("\nIngrese el número: "))
                        colTel["Celular"] = cel
                        camper[cc]["Telefonos"].append(colTel)
                        opc = int(input("\n¿Deseas ingresar otro número de contacto?\n\t1. SI\n\t2. NO\n"))
                        if opc - 1:
                            bandera2 = False

            except Exception as Error:
                traceback_info = traceback.format_exc()
                os.system("clear")
                print(f"Excepción atrapada: {Error}")
                print(f"Información de la traza:\n{traceback_info}")
                print("\n---Ingrese nuevamente los datos---\n")
                return guardar_camper()

            with open(patch, "w") as f:
                f.write(json.dumps(camper, indent=4))

            print(f'\n----El camper {camper[cc]["Nombre"]} con número de documento {cc} ha sido registrado----\n')
            os.system("clear")
            return camper[cc] 
 
        elif op==2:
            os.system("clear")
            break
        else:
            print("\n---Ingrese un dato válido---")
        
#loads para poder cargar desde un json un diccionario de python 
#dumps para apartir de un diccionario de python crear un objeto de json





