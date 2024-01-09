import traceback
import json
import os

patch = "trainer.json"
trainer = {}


def buscar_trainer(data: dict, clave):
    return data.get(str(clave))

with open(patch, "r") as f:
    trainer = json.load(f)

def guardar_trainer() -> str:
    while True:
        print("*****************************")
        print("*      REGISTRO TRAINER     *")
        print("*****************************")
        
        try:
            op=int(input("1. Registrar trainer\n2. Atras\n"))
        except ValueError:
            print("\n---Ingrese un número---")
        
        if op==1:
            global tainer
            try:
                cc = int(input("\nIngrese el número de documento del trainer: "))
                #print("Trainer antes de buscar_trainer:", trainer)
                trainer_info = buscar_trainer(trainer, cc)
                #print("Trainer después de buscar_trainer:", trainer)

                if trainer_info:
                    print("\n      ---El trainer ya está inscrito---        ")
                    print(f"---Información del tainer con documento {cc}---")
                    for key, value in trainer_info.items():
                        if isinstance(value, dict):
                            print(f"{key}:")
                            for subkey, subvalue in value.items():
                                print(f"  {subkey}: {subvalue}")
                        else:
                            print(f"{key}: {value}")
                    print("\n---Ingrese un camper nuevo---\n")        
                    return guardar_trainer()
                else:
                    print(f"\n---El trainer con documento {cc} no está registrado---")
                    
                    
                trainer[cc] = {          
                    "Documento": cc,
                    "Nombre": str(input("\nIngrese el nombre del trainer: ")),
                    "Apellido": str(input("\nIngrese el apellido del trainer: ")),
                    "Horario":{
                        "1":[],
                        "Opcional":[]
                        },
                    "Ruta":[]
                }
                
                # Para que sellecione el horario en el que quiera trabajar
                opcion = int(input("\n---Seleccione el horario de trabajo---\n\t1. 6:00 am a 9:30 am\n\t2. 10:00 am a 1:30 pm\n\t3. 2:00 pm a 5:30 pm\n\t4. 6:00 pm a 9:30 pm\n"))
                if opcion == 1:
                    trainer[cc]["Horario"]["1"] = "6:00 am a 9:30 am"
                    opc=int(input("Desea trabajar en otro horario\n1. Si\n2. No\n"))
                    if opc == 1:
                        opcion = int(input("---Seleccione el horario de trabajo---\n\t1. 10:00 am a 1:30 pm\n\t2. 2:00 pm a 5:30 pm\n\t3. 6:00 pm a 9:30 pm\n"))
                        if opcion== 1:
                            trainer[cc]["Horario"]["Opcional"] = "10:00 am a 1:30 pm"
                        elif opcion == 2:
                            trainer[cc]["Horario"]["Opcional"] = "2:00 pm a 5:30 pm"
                        elif opcion == 3:
                            trainer[cc]["Horario"]["Opcional"] = "6:00 pm a 9:30 pm"
                        else:
                            print("---Ingrese un número valido---")
                            return
                    elif opc == 2:
                        os.system("clear")
                        #break
                    else:
                        print("---Ingrese un número valido---")
                        return
                    
                elif opcion == 2:
                    trainer[cc]["Horario"]["1"] = "10:00 am a 1:30 pm"
                    opc=int(input("Desea trabajar en otro horario\n1. Si\n2. No"))
                    if opc == 1:
                        opcion = int(input("---Seleccione el horario de trabajo---\n\t1. 6:00 am a 9:30 am\n\t2. 2:00 pm a 5:30 pm\n\t3. 6:00 pm a 9:30 pm\n"))
                        if opcion== 1:
                            trainer[cc]["Horario"]["Opcional"] = "6:00 am a 9:30 am"
                        elif opcion == 2:
                            trainer[cc]["Horario"]["Opcional"] = "2:00 pm a 5:30 pm"
                        elif opcion == 3:
                            trainer[cc]["Horario"]["Opcional"] = "6:00 pm a 9:30 pm"
                        else:
                            print("---Ingrese un número valido---")
                            return
                    elif opc == 2:
                        os.system("clear")
                        #break
                    else:
                        print("---Ingrese un número valido---")
                        return
                    
                elif opcion == 3:
                    trainer[cc]["Horario"]["1"] = "2:00 pm a 5:30 pm"
                    opc=int(input("Desea trabajar en otro horario\n1. Si\n2. No"))
                    if opc == 1:
                        opcion = int(input("---Seleccione el horario de trabajo---\n\t1. 6:00 am a 9:30 am\n\t2. 10:00 am a 1:30 pm\n\t3. 6:00 pm a 9:30 pm\n"))

                        if opcion== 1:
                            trainer[cc]["Horario"]["Opcional"] = "6:00 am a 9:30 am"
                        elif opcion == 2:
                            trainer[cc]["Horario"]["Opcional"] = "10:00 am a 1:30 pm"
                        elif opcion == 3:
                            trainer[cc]["Horario"]["Opcional"] = "6:00 pm a 9:30 pm"
                        else:
                            print("---Ingrese un número valido---")
                            return
                    elif opc == 2:
                        os.system("clear")
                        #break
                    else:
                        print("---Ingrese un número valido---")
                        return
                    
                elif opcion == 4:
                    trainer[cc]["Horario"]["1"] = "6:00 pm a 9:30 pm"
                    opc=int(input("Desea trabajar en otro horario\n1. Si\n2. No"))
                    if opc == 1:
                        opcion = int(input("---Seleccione el horario de trabajo---\n\t1. 6:00 am a 9:30 am\n\t2. 10:00 am a 1:30 pm\n\t3. 2:00 pm a 5:30 pm\n"))
                        if opcion== 1:
                            trainer[cc]["Horario"]["Opcional"] = "6:00 am a 9:30 am"
                        elif opcion == 2:
                            trainer[cc]["Horario"]["Opcional"] = "10:00 am a 1:30 pm"
                        elif opcion == 3:
                            trainer[cc]["Horario"]["Opcional"] = "2:00 pm a 5:30 pm"
                        else:
                            print("---Ingrese un número valido---")
                            return
                    elif opc == 2:
                        os.system("clear")
                        #break
                    else:
                        print("---Ingrese un número valido---")
                        return
                else:
                    print("---Ingrese un número valido---")     
                    return
                    
                # Solicitar la ruta de entrenamiento
                ruta = int(input("Seleccione la ruta de entrenamiento:\n\t1. Ruta NodeJS\n\t2. Ruta Java\n\t3. Ruta NetCore\n"))
                # Asignar la ruta de entrenamiento según la opción seleccionada
                if ruta == 1:
                    trainer[cc]["Ruta"] = "Ruta NodeJS"
                elif ruta == 2:
                    trainer[cc]["Ruta"] = "Ruta Java"
                elif ruta == 3:
                    trainer[cc]["Ruta"]  = "Ruta NetCore"
                else:
                    print("---Ingrese un número valido---")
                    return         
            
            
            except Exception as Error:
                traceback_info = traceback.format_exc()
                os.system("clear")
                print(f"Excepción atrapada: {Error}")
                print(f"Información de la traza:\n{traceback_info}")
                print("\n---Ingrese nuevamente los datos---\n")
                return guardar_trainer()

            with open(patch, "w") as f:
                f.write(json.dumps(trainer, indent=4))

            print(f'Ruta de entrenamiento {trainer[cc]["Ruta"]} asignada y guardada exitosamente para el entrenador {trainer[cc]["Nombre"]}  en el horario {trainer[cc]["Horario"]} ---')
 
        elif op==2:
            os.system("clear")
            break
        else:
            print("\n---Ingrese un dato válido---")
 
       



  
