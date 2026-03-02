#08/02
#Treniņa uzdevums: Python cikls while

# 1. uzdevums – skaitītājs (number)
#Izmanto ciklu while, lai: izvadītu skaitļus no 1 līdz 10

skaitlis = 1 
while skaitlis <= 10:
    print(skaitlis)
    skaitlis += 1 

#2. uzdevums – pāra skaitļi
#Izmanto ciklu while, lai: izvadītu tikai pāra skaitļus no 1 līdz 20

skaitlis = 1

while skaitlis <= 20:
    if skaitlis % 2 == 0:

        print(skaitlis)
    skaitlis += 1

#3. uzdevums – teksts (string)
#Dots teksts:
text = "Python"

#Izmanto ciklu while, lai: izvadītu katru burtu atsevišķā rindā
i = 0
while i < len(text):
    print(text[i])
    i += 1

#4. uzdevums – saraksts (list)
#Dots saraksts:
 
numbers = [3, 6, 1, 8, 4]
 
#Izmanto ciklu while, lai: izvadītu visus saraksta elementus, saskaitītu un izvadītu visu skaitļu summu
i = 0
summa = 0

while i < len(numbers):
    print(numbers[i])
    summa += numbers[i]
    i += 1  

print("Summa:", summa)

#5. uzdevums – nosacījums (⭐)
#Izmanto ciklu while, lai: palielinātu skaitli number, līdz tas kļūst lielāks par 50

number = 5

while number <= 50:
    print(number)
    number += 1 
 