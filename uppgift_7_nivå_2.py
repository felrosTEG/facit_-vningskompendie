import random # för att kunna slumpa fram tärningskast

def kontrollera_heltal_inmatning(): # kontrollerar input med heltal
    # funktionen tar inte in något, funktionen returnerar ett tal användaren har skrivit in
    while True: # kör sålänge inmatningen är fel
        try:
            tal = int(input()) # tar in svaret på frågan
            return tal # ger tillbaka talet användaren skrev in
        except ValueError: # om användaren inte skrev in ett heltal
            print("Ditt tal är inte ett heltal, försök igen.") # då får hen försöka igen


def kasta_tärningar(antal_kast, antal_tärningar): # kastar tärningar och sammanställer resultaten
    # funktionen tar in antal kast och antal tärningar, funktionen returnerar en sammanställning av resultaten i form av en dictionary
    antal_resultat = {} # räknar antaler av de olika resultaten

    for i in range(antal_kast): # slår rätt antal tärningskast
        kast_resultat = [] # sparar resultatet från de olika tärningarna
        for j in range(antal_tärningar): # för antalet tärningar
            resultat = random.randint(1,6) # slår tärningen
            kast_resultat.append(resultat) # lägger till i listan med resultat från de olika tärningarna
        summa = sum(kast_resultat) # räknar summan för alla tärningar
        if summa in antal_resultat.keys(): # om summan redan har räknats någon gång
            antal_resultat[summa] = antal_resultat[summa] + 1 # då adderar vi till hur många gånger summan har räknats
        else: # om summan aldrig har räknats förut
            antal_resultat[summa] = 1 # då har den nu räknats en gång
    
    return antal_resultat # returnerar sammanställningen i form av en dictionary


def main(): # huvudfunktion som kör programmet
    print("Skriv in hur många tärningar du vill kasta: ", end = "") # avslutas med "" istället för standard som är endline för att göra det snyggare
    antal_tärningar = kontrollera_heltal_inmatning() # tar in antal tärningar från användaren
    print("Skriv in hur många kast du vill ska göras: ", end = "") # avslutas med "" istället för standard som är endline för att göra det snyggare
    antal_kast = kontrollera_heltal_inmatning() # tar in antal kast från användaren
    resultat_sammanställning = kasta_tärningar(antal_kast, antal_tärningar) # får ett sammanställt resultat
    
    lista_med_resultat = list(resultat_sammanställning.keys()) # gör en lista med nycklarna som är de olika möjliga resultaten
    lista_med_resultat.sort() # sorterar listan för att utskriften ska bli i en fin ordning
    for resultat in lista_med_resultat: # skriver ut alla resultat efter varandra
        print(f"{resultat}: {resultat_sammanställning[resultat]}")
    
main() # kör programmet
