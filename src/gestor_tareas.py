def print_menu():
    print("******************************************")
    print("****                                  ****")
    print("*----------- GESTOR DE TAREAS -----------*")
    print("*---------- 1. Mostrar Tareas  ----------*")
    print("*---------- 2. Agregar Tarea  -----------*")
    print("*----3. Marcar Tarea como Completada  ---*")
    print("*---------- 4. Eliminar Tarea  ----------*")
    print("*--------------- 5. Salir ---------------*")
    print("****                                  ****")
    print("******************************************")


def get_tarea():
    tarea = input()
    print(str(tarea))
    for i in range (1, 6):
        if int(tarea) == i:
            return tarea
    return 0

def add_tarea(tareas, tarea, estado):
    tareas[tarea] = estado

print_menu()
tarea = get_tarea()
if tarea == 0:
    print("Opcion incorrecta")

tareas = {}
if 
print(tareas) 

