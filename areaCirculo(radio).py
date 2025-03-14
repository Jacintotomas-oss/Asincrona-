def CalcularAreaCirculo():
    radio = float(input("ingrese el radio del circulo:"))
    if radio <= 0:
        print("El valor ingresado no es valido")  
    else:
        area = 3.1416 * radio**2
    print(f"el area encontraa es {area}")

     
CalcularAreaCirculo()