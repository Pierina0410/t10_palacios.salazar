import libreria
def pedir_lap1():
    print("Se ingreso laptop #1")
def pedir_lap2():
    print("Se ingreso laptop #2")
def pedir_lap3():
    print("Se ingreso laptop #3")
def pedir_lap4():
    print("Se ingreso laptop #4")

def pedir_pc1():
    print("Se ingreso computadora 1")
def pedir_pc2():
    print("Se ingreso computadora 2")
def pedir_pc3():
    print("Se ingreso computadora 3")
def pedir_pc4():
    print("Se ingreso computadora 4")

def ingrese_laptop():
    opc=0
    max=5
    while (opc!=max):
        print("##### LAPTOPS #####")
        print("#1. lenovo        #")
        print("#2. Aces          #")
        print("#3. Gamer         #")
        print("#4. Apple         #")
        print("#5. Salir         #")
        print("###################")
        opc=libreria.pedir_numero("Ingrese opcion: ",1,5)
        if (opc==1):
            pedir_lap1()
        if (opc==2):
            pedir_lap2()
        if (opc==3):
            pedir_lap3()
        if (opc==4):
            pedir_lap4()

def ingrese_computadora():
    opc=0
    max=5
    while (opc!=max):
        print("##### SUB-MENU #####")
        print("#1. Hp             #")
        print("#2. Sony           #")
        print("#3. Samsung        #")
        print("#4. Lg             #")
        print("#5. Salir          #")
        print("####################")
        opc=libreria.pedir_numero("Ingrese opcion: ", 1,5)
        if (opc==1):
            pedir_pc1()
        if (opc==2):
            pedir_pc2()
        if (opc==3):
            pedir_pc4()


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
