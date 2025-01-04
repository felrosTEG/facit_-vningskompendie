# Omvandlingskonstanter
kilometer_till_mile = 1.606
celsius_till_fahrenheit_multiplier = 9.0/5.0
celsius_till_fahrenheit_add = 32
cup_to_deciliter = 2.366
kg_to_pound = 0.454

kör = True

while kör: # Så länge programmet körs
    print("Välkommen, du får nu välja vilken enhetskonvertering du vill göra.")
    print("1. kilometer till engelska miles")
    print("2. engelska miles till kilometer")
    print("3. celcius till fahrenheit")
    print("4. fahrenheit to celsius")
    print("5. deciliter till cup")
    print("6. cup till deciliter")
    print("7. kg till pound")
    print("8. pund till kg")
    val = input("skriv in ditt val från menyn: ") # Användarens val i menyn

    att_omvandla = float(input("Skriv in hur många av din enhet du har: "))
    
    # Beräknar det nya värdet beroende på användarens input
    if val == "1":
        omvandlad = att_omvandla*kilometer_till_mile
    
    elif val == "2":
        omvandlad = att_omvandla/kilometer_till_mile
    
    elif val == "3":
        omvandlad = att_omvandla * celsius_till_fahrenheit_multiplier + celsius_till_fahrenheit_add
    
    elif val == "4":
        omvandlad = (att_omvandla - celsius_till_fahrenheit_add) / celsius_till_fahrenheit_multiplier
    
    elif val == "5":
        omvandlad = att_omvandla / cup_to_deciliter
    
    elif val == "6":
        omvandlad = att_omvandla * cup_to_deciliter
    
    elif val == "7":
        omvandlad = att_omvandla * kg_to_pound
    
    elif val == "8":
        omvandlad = att_omvandla / kg_to_pound

    print(f"Din nya omvandlade mängd är: {omvandlad}") # Skriver ut svaret

    avsluta = input("Vill du avsluta programmet? Skriv A, annars tryck enter: ")
    if avsluta == "A": # Om användaren vill avsluta programmet så kommer loopen att brytas
        kör = False

