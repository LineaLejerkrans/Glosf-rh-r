#Johanna Genander Linéa Lejerkrans
# 19-09-22
#jämför användarens svar med dett rätta svaret 
def forhor(sve, eng):
    svar=input("Skriv '" + sve + "' på engelska: ")
    if svar.lower()==eng:
        return(1) #retuneras om det är rätt
            
    else:
        return(0) #retuneras om det är fel 

#funktionen tar in två listor med ord där den för varje ordpar anropar funktionen forhor för jämförning
def lista(lista1, lista2):
    poang=0
    for i in range(len(lista1)):
        if forhor(lista1[i], lista2[i]) == 1:
            print("Det är korrekt!")
            poang += 1

        else: 
            print("Det är tyvärr fel. \nDet rätta svaret är: " + lista2[i])

    return poang

#anropar funktionen lista med två listor med ord skriver sedan med returvärdet ut vilken poäng du fick
def main():
    svenska=["katt", "hund", "gris", "fågel", "råtta", "orm"]
    engelska=["cat", "dog", "pig", "bird", "rat", "snake"]  
    poang = lista(svenska, engelska)

    print("Du fick " + str(poang) + " poäng")

main()
