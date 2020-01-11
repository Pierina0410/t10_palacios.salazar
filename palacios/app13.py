import libreria
def pedir_ins1():
    print("Se agrego instituto 1")
def pedir_ins2():
    print("Se agrego instituto 2")

def pedir_u1():
    print("Se agrego universidad 1")
def pedir_u2():
    print("Se agrego universidad 2")


def agregar_inst():
    opc=0
    max=3
    while(opc!=max):
        print("##### INSTITUTOS  ######")
        print("#1. J.M.B              #")
        print("#2. FEDERAL ALEMANA    #")
        print("#3. Salir              #")
        print("########################")
        opc=libreria.pedir_numero("Ingrese Instituto:",1,3)
        if(opc==1):
            pedir_ins1()
        if(opc==2):
            pedir_ins2()

def agregar_uni():
    opc=0
    max=3
    while(opc!=max):
        print("##### UNIVERSIDAD ######")
        print("#1. USS                #")
        print("#2. USMP               #")
        print("#3. Salir              #")
        print("########################")
        opc=libreria.pedir_numero("Ingrese universidad:",1,3)
        if(opc==1):
            pedir_u1()
        if(opc==2):
            pedir_u2()
opc=0
max=3
while(opc!=max):

    print("#########Menú ##################")
    print("#1.-universidad                #")
    print("#2.-instituto                  #")
    print("#3.-salir                      #")
    print("################################")
    opc=libreria.pedir_numero("ingrese opción:",1,3)
    if(opc==1):
        agregar_uni()
    if(opc==2):
        agregar_inst()
