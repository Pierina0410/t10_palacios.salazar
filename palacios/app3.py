import libreria
def agregar_marca():
    input("Agregar marca: ")
    print("Se ingreso marca")
def agregar_modelo():
    input("Agregar modelo: ")
    print("Se ingreso modelo")

opc=0
max=3
while(opc!=max):
    print("######### MENU ##########")
    print("# 1. agregar marca       #")
    print("# 2. aagregar modelo              #")
    print("# 3. salir              #")
    print("#########################")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if(opc==1):
        agregar_marca()
    if(opc==2):
        agregar_modelo()

print("Programa finalizado")
# fin_menu
