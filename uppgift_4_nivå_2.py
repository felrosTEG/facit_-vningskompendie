def kolla_mening(mening): # Funktion som avgör om en mening är komplicerad.
    # Funktionen tar in en mening och returnerar en bool som anger om meningen är komplicerad eller inte
    vokaler = ("a", "o", "u", "å", "e", "i", "y", "ä", "ö") # Vi behöver inte tänka på skiljetecken, bokstäver som inte är vokaler är alltså kontonanter

    ord_lista = mening.split() # Delar upp meningen i en lista med ord

    ord_fler_än_fyra_konsonanter = 0 # räknar antal ord med många konsonanter
    ord_längre_än_fem = 0 # räknar långa ord

    for ordet in ord_lista: # loopar igenom alla ord i listan
        if len(ordet)>5: # om ordet är längra än 5 bokstäver
            ord_längre_än_fem += 1 # då räknas det som ett långt ord
        
        antal_konsonanter = 0 # räknar konsonanter i ordet
        for bokstav in ordet: # loopar igenom ordets bokstäver
            if bokstav not in vokaler: # om det är en konsonant
                antal_konsonanter += 1
        
        if antal_konsonanter > 4: # om det hade många konsonanter så ska det räknas till ord med många konsonanter
            ord_fler_än_fyra_konsonanter += 1

    if ord_fler_än_fyra_konsonanter > 3 and ord_längre_än_fem > 3: # kollar om meningen är komplicerad
        return True # returnerar true om meningen är komplicerad

    else:
        return False # returnerar false om meningen inte är komplicerad
    
def main(): # huvudfunktion som kär programmet
    kör = True
    while kör: # sålänge programmet ska forstsätta
        text = input("Var vänlig skriv in din text. Använd endast skiljetecken ., ! och ? samt bokstäver. Inga radbrytningar får finnas med.\n")
        text = text.replace("!",".") # byter ut alla ! mot . för att underlätta split sen
        text = text.replace("?",".") # byter ut alla ? mot . för att underlätta split sen
        meningar = text.split(".") # delar upp texten i meningar
        antal_komplicerade = 0 # håller koll på antalet komplicerade meningar

        for mening in meningar: # loopar igenom alla meningar
            if mening == " " or mening == "": # för att inte räkna tomma meningar
                meningar.remove(mening) # vi vill inte ha med tomma meningar
            else: # för icke-tomma meningar
                komplicerad = kolla_mening(mening) # kolla om den är komplicerad
                if komplicerad: # räknar upp antal komplicerade
                    antal_komplicerade += 1
        
        antal_meningar = len(meningar) # antalet meningar räknas här för att inte få med eventuella tomma meningar

        if antal_komplicerade == 0: # för att undvida division med 0
            print("Texten är inte komplicerad.")

        elif antal_meningar/antal_komplicerade <2: # om fler än hälften är komplicerade
            print("Texten är komplicerad!")
        
        else:
            print("Texten är inte komplicerad.")
        
        avsluta = input("Om du vill avsluta programmet, skriv A. Annars tryck enter. ")
        if avsluta == "A": # om användaren vill avsluta programmet
            return 0

main() # kör huvudfunktionen