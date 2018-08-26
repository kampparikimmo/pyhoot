#kahoot ohjelma Made by korean123

#Yleiset muuttujat



rivi1 = "wan"
rivi2 = "thuu"
rivi3 = "trii"
rivi4 = "fur"
rivi5 = "faiv"
rivi6 = "six"
nro = 1
avain = (110307)

lausepituus = len(rivi1)    # muuta tämä

alkuperainenlause = (rivi1) # muuta tämä
#kryptataan lause
def kryptaus():
    print(alkuperainenlause)
    for i in range(lausepituus):
        alkuperainennumero = ord(alkuperainenlause[i])
        alkuperainenlause = alkuperainenlause[:i] + chr(alkuperainennumero+3) + alkuperainenlause[i+1:] # muuta tämä
    print(alkuperainenlause)
    
#puretaan kryptaus
def purku():
    for i in range(lausepituus):
        alkuperainennumero = ord(alkuperainenlause[i])
        alkuperainenlause = alkuperainenlause[:i] + chr(alkuperainennumero-3) + alkuperainenlause[i+1:] # muuta tämä
    print(alkuperainenlause)
