#kahoot ohjelma Made by korean123

import time

#Yleiset muuttujat

nro = 1
avain = (110307)
kryptattu_kysymys = ""
alkuperainenlause = ""
kierros = 0
lause = ["","","","","","","",""] #näitä enemmän kuin on rivejä tiedostossa

def editori():
    TRITYS = 0
    global alkuperainenlause
    global kierros
    global kryptattu_kysymys
    while True:
        if TRITYS == 3:
             break;
            
        salasana = input('Syötä salasana > ')
        if salasana == "123":
            editointimuoto = input("Haluatko luoda uuden kahootin vai muokata olemassaolevaa? (uusi,muokata) > ")
            if editointimuoto == "uusi":
                nimi = input('Kirjoita kahootin nimi tähän >>> ')
                text_file = open(nimi+".txt", "w")
                
                kysymys = input('Kirjoita kysymys tähän >>> ')
                lausepituus = len(kysymys)
                kryptattu_kysymys=kysymys
                for i in range(lausepituus):
                    kierros += 1
                    alkuperainennumero = ord(kryptattu_kysymys[i])
                    kryptattu_kysymys = kryptattu_kysymys[:i] + chr(alkuperainennumero+3)+ kryptattu_kysymys[i+1:]
                text_file.write(kryptattu_kysymys+"\n")
                    
                i = 0    
                eka_vastaus = input('#1 Kirjoita ensimmäinen vaihtoehto > ')
                lausepituus = len(eka_vastaus)
                kryptattu_kysymys=eka_vastaus
                for i in range(lausepituus):
                    kierros += 1
                    alkuperainennumero = ord(kryptattu_kysymys[i])
                    kryptattu_kysymys = kryptattu_kysymys[:i] + chr(alkuperainennumero+3)+ kryptattu_kysymys[i+1:]
                text_file.write(kryptattu_kysymys+"\n")
                    
                toka_vastaus = input('#2 Kirjoita toinen vaihtoehto > ')
                lausepituus = len(toka_vastaus)
                kryptattu_kysymys=toka_vastaus
                for i in range(lausepituus):
                    kierros += 1
                    alkuperainennumero = ord(kryptattu_kysymys[i])
                    kryptattu_kysymys = kryptattu_kysymys[:i] + chr(alkuperainennumero+3)+ kryptattu_kysymys[i+1:]
                text_file.write(kryptattu_kysymys+"\n")
                    
                kolmas_vastaus = input('#3 Kirjoita kolmas vaihtoehto > ')
                lausepituus = len(kolmas_vastaus)
                kryptattu_kysymys=kolmas_vastaus
                for i in range(lausepituus):
                    kierros += 1
                    alkuperainennumero = ord(kryptattu_kysymys[i])
                    kryptattu_kysymys = kryptattu_kysymys[:i] + chr(alkuperainennumero+3)+ kryptattu_kysymys[i+1:]
                text_file.write(kryptattu_kysymys+"\n")
                    
                neljas_vastaus = input('#4 Kirjoita neljäs vaihtoehto > ')
                lausepituus = len(neljas_vastaus)
                kryptattu_kysymys=neljas_vastaus
                for i in range(lausepituus):
                    kierros += 1
                    alkuperainennumero = ord(kryptattu_kysymys[i])
                    kryptattu_kysymys = kryptattu_kysymys[:i] + chr(alkuperainennumero+3)+ kryptattu_kysymys[i+1:]
                text_file.write(kryptattu_kysymys+"\n")
                    
                oikea = input('Laita numero 1,2,3 tai 4 että mikä on oikea vastaus > ')
                lausepituus = len(oikea)
                kryptattu_kysymys=oikea
                for i in range(lausepituus):
                    kierros += 1
                    alkuperainennumero = ord(kryptattu_kysymys[i])
                    kryptattu_kysymys = kryptattu_kysymys[:i] + chr(alkuperainennumero+3)+ kryptattu_kysymys[i+1:]
                text_file.write(kryptattu_kysymys)
                    
                text_file.close()

            else:
                muokattava = input("Kahootin nimi jota haluat muokata > ")
                with open(muokattava+".txt", "r+") as f:
                    vanha = f.read()
                    print (vanha)
                    
        else:
            TRITYS += 1



def pelaamaan():
    numero = 0
    print("Valitse oikea Kahoot: ")
    kahoot_valinta = input(">> ")
    file = open(kahoot_valinta+".txt", "r")
    for line in file:
        print (line)
        numero = numero + 1
        lause[numero] = line.strip()
        
        
    pelaajan_arvaus = input('Minkä luulet olevat oikea vastaus? (1,2,3 tai4)')
    if pelaajan_arvaus == lause[6]:
        print("oikein!")
    else:
        print("väärin! (:<")     


#kryptataan lause
#def kryptaus(alkuperainenlause):
#    lausepituus = len(alkuperainenlause)
#    for i in range(lausepituus):
#        alkuperainennumero = ord(alkuperainenlause[i])
#        alkuperainenlause = alkuperainenlause[:i] + chr(alkuperainennumero+3) + alkuperainenlause[i+1:] # muuta tämä
#    text_file.write(alkuperainenlause+"\n")
    
#puretaan kryptaus
#def purku():
#    global alkuperainenlause
#    for i in range(lausepituus):
#        alkuperainennumero = ord(alkuperainenlause[i])
#        alkuperainenlause = alkuperainenlause[:i] + chr(alkuperainennumero-3) + alkuperainenlause[i+1:] # muuta tämä

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

