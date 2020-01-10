import libreria
def ingrese_laptop():
    libreria.pedir_nombre("ingrese nombre de laptop:")
    print("se ingreso nombre de laptop")
def ingrese_computadora():
    libreria.pedir_nombre("ingrese nombre de computadora:")
    print("se ingreso nombre de computadora")

opc=0
max=3
while(opc!=max):
    print("###### MENU #######")
    print("# 1. Laptop       #")
    print("# 2. Computadora  #")
    print("# 3. Salir        #")
    print("###################")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)


    if(opc==1):
        ingrese_laptop()
    if(opc==2):
        ingrese_computadora()
print("fin del programa")
