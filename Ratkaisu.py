import ast

global kilpailu


    
    
#Lisää tulos muistisäiliööm
def lisaaTulos(kilpailu, kilpailija, tulos):
         
     kilpailu[kilpailija] = tulos
        
#Tulostaa muistisäiliön            
def tulostaKilpailu(nimi, kilpailu):
    
        print("Kilpailu: " + nimi)
        for x in kilpailu:
            print(str(x) + " : " + str(kilpailu[x].rstrip()))
        return
   

#Tallentaa muistisäiliön
def tallennaKilpailu(nimi, kilpailu):
    try:
        f = open(nimi + ".txt", "a+")
    
        for x in kilpailu:
            f.write(str(x) + " , " + str(kilpailu[x]) + "\n")

        f.close()
        return True
    except:
        return False

#Lataa tiedostosta muistisäiliöön
def lataaKilpailu(nimi, kilpailu):
    
        
        tiedosto = (nimi + ".txt")

        try:
            f = open(tiedosto, "r")
            
            for line in f:
                (key, val) = line.split(",")
                kilpailu[key] = val
            
            f.close()
            return True
        except FileNotFoundError:
            print("Kilpailua ei löytynyt!")
            return False

        
        
    






# PÄÄOHJELMA

kilpailu = dict()
nimi = ""




while True:

    valinta = input("Anna valinta (n - aloita uusi, l - lataa vanha, s - tallenna, p - tulokset, i - lisää, q - lopeta): ")

    #Tekee uuden tekstiedoston ja tallentaa nimen säiliöön
    if valinta == "n" or valinta == "N":
       
       nimi = input("Anna kilpailun nimi: ")
       kilpailu = dict()
       f = open(nimi + ".txt", "w")
       f.write("")
       f.close()
       
       
    #Lataa nimisäiliön mukaisen tiedoston
    if valinta == "l" or valinta == "L":
       
        nimi = input("Anna kilpailun nimi: ")
        kilpailu = dict()
        lataaKilpailu(nimi, kilpailu)
        
        

    #Tallentaa kilpailusäiliön tiedostoon    
    if valinta == "s" or valinta == "S":
        tallennaKilpailu(nimi, kilpailu)
        #kilpailu = dict()
        #nimi = "" 
        #näitä arvoja ei näköjään kuulu alustaa tallentamisen jälkeen?
        #eli kun tallentaa niin noi tiedot kuuluu jäädä vielä muistisäiliöön?
    
    #Tulostaa kilpailusäiliön
    if valinta == "p" or valinta == "P":
        
       tulostaKilpailu(nimi, kilpailu)            
        
    #Lisää kilpailijan ja tuloksen kilpailusäiliöön
    if valinta == "i" or valinta == "I":
        
        if nimi == "":
            nimi = input("Anna kilpailun nimi: ")

        kilpailija = input("Anna kilpailija: ")
        
        while kilpailija !="":
            tulos = input("Anna tulos: ")
            lisaaTulos(kilpailu, kilpailija, tulos)
            kilpailija = input("Anna kilpailija: ")
    
    #Lopettaa ohjelman
    if valinta == "q" or valinta == "Q":
        break
    



   