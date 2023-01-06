from random import randint, sample
from time import sleep
from loja import Ativa_Loja
import os
import json

file = "./Database/enemies.json"

rand = 0

Max_HP = 100

Moedas = 0

Hp = 100
Forca = 2000
Defesa = 15
Agilidade = 1500
Arma = 10

M_Nome = "a"
M_Hp = 0
M_Forca = 0
M_Defesa = 0
M_Agilidade = 0
M_Arma = 0

contador = 0

num_Loja = 1
loja_Ativada = 0

def batalha(M_Nome, M_Hp, M_Forca, M_Defesa, M_Agilidade, M_Arma, rand, contador):

    global Max_HP

    global Hp
    global Forca
    global Defesa
    global Agilidade
    global Arma
    
    global Moedas

    global num_Loja
    global loja_Ativada

    contador = 0

    while Hp > 0:

        rand = (randint(1,5))
        
        chance_Loja = randint(num_Loja, 100)
        chance_Loja2 = randint(2, 10)

        atributos = ['HP','Força','Defesa','Agilidade']

        randValue = []
        randStat = sample(atributos, 2)

        if contador <=10:

            rand_Easy = randint(1, 5)

            with open (file) as base:
                temp = json.load(base)
                for entry in temp:
                    M_Id = entry["id"]

                    if M_Id == rand_Easy:

                        M_Dif = entry["dificuldade"]
                        M_Nome = entry["nome"]
                        M_Hp = entry["hp"]
                        M_Forca = entry["forca"]
                        M_Defesa = entry["defesa"]
                        M_Agilidade = entry["agilidade"]
                        M_Arma = entry["arma"]

        elif contador >10 and contador <=20:

            rand_Medium = randint(6, 10)

            with open (file) as base:
                temp = json.load(base)
                for entry in temp:
                    M_Id = entry["id"]
                    M_Dif = entry["dificuldade"]

                    if M_Dif == 2:

                        if M_Id == rand_Medium:

                            M_Nome = entry["nome"]
                            M_Hp = entry["hp"]
                            M_Forca = entry["forca"]
                            M_Defesa = entry["defesa"]
                            M_Agilidade = entry["agilidade"]
                            M_Arma = entry["arma"]

        elif contador >20:

            rand_Hard = randint(11, 15)

            with open (file) as base:
                temp = json.load(base)
                for entry in temp:
                    M_Id = entry["id"]
                    M_Dif = entry["dificuldade"]

                    if M_Dif == 3:

                        if M_Id == rand_Hard:

                            M_Nome = entry["nome"]
                            M_Hp = entry["hp"]
                            M_Forca = entry["forca"]
                            M_Defesa = entry["defesa"]
                            M_Agilidade = entry["agilidade"]
                            M_Arma = entry["arma"]

        while M_Hp > 0:

            if M_Agilidade > Agilidade:

                print(" ")
                print("Batalhas Vencidas: {}".format(contador))
                print(" ")
                print("-=-=- Inimigo: {} -=-=-".format(M_Nome))
                print("---------------------------------")
                print("HP do Inimigo: {}".format(M_Hp))
                print(" ")
                print("-=-=-=- Jogador -=-=-=-")
                print("---------------------------------")
                print("Status:")
                print(" ")
                print("Hp: {}".format(Hp))
                print("Força: {}".format(Forca))
                print("Defesa: {}".format(Defesa))
                print("Agilidade: {}".format(Agilidade))
                print("Arma: {}".format(Arma))
                print(" ")
                print("Moedas: {}".format(Moedas))
                print(" ")
                input("Prescione Enter para continuar")
                os.system('cls') or None

                while True:

                    print("Vez do Inimigo!")
                    sleep(2)
                    print("O inimigo ataca!")
                    print("----------------")
                    print(" 1 - Esquivar")
                    print(" 2 - Bloquear")
                    Escolha = input( )

                    if Escolha == "1":

                        esq = randint(1, Agilidade)
                        M_esq = randint(1, M_Agilidade)

                        M_esq = M_esq*1.3

                        if esq>M_esq:
                            print("Esquivou do Ataque!")
                            break

                        else:
                            print("Não conseguiu esquivar!")
                            M_Dano = 2*M_Arma+10*(M_Forca/Defesa)
                            Hp = Hp-M_Dano
                            print("Você perdeu {} de vida!".format(M_Dano))
                            break

                    elif Escolha == "2":

                            bloq = randint(1, Defesa)
                            M_bloq = randint(1, M_Defesa)

                            M_bloq = M_bloq*1.2

                            if bloq>M_bloq:
                                print("Você bloqueou o Ataque!")
                                M_Dano = 2*M_Arma+10*(M_Forca/Defesa)
                                Hp = Hp-(M_Dano/2)
                                print("Você perdeu {} de vida!".format(M_Dano/2))
                                break

                            else:
                                print("Não conseguiu bloquear!")
                                M_Dano = 2*M_Arma+10*(M_Forca/Defesa)
                                Hp = Hp-M_Dano
                                print("Você perdeu {} de vida!".format(M_Dano))  
                                break
                    else:
                        print("-- Escolha invalida --")
                        sleep(1)
                        os.system('cls') or None


                sleep(1)
                os.system('cls') or None
                if Hp <= 0:
                    os.system('cls') or None
                    print("-=- Voce Perdeu! -=-")    
                    print(" ")
                    print("Numero de Vitórias: {}".format(contador))
                    print(" ")
                    break                       

                print(" ")
                print("Batalhas Vencidas: {}".format(contador))
                print(" ")
                print("-=-=- Inimigo: {} -=-=-".format(M_Nome))
                print("---------------------------------")
                print("HP do Inimigo: {}".format(M_Hp))
                print(" ")
                print("-=-=-=- Jogador -=-=-=-")
                print("---------------------------------")
                print("Status:")
                print(" ")
                print("Hp: {}".format(Hp))
                print("Força: {}".format(Forca))
                print("Defesa: {}".format(Defesa))
                print("Agilidade: {}".format(Agilidade))
                print("Arma: {}".format(Arma))
                print(" ")
                print("Moedas: {}".format(Moedas))
                print(" ")
                print("Sua vez!")
                print("---------------------------------")
                input("Prescione Enter para Atacar")
                Dano = 2*Arma+10*(Forca/M_Defesa)
                M_Hp = M_Hp-Dano
                sleep(1)
                print("Você Causou",Dano,"de Dano!")
                sleep(1)
                os.system('cls') or None
                if Hp <= 0:
                    os.system('cls') or None
                    print("-=- Voce Perdeu! -=-")    
                    print(" ")
                    print("Numero de Vitórias: {}".format(contador))
                    print(" ")
                    break 
                if M_Hp <=0:

                    num_moedas = randint(0, 5)
                    Moedas = Moedas + num_moedas

                    print("-=- Você Venceu! -=-")
                    print("-----------------------")
                    print("Você Recebeu {} moedas!".format(num_moedas))
                    print("-----------------------")
                    print("Seus Status:")
                    print(" ")
                    print("Hp: {}".format(Hp))
                    print("Força: {}".format(Forca))
                    print("Defesa: {}".format(Defesa))
                    print("Agilidade: {}".format(Agilidade))
                    print("Arma: {}".format(Arma))
                    print(" ")
                    input("Prescione Enter para Continuar")
                    os.system('cls') or None
            
            else:
                print(" ")
                print("Batalhas Vencidas: {}".format(contador))
                print(" ")
                print("-=-=- Inimigo: {} -=-=-".format(M_Nome))
                print("---------------------------------")
                print("HP do Inimigo: {}".format(M_Hp))
                print(" ")
                print("-=-=-=- Jogador -=-=-=-")
                print("---------------------------------")
                print("Status:")
                print(" ")
                print("Hp: {}".format(Hp))
                print("Força: {}".format(Forca))
                print("Defesa: {}".format(Defesa))
                print("Agilidade: {}".format(Agilidade))
                print("Arma: {}".format(Arma))
                print(" ")
                print("Moedas: {}".format(Moedas))
                print(" ")
                print("Sua vez!")
                print("---------------------------------")
                input("Prescione Enter para Atacar")
                Dano = 2*Arma+10*(Forca/M_Defesa)
                M_Hp = M_Hp-Dano
                sleep(1)
                print("Você Causou",Dano,"de Dano!")
                sleep(1)
                os.system('cls') or None
                if Hp <= 0:
                    os.system('cls') or None
                    print("-=- Voce Perdeu! -=-")    
                    print(" ")
                    print("Numero de Vitórias: {}".format(contador))
                    print(" ")
                    break 
                if M_Hp <=0:

                    num_moedas = randint(0, 5)
                    Moedas = Moedas + num_moedas

                    print("-=- Você Venceu! -=-")
                    print("-----------------------")
                    print("Você Recebeu {} moedas!".format(num_moedas))
                    print("-----------------------")
                    print("Seus Status:")
                    print(" ")
                    print("Hp: {}".format(Hp))
                    print("Força: {}".format(Forca))
                    print("Defesa: {}".format(Defesa))
                    print("Agilidade: {}".format(Agilidade))
                    print("Arma: {}".format(Arma))
                    print(" ")
                    input("Prescione Enter para Continuar")
                    os.system('cls') or None
                else:
                    print(" ")
                    print("Batalhas Vencidas: {}".format(contador))
                    print(" ")
                    print("-=-=- Inimigo: {} -=-=-".format(M_Nome))
                    print("---------------------------------")
                    print("HP do Inimigo: {}".format(M_Hp))
                    print(" ")
                    print("-=-=-=- Jogador -=-=-=-")
                    print("---------------------------------")
                    print("Status:")
                    print(" ")
                    print("Hp: {}".format(Hp))
                    print("Força: {}".format(Forca))
                    print("Defesa: {}".format(Defesa))
                    print("Agilidade: {}".format(Agilidade))
                    print("Arma: {}".format(Arma))
                    print(" ")
                    print("Moedas: {}".format(Moedas))
                    print(" ")
                    input("Prescione Enter para continuar")
                    os.system('cls') or None

                    while True:

                        print("Vez do Inimigo!")
                        sleep(2)
                        print("O inimigo ataca!")
                        print("----------------")
                        print(" 1 - Esquivar")
                        print(" 2 - Bloquear")
                        Escolha = input( )

                        if Escolha == "1":

                            esq = randint(1, Agilidade)
                            M_esq = randint(1, M_Agilidade)

                            M_esq = M_esq*1.3

                            if esq>M_esq:
                                print("Esquivou do Ataque!")
                                break

                            else:
                                print("Não conseguiu esquivar!")
                                M_Dano = 2*M_Arma+10*(M_Forca/Defesa)
                                Hp = Hp-M_Dano
                                print("Você perdeu {} de vida!".format(M_Dano))
                                break

                        elif Escolha == "2":

                                bloq = randint(1, Defesa)
                                M_bloq = randint(1, M_Defesa)

                                M_bloq = M_bloq*1.2

                                if bloq>M_bloq:
                                    print("Você bloqueou o Ataque!")
                                    M_Dano = 2*M_Arma+10*(M_Forca/Defesa)
                                    Hp = Hp-(M_Dano/2)
                                    print("Você perdeu {} de vida!".format(M_Dano/2))
                                    break

                                else:
                                    print("Não conseguiu bloquear!")
                                    M_Dano = 2*M_Arma+10*(M_Forca/Defesa)
                                    Hp = Hp-M_Dano
                                    print("Você perdeu {} de vida!".format(M_Dano))
                                    break        

                        else:
                            print("-- Escolha invalida --")
                            sleep(1)
                            os.system('cls') or None

                    sleep(1)
                    os.system('cls') or None
                    if Hp <= 0:
                        os.system('cls') or None
                        print("-=- Voce Perdeu! -=-")    
                        print(" ")
                        print("Numero de Vitórias: {}".format(contador))
                        print(" ")
                        break 

            if M_Hp <= 0 and contador%2 == 0:       

                #Ativa_Loja(num_moedas)     

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

                while True:

                    #print("{} + {} --- {}".format(num_Loja, chance_Loja2, chance_Loja)) -- Teste Chance da Loja Aparecer
                    print("---------------------------")
                    print("-=- Escolha seu Bonus: -=-")
                    print("---------------------------")
                    print(" ")
                    sleep(1)    

                    print("1 - Bonus de +{} de {}".format(randValue[0], randStat[0]))
                    print("2 - Bonus de +{} de {}".format(randValue[1], randStat[1]))
                    escolhaBonus = input(" ")
                    os.system('cls') or None

                    if escolhaBonus == "1":
                        if randStat[0] == "HP":
                            Max_HP += randValue[0]
                            Hp += randValue[0]
                            break

                        elif randStat[0] == "Força":
                            Forca += randValue[0]
                            break
                        
                        elif randStat[0] == "Defesa":
                            Defesa += randValue[0]
                            break

                        elif randStat[0] == "Agilidade":
                            Agilidade += randValue[0]
                            break

                    elif escolhaBonus == "2":
                        if randStat[1] == "HP":
                            Max_HP += randValue[1]
                            Hp += randValue[1]
                            break

                        elif randStat[1] == "Força":
                            Forca += randValue[1]
                            break
                        
                        elif randStat[1] == "Defesa":
                            Defesa += randValue[1]
                            break

                        elif randStat[1] == "Agilidade":
                            Agilidade += randValue[1]
                            break

                    else:
                        print("-- Escolha Invalida --")    
                        sleep(1)
                        os.system('cls') or None

                print("Seus Status foi aumentado com sucesso!")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print("Prescione Enter para Continuar")
                input(" ")
                os.system('cls') or None

                if contador == 10:
                    print("Seu HP foi restaurado!")
                    print("-=-=-=-=-=-=-=-=-=-=-=-")
                    Hp = Max_HP
                    sleep(1)
                    os.system('cls') or None
                elif contador == 20:
                    print("Seu HP foi restaurado!")
                    print("-=-=-=-=-=-=-=-=-=-=-=-")
                    Hp = Max_HP
                    sleep(1)
                    os.system('cls') or None
                elif contador == 30:
                    print("Seu HP foi restaurado!")
                    print("-=-=-=-=-=-=-=-=-=-=-=-")
                    Hp = Max_HP
                    sleep(1)
                    os.system('cls') or None

            if num_Loja >= 100:
                num_Loja = 100

            if num_Loja == chance_Loja:
                Ativa_Loja(num_moedas)
                loja_Ativada += 1
                num_Loja = 1
            else:
                num_Loja += 2*chance_Loja2-loja_Ativada

        contador = contador+1

