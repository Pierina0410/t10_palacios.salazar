import libreria
def pedir_pimentel ():
    libreria.pedir_playa("ingrese pimentel:")
    print("se ingreso pimentel")
def pedir_SanJose ():
    libreria.pedir_playa("ingrese SanJose:")
    print("se ingreso SanJose")
def pedir_LasRocas ():
    libreria.pedir_playa("ingrese LasRocas:")
    print("se ingreso las Rocas")
def pedir_zorritos ():
    libreria.pedir_playa("ingrese zorritos:")
    print("se ingreso Zorritos")
def pedir_mancora ():
    libreria.pedir_playa("ingrese mancora:")
    print("se ingreso Máncora")
def pedir_laLeche ():
    libreria.pedir_rio("ingrese la leche:")
    print("se ingreso la leche")
def pedir_rimac ():
    libreria.pedir_rio("ingrese rimac:")
    print("se ingreso rimac")
def pedir_santa ():
    libreria.pedir_rio("ingrese santa")
    print("se ingreso Santa")
def pedir_tumbes():
    libreria.pedir_rio("ingrese tumbes:")
    print("se ingreso Tumbes")

def agregar_playa():
    opc=0
    max=6
    while(opc!=max):
        print("#########Menú rios##############")
        print("#1.-Pimentel                     #")
        print("#2.-San José                     #")
        print("#3.-Las Rocas                    #")
        print("#4.-Zorritos                     #")
        print("#5.-Máncora                      #")
        print("#6.-salir                      #")
        opc=libreria.pedir_numero("ingrese opción:",1,6)
    if (opc==1):
        pedir_pimentel()
    if (opc==2):
         pedir_SanJose()
    if (opc==3):
        pedir_LasRocas()
    if (opc==4):
         pedir_zorritos()
    if (opc==5):
         pedir_mancora()


def agregar_rio():
    opc=0
    max=5
    while(opc!=max):
        print("#########Menú rios##############")
        print("#1.-La leche                   #")
        print("#2.-rimac                      #")
        print("#3.-santa                      #")
        print("#4.-tumbes                     #")
        print("#5.-salir                      #")
        opc=libreria.pedir_numero("ingrese opción:",1,6)
    if (opc==1):
        pedir_laLeche()
    if (opc==2):
         pedir_rimac()
    if (opc==3):
        pedir_santa()
    if (opc==4):
         pedir_tumbes()
opc=0
max=3
while(opc!=max):
        print("#########Menú ##################")
        print("#1.-Frutas                     #")
        print("#2.-verduras                   #")
        print("#3.-salir                      #")
        opc=libreria.pedir_numero("ingrese opción:",1,3)
        if(opc==1):
            agregar_playa()
        if(opc==2):
            agregar_rio()





print("programa finalizado")
#fin_menu
