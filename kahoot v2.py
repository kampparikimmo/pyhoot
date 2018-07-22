#kahoot ohjelma Made by korean123

#Yleiset muuttujat
alku = ""
vanha = ["","","","","","",""]

#Aliohjelma: editori, jolla luodaan kysely    
def editori():
    TRITYS = 0
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
                pituus = len(kysymys)
                print(pituus)
                if pituus < 50:
                    empty = 50 - pituus
                    text_file.write(kysymys)
                    for merkki in range(empty-1):
                        text_file.write(" ")
                    text_file.write("\n")
                    
                eka_vastaus = input('#1 Kirjoita ensimmäinen vaihtoehto > ')
                pituus = len(eka_vastaus)
                print(pituus)
                if pituus < 50:
                    empty = 50 - pituus
                    text_file.write(eka_vastaus)
                    for merkki in range(empty-1):
                        text_file.write(" ")
                    text_file.write("\n")  
                #text_file.write(eka_vastaus+"\n")
                    
                toka_vastaus = input('#2 Kirjoita toinen vaihtoehto > ')
                pituus = len(toka_vastaus)
                print(pituus)
                if pituus < 50:
                    empty = 50- pituus
                    text_file.write(toka_vastaus)
                    for merkki in range(empty-1):
                        text_file.write(" ")
                    text_file.write("\n")  
                #text_file.write(toka_vastaus+"\n")
                    
                kolmas_vastaus = input('#3 Kirjoita kolmas vaihtoehto > ')
                pituus = len(kolmas_vastaus)
                print(pituus)
                if pituus < 50:
                    empty = 50 - pituus
                    text_file.write(kolmas_vastaus)
                    for merkki in range(empty-1):
                        text_file.write(" ")
                    text_file.write("\n")  
                #text_file.write(kolmas_vastaus+"\n")
                    
                neljäs_vastaus = input('#4 Kirjoita neljäs vaihtoehto > ')
                pituus = len(neljäs_vastaus)
                print(pituus)
                if pituus < 50:
                    empty = 50 - pituus
                    text_file.write(neljäs_vastaus)
                    for merkki in range(empty-1):
                        text_file.write(" ")
                    text_file.write("\n")  
                #text_file.write(neljäs_vastaus+"\n")
                    
                oikea = input('Laita numero 1,2,3 tai 4 että mikä on oikea vastaus > ')
                pituus = len(oikea)
                print(pituus)
                if pituus < 50:
                    empty = 50- pituus
                    text_file.write(oikea)
                    for merkki in range(empty-1):
                        text_file.write(" ")
                    text_file.write("\n")  
                #text_file.write(oikea+"\n")
                    
                text_file.close()

            else:
                muokattava = input("Kahootin nimi jota haluat muokata > ")
                with open(muokattava+".txt", "r+") as f:
                    vanha = f.read()
                    print (vanha)
                    
        else:
            TRITYS += 1
    

def pelaamaan():
    print("Valitse oikea Kahoot: ")
    kahoot_valinta = input(">> ")
    with open(kahoot_valinta+".txt", "r") as f:
                    for i in range(6):
                        vanha[i] = f.read(38)
                        print (vanha[i])

               
    if alku.lower() == "pelaa": 
        print(nimi)
        print(kysymys)
        print('1. ', eka_vastaus)
        print('2. ', toka_vastaus)
        print('3. ', kolmas_vastaus)
        print('4. ', neljäs_vastaus)
        oikea2 = input('Minkä luulet olevat oikea vastaus? (1,2,3 tai4)')
        if oikea2 == oikea:
            print("oikein!")
        else:
            print("väärin!")
        

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

valikko()
