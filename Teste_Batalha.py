import mysql.connector
from random import randint, sample
from time import sleep
import os

con = mysql.connector.connect(host='localhost',database='jogo_batalha',username='root',password='masterkey')

rand = 0

Max_HP = 100

Hp = 100
Forca = 500
Defesa = 20
Agilidade = 100
Arma = 10

M_Nome = "a"
M_Hp = 0
M_Forca = 0
M_Defesa = 0
M_Agilidade = 0
M_Arma = 0

contador = 0

def batalha(M_Nome, M_Hp, M_Forca, M_Defesa, M_Agilidade, M_Arma, rand, contador):

    global Max_HP

    global Hp
    global Forca
    global Defesa
    global Agilidade
    global Arma

    contador = 0

    while Hp > 0:

        rand = (randint(1,5))

        atributos = ['HP','Força','Defesa','Agilidade','Arma']

        randValue = []
        randStat = sample(atributos, 3)

        if contador <=10:

            if con.is_connected():

                cursor = con.cursor()
                cursor.execute("select easy_Nome from easy_enemies where easy_code = %s", (rand,))
                M_Nome = cursor.fetchone()
                cursor.execute("select easy_Hp from easy_enemies where easy_code = %s", (rand,))
                M_Hp = cursor.fetchone()
                cursor.execute("select easy_Forca from easy_enemies where easy_code = %s", (rand,))
                M_Forca = cursor.fetchone()
                cursor.execute("select easy_Defesa from easy_enemies where easy_code = %s", (rand,))
                M_Defesa = cursor.fetchone()
                cursor.execute("select easy_Agilidade from easy_enemies where easy_code = %s", (rand,))
                M_Agilidade = cursor.fetchone()
                cursor.execute("select easy_Arma from easy_enemies where easy_code = %s", (rand,))
                M_Arma = cursor.fetchone()
        
        elif contador >10 and contador <=20:

             if con.is_connected():

                cursor = con.cursor()
                cursor.execute("select medium_Nome from medium_enemies where medium_code = %s", (rand,))
                M_Nome = cursor.fetchone()
                cursor.execute("select medium_Hp from medium_enemies where medium_code = %s", (rand,))
                M_Hp = cursor.fetchone()
                cursor.execute("select medium_Forca from medium_enemies where medium_code = %s", (rand,))
                M_Forca = cursor.fetchone()
                cursor.execute("select medium_Defesa from medium_enemies where medium_code = %s", (rand,))
                M_Defesa = cursor.fetchone()
                cursor.execute("select medium_Agilidade from medium_enemies where medium_code = %s", (rand,))
                M_Agilidade = cursor.fetchone()
                cursor.execute("select medium_Arma from medium_enemies where medium_code = %s", (rand,))
                M_Arma = cursor.fetchone()

        elif contador >20:

            if con.is_connected():

                cursor = con.cursor()
                cursor.execute("select hard_Nome from hard_enemies where hard_code = %s", (rand,))
                M_Nome = cursor.fetchone()
                cursor.execute("select hard_Hp from hard_enemies where hard_code = %s", (rand,))
                M_Hp = cursor.fetchone()
                cursor.execute("select hard_Forca from hard_enemies where hard_code = %s", (rand,))
                M_Forca = cursor.fetchone()
                cursor.execute("select hard_Defesa from hard_enemies where hard_code = %s", (rand,))
                M_Defesa = cursor.fetchone()
                cursor.execute("select hard_Agilidade from hard_enemies where hard_code = %s", (rand,))
                M_Agilidade = cursor.fetchone()
                cursor.execute("select hard_Arma from hard_enemies where hard_code = %s", (rand,))
                M_Arma = cursor.fetchone()

        a = "."
        M_Nome = ''.join(x for x in M_Nome if x not in a)    
        M_Nome = M_Nome.replace(',','.')

        s_Hp = [str(i) for i in M_Hp] 
        M_Hp = str("".join(s_Hp))
        M_Hp = int(M_Hp)

        s_Forca = [str(i) for i in M_Forca] 
        M_Forca = str("".join(s_Forca))
        M_Forca = int(M_Forca)

        s_Defesa = [str(i) for i in M_Defesa] 
        M_Defesa = str("".join(s_Defesa))
        M_Defesa = int(M_Defesa)

        s_Agilidade = [str(i) for i in M_Agilidade] 
        M_Agilidade = str("".join(s_Agilidade))
        M_Agilidade = int(M_Agilidade)

        s_Arma = [str(i) for i in M_Arma] 
        M_Arma = str("".join(s_Arma))
        M_Arma = int(M_Arma)

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
                    print("Você Venceu!")
                    print("------------")
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
                    print("Você Venceu!")
                    print("------------")
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
                
                if randStat[2] == "HP":
                    randValue[2] = randint(10, 25)

                while True:

                    print("---------------------------")
                    print("-=- Escolha seu Bonus: -=-")
                    print("---------------------------")
                    print(" ")
                    sleep(1)    

                    print("1 - Bonus de +{} de {}".format(randValue[0], randStat[0]))
                    print("2 - Bonus de +{} de {}".format(randValue[1], randStat[1]))
                    print("3 - Bonus de +{} de {}".format(randValue[2], randStat[2]))
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
                        
                        elif randStat[0] == "Arma":
                            Arma += randValue[0]
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
                        
                        elif randStat[1] == "Arma":
                            Arma += randValue[1]
                            break

                    elif escolhaBonus == "3":
                        if randStat[2] == "HP":
                            Max_HP += randValue[1]
                            Hp += randValue[2]
                            break

                        elif randStat[2] == "Força":
                            Forca += randValue[2]
                            break
                        
                        elif randStat[2] == "Defesa":
                            Defesa += randValue[2]
                            break

                        elif randStat[2] == "Agilidade":
                            Agilidade += randValue[2]
                            break
                        
                        elif randStat[2] == "Arma":
                            Arma += randValue[2]
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

        contador = contador+1

