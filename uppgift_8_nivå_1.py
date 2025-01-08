näst_senaste = 0 # håller koll på det näst senaste talet som är 0 från början
senaste = 1 # håller koll på det senaste talet som är 1 från början

antal_tal = int(input("Hur många fibonaccital vill du beräkna? "))

print(näst_senaste) # skriver ut det första talet
print(senaste) # skriver ut det andra talet
for i in range(2, antal_tal): # loopar igenom resten av talen
    nytt_tal = näst_senaste + senaste # beräknar det nya talet
    print(nytt_tal) # skriver ut det nya talet
    näst_senaste = senaste # det senaste talet blir nu det näst senaste
    senaste = nytt_tal # det nya talet blir nu det senaste talet
