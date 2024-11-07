#codificacion cammel case
# 1.5 float  35 int Maria = Str

ventasTotales = 0.0 

#solicitar el numero de producos
numProductos = int(input("Ingrese el numero a gestionar"))


#listas para almacenar una informacion 
nombres = [ ]
precios = [ ]
cantidades = [ ]

print ("ingreso incial de productos a la tienda:")
for i in range (numProductos): 
  print (f'producto {i+1}: ')
  nombre = input ('ingrese el nombre del producto: ').lower()
  nombres.append(nombre)
  precio = float (input ('ingrese el pecio del producto: '))
  precios.append(precio)
  cantidad = int (input ('Digite la cantidad del produto: '))
  cantidades.append(cantidad)
 
#ciclo primicipal menu 
while True: 
    print('\n ---MENU DE GESTIÓN DROGERIA---')
    print('1. Vender Producto')
    print('2. Mostrar inventario')
    print('3. Mostrar Ventas Totales')
    print('4. Salir')
    opcion = int(input('ingrese una opción: '))

if opcion == 1:
    print('\nVender Producto')
    nombreVenta = input('Ingrese el nombre del producto a vender ').lower()
    cantidadVender = int(input('Ingrese la cantidad a vender: '))
    productoEncontrado = False
    
    for i in range(len(nombres)):
        if nombres [i] == nombreVenta:
            productoEncontrado = True
            if cantidadVender <= cantidades[i]:
                totalVenta = cantidadVender * precios[i]
                ventasTotales += totalVenta
                cantidades[i] -= cantidadVender
                print(f'venta realizada. total de esta venta ${totalVenta:.2f}')
                print(f'Quedan {cantidades[i]} unidades de {nombres[i]} en el inventario')
                
            else:
                print(f'cantidad insuficiente en el inventaro. ya que en stock solo tenemos {cantidades[i]}')
            break
        
if not productoEncontrado:
    print('producto no encotrado en el invetario')
       
elif opcion == 2:
    print('\nInvetrio de Productos')
    for i in range (len(nombres)):
     print(f'Producto {i+1}: {nombres[i].capitalize()}, Precio: ${precios[i]:.2f}, Cantidad: {cantidades[i]}')
            
elif opcion ==3:
    print(f'\nVentas Totales acumuladas: ${ventasTotales: .2f}')
        
elif opcion ==4:
    print('\nGracias por usar el sistema de gestión drogeria dev senior ')
       
    
else:
    print('\nOpcion invalidad. Ingresar entre (1-4)')
        
        
              
        
            
         
       
                
                
                
                
                
                
            
            
         
        
    
    
    

        