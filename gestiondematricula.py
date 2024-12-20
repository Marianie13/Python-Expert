estudiantes = []
cursos = ['Java', 'Python']
docentes = []
horarios = []
modificar = ['Nombre', 'Curso']
eliminarestudinte = []
cambiodocente = []
modificarhorario = []
estadoSistema = []


#funcion para matricular un estudiante
def matricularEstudiante():
    nombre = input ('Digite el nombre de estudiante: ')
    print ('selecione el curso a matricular: ')
    for i, curso in enumerate(cursos):
        print (f'{i+1}: {curso}') 
    
    cursoSeleccionado = int (input('Ingrese el numero de curso: '))
    if cursoSeleccionado > 0 and cursoSeleccionado <= len(cursos):
         curso = cursos [cursoSeleccionado-1]
         estudiante =  {'nombre':  nombre, 'curso': curso}
         estudiantes.append(estudiante)
         print(f'Estudiante: {nombre}, matriculado en el curso {curso} ')
    else:
        print(f'Opcion de curso no valida, recuerde que solo hay {len(cursos)} cursos ')

#funcion para asignar un docente a un curso
def asignarDocente():
    print('Seleccionar el curso al que desea asiganr un docente ')
    for i, curso in enumerate(cursos):
        print (f'{i+1}: {curso}') 
        
    cursoSeleccionado = int (input('Ingrese el numero de curso: '))
    if cursoSeleccionado > 0 and cursoSeleccionado <= len(cursos):
         curso = cursos [cursoSeleccionado-1] 
         nombreDocente = input('Ingrese el nombre del docente:  ')
         docente =  {'nombre':  nombreDocente, 'curso': curso}
         docentes.append(docente)
         print(f'Docente: {nombreDocente}, asignado en el curso {curso} ')
    else:
        print(f'Opcion de curso no valida, recuerde que solo hay {len(cursos)} cursos ')
        
#TODO Función cambio de docente asignado
def cambioDocente():
    nombre = input('Digite el nombre del docente a modificar : ')
    
    #Buscar el docente en la lista
    for docente in docentes:
        if docente['nombre'] == nombre:
            docente_encontrado = docente
            break
    
    if docente_encontrado:
        print("Seleccione el dato a modificar:")
        print("1: Nombre del docente")
        print("2: Curso asignado")
        opcion_modificar = int(input("Digite el número de la opción a modificar: "))
        
    if opcion_modificar == 1: 
       nuevo_nombre = input ('ingrese el nombre del docente: ')
       docente_encontrado ['nombre'] = nuevo_nombre
       print(f'Información actualizada: Nuevo nombre del docente: {nuevo_nombre}')
    
    elif opcion_modificar == 2:  # Modificar el curso asignado
            print("Seleccione el nuevo curso para el docente:")
            for i, curso in enumerate(cursos):
                print(f'{i+1}: {curso}')
            
            nuevo_curso = int(input("Digite el número del curso: "))
            if 0 < nuevo_curso <= len(cursos):
                docente_encontrado['curso'] = cursos[nuevo_curso - 1]
                print(f"Información actualizada: Docente {nombre}, nuevo curso asignado: {docente_encontrado['curso']}")
            else:
                print(f"Opción de curso no válida, recuerde que solo hay {len(cursos)} cursos")
    else:
        print("Docente no encontrado.")
       
#Función para asignar horario a un curso 
def asignarHorario():
    print('Seleccionar el curso al que desea asignar un horario')
    for i, curso in enumerate(cursos):
        print (f'{i+1}: {curso}') 
    
    cursoSeleccionado = int (input('Ingrese el numero de curso: '))
    if cursoSeleccionado > 0 and cursoSeleccionado <= len(cursos):
         curso = cursos [cursoSeleccionado-1]
         días = input ('Ingrese los días de clase (ej: martes y jueves): ')
         hora = input ('Ingrese la hora de la clase (ej: 6 pm ) ')
         horario = { 'curso': curso, 'días': días, 'hora': hora}
         horarios.append(horario)
         print(f'Horario asignado al curso:  {curso}, {días} a las {hora} ')
    else: 
        print(f'Opcion de curso no valida, recuerde que solo hay {len(cursos)} cursos ')

#TODO función modificación de horarios de clase

def modificarhorario():
    nombre = input('Digite el curso de cambio de horario: ')
    for i, curso in enumerate(cursos):
        print(f"{i+1}: {curso}")
        
    cursoSeleccionado = int(input("Ingrese el número del curso: "))
    if 0 < cursoSeleccionado <= len(cursos):
        curso = cursos[cursoSeleccionado - 1]
        
        horario_encontrado = None
        for horario in horarios:
            if horario['curso'] == curso:
                horario_encontrado = horario
                break
        
        if horario_encontrado:
            print("Seleccione el dato a modificar:")
            print("1: Días")
            print("2: Hora")
            
        opcion_modificar = int(input("Digite el número de la opción a modificar: "))

        if opcion_modificar == 1:  # Modificar los días
                nuevos_dias = input("Ingrese los nuevos días de clase (ej: lunes y miércoles): ")
                horario_encontrado['días'] = nuevos_dias
                print(f"Información actualizada: Días del curso {curso}: {nuevos_dias}")

        elif opcion_modificar == 2:  # Modificar la hora
                nueva_hora = input("Ingrese la nueva hora de la clase (ej: 7 pm): ")
                horario_encontrado['hora'] = nueva_hora
                print(f"Información actualizada: Hora del curso {curso}: {nueva_hora}")

        else:
                print("Opción no válida.")
                  
#TODO Función para editar un estudiante matriculado
def modificarEstudiante():
    nombre = input('Digite el nombre de estudiante: ')
    estudiante_encontrado = None
    
    # Buscar el estudiante en la lista de matriculados 
    for estudiante in estudiantes:
        if estudiante['nombre'] == nombre:
            estudiante_encontrado = estudiante
            break
    
    # Estudiante encontrado 
    if estudiante_encontrado:
        print("Seleccione el dato a modificar:")
        for i, opcion in enumerate(modificar):
            print(f'{i+1}: {opcion}')
        
        # Mostrar las opciones a modificar 
        opcion_modificar = int(input("Digite el número de la opción a modificar: "))
        
        if opcion_modificar == 1:  # Modificar el nombre
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            estudiante_encontrado['nombre'] = nuevo_nombre
            print(f"Información actualizada: Nuevo nombre del estudiante: {nuevo_nombre}")
        
        elif opcion_modificar == 2:  # Modificar el curso
            print("Seleccione el nuevo curso del estudiante:")
            for i, curso in enumerate(cursos):
                print(f'{i+1}: {curso}')
            
            nuevo_curso = int(input('Digite el número del curso: '))
            if 0 < nuevo_curso <= len(cursos):
                estudiante_encontrado['curso'] = cursos[nuevo_curso - 1]
                print(f"Información actualizada: Estudiante {nombre}, nuevo curso: {estudiante_encontrado['curso']}")
            else:
                print(f"Opción de curso no válida, recuerde que solo hay {len(cursos)} cursos")
    else:
        print("Estudiante no encontrado.")

#TODO Funcion para eliminar astudiante

def eliminarEstudiante():
    nombre = input('Digite el nombre del estudiante a eliminar: ')
    estudiante_encontrado = None
    
    #Buscar el estudiante en la lista de matriculados 
    for estudiante in estudiantes:
        if estudiante['nombre'] == nombre:
            estudiante_encontrado = estudiante
            break
    
    #Eliminar el estudiante
    if estudiante_encontrado:
        estudiantes.remove(estudiante_encontrado)
        print(f'Estudiante {nombre} eliminado exitosamente.')
    else:
        print('Estudiante no encontrado.')
        
#TODO Funcion mostar el estado del sistema 
def estadoSistema():
    print("\n=== Estado Completo del Sistema ===")
    
    # Mostrar estudiantes matriculados
    print("\nEstudiantes Matriculados:")
    if estudiantes:
        for estudiante in estudiantes:
            print(f"- Nombre: {estudiante['nombre']}, Curso: {estudiante['curso']}")
    else:
        print("No hay estudiantes matriculados.")
    
    # Mostrar docentes asignados
    print("\nDocentes Asignados:")
    if docentes:
        for docente in docentes:
            print(f"- Nombre: {docente['nombre']}, Curso: {docente['curso']}")
    else:
        print("No hay docentes asignados.")
    
    # Mostrar horarios asignados
    print("\nHorarios de los Cursos:")
    if horarios:
        for horario in horarios:
            print(f"- Curso: {horario['curso']}, Días: {horario['días']}, Hora: {horario['hora']}")
    else:
        print("No hay horarios asignados.")
    
    print("\n===================================\n")
   
#mostrar  estudiante             
def mostrarEstudiantes():
    if estudiantes:
        print ('Lista de estuantes matriculados')
        for estudiante in estudiantes:
            print(f'Estudiante: {estudiante['nombre']} Curso: {estudiante['curso']}')
    else:
        print('no hay estudiantes matriculados')
        
def mostrarDocentes():
    if docentes:
        print ('Lista de docenetes asigandos')
        for docente in docentes:
            print(f'Docentes: {docente['nombre']} Curso: {docente['curso']}')
    else:
        print('no hay docentes asiganados')
        
def mostrarHorarios():
    if horarios:
        print ('\n horarios de los cursos')
        for horario in horarios:
            print(f'curso: {horario['curso']} Días: {horario['días']}, Hora: {horario['hora']}')
    else:
        print('no hay horarios asignados')
        
while True:
    print('\n Sistema de matricula de Dev Senior')
    print('1. Matricular estudiante') 
    print('2. Asignar docente a un curso')
    print('3. Asignar horario a un curso')
    print('4. Mostrar la lista de estuantes matriculados')
    print('5. Mostrar la lista de docentes asigandos')
    print('6. Mostrar horarios de los cursos')
    print('7. Modificar horarios de curso')
    print('8. Modificar información de un estudiante')
    print('9. Cambio docente asignado')
    print('10. Eliminar estudiante')
    print('11. Mostrar el estado del sistema')
    print('12. Salir')
    
    opcion = int(input ('digite la opcion: '))
    
    if opcion == 1:
        matricularEstudiante()
    elif opcion ==2: 
        asignarDocente()
    elif opcion ==3: 
        asignarHorario()
    elif opcion ==4: 
        mostrarEstudiantes()
    elif opcion ==5: 
        mostrarDocentes()
    elif opcion ==6: 
        mostrarHorarios()
    elif opcion ==7: 
        modificarhorario()
    elif opcion ==8: 
        modificarEstudiante()
    elif opcion ==9: 
        cambioDocente()
    elif opcion ==10: 
        eliminarEstudiante()
    elif opcion ==11: 
        estadoSistema()
    elif opcion ==12: 
        print('Gracias por usar el sistema de matriculas de dev senior ')
        break
    else:
        print('Opcion no valida, intente de nuevo')
        
        
       
    

        
        
         
            
        
        
    
        
         
        
        
    
        
        
    
         
    
    
         
        
         
         
         
        
    
        