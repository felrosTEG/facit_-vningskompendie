användare = {} # Sparar användare och deras saldo

kör = True

while kör: # sålänge programmet körs

    # menyn skrivs ut
    namn = input("Välkommen! Ange ditt namn: ")
    print("Här kommer de val du har:")
    print("1. Skapa ett nytt konto")
    print("2. Se ditt saldo")
    print("3. Ta ut pengar")
    print("4. Sätta in pengar")
    print("5. Avlsuta programmet")
    meny_val = input("Ange ditt val med en siffra: ") # tar in användarens val

    if meny_val == "1": # om skapa nytt konto
        användare[namn] = 0 # lägger till användaren med saldo 0
        print("Ditt konto är tillagt med saldot 0.")
        
    if meny_val == "2": # om se saldo
        saldo = användare[namn] # plockar ut saldot ur dictionaryn
        print(f"Ditt saldo är {saldo}") # skriver ut saldot
    
    if meny_val == "3": # om ta ut pengar
        summa = int(input("Hur mycket pengar vill du ta ut? "))
        saldo = användare[namn] # tar ut saldot
        saldo = saldo - summa # tar bort pengar
        användare[namn] = saldo # sätter in det nya saldot

    if meny_val == "4": # om sätta in pengar
        summa = int(input("Hur mycket pengar vill du sätta in (ange ett heltal)? "))
        saldo = användare[namn] # tar ut saldot
        saldo = saldo + summa # lägger till pengar
        användare[namn] = saldo # sätter in det nya saldot
    
    if meny_val == "5": # avslutar programmet om användaren valde det
        kör = False