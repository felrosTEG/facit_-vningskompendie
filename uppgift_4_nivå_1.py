vokaler = ("a", "o", "u", "å", "e", "i", "y", "ä", "ö") # Vi behöver inte tänka på skiljetecken, bokstäver som inte är vokaler är alltså kontonanter

mening = input("Skriv in meningen som du vill veta om den är komplicerad")
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

if ord_fler_än_fyra_konsonanter > 3 and ord_längre_än_fem > 3: # kollar om texten är komplicerad
    print("Din text är komplicerad!")

else:
    print("Din text är inte komplicerad.")

