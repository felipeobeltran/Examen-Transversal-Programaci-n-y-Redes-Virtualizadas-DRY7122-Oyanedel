import urllib.parse
import requests 

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "MEAetjR6k2BP9CiqjWvr4k8XjFFgxisx"

while True:
    orig = input("Ciudad de Origen: ")
    if orig == "S":
        break
    dest = input("Ciudad de Destino: ")
    if dest == "S":
        break
    
    url = main_api + urllib.parse.urlencode({"key":key,"from":orig,"to":dest})
    print("Dirección URL:"+(url))

    json_data = requests.get(url).json()
    json_status = json_data ["info"] ["statuscode"]

    if json_status == 0:
        print ("Estado de API:" + str(json_status) + " = Consulta de ruta exitosa.\n")

    print("===============================================")
    print("Distancia entre " + (orig) + " to " + (dest))
    print("Kilómetros: {:.1f}".format(json_data["route"]["distance"] * 1.61))
    print("Duración del viaje: " + (json_data["route"]["formattedTime"]))
    print("Combustible utilizado (ltr): {:.1f}".format(json_data["route"].get("fuelUsed", 0)*3.78))
    print("===============================================")
    for each in json_data["route"]["legs"][0]["maneuvers"]:
        print ((each["narrative"]) + ("{:.1f}".format((each["distance"])*1.61) + " km)"))

