import libreria
assert (libreria.validar_playa("pimentel")==True)
assert (libreria.validar_playa("1")==False)
assert (libreria.validar_rio("hoola")==False)
assert (libreria.validar_rio("pimentel")==False)
assert (libreria.validar_satelite("1")==False)
assert (libreria.validar_satelite("luna")==True)
assert (libreria.validar_planeta("1")==False)
assert (libreria.validar_planeta("luna")==True)

