import mysql.connector
from time import sleep
import os

Nome_Player = "a"
Senha_Player = "a"

def cria_Usuario(Nome_Player, Senha_Player):

    con = mysql.connector.connect(host='localhost',database='jogo_batalha',username='root',password='masterkey')

    if con.is_connected():
        cursor = con.cursor()

        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print("-=- Criação de Usuario -=-")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print(" ")
        input("Prescione Enter para Começar")
        sleep(1)
        os.system('cls') or None
        print("Insira seu Nome de Usuario")
        Nome_Player = input()
        sleep(0.5)
        print("Insira sua Senha:")
        Senha_Player = input()

        insert_Query = "INSERT INTO player (player_Nome, player_Senha, player_MaxHp, player_Hp, player_Forca, player_Defesa, player_Agilidade, player_Arma) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        user_Atributes = (Nome_Player, Senha_Player, 100, 100, 15, 15, 10, 10)
        
        cursor.execute(insert_Query, user_Atributes)

        con.commit()

        print("Usuario Criado!")

        cursor.close
        con.close

cria_Usuario(Nome_Player, Senha_Player)