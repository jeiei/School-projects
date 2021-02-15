import sqlite3
from sqlite3 import Error


from asiakas import Asiakas
from tilaus import Tilaus
from tuote import Tuote





def create_connection(db_file):
    ## Esimerkki sivustolta: https://www.sqlitetutorial.net/sqlite-python/ 
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return conn
 
 
# Funktio, joka tulostaa valikon, ja palauttaa tehdyn valinnan
def valikko():
    print("Kauppa-tietokannan raportointisovellus")
    print("1 - Listaa kaikki asiakkaat")
    print("2 - Listaa kaikki tuotteet")
    print("3 - Listaa kaikki halutun asiakkaan tilaukset")
    print("4 - Listaa kaikki halutun tuotteen tilaukset")
    print("5 - Listaa halutun tilauksen tilausrivit")
    print("6 - Listaa kaikki tilaukset halutusta päivämäärästä lähtien")
    print("0 - lopeta")
    jatka = input("Anna valinta: ")
    return jatka
 



### PÄÄOHJELMA ###

## Polku, jossa kauppa.db on
tietokanta = r"C:\Users\JIHU\OneDrive - LUT University\Läksyt\python\Toka kurssi\kauppadb\kauppadb\kauppa.db"

# luodaan yhteys tietokantaan
conn = create_connection(tietokanta)
asi = Asiakas(conn)
tte = Tuote(conn)
til = Tilaus(conn)
 
if conn is not None:  # Mikäli tietokantayhteys saatiin luotua:
    lopeta = False   
    
    
    while lopeta == False:
        jatka = valikko()
        if jatka == "0":
            print("Sovellus lopetetaan")
            lopeta = True
            

        elif jatka == "1":
            print("\n")
            
            asi.HaeKaikkiAsiakkaat()
            print("\n")
        elif jatka == "2":
            print("\n")
            
            tte.haeKaikkiTuotteet()
            print("\n")
        elif jatka == "3":
            x = 0
            print("\n")
            
            hakuehto = input("Hakuehto: ")
            hakuehto, x = asi.HakuEhdonTestaus(hakuehto)
            if x == 1:
                asi.HaeAsiakasNimella(hakuehto)
                asi.TulostaAsiakkaanTilaukset(hakuehto)
            if x == 2:
                asi.HaeAsiakasNumerolla(hakuehto)
                asi.TulostaAsiakkaanTilaukset(hakuehto)
            if x == 0:
                print("Ei raportoitavaa")
    
            print("\n")
        elif jatka == "4":
            x = 0
            print("\n")
            
            hakuehto = input("Hakuehto: ")
            print("\n")
            hakuehto, x = tte.HakuEhdonTestaus(hakuehto)
            if x == 1:
                tuotenro = tte.HaeTuoteNimella(hakuehto)
                hakuehto = tuotenro
                tte.TulostaTuotteenTilaukset(hakuehto)
            if x == 2:
                tte.HaeTuoteNumerolla(hakuehto)
                tte.TulostaTuotteenTilaukset(hakuehto)
            if x == 0:
                print("Ei raportoitavaa")

            print("\n")
        elif jatka == "5":
            x = 0
            print("\n")
            hakuehto = input("Hakuehto: ")
            print("\n")
            x = til.HaeTilaus(hakuehto)
            if x == 1:
                til.TulostaTilauksenRivit(hakuehto)
            if x == 0:
                print("Ei raportoitavaa")
            print("\n")
            
        elif jatka == "6":
            print("\n")
            hakuehto = input("Hakuehto: ")
            print("\n")
            til.HaeTilausPvm(hakuehto)
            print("\n")


        else:
            print("Virheellinen valinta")
            print("\n")

            
    conn.close()   # suljetaan yhteys

else:
    print("Virhe! Yhteyttä tietokantaan ei voida luoda.")




