import libreria
def jugar_futbol():
    libreria.pedir_nombre("ingrese nombre de jugador:")
    print("se ingreso jugador para futbol")
def jugar_voley():
    libreria.pedir_nombre("ingrese nombre de juagdor:")
    print("se ingreso jugador para voley")
#fin_def

opc=0
max=3
while(opc!=max):
    print("###### MENU #######")
    print("# 1.JUGAR FUTBOL  #")
    print("# 2.JUGAR VOLEY   #")
    print("# 3.SALIR         #")
    opc=libreria.pedir_numero("ingrese opcion:",1,3)
    #fin_while

    #Mapeo
    if(opc==1):
        jugar_futbol()
    if(opc==2):
        jugar_voley()
print("fin del programa")
#fin_menu
