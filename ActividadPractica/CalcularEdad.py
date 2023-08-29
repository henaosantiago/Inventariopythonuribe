ingresar=" Calcular la edad "
print (f'{ingresar:_^90}')


op = 1

while op != 0:
    calcularEdad = int(input(" ----Ingrese la edad de la persona---- "))
    if(calcularEdad > 0 and calcularEdad <= 14):
        print("Niño")
    elif(calcularEdad > 15 and calcularEdad < 28):
        print("Joven")
    elif(calcularEdad >=28 and calcularEdad < 60):
        print("Adulto")
    elif(calcularEdad >= 60 and calcularEdad < 110):
        print("Adulto Mayor")
    else:
        print("El rango de edad es invalido")
    op = int(input("----Ingrese una opcion---- \n1. Ingresar otra edad \n0. salir\n---------------------------------------"))
    

print("Fin del proceso ")