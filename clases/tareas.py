from datetime import date

class Tareas:
    def __init__(self):
        #se define unconstructor con dos variables, el ()id sera le contador de registros y tareas el diccionario que almacenara las tareas
        self.__id = 0
        self.__tareas = {}
        
    # se definen cada metodo segun las opciones del menu (crear, modificar tarea, modificar status, listar y eliminar tareas)
    # cada procedimeinto tiene la captura de errores utilisando (try, except)
    #cada procedimeinto rgresa el resultado  el cual sera impreso por pantalla
    def crear_tarea(self, nombre, descripcion):
        try:
            if type(nombre) != str:
                raise ValueError('Error - Nombre no es una Cadena de texto Valida, favor utilice letras o numeros solamente')
            if type(descripcion) != str:
                raise ValueError('Error - Descripcion no es una Cadena de texto Valida, favor utilice letras o numeros solamente')
            self.__id = self.__id + 1
            nueva_tarea = {
                "id" : self.__id,
                "nombre" : nombre,
                "status" : "Pendiente",
                "descripcion" : descripcion,
                "fecha_creacion" : date.today()
            }
            self.__tareas[self.__id]=nueva_tarea
            return('Tarea creada')
        except ValueError as e:
            return str(e)
        
        
    def modificar_tarea(self, id_str, nombre, descripcion):
        try:
            id = int(id_str)
            if not self.__tareas:
                raise ValueError('Error - No hay tareas creadas')
            if type(id) != int or id < 0:
                raise ValueError(f'Error - ID ({id}) ingresado no es valido')
            if id not in self.__tareas:
                raise ValueError(f'Error - ID ({id}) de la Atrea NO existe')
            if type(nombre) != str:
                raise ValueError('Error - Nombre no es una Cadena de texto Valida, favor utilice letras o numeros solamente')
            else:
                self.__tareas[id]['nombre'] = nombre
            if type(descripcion) != str:
                raise ValueError('Error - Descripcion no es una Cadena de texto Valida, favor utilice letras o numeros solamente')
            else:
                self.__tareas[id]['descripcion'] = descripcion
            return('Tarea Modificada correctamente')
        except ValueError as e:
            return str(e)
    
    def status_tarea(self, id_str, status):
        try:
            id = int(id_str)
            if not self.__tareas:
                raise ValueError('Error - No hay tareas creadas')
            if type(id) != int or id < 0:
                raise ValueError(f'Error - ID ({id}) ingresado no es valido')
            if id not in self.__tareas:
                raise ValueError(f'Error - ID ({id}) de la Atrea NO existe')
            if type(status) != str:
                raise ValueError('Error - Status no es una Cadena de texto Valida, favor utilice P, E o T solamente')
            if status != "P" and status != "p" and status != "E" and status != "e" and status != "T" and status != "t":
                raise ValueError(f'Error - Opcion ({status}) de Status no es Valida, favor utilice P, E o T solamente')
            elif status == "P" or status =="p":
                self.__tareas[id]['status'] = "Pendiente"
            elif status == "T" or status =="t":
                self.__tareas[id]['status'] = "Tarminada"
            elif status == "E" or status =="e":
                self.__tareas[id]['status'] = "Ejecutando"
            return('Status Modificada correctamente')
        except ValueError as e:
            return str(e)
        
    def eliminar_tarea(self, id_str):
        try:
            id = int(id_str)
            if not self.__tareas:
                raise ValueError('Error - No hay tareas creadas')
            if type(id) != int or id < 0:
                raise ValueError(f'Error - ID ({id}) ingresado no es valido')
            if id not in self.__tareas:
                raise ValueError(f'Error - ID ({id}) de la Atrea NO existe')
            
            del self.__tareas[id]
            
            return(f"Tarea ({id}) eliminada Correctamente")
        except ValueError as e:
            return str(e)
            
    
    def listar_tareas(self, opcion):
        try:
            if not self.__tareas:
                raise ValueError('Error - No hay tareas creadas')
            if type(opcion) != str:
                raise ValueError('Error - opcion no es una Cadena de texto Valida, favor utilice P, E, T o D solamente')
            if opcion != "P" and opcion != "p" and opcion != "E" and opcion != "e" and opcion != "T" and opcion != "t" and opcion != "D" and opcion != "d":
                raise ValueError(f'Error - Opcion ({opcion}) de opcion no es Valida, favor utilice P, E, T o D solamente')
            elif opcion == "P" or opcion =="p":
                listarPor = "Pendiente"
            elif opcion == "T" or opcion =="t":
                listarPor = "Terminada"
            elif opcion == "E" or opcion =="e":
                listarPor = "Ejecutando"
            elif opcion == "D" or opcion =="d": 
                listarPor = "Todas"                
            
            lista_tareas =[]
            for tarea in self.__tareas.values():
                if listarPor == "Todas":
                    datos_tarea = (
                        f"ID: {tarea['id']}\n"
                        f"Nombre: {tarea['nombre']}\n"
                        f"Estado: {tarea['status']}\n"
                        f"Descripción: {tarea['descripcion']}\n"
                        f"Fecha de Creación: {tarea['fecha_creacion']}\n"
                    )
                    lista_tareas.append(datos_tarea)
                elif tarea["status"] == listarPor:
                    datos_tarea = (
                        f"ID: {tarea['id']}\n"
                        f"Nombre: {tarea['nombre']}\n"
                        f"Estado: {tarea['status']}\n"
                        f"Descripción: {tarea['descripcion']}\n"
                        f"Fecha de Creación: {tarea['fecha_creacion']}\n"
                    )
                    lista_tareas.append(datos_tarea)
            cantidad = len(lista_tareas)
            return f"{'\n'.join(lista_tareas)}\nTotal de tareas: {cantidad}"
        except ValueError as e:
            return str(e)

        

        