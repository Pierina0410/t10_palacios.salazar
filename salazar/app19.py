import libreria
def pedir_fac1():
    print("Se agrego Facultad de Enfermeria")
def pedir_fac2():
    print("Se agrego Facultad de Derecho")
def pedir_fac3():
    print("Se agrego Facultad de Ciencias sociales")

def pedir_u1():
    print("Se agrego universidad 1")
def pedir_u2():
    print("Se agrego universidad 2")
def pedir_u3():
    print("Se agrego universidad 3")


def ingresar_universidad():
    opc=0
    max=4
    while(opc!=max):
        print("###### UNIVERSIDAD #####")
        print("#1. UNPRG              #")
        print("#2. UCV                #")
        print("#3. USS                #")
        print("#4. Salir              #")
        print("########################")
        opc=libreria.pedir_numero("Ingrese Universidad: ", 1,4)

        #Mapeo
        if (opc==1):
            pedir_u1()
        if (opc==2):
            pedir_u2()
        if (opc==3):
            pedir_u3()


def ingresar_facultad():
    opc=0
    max=4
    while(opc!=max):
        print("####### FACULTAD #######")
        print("#1. Enfermeria         #")
        print("#2. Derecho            #")
        print("#3. Ciencias Solciales #")
        print("#4. Salir              #")
        print("########################")
        opc=libreria.pedir_numero("Ingrese facultad: ", 1,4)

        #Mapeo
        if (opc==1):
            pedir_fac1()
        if (opc==2):
            pedir_fac2()
        if (opc==3):
            pedir_fac3()





opc=0
max=3
while(opc!=3):
    print("########### MENU #############")
    print("# 1. Universidad             #")
    print("# 2. Facultad                #")
    print("# 3. salir                   #")
    print("##############################")
    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if(opc==1):
        ingresar_universidad()
    if(opc==2):
        ingresar_facultad()

print("Programa finalizado")
# fin de menu
