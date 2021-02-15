def main(): #pääohjelmafunktio
    
    print("Hello there! Submit values to get their biggest common factor! Press enter to close the program.\n")

    try:
        x,y = input("Enter two values: ").split()
        while True:
            if x or y != "":
                x = float(x)
                y = float(y)
                xl = xf(x)
                yl = yf(y)
                syt(xl,yl)
                x,y = input("Enter two values: ").split()
    except:
        print("Ohjelma suljetaan")
        

#     xl = xf(x) 
#     yl = yf(y)
#     syt(xl,yl)
        
          
#Tallennetaan X:n tekijät listaan 
def xf(x):
    xl = []
    c = x
    while c > 1:

        #print("x: ",float(c-1))
        c = float(c-1)
        if x % c == 0 and c != 0:
            xl.append(c)
            #print("Jaollinen luku ja lista: ",c,xl)
    return(xl)
    
    
#Tallennetaan Y:n tekijät listaan    
def yf(y):
    yl = []
    d = y
    while d > 1:
        #print("y: ",float(d-1))
        d = float(d-1)
        if y % d == 0:
            yl.append(d)
            #print("Jaollinen luku ja lista: ",d,yl)
    return(yl)        
    
    
#Luetaan molemmista listoista yhteiset tekijät ja otetaan tekijöistä suurin yhteinen tekijä    
def syt(xl,yl):
    #print(xl)
    #print(yl)
    syt = set(xl).intersection(yl)
    #print(syt)
    print(max(syt))
    
#Pääohjelmafunktion käynnistys jos tämä on käynnistystiedosto
if __name__=="__main__":
    main()
    
#Kommentoidut printit ovat testereitä