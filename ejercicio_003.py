savedpw="prueba123"
enteredpw= ""

while True:
    try:
        enteredpw=input("Favor de introducir su contraseña: ")
        if savedpw == enteredpw:
            print("Ingreso de sesión exitoso")
        break
    except:
     print("La contraseña no coincide, favor de intentar nuevamente")   
