print("¡Bienvenido al Gestor de Tareas!")

def agregar_tarea():
    tarea = input("\nEscribe una nueva tarea: ")
    with open("tareas.txt", "a") as archivo:
        archivo.write(tarea + "\n")
    print("Tarea guardada.")

def ver_tareas():
    print("\n--- Lista de Tareas ---")
    try:
        with open("tareas.txt", "r") as archivo:
            print(archivo.read())
    except FileNotFoundError:
        print("No hay tareas aún.")

while True:
    print("\nOpciones:")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Salir")
    
    opcion = input("Selecciona una opción (1-3): ")
    
    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        ver_tareas()
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intenta de nuevo.")