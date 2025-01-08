def kontrollera_input(): # kontrollerar input av heltal så att det inte kraschar
    # funktionen tar inte in något och returnerar talet som användaren skrivit in
    felaktig_inmatning = True
    while felaktig_inmatning: # sålänge inmatningen är fel
        try:
            tal = int(input("Skriv in ditt tal: ")) # användaren skriver in ett tal
            return tal # returnerar talet användaren skrev in
        except ValueError: # om det inte var ett heltal
            print("Ditt tal är inte ett heltal, försök igen.")

def skriv_ut_tal(start,slut, aktuellt_tal): # skriver ut multiplikationerna snyggt
    # funktionen tar in ett starttal ett sluttal och det aktuella talet som vi utgår ifrån av de två valda talen
    for tal_multiplicera in range(start,slut): # loopar igenom de multiplikationer som ska skrivas ut
        svar = tal_multiplicera * aktuellt_tal # räkna ut svaret på multiplikationen
        print(f"{aktuellt_tal} * {tal_multiplicera} = {svar}") # skriv ut det snyggt

def main(): # huvudfunktion som kör programmet
    tal_1 = kontrollera_input() # användarens första valda tal
    tal_2 = kontrollera_input() # användarens andra valda tal
    
    if tal_1 < tal_2: # om det första talet är mindre än det andra
        skriv_ut_tal(tal_1, tal_2+1, tal_1) # skriver ut första omgången multiplikationer
        skriv_ut_tal(tal_1+1, tal_2+1, tal_2) # skriver ut andra omgången av multiplikationer
    
    elif tal_2 < tal_1: # om det andra talet är mindre än det första
        skriv_ut_tal(tal_2, tal_1+1, tal_2) # skriver ut första omgången av multiplikationer
        skriv_ut_tal(tal_2+1, tal_1+1, tal_1) # skriver ut andra omgången av multiplikationer
    
    else: # om talen är lika stora
        print(f"{tal_1} * {tal_2} = {tal_1*tal_2}") # då finns bara en multiplikation som ska skrivas ut

main() # kör programmet
