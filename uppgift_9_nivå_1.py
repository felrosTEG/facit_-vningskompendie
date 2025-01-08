lösenord_fel = True
while lösenord_fel: # sålänge användaren misslyckas med att skapa ett lösenord
    lösenord = input("Välj ditt lösenord: ")

    if len(lösenord) >= 8: # om lösenordet är minst 8 tecken
        if lösenord != "lösenord" and lösenord != "Lösenord": # om det inte är lösenord eller Lösenord
            siffra = False # antar att det inte finns någon siffra
            for tecken in lösenord: # kollar på varje tecken i lösenordet
                if tecken.isnumeric(): # om tecknet är en siffra
                    siffra = True # då finns det en siffra
                    break # då behöver vi inte kolla resten av tecknena
            
            if siffra: # om det fanns minst en siffra
                print("Ditt lösenord är okej!")
                lösenord_fel = False # då hoppar vi ur while-loopen

    else: # om lösenordet inte är okej
        print("Ditt lösenord är inte okej. Det behöver innehålla minst 8 tecken, minst en siffra och får inte vara \"lösenord\" eller \"Lösenord\"")
        print("Du får försöka igen.")