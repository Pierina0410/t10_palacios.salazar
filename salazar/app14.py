import libreria

def agregar_natacion():
    print("se agrego el deporte natacion")
def  agregar_futbol():
    print("Se agrego el deporte futbol")
def  agregar_basque():
    print("Se agrego el deporte basquebaal")
def  agregar_tenis():
    print("Se agrego el deporte tenis")
def  agregar_voley():
    print("Se agrego el deporte voley")

def jugar_deporte():
    opc=0
    max=6
    while(opc!=max):
        print("##### DEPORTES #####")
        print("# 1. natacion      #")
        print("# 2. futbol        #")
        print("# 3. basquetbool   #")
        print("# 4. tenis         #")
        print("# 5. voley         #")
        print("# 6. Salir         #")
        print("####################")
        opc=libreria.pedir_numero("Ingrese opcion:",1,6)

    if (opc==1):
        agregar_natacion()
    if (opc==2):
        agregar_futbol()
    if (opc==3):
        agregar_basque()
    if (opc==4):
        agregar_tenis()
    if (opc==5):
        agregar_voley()

# Menu
opc=0
max=2
while(opc!=max):
    print("###### MENU #######")
    print("# 1.DEPORTES      #")
    print("# 2.SALIR         #")
    print("###################")
    opc=libreria.pedir_numero("ingrese opcion:",1,2)

    if(opc==1):
        jugar_deporte()

print("fin del programa")
