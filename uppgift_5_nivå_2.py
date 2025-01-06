def meny_ej_inloggad():
    print("Välkommen till vår bank!")
    print("Du har följande val:")
    print("1. Skapa ett nytt konto hos banken")
    print("2. Logga in på ditt konto")
    print("3. Avsluta programmet")

def meny_inloggad():
    print("Du har nu följande val:")
    print("1. Se kontouppgifter (inklusive saldo)")
    print("2. Sätta in eller ta ut pengar")
    print("3. Logga ut")
    print("4. Avsluta ditt konto hos banken")

def kontrollera_inmatning_meny(antal_val):
    fel_val = True
    
    while fel_val:
        try:
            val = int(input("Vänligen ange numret för ditt val: "))
            if val in range(1,antal_val+1):
                return val # Om det blir rätt så returnerar vi valet, då bryts funktionen helt
            else:
                raise ValueError
        except ValueError:
            print("Felaktig input, du får försöka igen. Välj den siffra som motsvarar ditt val.")


def skapa_konto(användare):
    print("Vad roligt att du vill skapa ett konto hos oss!")
    inkorrekt_inmatning = True

    while inkorrekt_inmatning:
        namn = input("Vad är ditt namn? ")
        if namn == "" or namn == " ":
            print("Ditt namn behöver innehålla något, du får försöka igen.")
        elif namn in användare.keys():
            print("Det namnet finns redan, du får välja ett annat.")
        else:
            inkorrekt_inmatning = False
    
    lösenord = input("Vänligen ange det lösenord du vill ha.")
    användare[namn] = [lösenord, 0]
    print("Ditt konto är nu skapat!")
    
    return användare

def logga_in(användare):
    felaktig_inloggning = True
    antal_försök = 0

    while felaktig_inloggning:
        namn = input("Vänligen ange ditt namn: ")
        lösenord = input("Vänligen ange ditt lösenord: ")
        if namn in användare.keys() and användare[namn][0] == lösenord:
            print("Du är inloggad!")
            return namn
            
        else:
            print("Användarnamn eller lösenord är felaktigt. Du får totalt tre försök.")
            antal_försök += 1
        
        if antal_försök == 3:
            return False

def sätta_in_ta_ut(användare, nuvarande_användare):
    print("Du får välja mellan att:")
    print("1. Sätta in pengar")
    print("2. Ta ut pengar")
    val_i_meny = kontrollera_inmatning_meny(2)

    if val_i_meny == 1:
        handling = "sätta in"
    
    else:
        handling = "ta ut"

    felaktig_summa = True
    while felaktig_summa:
        try:
            summa = int(input(f"Ange den summa som du vill {handling}: "))
            if val_i_meny == 2 and summa > användare[nuvarande_användare][1]:
                raise ValueError
            else:
                felaktig_summa = False
        except ValueError:
            print("Du har matat in en felaktig eller för stor summa.")
    
    if val_i_meny == 1:
        användare[nuvarande_användare][1] = användare[nuvarande_användare][1]+summa
    
    else:
        användare[nuvarande_användare][1] = användare[nuvarande_användare][1]-summa
    
    return användare



def main():
    inloggad = False
    nuvarande_användare = None
    användare = {}

    while True:
        if not inloggad:
            meny_ej_inloggad()
            meny_val = kontrollera_inmatning_meny(3)

            if meny_val == 1:
                användare = skapa_konto(användare)
            
            elif meny_val == 2:
                nuvarande_användare = logga_in(användare)
                if nuvarande_användare == False:
                    print("Inloggningen misslyckades.")
                else:
                    print("Du är nu inloggad.")
                    inloggad = True
            
            elif meny_val == 3:
                return 0
        
        else:
            meny_inloggad()
            meny_val = kontrollera_inmatning_meny(4)

            if meny_val == 1:
                print(f"Du är inloggad med namnet {nuvarande_användare}")
                print(f"Ditt lösenord är {användare[nuvarande_användare][0]}")
                print(f"Ditt saldo är {användare[nuvarande_användare][1]} kr")
            
            elif meny_val == 2:
                användare = sätta_in_ta_ut(användare, nuvarande_användare)

            elif meny_val == 3:
                nuvarande_användare = None
                inloggad = False
                print("Du är nu utloggad.")

            elif meny_val == 4:
                försäkran_fel = True
                while försäkran_fel:
                    säker = input("Är du säker på att du vill radera ditt konto? Skriv J för ja och N för nej: ")
                    if säker == "J" or säker == "N":
                        försäkran_fel = False
                    else:
                        print("Vänligen svara med J eller N.")
                if säker == "J":
                    användare.pop(nuvarande_användare)
                    nuvarande_användare = None
                    inloggad = False
                    print("Din användare är borttagen och du är utloggad.")
                
                else:
                    print("Okej, då skickas du tillbaka till menyn.")

main()