#16/04
#Spēles punktu aprēķins


#funkcijas izveidošana 
def rekini_punktus(limenis, bonusi, dubultie):

    #Punktu aprēķins - pamata punkti
#par katru līmeni: 100 punkti
#par katru bonusu: 20 punkti
    pamataPunkti = limenis * 100 + bonusi * 20

    #ja dubultie ir True:
    #visi punkti tiek dubultoti
    if dubultie: #dubultie == True
        punkti = pamataPunkti * 2
    else:
        punkti = pamataPunkti
    #Ja kopējais punktu skaits pārsniedz 1000:
    #tiek piešķirts papildus bonuss 150 punkti
    if punkti > 1000:
        punkti = punkti + 150

        return punkti
    
    print(rekini_punktus(100,10,False))