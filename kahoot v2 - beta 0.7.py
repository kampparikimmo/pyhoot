#kahoot ohjelma Made by korean123

import time
from tkinter import *

#Yleiset muuttujat

nro = 1
avain = (110307)
kryptattu_kysymys = ""
alkuperainenlause = ""
kierros = 0
lause = ["","","","","","","",""] #näitä enemmän kuin on rivejä tiedostossa
i = 1
colors = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
    'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
    'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
    'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
    'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
    'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
    'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
    'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
    'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
    'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
    'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
    'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
    'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
    'indian red', 'saddle brown', 'sandy brown',
    'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
    'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
    'pale violet red', 'maroon', 'medium violet red', 'violet red',
    'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
    'thistle', 'snow2', 'snow3',
    'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
    'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
    'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
    'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
    'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
    'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
    'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
    'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
    'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
    'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
    'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
    'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
    'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
    'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
    'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
    'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
    'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
    'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
    'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
    'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
    'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
    'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
    'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
    'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
    'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
    'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
    'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
    'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
    'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
    'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
    'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
    'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
    'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
    'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
    'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
    'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
    'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
    'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
    'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
    'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
    'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
    'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
    'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
    'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
    'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
    'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',]

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
                text_file.write(kryptattu_kysymys+"\n")
                    
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
        lausepituus = len(line)
        kryptattu_kysymys=line
        for i in range(lausepituus-1):
                    alkuperainennumero = ord(kryptattu_kysymys[i])
                    kryptattu_kysymys = kryptattu_kysymys[:i] + chr(alkuperainennumero-3)+ kryptattu_kysymys[i+1:]
        numero = numero + 1
        lause[numero] = kryptattu_kysymys.strip()
        if numero < 6:
            print(lause[numero])
        
        
    pelaajan_arvaus = input('Minkä luulet olevat oikea vastaus? (1,2,3 tai4)')
    if pelaajan_arvaus == lause[6]:
        print("oikein!")
    else:
        print("väärin! (:<")     


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

#valikko()


screen = Tk()
screen.title("Pyhoot 0.7 beta")
mainframe = Frame(screen , heigh = 200, width = 500, background=colors[i])
print(i)


intro = Label(mainframe, text = "Valitse pyhootin käyttömuoto.")
intro.pack()
pelaaNappi = Button(mainframe, text="Pelaa", command=pelaamaan)
pelaaNappi.pack()
editoriNappi = Button(mainframe, text="Editori", command=editori)
editoriNappi.pack()
suljeNappi = Button(mainframe, text="Sulje", command=screen.destroy)
suljeNappi.pack()

mainframe.pack_propagate(0)
mainframe.pack(padx = 0, pady =  5)

screen.mainloop()






        

