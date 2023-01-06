from random import randint
from time import sleep
import os
import json

file = "./Database/itens.json"

Moedas = 500

Itens = []

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

        if compra == 1:
            if Moedas >= Itens[1]:
                print("{} adiquirido!".format(Itens[0]))
                Moedas = Moedas - Itens[1]
                break
            else:
                print("Você não possui moedas o suficiente")
                sleep(1)
                os.system('cls') or None

        elif compra == 2:
            if Moedas >= Itens[4]:
                print("{} adiquirido!".format(Itens[3]))
                Moedas = Moedas - Itens[4]
                break
            else:
                print("Você não possui moedas o suficiente")
                sleep(1)
                os.system('cls') or None

        elif compra == 3:
            print("Não comprou nada!")
            os.system('cls') or None
            break
        
        else:
            print("Alternativa Invalida")
            sleep(1)
            os.system('cls') or None