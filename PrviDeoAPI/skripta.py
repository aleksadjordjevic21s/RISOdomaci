import http.client
import json

kon=http.client.HTTPSConnection("getpantry.cloud")

predmeti=["RISO", "MTPP", "PVA"]

class objekat: 
    adresa="Prof Vasica",
    mesto="Beograd",
    telefon="061123654"
objekat=objekat()

payload=json.dumps({
  "id" : "123abc",
  "ime": "Aleksa",
  "prezime": "Djordjevic",
  "smer": "IT",
  "predmet": predmeti,
  "prosek" : "8",
  "kontakt": [objekat.adresa, objekat.mesto, objekat.telefon] 

})

headers={
  'Content-Type': 'application/json'
}

kon.request("POST", "/apiv1/pantry/3ab3757e-2586-4248-8cd5-843b30ae8ab8/basket/prvidomaci", payload, headers)
odgovor=kon.getresponse()
podaci=odgovor.read()
print(podaci.decode("utf-8"))