import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
llavesita = "YVTYGUt3qAvclqPiS4rrDBaHWXK7Wd3h"

while True:
   origenal = input("Empieze con su origen, estimado: ")
   if origenal == "salir" or origenal == "s":
        break

   destino = input("ingrese su épico destino, estimadísimo: ")
   if destino == "salir" or destino == "s":
        break


   url = main_api + urllib.parse.urlencode({"key" :llavesita, "from" :origenal, "to" :destino})

   json_dato = requests.get(url).json()

   print("URL:" + (url))

   json_estado = json_dato ["info"] ["statuscode"]

   if json_estado == 0:
    print("API Status:" + str(json_estado) + "= Una ruta perfectirijilla.\n")
    print("=============================================")
    print("Directions from " + (origenal) + " to " + (destino))
    print("Trip Duration:   " + (json_dato["route"]["formattedTime"]))
    print("Kilometers:      " + str("{:.2f}".format((json_dato["route"]["distance"])*1.61)))
    print("=============================================")
    print("=============================================")
    for each in json_dato["route"]["legs"][0]["maneuvers"]:
     print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
     print("=============================================\n")

   elif json_estado == 402:
        print("**********************************************")
        print("Status Code: " + str(json_estado) + "; escribió mal alguno de los sitios, por favor reintente y pongase serio.")
        print("**********************************************\n")
   elif json_estado == 611:
        print("**********************************************")
        print("Status Code: " + str(json_estado) + "; mijo usted se equivoco al escribir la entrada o no se, pero arreglelo.")
        print("**********************************************\n")
   else:
        print("************************************************************************")
        print("For Staus Code: " + str(json_estado) + "; Refer to:")
