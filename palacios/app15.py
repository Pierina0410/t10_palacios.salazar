import libreria
def pedir_sandia ():
    libreria.pedir_frutas("ingrese sandia:")
    print("se ingreso sandia")
def pedir_papaya ():
    libreria.pedir_frutas("ingrese papaya:")
    print("se ingreso papaya")
def pedir_melon ():
    libreria.pedir_frutas("ingrese melon:")
    print("se ingreso melon")
def pedir_naranja ():
    libreria.pedir_frutas("ingrese naranja:")
    print("se ingreso naranja")
def pedir_platano ():
    libreria.pedir_frutas("ingrese platano:")
    print("se ingreso platano")
def pedir_zapallo ():
    libreria.pedir_verduras("ingrese zapallo:")
    print("se ingreso zapallo")
def pedir_loche ():
    libreria.pedir_verduras("ingrese loche:")
    print("se ingreso loche")
def pedir_brocoli ():
    libreria.pedir_verduras("ingrese brocoli")
    print("se ingreso brocoli")
def pedir_cebolla():
    libreria.pedir_verduras("ingrese cebolla:")
    print("se ingreso cebolla")

def agregar_frutas():
    opc=0
    max=6
    while(opc!=max):
        print("#########Menú verdurass##############")
        print("#1.-sandia                     #")
        print("#2.-San José                     #")
        print("#3.-melon                    #")
        print("#4.-naranja                     #")
        print("#5.-platano                      #")
        print("#6.-salir                      #")
        opc=libreria.pedir_numero("ingrese opción:",1,6)
    if (opc==1):
        pedir_sandia()
    if (opc==2):
         pedir_papaya()
    if (opc==3):
        pedir_melon()
    if (opc==4):
         pedir_naranja()
    if (opc==5):
         pedir_platano()


def agregar_verduras():
    opc=0
    max=5
    while(opc!=max):
        print("#########Menú verdurass##############")
        print("#1.-zapallo                   #")
        print("#2.-loche                      #")
        print("#3.-brocoli                      #")
        print("#4.-cebolla                     #")
        print("#5.-salir                      #")
        opc=libreria.pedir_numero("ingrese opción:",1,6)
    if (opc==1):
        pedir_zapallo()
    if (opc==2):
         pedir_loche()
    if (opc==3):
        pedir_brocoli()
    if (opc==4):
         pedir_cebolla()
opc=0
max=3
while(opc!=max):
        print("#########Menú ##################")
        print("#1.-Frutas                     #")
        print("#2.-verduras                   #")
        print("#3.-salir                      #")
        opc=libreria.pedir_numero("ingrese opción:",1,3)
        if(opc==1):
            agregar_frutas()
        if(opc==2):
            agregar_verduras()
