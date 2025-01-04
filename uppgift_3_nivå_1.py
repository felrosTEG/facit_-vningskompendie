# Omvandlingskonstanter
mile_till_kilometer = 1.606
cup_to_deciliter = 2.366
kg_to_pound = 0.454

kör = True

while kör: # Så länge programmet körs
    print("Välkommen, du får nu välja vilken enhetskonvertering du vill göra.")
    print("1. kilometer till engelska miles")
    print("2. engelska miles till kilometer")
    print("3. deciliter till cup")
    print("4. cup till deciliter")
    print("5. kg till pound")
    print("6. pund till kg")
    val = input("skriv in ditt val från menyn: ") # Användarens val i menyn

    att_omvandla = float(input("Skriv in hur många av din enhet du har: "))
    
    # Beräknar det nya värdet beroende på användarens input
    if val == "1":
        omvandlad = att_omvandla / kilometer_till_mile
    
    elif val == "2":
        omvandlad = att_omvandla * kilometer_till_mile
    
    elif val == "3":
        omvandlad = att_omvandla / cup_to_deciliter
    
    elif val == "4":
        omvandlad = att_omvandla * cup_to_deciliter
    
    elif val == "5":
        omvandlad = att_omvandla * kg_to_pound
    
    elif val == "6":
        omvandlad = att_omvandla / kg_to_pound

    print(f"Din nya omvandlade mängd är: {omvandlad}") # Skriver ut svaret

    avsluta = input("Vill du avsluta programmet? Skriv A, annars tryck enter: ")
    if avsluta == "A": # Om användaren vill avsluta programmet så kommer loopen att brytas
        kör = False

