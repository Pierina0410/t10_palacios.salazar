import libreria
def agregar_pais1():
    input("Eliga el pais: ")
    print("Se eligio el pais 1")
def agregar_pais2():
    print("Se eligio el pais 2")
def agregar_pais3():
    print("Se eligio el pais 3")
def agregar_pais4():
    print("Se eligio el pais 4")


def agregar_pais():
    opc=0
    max=5
    while(opc!=max):
        print("## Agregar Pais ##")
        print("# 1. Peru        #")
        print("# 2. Argentina   #")
        print("# 3. Chile       #")
        print("# 4. Colombia    #")
        print("# 5. Salir       #")
        print("##################")
        opc=libreria.pedir_numero("Ingrese opcion", 1,5)
    if (opc==1):
        agregar_pais1()
    if (opc==2):
        agregar_pais2()
    if (opc==3):
        agregar_pais3()
    if (opc==4):
        agregar_pais4()


def agregar_capital():
    opc=0
    max=5
    while(opc!=max):
        print("### sub-menu Capital ###")
        print("# 1. Lima              #")
        print("# 2. Buenos Aires      #")
        print("# 3. Santiago          #")
        print("# 4. Bogota            #")
        print("# 5. Salir             #")
        print("########################")
        opc=libreria.pedir_numero("Ingrese opcion de capital:",1,5)

opc=0
max=3
while(opc!=3):
    print("######### MENU ##########")
    print("# 1. Pais:              #")
    print("# 2. Capital            #")
    print("# 3. salir              #")
    print("#########################")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if(opc==1):
        agregar_pais()
    if(opc==2):
        agregar_capital()

print("fin del programa")
# fin de menu
