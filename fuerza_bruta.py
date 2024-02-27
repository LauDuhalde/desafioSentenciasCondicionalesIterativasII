from string import ascii_lowercase
import getpass

#se pide contraseña con getpass para que no se vea
contraseña = getpass.getpass("Ingrese la contraseña: ").lower()

intentos =0
for letra_contraseña in contraseña:
    for letra in ascii_lowercase:
        intentos+=1
        if(letra_contraseña==letra):
            #Se termina ciclo ascii para continuar con la siguiente letra de la contraseña
            break

#Se imprime contraseña solo para comprobación
print(f"La contraseña '{contraseña}' fue forzada en {intentos} intentos")