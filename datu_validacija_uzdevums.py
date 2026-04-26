#Datu validācija
#26/04

#Prasa lietotājam ievadīt vārdu
vards = input("Ievadi savu vārdu:")
print (vards)

#Pārbaude
#vai ievade nav tukša
if len(vards) > 0: 
 print("OK")
else: 
 print("Nepareiza ievade")

#vai sākas ar lielo burtu
if vards[0].isupper():
 print("OK")
else: 
 print("Nepareiza ievade")