import libreria

def pedir_ulises():
    print("se ingreso ulises")

def pedir_metamorfosis():
    print("se ingreso metamorfosis")

def pedir_movidick():
    print("se ingreso movidick")

def pedir_dracula():
    print("se ingreso dracula")

def pedir_LasPenas():
    print("se ingreso LasPenas")

def pedir_pacoYunque():
    print("se ingreso pacoYunque")

def pedir_matalache():
    print("se ingreso matalache")

def pedir_caballeroCarmelo():
    print("se ingreso caballeroCarmelo")

def pedir_vueloDeLosCondores():
    print("se ingreso vueloDeLosCondores")

def agregar_novela():
    opc=0
    max=6
    while(opc!=max):
        print("#########Menú cuentos #############")
        print("#1.-ulises                        #")
        print("#2.-San José                      #")
        print("#3.-movidick                      #")
        print("#4.-dracula                       #")
        print("#5.-LasPenas                      #")
        print("#6.-salir                         #")
        print("###################################")
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
        print("#1.-pacoYunque                    #")
        print("#2.-matalache                     #")
        print("#3.-caballeroCarmelo              #")
        print("#4.-vueloDeLosCondores            #")
        print("#5.-salir                         #")
        print("###################################")
        opc=libreria.pedir_numero("ingrese opción:",1,5)
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
    print("##########Menú ##################")
    print("#1.-NOVELAS                     #")
    print("#2.-CUENTOS                     #")
    print("#3.-SALIR                       #")
    print("#################################")
    opc=libreria.pedir_numero("ingrese opción:",1,3)
    if(opc==1):
        agregar_novela()
    if(opc==2):
        agregar_cuento()
