
def meny_val(): # Sköter menyval och kontrollerar om de är korrekta
    # Detta gjordes till en funktion eftersom att samma val behövde kontrolleras flera gånger
    fel_val = True
    
    while fel_val: # Loopen körs sålänge användaren skriver in något felaktigt
        val = input("Vänligen ange numret för ditt val (1 eller 2): ")
        if val == "1" or val == "2":
            return val # Om det blir rätt så returnerar vi valet, då bryts funktionen helt
        else:
            print("Felaktig input, du får försöka igen. Välj 1 eller 2.")

def lägg_till_ny_kund(kund_dict): #Lägger till en ny kund i dictionaryn.
    # Funktionen tar in dictionaryn med kunder och returnerar den uppdaterade dictionaryn samt nuvarande kundens namn
    namn_ej_giltigt = True
    while namn_ej_giltigt: # Körs sålänge kunden inte skriver in ett giltigt namn
        namn = input("Vänligen ange ditt namn: ")
        if namn == "": # Namnet behöver innehålla något
            print("Du behöver välja ett namn som innehåller minst ett tecken.")
        elif namn in kund_dict.keys(): # Namnet får inte redan finnas i dictionaryn
            print("Namnet finns redan, du får välja ett annat.")
        else: # Om allt har gått rätt till
            kund_dict[namn] = [] # Lägg till kunden
            return kund_dict, namn # Returnera den uppdaterade dictionaryn och det aktuella namnet

    

def kontrollera_existerande_kund(kund_dict): # Kontrollerar en existerande kund så att den finns
    # Funktionen tar in kund-dictionaryn och returnerar den uppdaterade dictionaryn samt nuvarande kundens namn
    antal_försök = 0
    namn_ej_giltigt = True
    while namn_ej_giltigt: # Så länge namnet inte är giltigt
        namn = input("Välkommen tillbaka. Vänligen ange ditt namn: ")
        if namn in kund_dict.keys(): # Om namnet finns i dicitonaryn så är det giltigt
            namn_ej_giltigt = False # Då hoppar vi ut ur loopen
        
        else: # Om namnet inte finns får personen försöka igen, men bara tre gånger totalt
            print("Namnet finns inte. Du får totalt 3 försök")
            antal_försök += 1 # Räknar antalet försök
            if antal_försök == 3: # Om max antal försök är nådda
                print("Tyvärr verkar din varukorg inte finnas kvar. Du får skapa en ny.")
                kund_dict, namn = lägg_till_ny_kund(kund_dict) # Då kär vi funktionen för ny kund istället
                namn_ej_giltigt = False # Sedan hoppar vi ut ur loopen

    return kund_dict, namn # Returnerar den eventuellt uppdaterade dictionaryn och det aktuella namnet


def kontrollera_input_varor(antal_varor): # Kontrollerar så att inputen av varor går rätt till
    # funktionen tar in antal varor som finns i affären och returnerar en lista med nummer på de varor kunden vill köpa
    felaktig_inmatning = True
    while felaktig_inmatning: # sålänge inmatningen är fel
        varor_input = input("Vänligen ange numret på de varor du vill köpa. Separera med kommatecken: ")
        varor_att_köpa = varor_input.split(",") # delar upp numrena som användaren skrev in till en lista
        try:
            for index in range(len(varor_att_köpa)): # loopar igenom listan från inputen
                varor_att_köpa[index] = int(varor_att_köpa[index]) # ändrar alla element till int
                if varor_att_köpa[index] not in range(antal_varor): # om något element inte är inom antal varor som finns
                    raise ValueError # då är något fel
            return varor_att_köpa # om allt har gått rätt returnerar vi listan med nummer på de varor som ska köpas
        except ValueError: # om någon sak i listan inte gick att göra till int
            print("Något av det du skrev finns inte att välja på. Skriv in giltiga val separerade med kommatecken.")


def handla(kund_dict, namn): # Genomför själva handlingen
    # Funktionen tar in dictionaryn med kunder och det aktuella namnet, den returnerar den uppdaterade dictionaryn
    varor_i_affär = ("mjölk", "smör", "mjöl", "juice", "paprika", "gurka") # affärens varor ändras inte, därför valde jag tuple
    varu_nummer = 0 # för att lättare kunna hålla koll på vilken vara kunden vill köpa
    for vara in varor_i_affär: # skriver ut alla varor med deras nummer framför
        print(varu_nummer, vara)
        varu_nummer += 1 # öka numret för varje vara
    
    varor_att_köpa = kontrollera_input_varor(len(varor_i_affär)) # tar in vilka varor kunden vill köpa
    
    for nummer in varor_att_köpa: # loopar igenom listan med nummer på varor som användaren ville köpa
        kund_dict[namn].append(varor_i_affär[nummer]) # lägger till varan kunden ville köpa i hens kundkorg
    
    print("Tack för dina inköp. Du får nu välja mellan följande val:")
    print("1. Betala nu")
    print("2. Spara kundkorgen till senare")
    vill_betala = meny_val() # Kontrollerar och tar in menyvalet
    if vill_betala == "1": # Om kunden vill betala
        skriv_kvitto(kund_dict, namn) # Skriv ut kvittot
        kund_dict.pop(namn) # Tar bort kunden som har betalat från dictionaryn
    
    return kund_dict # Returnerar den uppdaterade dictionaryn


def skriv_kvitto(kund_dict, namn): # Skriver ut en kunds kvitto
    # Funktionen tar in dictionaryn med kunder och det aktuella namnet
    print("Tack! Här är ditt kvitto: ")
    for köpt_vara in kund_dict[namn]: # skriver ut varorna kunden har köpt
        print(köpt_vara)


def main(): # Huvudfunktionen där allt körs
    kunder = {} # en tom dictionary för att lagra kunder och varor
                # kundernas namn är nycklar (key) och varorna är i en lista som är värdet (value)
    handlar = True # för att se till att programmet kan avslutas eller fortsätta

    while handlar: # Så länge affären är öppen
        print("Hej och välkommen till affären! Du får nu välja mellan att:")
        print("1. Starta en helt ny handling")
        print("2. Fortsätta på en tidigare handling")
        ny_handling = meny_val() # Hanterar menyval

        if ny_handling == "1": # Om ny kund
            kunder, aktuellt_namn = lägg_till_ny_kund(kunder) # lägg till den nya kunden
    
        else: # Om gammal kund
            kunder, aktuellt_namn = kontrollera_existerande_kund(kunder) # kontrollera att den existerar
        
        kunder = handla(kunder, aktuellt_namn) # Låt kunden handla
        

        print("Tack för ditt besök! Du får nu välja mellan följande två val:")
        print("1. Butiken fortsätter att vara öppen för en till kund")
        print("2. Butiken stänger (programmet avslutas)")
        fortsätta = meny_val() # Kontrollerar menyval
        if fortsätta == "2": # Om butiken ska stänga hoppar vi ur main
            return 0
        
main() # Ser till att programmet körs