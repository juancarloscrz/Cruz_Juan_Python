
nombre=(input("¿Cuál es tu nombre ? "))
apellido_1=(input("¿Cuál es tu primer apellido? "))
apellido_2=(input("Cúal es tu segundo apellido? "))
año=int(input("En qué año naciste? "))
AÑO_ACTUAL=2023
mes=int(input("En qué mes del año naciste?(Introducir formato mm): "))
dia=int(input("En qué día del mes naciste?(Introducir formato dd): "))

print('---')
print('Procesando...')
print('---')

print(f"Este es  tu nombre completo en mayusculas:  {nombre.upper()} {apellido_1.upper()} {apellido_2.upper()}")  
print(f"Este es  tu nombre competo en minuscula:  {nombre.lower()} {apellido_1.lower()} {apellido_2.lower()}") 
print(f"Esta es tu fecha de nacimiento:  {dia} - {mes} - {año}")  

def edad(a,b):
    edad=int(a-b)
    return edad

edad_usuario=edad(AÑO_ACTUAL,año)
print (f"Tu edad es: {edad_usuario} años")

def obtener_vocales(frase):
    vocales='aeiouAEIOU'
    return [c for c in frase if c in vocales]

nombre_completo=nombre+apellido_1+apellido_2
total_vocales=obtener_vocales(nombre_completo)

numero_de_vocales=len(obtener_vocales(total_vocales))
print(f"Tú nombre completo tiene un total de {numero_de_vocales} vocales")

total_de_letras=len(nombre_completo)
print(f"Tú nombre completo tiene un total de {total_de_letras} letras")

tipo_caracter=isinstance(edad_usuario,int)
print (f"¿Tu edad es un caracter de tipo número? {tipo_caracter}")

es_alpha=nombre_completo.isalpha()
print(f"¿Tu nombre completo es un caracter de tipo alfanumerico? {es_alpha}")

edad_futura=edad_usuario+10
print(f" En 10 años tendras: {edad_futura} años")


edad_futura=edad_usuario+20
promedio_edad=(edad_usuario+edad_futura)/2
print(f"La media de tu edad actual y tu edad en 20 años es {promedio_edad}")

print('Adios!')