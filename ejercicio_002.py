nombre=input("¿Como te llamas? ")
genero=input("Cual es tu sexo (H o M)? ")

if (genero == "M" and nombre.upper()<"M") or (genero =="H" and nombre.upper()>"N"):
    print("Tu grupo es el A")
else:
    print("Tu grupo es el B")  

    