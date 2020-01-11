import libreria
def pedir_florida():
    libreria.pedir_estadoEEUU("ingrese estadoEEUU:")
    print("Se ingreso la estadoEEUU")

def pedir_california():
    print("Se agreo la california")
def pedir_texas():
    print("se agrego texas")

def pedir_buriatia():
    libreria.pedir_estadorusia("Ingrese estadorusia:")
    print("se agrego buriatia")
def pedir_bascortostan():
    print("se agrego el bascortostan")
def pedir_Altai():
    print("Se agrego Altai")
def pedir_kalmukia():
    print("se agrego kalmukia")

def agregar_estadoEEUU():
    opc=0
    max=4
    while(opc!=max):
       print("##### menu-estadosEEUU #####")
       print("# 1.- florida         #")
       print("# 2.- california           #")
       print("# 3.- texas       #")
       print("# 4.-salir            #")
       print("#######################")
       opc=libreria.pedir_numero("ingrese opcion:",1,4)

       if(opc==1):
           pedir_florida()
       if(opc==2):
           pedir_california()
       if(opc==3):
           pedir_texas()

def agregar_estadorusia():
    opc=0
    max=5
    while(opc!=max):
       print("####sub-menu-estadosrusia####")
       print("# 1.- buriatia              #")
       print("# 2.- bascortostan           #")
       print("# 3.- Altai          #")
       print("# 4.- kalmukia         #")
       print("# 5.- salir             #")
       print("#########################")
       opc=libreria.pedir_numero("ingrese opcion:",1,5)

       if(opc==1):
            pedir_buriatia()
       if(opc==2):
            pedir_bascortostan()
       if(opc==3):
            pedir_Altai()
       if(opc==4):
            pedir_kalmukia()


opc=0
max=3
while(opc!=max):
    print("########### MENU #############")
    print("# 1. estadoEEUU                   #")
    print("# 2. estadorusia                 #")
    print("# 3. salir                   #")
    print("##############################")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if(opc==1):
        agregar_estadoEEUU()
    if(opc==2):
        agregar_estadorusia()

print("Programa finalizado")
# fin de menu
