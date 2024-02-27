ventas = { "Enero": 15000, 
          "Febrero": 22000, 
          "Marzo": 12000, 
          "Abril": 17000, 
          "Mayo": 81000, 
          "Junio": 13000, 
          "Julio": 21000, 
          "Agosto": 41200, 
          "Septiembre": 25000, 
          "Octubre": 21500, 
          "Noviembre": 91000, 
          "Diciembre": 21000, }

limite_ventas = int(input("Ingrese el límite de ventas: "))

# Recorrer diccionario: for mes, venta in ventas.items()
ventas_filtradas = {mes: venta for mes, venta in ventas.items() if venta >= limite_ventas}

print(ventas_filtradas)

