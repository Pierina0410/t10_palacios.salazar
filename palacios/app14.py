import libreria
def pedir_ulises ():
    libreria.pedir_novela("ingrese ulises:")
    print("se ingreso ulises")
def pedir_metamorfosis ():
    libreria.pedir_novela("ingrese metamorfosis:")
    print("se ingreso metamorfosis")
def pedir_movidick ():
    libreria.pedir_novela("ingrese movidick:")
    print("se ingreso movidick")
def pedir_dracula ():
    libreria.pedir_novela("ingrese dracula:")
    print("se ingreso dracula")
def pedir_LasPenas ():
    libreria.pedir_novela("ingrese LasPenas:")
    print("se ingreso LasPenas")
def pedir_pacoYunque ():
    libreria.pedir_cuento("ingrese pacoYunque:")
    print("se ingreso pacoYunque")
def pedir_matalache ():
    libreria.pedir_cuento("ingrese matalache:")
    print("se ingreso matalache")
def pedir_caballeroCarmelo ():
    libreria.pedir_cuento("ingrese caballeroCarmelo")
    print("se ingreso caballeroCarmelo")
def pedir_vueloDeLosCondores():
    libreria.pedir_cuento("ingrese vueloDeLosCondores:")
    print("se ingreso vueloDeLosCondores")

def agregar_novela():
    opc=0
    max=6
    while(opc!=max):
        print("#########Menú cuentos##############")
        print("#1.-ulises                     #")
        print("#2.-San José                     #")
        print("#3.-movidick                    #")
        print("#4.-dracula                     #")
        print("#5.-LasPenas                      #")
        print("#6.-salir                      #")
        opc=libreria.pedir_numero("ingrese opción:",1,6)
    if (opc==1):
        pedir_ulises()
    if (opc==2):
         pedir_metamorfosis()
    if (opc==3):
        pedir_movidick()
    if (opc==4):
         pedir_dracula()
    if (opc==5):
         pedir_LasPenas()


def agregar_cuento():
    opc=0
    max=5
    while(opc!=max):
        print("#########Menú cuentos##############")
        print("#1.-pacoYunque                   #")
        print("#2.-matalache                      #")
        print("#3.-caballeroCarmelo                      #")
        print("#4.-vueloDeLosCondores                     #")
        print("#5.-salir                      #")
        opc=libreria.pedir_numero("ingrese opción:",1,6)
    if (opc==1):
        pedir_pacoYunque()
    if (opc==2):
         pedir_matalache()
    if (opc==3):
        pedir_caballeroCarmelo()
    if (opc==4):
         pedir_vueloDeLosCondores()
opc=0
max=3
while(opc!=max):
        print("#########Menú ##################")
        print("#1.-Frutas                     #")
        print("#2.-verduras                   #")
        print("#3.-salir                      #")
        opc=libreria.pedir_numero("ingrese opción:",1,3)
        if(opc==1):
            agregar_novela()
        if(opc==2):
            agregar_cuento()
