import libreria
def pedir_elasticidad():
    libreria.pedir_intensivas("ingrese intensivas:")
    print("Se ingreso la intensivas")

def pedir_velocidad():
    print("Se agreo la velocidad")
def pedir_temperatura():
    print("se agrego temperatura")

def pedir_peso():
    libreria.pedir_estadorusia("Ingrese estadorusia:")
    print("se agrego peso")
def pedir_fuerza():
    print("se agrego el fuerza")
def pedir_volumen():
    print("Se agrego volumen")
def pedir_longitud():
    print("se agrego longitud")

def agregar_intensivas():
    opc=0
    max=4
    while(opc!=max):
       print("##### menu-intensivas #####")
       print("# 1.- elasticidad         #")
       print("# 2.- velocidad           #")
       print("# 3.- temperatura       #")
       print("# 4.-salir            #")
       print("#######################")
       opc=libreria.pedir_numero("ingrese opcion:",1,4)

       if(opc==1):
           pedir_elasticidad()
       if(opc==2):
           pedir_velocidad()
       if(opc==3):
           pedir_temperatura()

def agregar_estadorusia():
    opc=0
    max=5
    while(opc!=max):
       print("####sub-menu-extensivas####")
       print("# 1.- peso              #")
       print("# 2.- fuerza           #")
       print("# 3.- volumen          #")
       print("# 4.- longitud         #")
       print("# 5.- salir             #")
       print("#########################")
       opc=libreria.pedir_numero("ingrese opcion:",1,5)

       if(opc==1):
            pedir_peso()
       if(opc==2):
            pedir_fuerza()
       if(opc==3):
            pedir_volumen()
       if(opc==4):
            pedir_longitud()


opc=0
max=3
while(opc!=max):
    print("########### MENU #############")
    print("# 1. intensivas                   #")
    print("# 2. estadorusia                 #")
    print("# 3. salir                   #")
    print("##############################")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if(opc==1):
        agregar_intensivas()
    if(opc==2):
        agregar_estadorusia()

print("Programa finalizado")
# fin de menu
