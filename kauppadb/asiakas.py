## Asiakas-luokka


class Asiakas:

    # Asiakkaalla on seuraavat tiedot tietokantataulussa nimeltä asiakas:
    # asnro - asiakasnumero
    # snimi - sukunimi
    # enimi - etunimi
    # email - sähköpostiosoite
    # puh   - puhelinnumero

    def __init__(self, connection):
        self.conn = connection
        self.cur = self.conn.cursor()

#    def selvitaHakuehto(self, hakuehto):
#        try:
#            hakulause = "SELECT * FROM asiakas where asnro = '" + hakuehto + "'"
#            x = self.cur.execute(hakulause)  
#            rivi = self.cur.fetchall()            
#            self.TulostaAsiakas(rivi)
#            
#        except Exception as e:
#            print("Riviä ei pystytty lukemaan asiakas-taulusta: {}.".format(e))

    # Asiakkaan haku asiakasnumerolla
    # Tämän sisällä kutsutaan TulostaAsiakas()
    def HaeAsiakasNumerolla(self, _hakunro):
        try:
            hakulause = "SELECT * FROM asiakas where asnro = '" + _hakunro + "'"
            self.cur.execute(hakulause)  
            rivi = self.cur.fetchall()
            self.TulostaAsiakas(rivi)

        except Exception as e:
            print("Riviä ei pystytty lukemaan asiakas-taulusta: {}.".format(e))
            

    # Asiakkaan haku sukunimellä
    def HaeAsiakasNimella(self, _hakunimi):
        try:
            hakulause = "SELECT * FROM asiakas where snimi = '" + _hakunimi + "'"
            self.cur.execute(hakulause)  
            rivi = self.cur.fetchall()
            self.TulostaAsiakas(rivi)

        except Exception as e:
            print("Riviä ei pystytty lukemaan asiakas-taulusta: {}.".format(e))
      

    # Haetaan kaikki asiakkaat
    # Tämän sisällä kutsutaan TulostaAsiakas()
    def HaeKaikkiAsiakkaat(self):
        try:
            self.cur.execute("SELECT * FROM asiakas")
            rivit = self.cur.fetchall()
            self.TulostaAsiakas(rivit)
        except Exception as e:
            print("Rivejä ei pystytty lukemaan asiakas-taulusta: {}.".format(e)) 

    # Tulostetaan 1 asiakas kerrallaan
    # Tänne parametrina rivit, jotka select on hakenut
    def TulostaAsiakas(self, rivit):
      
        print("%-15s %-15s %-25s %s" %("Asiakasnumero","Nimi","Email","Puhelin"))
        for rivi in rivit:
            print("%-15s %-15s %-25s %s" %(str(rivi[0]),str(rivi[1]) +" "+ str(rivi[2]),str(rivi[3]), str(rivi[4])))
           
        
           

    # Tulostetaan 1 asiakkaan kaikki tilaukset
    def TulostaAsiakkaanTilaukset(self, hakuehto):
        try:
            hakulause = "SELECT tilausnro, pvm FROM asiakas, tilaus where asiakas.asnro = tilaus.asnro and asiakas.asnro = '" + hakuehto + "'"
            self.cur.execute(hakulause)  
            rivit = self.cur.fetchall()
            if rivit == []:
                hakulause = "SELECT tilausnro, pvm FROM asiakas, tilaus where asiakas.asnro = tilaus.asnro and asiakas.snimi = '" + hakuehto + "'"
                self.cur.execute(hakulause)  
                rivit = self.cur.fetchall()
            print("%-15s %s" % ("Tilausnumero", "Pvm"))
            for rivi in rivit:
                print("%-15s %s" %(str(rivi[0]),str(rivi[1])))
        except Exception as e:
            print("Riviä ei pystytty lukemaan asiakas- tai tilaus-taulusta: {}.".format(e))

    def HakuEhdonTestaus(self, hakuehto):
        x = 0
        hakulause = "SELECT * FROM asiakas where asnro = '" + hakuehto + "'"
        self.cur.execute(hakulause)  
        rivit = self.cur.fetchall()
        if rivit == []:
            hakuehto = hakuehto.capitalize()
            hakulause = "SELECT * FROM asiakas where snimi = '" + hakuehto + "'"
            self.cur.execute(hakulause)  
            rivit = self.cur.fetchall()
            if rivit == []:
                x = 0
                return hakuehto, x
            else:
                x = 1
                return hakuehto, x
        elif rivit != []:
            x = 2
            return hakuehto, x