import mysql.connector
from time import sleep
import os

Nome_Player = "a"
Senha_Player = "a"

def Login(Nome_Player, Senha_Player):

    con = mysql.connector.connect(host='localhost',database='jogo_batalha',username='root',password='masterkey')

    if con.is_connected():
        cursor = con.cursor()

        print("-=-=-=-=-=-=-")
        print("-=- Login -=-")
        print("-=-=-=-=-=-=-")
        print(" ")
        Nome_Player = input("Usuario: ")
        sleep(1)
        Senha_Player = input("Senha: ")

        cursor.execute("SELECT player_Nome, player_Senha FROM player WHERE player_Nome = %s", (Nome_Player,))
        result = cursor.fetchall()

        for record in result:
            if Nome_Player == record[0]:
                if Senha_Player == record[1]:
                    print("Login efetuado com Sucesso!")
                else:
                    print("Usuario ou Senha Invalidos")  
            else:
                print("Usuario ou Senha Invalidos")
                
Login(Nome_Player, Senha_Player)