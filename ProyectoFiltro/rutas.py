import traceback
import json
import os
from camper import buscar_camper, guardar_camper

def cargar_camper():
    global camper
    try:
        with open("camper.json", "r") as f:
            camper = json.load(f)
    except FileNotFoundError:
        pass  

patch = "rutas.json"
rutas = {}

try:
    with open(patch, "r") as f:
        rutas = json.load(f)
except FileNotFoundError:
    pass  

def rutas_entrenamiento(camper_info=None):
    cargar_camper()
    print("*******************")
    print("*      RUTAS      *")
    print("*******************")
    try:
        if camper_info is None:
            id = int(input("Ingrese el documento del camper: "))
            camper_info = buscar_camper(camper, id)
        
        if camper_info:
            print(f"\n---El camper con documento {camper_info['Documento']} ya está registrado.---")
            try:
                opc=int(input("\nQue ruta desea escoger\n\t1. NodeJS\n\t2. Java\n\t3. NetCore\n"))
            except ValueError:
                print("\n---Ingrese numeros---")
                return opc 
        
            rutas[id]={
                "Documento":id,
                "NodeJS":{
                    "Fundamentos Programacion":["Introducion algoritmia","PSeInt","Python"],
                    "Programacion Web":["HTML","CSS","Bootstrap"],
                    "Programacion formal":[],
                    "Bases de datos":{
                        "Principal":[],
                        "Alternativo":[]
                        },
                    "Backend":[]
                    },
                "Java": {
                    "Fundamentos Programacion":["Introducion algoritmia","PSeInt","Python"],
                    "Programacion Web":["HTML","CSS","Bootstrap"],
                    "Programacion formal":[],
                    "Bases de datos":{
                        "Principal":[],
                        "Alternativo":[]
                        },
                    "Backend":[]
                    },
                "NetCore":{
                    "Fundamentos Programacion":["Introducion algoritmia","PSeInt","Python"],
                    "Programacion Web":["HTML","CSS","Bootstrap"],
                    "Programacion formal":[],
                    "Bases de datos":{
                        "Principal":[],
                        "Alternativo":[]
                        },
                    "Backend":[]
                }
            }
        
        
        
            
            #RUTA
            if opc == 1:
                print("\n*** RUTA NODEJS ***")
                #Temario de la ruta NoteJS: Programacion Formal
                try:
                    sel=int(input("\nQue tema desea para Programacion formal:\n\t1. Java\n\t2. JavaScript\n\t3. C#\n"))
                except ValueError:
                    print("\n---Ingrese numeros---")
                    return sel
                if sel==1:
                    rutas[id]["NodeJS"]["Programacion Web"]="Java"
                    
                elif sel==2:
                    rutas[id]["NodeJS"]["Programacion Web"]="JavaScript" 
                    
                elif sel==3:
                    rutas[id]["NodeJS"]["Programacion Web"]="C#" 
                else:
                    print("---Ingrese un número indicado---")
                    
                    
                #Temario de la ruta NoteJS: Bases de datos    
                try:
                    sel=int(input("\nQue tema principal desea para Bases de datos:\n\t1. Mysql\n\t2. MongoDb\n\t3. Postgresql\n"))
                except ValueError:
                    print("\n---Ingrese numeros---")
                    return sel
                if sel==1:
                    rutas[id]["NodeJS"]["Bases de datos"]["Principal"]="Mysql"
                    try:
                        sel=int(input("\nQue tema alternativo desea para Bases de datos:\n\t1. MongoDb\n\t2. Postgresql\n"))
                    except ValueError:
                        print("\n---Ingrese numeros---")
                        return opc
                    if sel==2:
                        rutas[id]["NodeJS"]["Bases de datos"]["Alternativo"]="MongoDb" 
                    elif sel==3:
                        rutas[id]["NodeJS"]["Bases de datos"]["Alternativo"]="Postgresql" 
                    else:
                        print("---Ingrese un número indicado---")  
                elif sel==2:
                    rutas[id]["NodeJS"]["Bases de datos"]["Principal"]="MongoDb" 
                    try:
                        sel=int(input("\nQue tema alternativo desea para Bases de datos:\n\t1. Mysql\n\t2. Postgresql\n"))
                    except ValueError:
                        print("\n---Ingrese numeros---")
                        return opc
                    if sel==1:
                        rutas[id]["NodeJS"]["Bases de datos"]["Alternativo"]="Mysql"
                    elif sel==2:
                        rutas[id]["NodeJS"]["Bases de datos"]["Alternativo"]="Postgresql" 
                    else:
                        print("---Ingrese un número indicado---")    
                elif sel==3:
                    rutas[id]["NodeJS"]["Bases de datos"]["Principal"]="Postgresql" 
                    try:
                        sel=int(input("\nQue tema alternativo desea para Bases de datos:\n\t1. Mysql\n\t2. MongoDb\n"))
                    except ValueError:
                        print("\n---Ingrese numeros---")
                        return opc
                    if sel==1:
                        rutas[id]["NodeJS"]["Bases de datos"]["Alternativo"]="Mysql"
                    elif sel==2:
                        rutas[id]["NodeJS"]["Bases de datos"]["Alternativo"]="MongoDb" 
                    else:
                        print("---Ingrese un número indicado---")       
                else:
                    print("---Ingrese un número indicado---")    
                
                #Temario de la ruta NodeJS: Backend
                try:
                    sel=int(input("\nQue tema desea para Backend:\n\t1. NetCore\n\t2. Spring Boot\n\t3. NodeJS y Express\n"))
                except ValueError:
                    print("\n---Ingrese numeros---")
                    return sel
                if sel==1:
                    rutas[id]["NodeJS"]["Backend"]="NetCore"
                    
                elif sel==2:
                    rutas[id]["NodeJS"]["Backend"]="Spring Boot" 
                    
                elif sel==3:
                    rutas[id]["NodeJS"]["Backend"]="NodeJS y Express" 
                else:
                    print("---Ingrese un número indicado---")
                    
                         
            #RUTA         
            elif opc == 2:
                print("\n*** RUTA JAVA ***")
                #Temario de la ruta Java: Programacion Formal
                try:
                    sel=int(input("\nQue tema desea para Programacion formal:\n\t1. Java\n\t2. JavaScript\n\t3. C#\n"))
                except ValueError:
                    print("\n---Ingrese numeros---")
                    return sel
                if sel==1:
                    rutas[id]["Java"]["Programacion Web"]="Java"
                    
                elif sel==2:
                    rutas[id]["Java"]["Programacion Web"]="JavaScript" 
                    
                elif sel==3:
                    rutas[id]["Java"]["Programacion Web"]="C#" 
                else:
                    print("---Ingrese un número indicado---")
                    
                    
                #Temario de la ruta Java: Bases de datos    
                try:
                    sel=int(input("\nQue tema principal desea para Bases de datos:\n\t1. Mysql\n\t2. MongoDb\n\t3. Postgresql\n"))
                except ValueError:
                    print("\n---Ingrese numeros---")
                    return sel
                if sel==1:
                    rutas[id]["Java"]["Bases de datos"]["Principal"]="Mysql"
                    try:
                        sel=int(input("\nQue tema alternativo desea para Bases de datos:\n\t1. MongoDb\n\t2. Postgresql\n"))
                    except ValueError:
                        print("\n---Ingrese numeros---")
                        return opc
                    if sel==2:
                        rutas[id]["Java"]["Bases de datos"]["Alternativo"]="MongoDb" 
                    elif sel==3:
                        rutas[id]["Java"]["Bases de datos"]["Alternativo"]="Postgresql" 
                    else:
                        print("---Ingrese un número indicado---")  
                elif sel==2:
                    rutas[id]["Java"]["Bases de datos"]["Principal"]="MongoDb" 
                    try:
                        sel=int(input("\nQue tema alternativo desea para Bases de datos:\n\t1. Mysql\n\t2. Postgresql\n"))
                    except ValueError:
                        print("\n---Ingrese numeros---")
                        return opc
                    if sel==1:
                        rutas[id]["Java"]["Bases de datos"]["Alternativo"]="Mysql"
                    elif sel==2:
                        rutas[id]["Java"]["Bases de datos"]["Alternativo"]="Postgresql" 
                    else:
                        print("---Ingrese un número indicado---")    
                elif sel==3:
                    rutas[id]["Java"]["Bases de datos"]["Principal"]="Postgresql" 
                    try:
                        sel=int(input("\nQue tema alternativo desea para Bases de datos:\n\t1. Mysql\n\t2. MongoDb\n"))
                    except ValueError:
                        print("\n---Ingrese numeros---")
                        return opc
                    if sel==1:
                        rutas[id]["Java"]["Bases de datos"]["Alternativo"]="Mysql"
                    elif sel==2:
                        rutas[id]["Java"]["Bases de datos"]["Alternativo"]="MongoDb" 
                    else:
                        print("---Ingrese un número indicado---")       
                else:
                    print("---Ingrese un número indicado---")    
                
                #Temario de la ruta Java: Backend
                try:
                    sel=int(input("\nQue tema desea para Backend:\n\t1. NetCore\n\t2. Spring Boot\n\t3. NodeJS y Express\n"))
                except ValueError:
                    print("\n---Ingrese numeros---")
                    return sel
                if sel==1:
                    rutas[id]["Java"]["Backend"]="NetCore"
                    
                elif sel==2:
                    rutas[id]["Java"]["Backend"]="Spring Boot" 
                    
                elif sel==3:
                    rutas[id]["Java"]["Backend"]="NodeJS y Express" 
                else:
                    print("---Ingrese un número indicado---")
                
                
                
                
            #RUTA     
            elif opc == 3:
                print("\n*** RUTA NETCORE ***")
                #Temario de la ruta NetCore: Programacion Formal
                try:
                    sel=int(input("\nQue tema desea para Programacion formal:\n\t1. Java\n\t2. JavaScript\n\t3. C#\n"))
                except ValueError:
                    print("\n---Ingrese numeros---")
                    return sel
                if sel==1:
                    rutas[id]["NetCore"]["Programacion Web"]="Java"
                    
                elif sel==2:
                    rutas[id]["NetCore"]["Programacion Web"]="JavaScript" 
                    
                elif sel==3:
                    rutas[id]["NetCore"]["Programacion Web"]="C#" 
                else:
                    print("---Ingrese un número indicado---")
                    
                    
                #Temario de la ruta NetCore: Bases de datos    
                try:
                    sel=int(input("\nQue tema principal desea para Bases de datos:\n\t1. Mysql\n\t2. MongoDb\n\t3. Postgresql\n"))
                except ValueError:
                    print("\n---Ingrese numeros---")
                    return sel
                if sel==1:
                    rutas[id]["NetCore"]["Bases de datos"]["Principal"]="Mysql"
                    try:
                        sel=int(input("\nQue tema alternativo desea para Bases de datos:\n\t1. MongoDb\n\t2. Postgresql\n"))
                    except ValueError:
                        print("\n---Ingrese numeros---")
                        return opc
                    if sel==2:
                        rutas[id]["NetCore"]["Bases de datos"]["Alternativo"]="MongoDb" 
                    elif sel==3:
                        rutas[id]["NetCore"]["Bases de datos"]["Alternativo"]="Postgresql" 
                    else:
                        print("---Ingrese un número indicado---")  
                elif sel==2:
                    rutas[id]["NetCore"]["Bases de datos"]["Principal"]="MongoDb" 
                    try:
                        sel=int(input("\nQue tema alternativo desea para Bases de datos:\n\t1. Mysql\n\t2. Postgresql\n"))
                    except ValueError:
                        print("\n---Ingrese numeros---")
                        return opc
                    if sel==1:
                        rutas[id]["NetCore"]["Bases de datos"]["Alternativo"]="Mysql"
                    elif sel==2:
                        rutas[id]["NetCore"]["Bases de datos"]["Alternativo"]="Postgresql" 
                    else:
                        print("---Ingrese un número indicado---")    
                elif sel==3:
                    rutas[id]["NetCore"]["Bases de datos"]["Principal"]="Postgresql" 
                    try:
                        sel=int(input("\nQue tema alternativo desea para Bases de datos:\n\t1. Mysql\n\t2. MongoDb\n"))
                    except ValueError:
                        print("\n---Ingrese numeros---")
                        return opc
                    if sel==1:
                        rutas[id]["NetCore"]["Bases de datos"]["Alternativo"]="Mysql"
                    elif sel==2:
                        rutas[id]["NetCore"]["Bases de datos"]["Alternativo"]="MongoDb" 
                    else:
                        print("---Ingrese un número indicado---")       
                else:
                    print("---Ingrese un número indicado---")    
                
                #Temario de la ruta NetCore: Backend
                try:
                    sel=int(input("\nQue tema desea para Backend:\n\t1. NetCore\n\t2. Spring Boot\n\t3. NodeJS y Express\n"))
                except ValueError:
                    print("\n---Ingrese numeros---")
                    return sel
                if sel==1:
                    rutas[id]["NetCore"]["Backend"]="NetCore"
                    
                elif sel==2:
                    rutas[id]["NetCore"]["Backend"]="Spring Boot" 
                    
                elif sel==3:
                    rutas[id]["NetCore"]["Backend"]="NodeJS y Express" 
                else:
                    print("---Ingrese un número indicado---")
                
                
                
            else:
                    ("\n---Ingrese un número indicado---")     
            
            
            
        else:
            print(f"\n---El camper con documento {id} no está registrado.---")
            opcion = input("¿Desea registrar el camper? (S/N): ").upper()

            if opcion == 'S':
                camper_info = guardar_camper()
                rutas_entrenamiento(camper_info)
            else:
                print("Operación cancelada. No se registró el camper.") 
                
        with open(patch, "w") as f:
            f.write(json.dumps(rutas, indent=4))
        
                   
    except Exception as Error:
        traceback_info = traceback.format_exc()
        os.system("clear")
        print(f"Excepción atrapada: {Error}")
        print(f"Información de la traza:\n{traceback_info}")
        print("\n---Ingrese nuevamente los datos---\n")
        return rutas_entrenamiento()            
                
                
            
            
            
