#se importa la clase Tareas del directorio atreas
from clases.tareas import Tareas
#se crea el objeto tarea
tareas = Tareas()

# se declara la variable (ciclo) en true, la cual servira com yyave para entrar o salir del ciclo whiel
ciclo = True
while ciclo:
# se pinta le menu de opciones
    print('')
    print('')
    print('Bienvenidos a Gesta - Gestion de Tareas ')
    print('Seleccione una opcion 1,2,3,4,5,0 del Menu')
    print('1- Crear Tarea')
    print('2- Modificar ')
    print('3- Modificar Status ')
    print('4- Listar Tareas')
    print('5- Eliminar Tarea')
    print('0- Salir del Sistema')
# se acepta entrada de teclado la opcion a ajecuar
    opcion = input('Indique su opción : ')
# se determina que opcion se selecciono y se procede a jetar los procesoso de la misma
# se capturan los datos que se requieran para ejecutar el procedimeinto selecionado
# se llama al procedimeinto y luego se imprime el resultado 
    if opcion == '1':
        print('')
        print('')
        print('Introdusca los datos de la tarea a CREAR')
        nombre = input('Nombre de la Tarea : ')
        descripcion = input('Descripción de la Tarea : ')
        resultado = tareas.crear_tarea(nombre, descripcion)
        print('')
        
        print(resultado)
    elif opcion == '2':
        print('')
        print('')
        print('Introdusca los datos de la tarea a MODIFICAR')
        id = input('ID de la Tarea a modificar : ')
        nombre = input('Nombre de la Tarea : ')
        descripcion = input('Descripción de la Tarea : ')
        resultado = tareas.modificar_tarea(id, nombre, descripcion)
        print('')
        print(resultado)
    elif opcion == '3':
        print('')
        print('')
        print('Introdusca el Id y el Status de la tarea a MODIFICAR')
        id = input('ID de la Tarea a modificar : ')
        status = input('Status : (P)endiente, (E)jecutando (T)erminada : ')
        resultado = tareas.status_tarea(id, status)
        print('')
        print(resultado)        
    elif opcion == '4':
        print('')
        print('')        
        print('Lista de las Tareas ')
        opcion = input('Listar las Tareas (P)endiente, (E)jecutando, (T)erminada, To(d)as : ')
        resultado = tareas.listar_tareas(opcion)
        print('')
        print(resultado)
    elif opcion == '5':
        print('')
        print('')
        print('Introdusca los datos de la tarea a ELIMINAR')
        id = input('ID de la Tarea a modificar : ')
        resultado = tareas.eliminar_tarea(id)
        print('')
        print(resultado)
    elif opcion == '0':
        print('')
        print('')
        print('Hasta la próxima')
        ciclo = False
    else:
        print('')
        print('')
        print('Opcion Invalida, Intente de nuevo, Gracias ')
    
    
    