
def kontrollera_antal_tal(): # kontrollerar inmatning av antal tal som ska skrivas ut
    # funktionen tar inte in något, funktionen returnerar ett tal användaren har skrivit in
    while True: # kör sålänge inmatningen är fel
        try:
            tal = int(input("Hur många tal i talföljden vill du skriva ut? "))
            return tal # ger tillbaka talet användaren skrev in
        except ValueError: # om användaren inte skrev in ett heltal
            print("Ditt tal är inte ett heltal, försök igen.") # då får hen försöka igen

def kontrollera_starttal(): # kontrollerar inmatningen av starttalen
    # funktionen tar inte in något, funktionen returnerar de två starttalen
    while True: # sålänge inmatningen är fel körs denna
        try:
            tal_1 = int(input("Skriv in ditt första starttal: "))
            tal_2 = int(input("Skriv in ditt andra starttal: "))
            
            if tal_1 >= 0 and tal_2 >= 0: # om starttalen är större än ellerr lika med 0
                if tal_1 < tal_2: # om det första talet är mindre än det andra
                    return tal_1, tal_2 # då är allt bra och talen returneras
                else:
                    print("Det första talet måste vara mindre än det andra.") # ger felmeddelande
            else:
                print("Båda talen måste vara större än eller lika med 0.") # ger felmeddelande
        
        except ValueError: # om något av talen inte var ett heltal
            print("Du måste skriva in heltal.")

def fibonacci(näst_senaste, senaste, antal_tal): # räknar ut och skriver ut talföljden
    # funktionen tar in strattalen och antal tal som ska skrivas ut
    print(näst_senaste) # skriver ut det första talet
    print(senaste) # skriver ut det andra talet
    for i in range(2, antal_tal): # loopar igenom resten av talen
        nytt_tal = näst_senaste + senaste # beräknar det nya talet
        print(nytt_tal) # skriver ut det nya talet
        näst_senaste = senaste # det senaste talet blir nu det näst senaste
        senaste = nytt_tal # det nya talet blir nu det senaste talet

def main(): # huvudfunktion som kör programmet
    näst_senaste, senaste = kontrollera_starttal() # tar fram starttalen
    antal = kontrollera_antal_tal() # tar fram antalet tal
    fibonacci(näst_senaste, senaste, antal) # beräknar talföljden och skriver ut talen

main() # kör programmet