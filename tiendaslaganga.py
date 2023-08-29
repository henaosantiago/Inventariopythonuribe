#MENU DE OPCIONES
#1.Ingresar producto bodega
#2. Verificar los productos en bodega
#3. Buscar un producto en la bodega 
#4. Editar un producto en la bodega
#5. Retirar un producto bodega 
#6. Salir
#producto : nombre , codigo , decripcion , foto , precio , cantidadEnbodega,fechaEntradaBodega

opcion=0
print ("TIENDA EL GANGAZO")
print("**********************")
print("1.Ingresar producto bodega")
print("2. Verificar los productos en bodega")
print("3. Buscar un producto en la bodega" )
print("4. Editar un producto en la bodega")
print("5. Retirar un producto bodega" )
print("6. Salir")
print("**********************")

productos =[]
while (opcion !=6):
    producto= {}
    opcion=int (input("Digita la opcion deseada: "))
    if opcion==1:
        producto["nombre"]=input("digita el nombre del producto: ")
        producto["codigo"]=int(input("digita el codigo del producto: "))
        producto["descripcion"]=input("digita el descripcion del producto: ")
        producto["foto"]=input("digita el foto del producto: ")
        producto["precio"]=input("digita el precio del producto: ")
        producto["stock"]=int(input("digita el stock del producto: "))
        producto["fechaEntradaBodega"]=input("digita la fecha de entrada: ")

        productos.append(producto)



    elif opcion==2:
        for  productosSeleccionado in productos:
            print(f"codigo={productosSeleccionado['codigo']}")
            print(f"nombre={productosSeleccionado['nombre']}")
            print(f"descripcion={productosSeleccionado['descripcion']}")
            print(f"foto={productosSeleccionado['foto']}")
            print(f"cantidad de en bodega={productosSeleccionado['stock']}")
            print(f"fecha de entrada ={productosSeleccionado['fechaEntradaBodega']}\n")

    elif opcion==3:
        pass
    elif opcion==4:
        pass
    elif opcion==5:
        pass
    elif opcion==6:
        pass
    else:
        print("Opcion invalida , vuelva a intentarlo")

