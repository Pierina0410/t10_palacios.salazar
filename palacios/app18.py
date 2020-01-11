import libreria

def pedir_silla1():
    print("Se agrego silla de plastico")
def pedir_silla2():
    print("Se agrego silla de madera")
def pedir_mesa1():
    print("Se agrego mesa de mader")
def pedir_mesa2():
    print("Se agrego mesa de fierro")
#fin_def

def agregar_silla():
    opc=0
    max=3
    while(opc!=max):
        print("##### SILLAS #####")
        print("#1. Plastico     #")
        print("#2. Madera       #")
        print("#3. Salir        #")
        print("##################")
        opc=libreria.pedir_numero("Ingrese tipo de silla: ",1,3)

        #Mapeo de submenu
        if (opc==1):
            pedir_silla1()
        if (opc==2):
            pedir_silla2()


def agregar_mesa():
    opc=0
    max=3
    while(opc!=max):
        print("##### MESAS  #####")
        print("#1. Madera       #")
        print("#2. Fierro       #")
        print("#3. Salir        #")
        print("##################")
        opc=libreria.pedir_numero("Ingrese tipo de mesa: ",1,3)

        #mapeo de sunmenu
        if (opc==1):
            pedir_mesa1()
        if (opc==2):
            pedir_mesa2()
#fin_while

opc=0
max=3
while(opc!=3):
    print("########### MENU #############")
    print("# 1. Silla                   #")
    print("# 2. Mesa                    #")
    print("# 3. salir                   #")
    print("##############################")
#fin_while

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    #Mapeo
    if(opc==1):
        agregar_silla()
    if(opc==2):
        agregar_mesa()

print("Programa finalizado")
# fin_de_menu
