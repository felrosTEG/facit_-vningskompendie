def meny_ej_inloggad(): # Skriver ut menyn om man inte är inloggad
    print("Välkommen till vår bank!")
    print("Du har följande val:")
    print("1. Skapa ett nytt konto hos banken")
    print("2. Logga in på ditt konto")
    print("3. Avsluta programmet")

def meny_inloggad(): # skriver ut menyn om man är inloggad
    print("Du har nu följande val:")
    print("1. Se kontouppgifter (inklusive saldo)")
    print("2. Sätta in eller ta ut pengar")
    print("3. Logga ut")
    print("4. Avsluta ditt konto hos banken")

def kontrollera_inmatning_meny(antal_val): # hanterar input när det är menyval
    # funktionen tar in antalet val i menyn och returnerar vilket val användaren gjorde
    fel_val = True
    
    while fel_val: # sålänge valet är ogiltigt
        try:
            val = int(input("Vänligen ange numret för ditt val: "))
            if val in range(1,antal_val+1): # kollar om valet är i rätt spann
                return val # Om det blir rätt så returnerar vi valet, då bryts funktionen helt
            else: # om det inte är i rätt spann
                raise ValueError # då ska det bli fel
        except ValueError: # om det inte är ett helttal eller inte i rätt spann
            print("Felaktig input, du får försöka igen. Välj den siffra som motsvarar ditt val.")


def skapa_konto(användare): # skapar ett konto
    # funktionen tar in dictionaryn med användare och returnerar den uppdaterade dictionaryn
    print("Vad roligt att du vill skapa ett konto hos oss!")
    inkorrekt_inmatning = True

    while inkorrekt_inmatning: # sålänge inmatningen är fel
        namn = input("Vad är ditt namn? ")
        if namn == "" or namn == " ": # om namnet inte innehåller någonting
            print("Ditt namn behöver innehålla något, du får försöka igen.")
        elif namn in användare.keys(): # om namnet rean finns
            print("Det namnet finns redan, du får välja ett annat.")
        else: # om allt har gått rätt till
            inkorrekt_inmatning = False # då bryter vi loopen
    
    lösenord = input("Vänligen ange det lösenord du vill ha.")
    användare[namn] = [lösenord, 0] # uppdaterar dicitonaryn med namn, lösenord och saldo
    print("Ditt konto är nu skapat!")
    
    return användare # returnerar den uppdaterade dictionaryn med användare

def logga_in(användare): # loggar in en användare
    # funktionen tar in dictionaryn med användare och returnerar namnet på den användare som har loggat in
    felaktig_inloggning = True
    antal_försök = 0 # räknar antalet inloggningsförsök

    while felaktig_inloggning: # sålänge inloggningen inte fungerar
        namn = input("Vänligen ange ditt namn: ")
        lösenord = input("Vänligen ange ditt lösenord: ")
        if namn in användare.keys() and användare[namn][0] == lösenord: # om användaren finns och lösenordet är rätt
            print("Du är inloggad!")
            return namn # returnera namnet på användaren som loggade in
            
        else: # om något gick fel
            print("Användarnamn eller lösenord är felaktigt. Du får totalt tre försök.")
            antal_försök += 1 # räkna upp antalet försök
        
        if antal_försök == 3: # om det har gjorts tre försök
            return False # returnera False, försöken är slut

def sätta_in_ta_ut(användare, nuvarande_användare): # hanterar insättning och uttag av pengar
    # funktionen tar in dictionaryn med användare och vilken användare som är inloggad nu, funktionen returnerar den uppdaterade dictionaryn med användare
    print("Du får välja mellan att:")
    print("1. Sätta in pengar")
    print("2. Ta ut pengar")
    val_i_meny = kontrollera_inmatning_meny(2) # ger menyvalet användaren gjorde

    # nedan if/else är för att utskriften ska bli snygg
    if val_i_meny == 1:
        handling = "sätta in"
    
    else:
        handling = "ta ut"

    felaktig_summa = True
    while felaktig_summa: # sålänge något är fel med summan som skrivs in
        try:
            summa = int(input(f"Ange den summa som du vill {handling}: "))
            if summa<0: # om användaren skrivit in ett negativt tal
                raise ValueError # då ska det bli fel
            elif val_i_meny == 2 and summa > användare[nuvarande_användare][1]: # om användaren försöker ta ut mer pengar än vad som finns
                raise ValueError # då ska det bli fel
            else: # annars om allt har gått rätt till
                felaktig_summa = False # då hoppar vi ur loopen
        except ValueError: # om något blev fel
            print("Du har matat in en felaktig eller för stor summa.")
    
    if val_i_meny == 1: # om användaren vill sätta in pengar
        användare[nuvarande_användare][1] = användare[nuvarande_användare][1]+summa # öka saldot
    
    else: # om användaren vill ta ut pengar
        användare[nuvarande_användare][1] = användare[nuvarande_användare][1]-summa # minska saldot
    
    return användare # returnera den uppdaterade dictionaryn med användare



def main(): # huvudfunktion som kör programmet
    inloggad = False # ingen är inloggad från start
    nuvarande_användare = None # håller koll på namnet på den som är inloggad
    användare = {} # håller koll på användare, nyckel är användarens namn och value är en lista med lösenord och saldo

    while True: # sålänge programmet körs
        if not inloggad: # om ingen är inloggad
            meny_ej_inloggad() # skriv menyn
            meny_val = kontrollera_inmatning_meny(3) # låt användaren välja i menyn

            if meny_val == 1: # om användaren vill skapa konto
                användare = skapa_konto(användare) # skapa konto
            
            elif meny_val == 2: # om användaren vill logga in
                nuvarande_användare = logga_in(användare) # kolla inloggning, håll koll på vem som är inloggad
                if nuvarande_användare == False: # om inloggningen inte lyckades, försöken tog slut
                    print("Inloggningen misslyckades.")
                else: # om inloggningen lyckades
                    print("Du är nu inloggad.")
                    inloggad = True # håller koll på att någon är inloggad
            
            elif meny_val == 3: # om användaren vill avsluta programmet
                return 0 # hoppa ur main
        
        else: # om någon är inloggad
            meny_inloggad() # skriv menyn
            meny_val = kontrollera_inmatning_meny(4) # låt användaren välja i menyn

            if meny_val == 1: # om användaren vill se sin information
                print(f"Du är inloggad med namnet {nuvarande_användare}")
                print(f"Ditt lösenord är {användare[nuvarande_användare][0]}")
                print(f"Ditt saldo är {användare[nuvarande_användare][1]} kr")
            
            elif meny_val == 2: # om användaren vill sätta in eller ta ut pengar
                användare = sätta_in_ta_ut(användare, nuvarande_användare) # sköter insättning och uttag

            elif meny_val == 3: # om användaren vill logga ut
                nuvarande_användare = None # håller koll på att ingen längre är inloggad
                inloggad = False # håller koll på att ingen längre är inloggad
                print("Du är nu utloggad.")

            elif meny_val == 4: # om användaren vill radera sitt konto
                försäkran_fel = True
                while försäkran_fel: # sålänge input blir fel på frågan
                    säker = input("Är du säker på att du vill radera ditt konto? Skriv J för ja och N för nej: ")
                    if säker == "J" or säker == "N": # ett giltigt svar på frågan
                        försäkran_fel = False # hoppa ur loopen
                    else: # om svaret inte är giltigt
                        print("Vänligen svara med J eller N.")
                if säker == "J": # om användaren helt säkert vill radera sitt konto
                    användare.pop(nuvarande_användare) # ta bort användaren
                    nuvarande_användare = None # rensar nuvarande användare
                    inloggad = False # ingen är längre inloggad
                    print("Din användare är borttagen och du är utloggad.")
                
                else: # om användaren ändrade sig och inte vill radera sitt konto
                    print("Okej, då skickas du tillbaka till menyn.")

main() # kör programmet