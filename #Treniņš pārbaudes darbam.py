#25/02/26
#Treniņš pārbaudes darbam

#1. uzdevums (2 punkti)
#Izskaidro:

#a) Kāpēc programmatūras izstrādē ir nepieciešama prasību specifikācija?
#b) Kas var notikt, ja kods tiek rakstīts bez skaidras specifikācijas?

#Atbilde: a) Lai  saprast uzdevumu un izpildīt to pēc prasībām.  
#b) Rezultāts var sanākt ne tāds, kādu gaida pasūtītājs vai arī var rasties kļūda.

#3. uzdevums (3 punkti)
#Sakārto programmatūras dzīves cikla posmus pareizā secībā:

#Testēšana
#Plānošana
#Uzturēšana
#Izstrāde
#Analīze

#Īsi paskaidro jebkurus divus no tiem.

#Atbilde: 1. Plānošana 2.Analīze 3.Izstrāde 4.Testēšana 5.Uzturēšana 
#Testēšana - Pārbaudam kā strādā kods un piefiksējam kļūdas.
#Izstrāde - Rakstam programmas kodu

#4. uzdevums 
#Dots apraksts:
#Programmētājs saglabā katru koda versiju, var atgriezties pie iepriekšējās versijas un strādāt komandā ar citiem.

#a) Kādu rīku viņš izmanto?
#b) Kādas ir 2 priekšrocības šim rīkam?

#Atbilde: a)GitHub un versiju vadības sistēmu.
#b)1.Pēc vajadzības var atrast jebkuru koda versiju. 
#2.Var bezgalīgi saglabāt jaunas koda versijas. 
#3.Var redzēt izmaiņu vēsturi

#5. uzdevums 
#Izskaidro jēdzienus ar piemēru:

#parametrs - Vērtība, ko nodod funkcijai. Piemērs: def summa(a, b):

#atgriežamā vērtība (return) - Vērtība, ko funkcija atgriež.

#loģiska izteiksme - Izteiksme ar rezultātu (True un False) Piemēram: x>5.

#datu tips - Datu veids, tādi kā :int, float, str, bool.

#mainīgais - ir nosaukums skaitlim vai vārdam, ko programma atceras.


#6. uzdevums 
#Specifikācija:

#Programma izvada tikai pāra skaitļus no 2 līdz 10.

#Kurš kods atbilst specifikācijai?

#A) for i in range(2,11):
#if i % 2 == 0:
#  print(i)

#B) for i in range(2,10,2):
#  print(i)

#C)for i in range(1,11):
#  print(i)

#Atzīmē pareizo/pareizos variantus un pamato.

#Atbilde: Pareizā atbilde ir A.

#7. uzdevums 

#Specifikācija:
#Izveido programmu, kas:
#izveido mainīgo vecums
#izvada tekstu:
#"Tev ir X gadi"

#Ievēro:
#korektu sintaksi
#koda stilu
#vismaz vienu komentāru

#Atbilde: 
vecums = 16
print("Tev ir",vecums,"gadi")

#8. uzdevums (4 punkti)
#Dots kods:

#skaitlis = input("Ievadi skaitli: ") 
#if skaitlis > 10:
#print("Lielāks par 10")
#else
#  print("Mazāks vai vienāds ar 10")

#a) Nosauc vismaz 3 kļūdas un paskaidro tās
#b) Uzraksti labotu kodu

#Atbilde a) 1.print bez atkāpes. 2. input atgriež string. 3.Pēc else nav kola
#b)skaitlis = int(input("Ievadi skaitli: "))
#if skaitlis > 10:
#  print("Lielāks par 10")
#else:
#  print("Mazāks vai vienāds ar 10")

#9. uzdevums 
#Specifikācija:

#Izveido funkciju kvadrats(skaitlis),
#kas atgriež skaitļa kvadrātu.

#Papildus:
#funkciju izsauc
#izdrukā rezultātu

#Atbilde
def kvadrats(skaitlis):
  return skaitlis * skaitlis
rezultats = kvadrats(5)
print(rezultats)

#10. uzdevums 
#Specifikācija:

#Izveido programmu, kas:
#pieprasa lietotājam ievadīt atzīmi (0–100)
#ja atzīme ≥ 90 → izvada "Izcili"
#ja atzīme ≥ 70 → izvada "Labi"
#citādi → izvada "Jāuzlabo"

#Programmai jābūt:
#ar komentāriem
#bez sintakses kļūdām
#ar pareizu zarošanos

atzime = int(input("Ievadi atzīmi (0-100):" )) #Ievada atzīmi
if atzime >= 90: #Parbauda vērtējumu
  print("Izcili")
elif atzime >= 70:
   print("Labi")
else: 
  print("Jāuzlabo")