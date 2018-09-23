#kahoot ohjelma Made by korean123

#Yleiset muuttujat

nro = 1
avain = (110307)
alkuperainenlause = ""
lause = ["","","","","","","",""] #näitä enemmän kuin on rivejä tiedostossa

def editori():
    TRITYS = 0
    global alkuperainenlause 
    while True:
        if TRITYS == 3:
             break;
            
        salasana = input('Syötä salasana > ')
        if salasana == "123":
            editointimuoto = input("Haluatko luoda uuden kahootin vai muokata olemassaolevaa? (uusi,muokata) > ")
            if editointimuoto == "uusi":
                nimi = input('Kirjoita kahootin nimi tähän >>> ')
                text_file = open(nimi+".txt", "w")
                
Tästäalkaa     # kysymys = input('Kirjoita kysymys tähän >>> ')
               # #kryptaus(kysymys)
               # lausepituus = len(kysymys)
               # for i in range(lausepituus):
               #     alkuperainennumero = ord(kysymys[i])
               #     alkuperainenlause = kysymys[:i] + chr(alkuperainennumero+3) + kysymys[i+1:]
               #     text_file.write(alkuperainenlause+"\n")    
                    
                eka_vastaus = input('#1 Kirjoita ensimmäinen vaihtoehto > ')
                text_file.write(eka_vastaus+"\n")
                    
                toka_vastaus = input('#2 Kirjoita toinen vaihtoehto > ')
                text_file.write(toka_vastaus+"\n")
                    
                kolmas_vastaus = input('#3 Kirjoita kolmas vaihtoehto > ')
                text_file.write(kolmas_vastaus+"\n")
                    
                neljäs_vastaus = input('#4 Kirjoita neljäs vaihtoehto > ')
                text_file.write(neljäs_vastaus+"\n")
                    
                oikea = input('Laita numero 1,2,3 tai 4 että mikä on oikea vastaus > ')
                text_file.write(oikea)
                    
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



