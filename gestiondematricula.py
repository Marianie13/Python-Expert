estudiantes = []
cursos = ['Java', 'Python']
docentes = []
horarios = []

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
    print('7. Salir')
    
    opcion = int(input ('digite la opcion: '))
    
    if opcion == 1:
        
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
        print('Gracias por usar el sistema de matriculas de dev senior ')
        break
    else:
        print('Opcion no valida, intente de nuevo')
        
      #Devo hacer una mejoras que estas en el grupo se discor   
    

        
        
         
            
        
        
    
        
         
        
        
    
        
        
    
         
    
    
         
        
         
         
         
        
    
        