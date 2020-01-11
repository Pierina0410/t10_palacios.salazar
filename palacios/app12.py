import libreria

def pedir_luna():
    print("se ingreso luna")

def pedir_calisto():
    print("se ingreso calisto")

def pedir_sinope():
    print("se ingreso las sinope")

def pedir_caronte():
    print("se ingreso caronte")

def pedir_tierra():
    print("se ingreso tierra")

def pedir_jupiter():
    print("se ingreso jupiter")

def pedir_marte():
    print("se ingreso marte")

def pedir_venus():
    print("se ingreso venus")

def agregar_satelite():
    opc=0
    max=5
    while(opc!=max):
        print("#########Menú satelites##############")
        print("#1.-luna                            #")
        print("#2.-calisto                         #")
        print("#3.-sinope                          #")
        print("#4.-caronte                         #")
        print("#5.-salir                           #")
        print("#####################################")
        opc=libreria.pedir_numero("ingrese opción:",1,5)
        if (opc==1):
            pedir_luna()
        if (opc==2):
            pedir_calisto()
        if (opc==3):
            pedir_sinope()
        if (opc==4):
            pedir_caronte()



def agregar_planeta():
    opc=0
    max=5
    while(opc!=max):
        print("######### planetas ##############")
        print("#1.-tierra                         #")
        print("#2.-jupiter                        #")
        print("#3.-marte                          #")
        print("#4.-venus                          #")
        print("#5.-salir                          #")
        print("####################################")
        opc=libreria.pedir_numero("ingrese opción:",1,5)
        if (opc==1):
            pedir_tierra()
        if (opc==2):
            pedir_jupiter()
        if (opc==3):
            pedir_marte()
        if (opc==4):
            pedir_venus()
opc=0
max=3
while(opc!=max):
    print("#########Menú ##################")
    print("#1.-satelite                   #")
    print("#2.-planetas                   #")
    print("#3.-salir                      #")
    print("################################")
    opc=libreria.pedir_numero("ingrese opción:",1,3)
    if(opc==1):
        agregar_satelite()
    if(opc==2):
        agregar_planeta()

print("programa finalizado")
#fin_menu
