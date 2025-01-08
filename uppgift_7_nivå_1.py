import random # för att kunna slå tärning behövs random

antal_kast = [0,0,0,0,0,0] # räknar antaler av de olika resultaten

for i in range(10000): # slår 10 000 tärningskast
    resultat = random.randint(1,6) # slår tärningen
    antal_kast[resultat-1] = antal_kast[resultat-1]+1 # lägger till resultatet på rätt ställe i listan

# skriver ut fint
print(f"ettor: {antal_kast[0]}")
print(f"tvåor: {antal_kast[1]}")
print(f"treor: {antal_kast[2]}")
print(f"fyror: {antal_kast[3]}")
print(f"femmor: {antal_kast[4]}")
print(f"sexor: {antal_kast[5]}")