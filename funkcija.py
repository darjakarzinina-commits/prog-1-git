#05/02

#Funkcijas
#Funkcijas pamatstruktura

#def funkcijas_nosaukums(parametri):
#darbības
#return rezultāts

#def - atslēgvārds funkcijas izveidei
#parametri - dati, ko funkcija saņem
#return - vērtība, ko funkcija atgriež (nav obliģāta)


#Piemers ar skaitļiem (number)
#Funkcija, kas aprēķina divu skaitļu summu
def summa(a,b):
     return a + b
print(summa(1,2))
print(summa(2,4)+5)

def summa(a,b):
     rezultats = a + b
     print(rezultats)
summa(1,1)
#print(summa(2,4)+5)

#Piemērs ar sarakstu (lists)
#Funnkcija, kas saskaita elementu sarakstā
def elementu_skaits(saraksts):
    skaits = 0
    for elements in saraksts:
         skaits += 1
         return skaits
    print(elementu_skaits([3,7,1,9])) 

#Piemērs ar vārdnīcu (dictionary)
#Funkcija, kas pārbauda vai vārdnīca ir noteikta atslēga
def vai_ir_atslega(dati,atslega):
     if atslega in dati:
          return "Atslēga ir atrasta"
     else:
          return "Atslēga nav atrasta"
students = {
 "vards": "Jānis", 
 "vecums": 16    
}
print(vai_ir_atslega(students, "vecums"))
     
