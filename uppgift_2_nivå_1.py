ord_att_testa = input("Skriv in ett ord så avgör jag om det är ett palindrom: ")
ord_att_testa = ord_att_testa.lower() # gör om alla bokstäver till små
ord_lista = list(ord_att_testa) # gör ordet till en lista med bokstäver
bakvänd_ord_lista = ord_lista.copy() # gör en kopia av listan för att kunna ha en som är omvänd
bakvänd_ord_lista.reverse() # vänder kopian så att den är bakochfram


if ord_lista == bakvänd_ord_lista: # om det är likadant både framåt och bakåt
    print("Det är ett palindrom")

else:
    print("Det är inte ett palindrom")