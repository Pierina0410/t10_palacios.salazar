import libreria
#validar frutas
assert (libreria.validar_frutas("apio")==False)
assert (libreria.validar_frutas("fresa")==False)
assert (libreria.validar_frutas("8")==False)
print("validar_fruta --> oK")

#Validar verduras
assert (libreria.validar_verduras("apio")==False)
assert (libreria.validar_verduras("animal")==False)
assert (libreria.validar_verduras("rojo")==False)
print("validar_verdura --> OK")

#validar nombre
assert (libreria.validar_nombre("ander")==True)
assert (libreria.validar_nombre(10)==False)
assert (libreria.validar_nombre("Ana") == True)
assert (libreria.validar_nombre(15)==False)
print("valida_nombre --> OK")

#validar entero
assert (libreria.validar_entero(12)==True)
assert (libreria.validar_entero(20)==True)
assert (libreria.validar_entero(2.3)==False)
assert (libreria.validar_entero("12")==False)
print("validar_entero --> OK")
