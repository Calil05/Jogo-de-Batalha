from random import randint
from time import sleep
import os
import json

file = "./Database/itens.json"

Moedas = 500

Itens = []

Hp = 0
Max_HP = 0


def Ativa_Loja(Moedas):

    for l in range(2):

        rand_Loja = randint(1, 5)

        with open (file) as base:
            temp = json.load(base)
            for entry in temp:
                Item_ID = entry["id"]

                if Item_ID == rand_Loja:
                    Itens.append(entry["nome"])
                    Itens.append(entry["valor"])
                    Itens.append(entry["desc"])

    while True:

        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print(" -=- Bem Vindo a Loja -=- ")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print("Moedas : {}".format(Moedas))
        print(" ")
        print(" Deseja comprar algo? ") 
        print(" ")
        print("1 - {}".format(Itens[0]))
        print("------------------------")
        print(Itens[2])
        print("Preco: {} moedas".format(Itens[1]))
        print(" ")
        print("2 - {}".format(Itens[3]))
        print("------------------------")
        print(Itens[5])
        print("Preco: {} moedas".format(Itens[4]))
        print(" ")
        print("3 - Não comprar nada")
        compra = int(input())
        print(" ")
        sleep(1)            

        if compra == 1:
            if Moedas >= Itens[1]:
                print("{} adiquirido!".format(Itens[0]))
                Item_Comprado = Itens[0]
                Coin = Itens[1]
                sleep(1)
                break
            else:
                print("Você não possui moedas o suficiente")
                sleep(1)
                os.system('cls') or None

        elif compra == 2:
            if Moedas >= Itens[4]:
                print("{} adiquirido!".format(Itens[3]))
                Item_Comprado = Itens[3]
                Coin = Itens[4]
                sleep(1)
                break
            else:
                print("Você não possui moedas o suficiente")
                sleep(1)
                os.system('cls') or None

        elif compra == 3:
            print("Não comprou nada!")
            Item_Comprado = "Nada"
            Coin = 0
            sleep(1)
            os.system('cls') or None
            break
        
        else:
            print("Alternativa Invalida")
            sleep(1)
            os.system('cls') or None
    
    return Item_Comprado, Coin
    

# Função Para a Utilização de Itens:

def Utiliza_Pocao(item, Hp, Max_HP):

    if item == "Pocao":
        
        if Hp >= Max_HP:
            rec = Max_HP - Hp
        else:
             rec = 30

        print("Recuperou 30 de HP")
        sleep(1)
        os.system('cls') or None

    elif item == "Pocao Grande":

        if Hp >= Max_HP:
            rec = Max_HP - Hp
        else:
             rec = 80

        print("Recuperou 80 de HP")
        sleep(1)
        os.system('cls') or None

    elif item == "Pocao Maxima":

        rec = Max_HP - Hp

        print("Recuperou Todo o HP")
        sleep(1)
        os.system('cls') or None

    return rec


#Ativa_Loja(Moedas)
#Ativa_Loja(Moedas)

#Utiliza_Itens(Item_Comprado)
