#23/04
#Datu validācija

#Lietotāja ievade
vecums =  input("Ievadi vecumu:")
print(vecums)

#Pārbauda, vai ir skaitlis
if vecums.isdigit(): #metode isdigit() pārbauda, vai dotie dati ir skaitlis un atgriež TRUE/FALSE vērtību
    print("Ir skailis")
    #Vecuma pārbaude
    if int(vecums) >= 18:
      print("Skolēns ir pilngadīgs.")
    else:
      print("Skolēns nav pilngadīgs.")    
else:
    print("Nav skaitlis")

