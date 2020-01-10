import libreria
def pedir_luz ():
    libreria.pedir_infinito("ingrese luz:")
    print("se ingreso luz")
def pedir_estrellas ():
    libreria.pedir_infinito("ingrese estrellas:")
    print("se ingreso estrellas")
def pedir_gases ():
    libreria.pedir_infinito("ingrese gases:")
    print("se ingreso gases")
def pedir_numeros ():
    libreria.pedir_infinito("ingrese numeros:")
    print("se ingreso numeros")
def pedir_energia ():
    libreria.pedir_infinito("ingrese energia:")
    print("se ingreso energia")
def pedir_humanos ():
    libreria.pedir_finitofinito("ingrese humanos:")
    print("se ingreso humanos")
def pedir_agua ():
    libreria.pedir_finitofinito("ingrese agua:")
    print("se ingreso agua")
def pedir_animales ():
    libreria.pedir_finitofinito("ingrese animales")
    print("se ingreso animales")
def pedir_koalas():
    libreria.pedir_finitofinito("ingrese koalas:")
    print("se ingreso koalas")

def agregar_infinito():
    opc=0
    max=6
    while(opc!=max):
        print("#########Menú infinitofinitos##############")
        print("#1.-luz                     #")
        print("#2.-San José                     #")
        print("#3.-gases                    #")
        print("#4.-numeros                     #")
        print("#5.-energia                      #")
        print("#6.-salir                      #")
        opc=libreria.pedir_numero("ingrese opción:",1,6)
    if (opc==1):
        pedir_luz()
    if (opc==2):
         pedir_estrellas()
    if (opc==3):
        pedir_gases()
    if (opc==4):
         pedir_numeros()
    if (opc==5):
         pedir_energia()


def agregar_infinitofinito():
    opc=0
    max=5
    while(opc!=max):
        print("#########Menú infinitofinitos##############")
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
        print("#1.-infinito                     #")
        print("#2.-finito                   #")
        print("#3.-salir                      #")
        opc=libreria.pedir_numero("ingrese opción:",1,3)
        if(opc==1):
            agregar_infinito()
        if(opc==2):
            agregar_infinitofinito()
