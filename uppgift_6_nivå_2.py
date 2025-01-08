tal_1 = int(input("Skriv in ditt första tal: ")) # tar in det första talet
tal_2 = int(input("Skriv in ditt andra tal: ")) # tar in det andra talet

for tal_multiplicera in range(tal_1, tal_2+1): # för alla tal av första delen (tex mellan 9 och 13 om det är de två talen)
    svar = tal_1 * tal_multiplicera # räkna ut svaret på multiplikationen
    print(f"{tal_1} * {tal_multiplicera} = {svar}") # skriver ut det snyggt

for tal_multiplicera_2 in range(tal_1+1,tal_2+1): # för de multiplikationer som är kvar (mellan 10 och 13 om talen är 9 och 13)
    svar_2 = tal_multiplicera_2 * tal_2 # räkna ut svaret på multiplikationen
    print(f"{tal_2} * {tal_multiplicera_2} = {svar_2}") # skriv ut det snyggt

