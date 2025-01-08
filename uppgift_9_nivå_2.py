def längd(lösenord): # kollar om längden på lösenordet är okej
    # funktionen tar in lösenordet och returnerar om längden är okej
    if len(lösenord) >= 8:
        return True # om den är okej returneras true
    else:
        return False # om den inte är okej returneras false

def enkelt(lösenord): # kollar om lösenordet är för enkelt
    # tar in lösenordet och returnerar true om det är okej och false om det är för enkelt
    if lösenord == "lösenord" or lösenord == "Lösenord":
        return False
    else:
        return True

def kolla_tecken(lösenord): # kollar saker som har med tecken och göra
    # funktionen tar in lösenord och returnerar hur lösenordet ligger till utifrån ett antal krav
    siffra = False # håller koll på om det finns en siffra i lösenordet
    stor_bokstav = False # håller koll på om det finns en stor bokstav i lösenordet
    frågetecken = False # håller koll på om det finns ett frågetecken i lösenordet
    utropstecken = False # håller koll på om det finns ett utropstecken i lösenordet
    bindestreck = False # håller koll på om det finns ett bindestreck i lösenordet
    fler_av_samma = False # håller koll på om det finns fler än tre av samma tecken i lösenordet

    for tecken in lösenord: # kollar på varje tecken i lösenordet
        if tecken.isnumeric(): # om tecknet är en siffra
            siffra = True # då finns det en siffra
        if tecken.isupper(): # kollar om tecknet är en stor bokstav
            stor_bokstav = True
        if tecken == "?": # kollar om tecknet är ett frågetecken
            frågetecken = True
        if tecken == "!": # kollar om tecknet är ett utropstecken
            utropstecken = True
        if tecken == "-": # kollar om tecknet är ett bindestreck
            bindestreck = True
        if lösenord.count(tecken)>3: # kollar om det finns fler än tre av tecknet i ordet
            fler_av_samma = True
    
    return siffra, stor_bokstav, frågetecken, utropstecken, bindestreck, fler_av_samma # ger tillbaka alla variabler som håller koll på lösenordet

def kolla_lösen(lösenord): # kollar om lösenordet är okej
    # tar in lösenordet och returnerar true om det är okej och false om det inte är okej
    längd = längd(lösenord) # kollar längden
    enkelt = enkelt(lösenord) # kollar om det är för enkelt
    siffra, stor_bokstav, frågetecken, utropstecken, bindestreck, fler_av_samma = kolla_tecken(lösenord) # kollar resterande faktorer

    # räknar ihop för att kunna avgöra om lösenordet innehåller två olika av de tre tecknena ["?", "!", "-"]
    if frågetecken:
        frågetecken = 1
    if utropstecken:
        utropstecken = 1
    if bindestreck:
        bindestreck = 1

    if längd and enkelt and siffra and stor_bokstav and not fler_av_samma: # om alla utom skiljetecknena är okej
        if frågetecken + utropstecken + bindestreck >= 2: # om minst två av skiljetecknena finns med
            return True # då är lösenordet okej
        else:
            return False # annars inte okej
    
    else:
        return False # annars inte okej

def skriv_info(): # skriver info om vad som krävs av lösenordet
    print("Ditt lösenord behöver uppfylla följande krav:")
    print("1. Lösenordet behöver vara minst 8 tecken långt")
    print("2. Lösenordet behöver innehålla en siffra")
    print("3. Lösenordet får inte vara \"lösenord\" eller \"Lösenord\"")
    print("4. Lösenordet behöver innehålla minst en stor bokstav")
    print("5. Lösenordet behöver innehålla två olika av tecknena [ !, ?, - ]")
    print("6. Lösenordet får inte ha fler än tre av samma bokstav")



def main(): # huvudfunktion som kör programmet
    while True: # sålänge lösenordet inte är okej
        lösenord = input("Skriv in ditt valda lösenord: ")
        lösen_okej = kolla_lösen(lösenord) # kollar om lösenordet är okej
        if lösen_okej: # om det är okej
            print("Ditt lösenord är godkänt!")
            return 0 # avsluta programmet
        else: # om det inte är okej
            print("Ditt lösen är inte okej.")
            skriv_info() # skriver ut information

main() # kör programmet
