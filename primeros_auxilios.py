#Funcion para validar que usuario ingrese si o no.
#En caso de respuesta no valida le pedirá reingreso hasta que sea valido
def validar_respuesta(respuesta):
    #Se ejecuta hasta que la respuesta sea valida
    while respuesta!= "si" and respuesta != "no":
        respuesta = input("Por favor, ingrese 'si' o 'no' (sin comillas): ").lower()
    return respuesta

#Programa principal
print("Responda 'si' o 'no' (sin comillas) a las siguientes preguntas para entregar los pasos a seguir")
respuesta = input("Responde a estimulos? ").lower()
respuesta = validar_respuesta(respuesta)

if(respuesta == "si"):
    print("Valorar la necesidad de llevarlo al hospital")
else:
    print("Abrir via aerea")
    respuesta = input("¿Respira? ").lower()
    respuesta = validar_respuesta(respuesta)
    if(respuesta=="si"):
        print("Permitirle posición de suficiente ventilación")
    else:
        print("Administrar 5 ventilaciones y llamar a ambulancia")
        #Se ejecuta hasta dar termino con break
        while True:
            respuesta = input("Signos de vida? ").lower()
            respuesta = validar_respuesta(respuesta)
            if(respuesta=="si"):
                print("Reevaluar a la espera de la ambulancia")
            else:
                print("Administrar compresiones torácicas hasta que llegue ambulancia")
            respuesta = input("Llegó ambulancia? ").lower()
            respuesta = validar_respuesta(respuesta)
            if(respuesta=="si"):
                break
            
           