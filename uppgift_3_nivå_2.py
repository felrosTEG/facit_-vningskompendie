def kontrollera_enhet(omvandlingar): # Sköter input av enhet som ska omvandlas och ser till att det blir rätt
    # Funktionen tar in dictionaryn med enheter och returnerar enheterna som ska omvandlas från och till
    felaktig_enhet = True

    while felaktig_enhet: # Så länge inputen är felaktig får användaren fortsätta försöka
        enhet_från = input("Ange vilken enhet du vill omvandla från: ")
        if enhet_från in omvandlingar.keys(): # Om enheten finns bland tillåtna enheter
            enhet_till = omvandlingar[enhet_från][0] # Tar ut vilken enhet omvandlingen sker till utifrån dictionaryn
            return enhet_från, enhet_till # Returnerar enhet till och enhet från
        else: # Om inmatningen är fel
            print("Du har angivit en enhet som inte går att välja.")
            print("Vänligen ange km, miles, dl, cup, kg eller pound.")

def beräkna_enhet(enhet_från, enhet_till, omvandlingar): # Beräknar värdet och skriver ut omvaningen
    # Tar in enheterna som ska omvanldas från och till och dictionaryn med enheter. Returnerar ingenting. 
    antal_fel = True

    while antal_fel: # Sålänge inmatningen är fel
        try:
            antal_in = float(input(f"Hur många {enhet_från} vill du omvandla? Ange ett decimaltal (med .): ")) # Hur många av enheten som ska omvandlas
            antal_ut = antal_in * omvandlingar[enhet_från][1] # Sköter omvandlingen genom talet som finns i dictionaryn med enheter
            print(f"{antal_in} {enhet_från} är {round(antal_ut,2)} {enhet_till}") # Snygg utskrift
            antal_fel = False # Bryter loopen om allt har gått rätt till
        except ValueError: # Om användaren inte skriver in en float
            print("Du skrev inte in ett korrekt decimaltal, du får försöka igen.")



def main(): # Huvudfunktionen som kör hela programmet
    omvandlingar = {
        "km":["miles", 1/1.606],
        "miles":["km", 1.606],
        "dl":["cup", 1/2.366],
        "cup":["dl", 2.366],
        "kg":["pound", 0.454],
        "pound":["kg", 1/0.454]
    } # En dictionary som lagrar enheter, det de kan omvandlas till samt det tal som ska multipliceras med för att omvandla

    kör = True

    while kör: # Programmet körs om och om igen
        print("Välkommen! Du får nu följande val:")
        print("De omvandlingar du kan göra är följande:")
        print("\tmellan km och miles")
        print("\tmellan dl och cup")
        print("\tmellan kg och pound")
        enhet_från, enhet_till = kontrollera_enhet(omvandlingar) # Får fram enheterna som ska omvandlas från och till

        beräkna_enhet(enhet_från, enhet_till, omvandlingar) # Beräknar och skriver ut omvandlingen

        print()
        avsluta = input("Tack för att du omvandlade! Om du vill avsluta programmet, skriv A, annars tryck vad som helst.")
        if avsluta == "A": # Bryter loopen om användaren vill avsluta programmet
            return 0
        
main() # Ser till att mainfunktionen körs