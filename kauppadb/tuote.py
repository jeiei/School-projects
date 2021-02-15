class Tuote:

    def __init__(self, connection):
        self.conn = connection
        self.cur = self.conn.cursor()

    def HaeTuoteNumerolla(self, _hakunro):
        try:
            hakulause = "SELECT * FROM tuote where tuotenro = '" + _hakunro + "'"
            self.cur.execute(hakulause)  
            rivi = self.cur.fetchall()
            self.TulostaTuote(rivi)
           
        except Exception as e:
            print("Riviä ei pystytty lukemaan tuote-taulusta: {}.".format(e))


    def HaeTuoteNimella(self, _hakunimi):
        try:
            hakulause = "SELECT * FROM tuote where nimi = '" + _hakunimi + "'"
            self.cur.execute(hakulause)  
            rivi = self.cur.fetchall()
            self.TulostaTuote(rivi)
            tnro = "SELECT tuotenro FROM tuote where nimi = '"+ _hakunimi +"'"  #Vaihdetaan hakuehto tuotenimestä tuotenumeroksi
            self.cur.execute(tnro)
            tnro = self.cur.fetchall()
            for x in tnro:
                tuotenro = x[0]    
            return tuotenro
        except Exception as e:
            print("Riviä ei pystytty lukemaan tuote-taulusta: {}.".format(e))
        

    def haeKaikkiTuotteet(self):
        try:
            self.cur.execute("SELECT * FROM tuote")
            rivit = self.cur.fetchall()
            self.TulostaTuote(rivit)
        except Exception as e:
            print("Rivejä ei pystytty lukemaan tuote-taulusta: {}.".format(e))


    def TulostaTuote(self, rivit):
        
        print("%-15s %-15s %s" %("Tuotenro","Nimi","Kuvaus"))
        for rivi in rivit:
            print("%-15s %-15s %s" %(str(rivi[0]),str(rivi[1]),str(rivi[2])))


    def TulostaTuotteenTilaukset(self, hakuehto):
        try:
            hakulause = "SELECT tilaus.tilausnro, pvm, snimi, enimi, kpl FROM tilaus, tilausrivi, asiakas where tilaus.tilausnro = tilausrivi.tilausnro and tilaus.asnro = asiakas.asnro and tilausrivi.tuotenro = '"+ hakuehto +"'"
            
            self.cur.execute(hakulause)  
            rivit = self.cur.fetchall()
            print("%-15s %-15s %-15s %s" %("Tilausnro", "Pvm", "Asiakas", "Kpl"))
            for rivi in rivit:
                
                print("%-15s %-15s %-15s %s" %(str(rivi[0]),str(rivi[1]),str(rivi[2]) + " " + str(rivi[3]), str(rivi[4])))
        except Exception as e:
            print("Riviä ei pystytty lukemaan asiakas- tai tilaus-taulusta: {}.".format(e))
        


    def HakuEhdonTestaus(self, hakuehto):
        x = 0
        hakulause = "SELECT * FROM tuote where tuotenro = '" + hakuehto + "'"
        self.cur.execute(hakulause)  
        rivit = self.cur.fetchall()
        if rivit == []:
            hakulause = "SELECT * FROM tuote where nimi = '" + hakuehto + "'"
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