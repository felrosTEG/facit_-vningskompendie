
def main():
    skiljetecken = (".","!",",","?")
    mening_att_testa = input("Skriv in ett ord eller en mening så avgör jag om det är ett palindrom: ")

    for tecken in skiljetecken:
        mening_att_testa = mening_att_testa.replace(tecken,"")

    mening_att_testa.lower()

    mening_lista = mening_att_testa.split()
    omvänd_lista = mening_lista.copy()


    if mening_lista == omvänd_lista:
        print("Det är ett palindrom")

    else:
        print("Det är inte ett palindrom")

main()