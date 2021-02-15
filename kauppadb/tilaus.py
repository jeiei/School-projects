## Tilaus-luokka

class Tilaus:
    # Tilauksella on seuraavat tiedot tietokantataulussa nimeltä tilaus:
    # tilausnro - tilausnumero
    # pvm       - tilauksen päivämäärä, muodossa ppkkvvvv
    # asnro     - tilauksen tehneen asiakkaan asiakasnumero

    # Parametrisoitu muodostinfunktio - constructor
    def __init__(self, connection):
        self.conn = connection
        self.cur = self.conn.cursor()

    def HaeTilausPvm(self, hakuehto):
        try:
            hakulause = "SELECT * from tilaus where pvm = '" + hakuehto + "'"
            self.cur.execute(hakulause)  
            rivi = self.cur.fetchall()
            if rivi != []:
                print("Alkupäivämäärän tilaukset:")
                self.TulostaTilaus(rivi)

                hakulause = "SELECT DISTINCT y.tilausnro, y.pvm, y.asnro FROM tilaus x, tilaus y where x.pvm = '" + hakuehto + "' and y.pvm > x.pvm and NOT y.pvm = x.pvm"
                self.cur.execute(hakulause)  
                rivi = self.cur.fetchall()
                self.TulostaTilaus(rivi)
    
            elif rivi == []:
                print("Ei raportoitavaa")
                
        except Exception as e:
            print("Riviä ei pystytty lukemaan tuote-taulusta: {}.".format(e))

    def HaeTilaus(self, hakuehto):
        x = 0
        try:
            hakulause = "SELECT * FROM tilaus where tilausnro = '" + hakuehto + "'"
            self.cur.execute(hakulause)  
            rivi = self.cur.fetchall()
            if rivi != []:
                self.TulostaTilaus(rivi)
                x = 1
                return x
            elif rivi == []:
                x = 0
                return x
           
        except Exception as e:
            print("Riviä ei pystytty lukemaan tuote-taulusta: {}.".format(e))

    def TulostaTilauksenRivit(self, hakuehto):
        try:
            hakulause = "SELECT tuotenro, kpl FROM tilaus, tilausrivi where tilausrivi.tilausnro = tilaus.tilausnro and tilaus.tilausnro = '" + hakuehto + "'"
            self.cur.execute(hakulause)  
            rivit = self.cur.fetchall()
            print("%-15s %s" % ("Tuotenumero", "Kpl"))
            for rivi in rivit:
                print("%-15s %s" %(str(rivi[0]),str(rivi[1])))
        except Exception as e:
            print("Riviä ei pystytty lukemaan asiakas- tai tilaus-taulusta: {}.".format(e))

    # Haetaan kaikki tilaukset
    # Tämän sisällä kutsutaan TulostaTilaus()
    def HaeKaikkiTilaukset(self):
        try:
            self.cur.execute("SELECT asiakas.snimi, pvm, tilausnro FROM tilaus, asiakas where asiakas.asnro = tilaus.asnro")
            rivit = self.cur.fetchall()
            self.TulostaTilaus(rivit)
        except Exception as e:
            print("Rivejä ei pystytty lukemaan tilaus-taulusta: {}.".format(e)) 

    # Tulostetaan 1 asiakas kerrallaan
    # Tänne parametrina rivit, jotka select on hakenut
    def TulostaTilaus(self, rivit):
        print("%-15s %-15s %s"%("Tilausnumero","pvm","Asiakasnumero"))
        for rivi in rivit:
            print("%-15s %-15s %s"%(str(rivi[0]), str(rivi[1]), str(rivi[2])))
