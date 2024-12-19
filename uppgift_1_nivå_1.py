varor_i_affär = ("mjölk", "smör", "mjöl", "juice", "paprika", "gurka") # affärens varor ändras inte, därför valde jag tuple

kundkorg = [] # där kundens varor kommer att läggas

handlar = True # för att se till att programmet kan avslutas eller fortsätta

while handlar: # sålänge någon kund fortfarande handlar
    print("Välkommen till affären, de varor vi har idag är:")
    varu_nummer = 0 # för att lättare kunna hålla koll på vilken vara kunden vill köpa
    for vara in varor_i_affär: # skriver ut alla varor med deras nummer framför
        print(varu_nummer, vara)
        varu_nummer += 1 # öka numret för varje vara
    
    varor_input = input("Vänligen ange numret på de varor du vill köpa. Separera med kommatecken: ")
    varor_att_köpa = varor_input.split(",") # delar upp numrena som användaren skrev in till en lista

    for nummer in varor_att_köpa: # loopar igenom listan med nummer på varor som användaren ville köpa
        index = int(nummer) # måste göra om till int om det ska kunna användas som index
        kundkorg.append(varor_i_affär[index]) # lägger till varan kunden ville köpa i hens kundkorg
    
    print("Tack! Här är ditt kvitto: ")
    for köpt_vara in kundkorg: # skriver ut varorna kunden har köpt
        print(köpt_vara)
    
    fortsätta = input("Vill en ny kund handla eller vill du avsluta? Skriv N för ny kund och A för avsluta. ")
    if fortsätta == "A": # om affären ska avslutas så kommer while-loopen inte att köras igen
        handlar = False