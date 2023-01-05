from random import randint, sample

#ARQUIVO APENAS PARA TESTE E VIZUALIZAÇÃO DA FUNCIONALIDADE DO BONUS

Hp = 100
Forca = 10
Defesa = 30
Agilidade = 1
Arma = 10

contador = 0

atributos = ['HP','Força','Defesa','Agilidade']

randValue = []
randStat = sample(atributos, 2)

for i in range(3):
    if contador <= 5:
        n = randint(1,3)
        randValue.append(n)
    
    elif contador >5 and contador <=10:
        n = randint(2,4)
        randValue.append(n)

    elif contador >10 and contador <=15:
        n = randint(3,6)
        randValue.append(n)
    
    elif contador >15 and contador <=20:
        n = randint(4,8)
        randValue.append(n)

    elif contador >20:
        n = randint(5,10)
        randValue.append(n)    

if randStat[0] == "HP":
    randValue[0] = randint(10, 25)

if randStat[1] == "HP":
    randValue[1] = randint(10, 25)

print("1 - Bonus de +{} de {}".format(randValue[0], randStat[0]))
print("2 - Bonus de +{} de {}".format(randValue[1], randStat[1]))
escolhaBonus = input()

if escolhaBonus == "1":
    if randStat[0] == "HP":
        Hp += randValue[0]

    elif randStat[0] == "Força":
        Forca += randValue[0]
    
    elif randStat[0] == "Defesa":
        Defesa += randValue[0]

    elif randStat[0] == "Agilidade":
        Agilidade += randValue[0]

elif escolhaBonus == "2":
    if randStat[1] == "HP":
        Hp += randValue[1]

    elif randStat[1] == "Força":
        Forca += randValue[1]
    
    elif randStat[1] == "Defesa":
        Defesa += randValue[1]

    elif randStat[1] == "Agilidade":
        Agilidade += randValue[1]