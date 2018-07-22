#kahoot ohjelma Made by korean123
from tkinter import *
#Yleiset muuttujat
alku = ""
vanha = ["","","","","","",""]
#kryptkysymys = ""
#kryptpituus = ""
#kryptv1 = ""
#kryptv2 = ""
#kryptv3 = ""
#kryptv4 = ""
#kryptv4num = ""
#kryptv3num = ""
#kryptv2num = ""
#kryptv1num = ""
oikea = ""

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
                kryptkysymys = kysymys
                kryptpituus = len(kryptkysymys)
                for i in range(kryptpituus):
                    kryptnumerokysymys = ord(kryptkysymys[i])
                    kryptkysymys = kryptkysymys[:i] + chr(kryptnumerokysymys+5) + kryptkysymys[i+1:]            
                pituus = len(kysymys)
                print(pituus)
                text_file.write(kryptkysymys + "\n")
                    
                eka_vastaus = input('#1 Kirjoita ensimmäinen vaihtoehto > ')
                kryptv1 = eka_vastaus
                vastauskryptpituus1 = len(kryptv1)
                pituus = len(eka_vastaus)
                for i in range(vastauskryptpituus1):
                    kryptv1num = ord(kryptv1[i])
                    kryptv1 = kryptv1[:i] + chr(kryptv1num+5) + kryptv1[i+1:]     
                print(pituus)
                text_file.write(kryptv1 + "\n")        #normalisti eka_vastaus
                
                    
                toka_vastaus = input('#2 Kirjoita toinen vaihtoehto > ')
                kryptv2 = toka_vastaus
                vastauskryptpituus2 = len(kryptv2)
                for i in range(vastauskryptpituus2):
                    kryptv2num = ord(kryptv2[i])
                    kryptv2 = kryptv2[:i] + chr(kryptv2num+5) + kryptv2[i+1:]
                pituus = len(toka_vastaus)
                print(pituus)
                text_file.write(kryptv2+"\n")
                    
                kolmas_vastaus = input('#3 Kirjoita kolmas vaihtoehto > ')
                kryptv3 = kolmas_vastaus
                vastauskryptpituus3 = len(kryptv3)
                for i in range(vastauskryptpituus3):
                    kryptv3num = ord(kryptv3[i])
                    kryptv3 = kryptv3[:i] + chr(kryptv3num+5) + kryptv3[i+1:]
                pituus = len(kolmas_vastaus)
                print(pituus)
                text_file.write(kryptv3+"\n")
                    
                neljäs_vastaus = input('#4 Kirjoita neljäs vaihtoehto > ')
                kryptv4 = neljäs_vastaus
                vastauskryptpituus4 = len(kryptv4)
                for i in range(vastauskryptpituus4):
                    kryptv4num = ord(kryptv4[i])
                    kryptv4 = kryptv4[:i] + chr(kryptv4num+5) + kryptv4[i+1:]
                pituus = len(neljäs_vastaus)
                print(pituus)
                text_file.write(kryptv4+"\n")
                    

                
                oikea = input('Laita numero 1,2,3 tai 4 että mikä on oikea vastaus > ')
                kryptoikea = oikea
                oikeakryptpituus = len(kryptoikea)
                for i in range(oikeakryptpituus):
                    oikeakryptnumero = ord(kryptoikea[i]) #muuttaa kirjaimen numeroksi
                    kryptoikea = kryptoikea[:i] + chr(oikeakryptnumero+5) + kryptoikea[i+1:]
                    print(kryptoikea)
                pituus = len(oikea)
                print(pituus)
                text_file.write(kryptoikea+"\n")
                    
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
    f = open(kahoot_valinta+".txt", "r")
    for i in range(6):
        for line in f:
            line = line[:-1]
            vanha = f.read(line)
            pituus = len(vanha)
            for nnn in range(0,pituus):
                vanhanumero = ord(vanha[nnn])
                vanha = vanha[:nnn] + chr(vanhanumero-5) + vanha[nnn+1:]            
            print (vanha)

               
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

#valikko()



window = Tk()
window.title("Kahoot valikko")
c = Canvas(window, width=300, height=100)

def valikkoA():
    pelaamaan()
def valikkoB():
    editori()
def valikkoC():
    #sulkemisfunktio
    print("")
pelaamaanButton = Button(window, text="Pelaa", command=valikkoA)
editoriButton = Button(window, text="Editori", command=valikkoB)
suljeButton = Button(window, text="Sulje", command=valikkoC)
pelaamaanButton.pack()
editoriButton.pack()
suljeButton.pack()
c.pack()
window.mainloop()











