import libreria

def agregar_departamento():
    input("Agregar departamento: ")
    print("Se ingreso nombre del departamento")

def agregar_capital():
    input("Agregar Capital: ")
    print("Se ingreso Capital de departamento")

opc=0
max=3
while(opc!=3):
    print("########### MENU #############")
    print("# 1. Departamento            #")
    print("# 2. Capital de departamento #")
    print("# 3. salir                   #")
    print("##############################")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if(opc==1):
        agregar_departamento()
    if(opc==2):
        agregar_capital()

print("Programa finalizado")
# fin de menu
