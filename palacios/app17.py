import libreria
def pedir_pitbull ():
    libreria.pedir_perros("ingrese pitbull:")
    print("se ingreso pitbull")
def pedir_labrador ():
    libreria.pedir_perros("ingrese labrador:")
    print("se ingreso labrador")
def pedir_gases ():
    libreria.pedir_perros("ingrese gases:")
    print("se ingreso gases")
def pedir_viquingo ():
    libreria.pedir_perros("ingrese viquingo:")
    print("se ingreso viquingo")
def pedir_piquines ():
    libreria.pedir_perros("ingrese piquines:")
    print("se ingreso piquines")
def pedir_humanos ():
    libreria.pedir_gatosgatos("ingrese humanos:")
    print("se ingreso humanos")
def pedir_agua ():
    libreria.pedir_gatosgatos("ingrese agua:")
    print("se ingreso agua")
def pedir_animales ():
    libreria.pedir_gatosgatos("ingrese animales")
    print("se ingreso animales")
def pedir_koalas():
    libreria.pedir_gatos("ingrese koalas:")
    print("se ingreso koalas")

def agregar_igatos():
    opc=0
    max=6
    while(opc!=max):
        print("#########Menú ##############")
        print("#1.-pitbull                     #")
        print("#2.-San José                     #")
        print("#3.-gases                    #")
        print("#4.-viquingo                     #")
        print("#5.-piquines                      #")
        print("#6.-salir                      #")
        opc=libreria.pedir_numero("ingrese opción:",1,6)
    if (opc==1):
        pedir_pitbull()
    if (opc==2):
         pedir_labrador()
    if (opc==3):
        pedir_gases()
    if (opc==4):
         pedir_viquingo()
    if (opc==5):
         pedir_piquines()


def agregar_perrosgatos():
    opc=0
    max=5
    while(opc!=max):
        print("#########Menú perrosgatoss##############")
        print("#1.-humanos                   #")
        print("#2.-agua                      #")
        print("#3.-animales                      #")
        print("#4.-koalas                     #")
        print("#5.-salir                      #")
        opc=libreria.pedir_numero("ingrese opción:",1,6)
    if (opc==1):
        pedir_humanos()
    if (opc==2):
         pedir_agua()
    if (opc==3):
        pedir_animales()
    if (opc==4):
         pedir_koalas()
opc=0
max=3
while(opc!=max):
        print("#########Menú ##################")
        print("#1.-perros                     #")
        print("#2.-gatos                   #")
        print("#3.-salir                      #")
        opc=libreria.pedir_numero("ingrese opción:",1,3)
        if(opc==1):
            agregar_perros()
        if(opc==2):
            agregar_gatos()
