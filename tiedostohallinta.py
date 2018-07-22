#Tässä tiedostonhallinnan esimerkkiohjelma
import time
nro = 0
rivinro = 0

def kirjoita_uusi():
    nimi = input("Minkä niminen tiedosto luodaan? ")
    tiedosto = open(nimi+".txt", "w+")
    kysymys = input("Kirjoita kysymys: > ")
    tiedosto.write(kysymys+"\n")
    vastaus = input("Mikä on vastaus kysymykseen? > ")
    tiedosto.write(vastaus+"\n")
    tiedosto.close()

def pelata():
    global nro
    global rivinro
    nimi = input("Minkä niminen peli avataan? ")
    tiedosto = open(nimi+".txt", "r")
    rivit = tiedosto.readlines()
    for rivi in rivit:
        rivinro = rivinro +1
    for ivir in range(0,rivinro):
        vastaus = input(
    tiedosto.close()

def tallenna():
    global nro
    nimi = input("Minkä niminen tiedosto avataan? ")
    tiedosto = open(nimi+".txt", "r")
    rivit = tiedosto.readlines()
    for rivi in rivit:
        nro = nro + 1
        print (str(nro)+". "+rivi)
    tiedosto.close()
    tiedosto = open(nimi+".txt", "a")
    kysymys = input("Kirjoita kysymys: > ")
    tiedosto.write(kysymys+"\n")
    vastaus = input("Mikä on vastaus kysymykseen? > ")
    tiedosto.write(vastaus+"\n")
    tiedosto.close()

while True:
    for tyhja_rivi in range(1,5):
        print ("\n")
    valinta = input("Haluatko (L)uoda uuden, (T)allentaa olemassaolevaan vai (P)elata? > ")
    if valinta == "p":
        pelata();
    elif valinta == "l":
        kirjoita_uusi();
    elif valinta == "t":
        tallenna();
    elif valinta == "x":
        break;
    time.sleep(1)



