import os
import traceback
from camper import*
from notas import*
from rutas import*
from trainer import*

bandera=True
while (bandera):
    try:
        print("*************************")
        print("*      CAMPUSLANDS      *")
        print("*************************")
        print("* Seguimiento Academico *")
        print("-------------------------")
        print("1. Registrar Camper")
        print("2. Registrar Prueba")
        print("3. Crear Ruta de Entrenamiento")
        print("4. Registrar Trainer")
        print("5. Listar Campers Inscritos")
        print("6. Evaluar Camper")
        print("7. Campers en Riesgo")
        print("8. Generar Reportes")
        print("9. Salir")
        try:
            opcion=int(input("\nQue desea hacer: "))
        except ValueError:
            print("\n---Ingrese un número---")
        if opcion == 1:
            os.system("clear")
            print(guardar_camper())
        elif opcion == 2:
            os.system("clear")
            if __name__ == "__main__":
                prueba_inicial()
        elif opcion == 3:
            os.system("clear")
            rutas_entrenamiento()
        elif opcion == 4:
            os.system("clear")
            guardar_trainer()       
        elif opcion == 9:
            os.system("clear")
            print("Saliendo del programa...")        
            input("Presione Enter para salir...")
            break
    except Exception as Error:
        traceback_info = traceback.format_exc()
        os.system("clear")
        print(f"Excepción atrapada: {Error}")
        print(f"Información de la traza:\n{traceback_info}")
        print("\n---Ingrese nuevamente los datos---\n")
        bandera=True
























