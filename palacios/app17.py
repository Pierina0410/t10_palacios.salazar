import libreria

def pedir_botella1():
    print("Se agrego botella de plastico")
def pedir_botella2():
    print("Se agrego botella de madera")
def pedir_caja1():
    print("Se agrego caja de mader")
def pedir_caja2():
    print("Se agrego caja de fierro")
#fin_def

def agregar_botella():
    opc=0
    max=3
    while(opc!=max):
        print("##### botellaS #####")
        print("#1. Plastico     #")
        print("#2. Madera       #")
        print("#3. Salir        #")
        print("##################")
        opc=libreria.pedir_numero("Ingrese tipo de botella: ",1,3)

        #Mapeo de submenu
        if (opc==1):
            pedir_botella1()
        if (opc==2):
            pedir_botella2()


def agregar_caja():
    opc=0
    max=3
    while(opc!=max):
        print("##### cajaS  #####")
        print("#1. Madera       #")
        print("#2. Fierro       #")
        print("#3. Salir        #")
        print("##################")
        opc=libreria.pedir_numero("Ingrese tipo de caja: ",1,3)

        #mapeo de sunmenu
        if (opc==1):
            pedir_caja1()
        if (opc==2):
            pedir_caja2()
#fin_while

opc=0
max=3
while(opc!=3):
    print("########### MENU #############")
    print("# 1. botella                   #")
    print("# 2. caja                    #")
    print("# 3. salir                   #")
    print("##############################")
#fin_while

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    #Mapeo
    if(opc==1):
        agregar_botella()
    if(opc==2):
        agregar_caja()

print("Programa finalizado")
# fin_de_menu
