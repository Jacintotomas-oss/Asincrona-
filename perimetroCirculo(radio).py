def calcularPerimetroCirculo():
    radio = float(input("ingrese el radio del circulo:"))
    if radio <=0:
     print("el valor ingresado no es valido")
    else:
        perimetro =2*3.1416*radio
        print(f"el perimetro del circulo es: {perimetro}")
        
calcularPerimetroCirculo()