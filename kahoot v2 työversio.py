#kahoot ohjelma Made by korean123

#Yleiset muuttujat

nro = 1
avain = (110307)
alkuperainenlause = ""

#kryptataan lause
def kryptaus():
    global alkuperainenlause
    global alkuperainennumero
    print(alkuperainenlause)
    for i in range(lausepituus):
        alkuperainennumero = ord(alkuperainenlause[i])
        alkuperainenlause = alkuperainenlause[:i] + chr(alkuperainennumero+3) + alkuperainenlause[i+1:] # muuta tämä
    
#puretaan kryptaus
def purku():
    global alkuperainenlause
    for i in range(lausepituus):
        alkuperainennumero = ord(alkuperainenlause[i])
        alkuperainenlause = alkuperainenlause[:i] + chr(alkuperainennumero-3) + alkuperainenlause[i+1:] # muuta tämä

#lausepituus = len(rivi1)    # muuta tämä

#alkuperainenlause = (rivi1) # muuta tämä

def valikko():
    global ohjelmamuoto
    ohjelmamuoto = ""
    print("Valikko")
    while ohjelmamuoto.lower() != "pelaamaan" or ohjelmamuoto.lower() != "editori" or ohjelmamuoto.lower() != "sulje":
        ohjelmamuoto = input("pelaamaan, editori vai sulje? >> ")
        if ohjelmamuoto.lower() == "pelaamaan":
            pelaamaan()
        elif ohjelmamuoto.lower() == "editori":
            editori()
        elif ohjelmamuoto.lower() == "sulje":
            #sulkemiskomento
            print("")
            break;
           #valikko loppuu.

valikko()

