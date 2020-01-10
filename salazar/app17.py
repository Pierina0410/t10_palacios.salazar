import libreria
def pedir_ceme1():
    print("Se ingreso la marca Pacasmayo")
def pedir_ceme2():
    print("Se ingreso la marca Forte")
def pedir_ceme3():
    print("Se ingreso la marca Apu")

def pedir_fierro1():
    print("Se ingreso fierro 1/4")
def pedir_fierro2():
    print("Se ingreso fierro 1/8")
def pedir_fierro3():
    print("Se ingreso fierro 1/2")

def agregar_cemento():
    opc=0
    max=4
    while(opc!=max):
        print("##### CEMENTO #####")
        print("#1. Pacasmayo     #")
        print("#2. Forte         #")
        print("#3. Apu           #"
        print("#4. Salir         #")
        print("###################")
        opc=libreria.pedir_numero("Ingrese opcion del cemento: ", 1,4)
        if (opc==1):
            pedir_ceme1()
        if (opc==2):
            pedir_ceme2()
        if (opc==3):
            pedir_ceme3()

def agregar_fierro():
    opc=0
    max=4
    while(opc!=max):
        print("##### FIERROS #####")
        print("#1. fierro 1/4    #")
        print("#2. fierro 1/8    #")
        print("#3. fierro 1/2    #")
        print("#4. Salir         #")
        print("###################")
        opc=libreria.pedir_numero("Ingrese opcion del fierro: ", 1,4)
        if (opc==1):
            pedir_fierro1()
        if (opc==2):
            pedir_fierro2()
        if (opc==3):
            pedir_fierro3()


opc=0
max=3
while(opc!=3):
    print("########### MENU #############")
    print("# 1. Cemento                 #")
    print("# 2. Fierro                  #")
    print("# 3. salir                   #")
    print("##############################")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if(opc==1):
        agregar_cemento()
    if(opc==2):
        agregar_fierro()

print("Programa finalizado")
# fin de menu
