from Teste_Batalha import batalha, Hp, M_Nome, M_Hp, M_Forca, M_Defesa, M_Agilidade, M_Arma, rand, contador
from user_Login import Login
from Create_User import cria_Usuario
from time import sleep
import os

print("-=--(+)--=-------------=--(+)--=-")
print("-=-=-    Jogo de Batalha    -=-=-")
print("-=--(+)--=-------------=--(+)--=-")
print(" ")
print(" 1 - Criar Conta")
print(" 2 - Login")
escolha_inicial = int(input())
os.system('cls') or None

if escolha_inicial == 1:

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

    cria_Usuario(Nome_Player, Senha_Player)
    print(" ")
    sleep(1)
    os.system('cls') or None

elif escolha_inicial == 2:

    print("-=-=-=-=-=-=-")
    print("-=- Login -=-")
    print("-=-=-=-=-=-=-")
    print(" ")
    Nome_Player = input("Usuario: ")
    sleep(1)
    Senha_Player = input("Senha: ")

    Login(Nome_Player, Senha_Player)
    print(" ")
    sleep(1)
    os.system('cls') or None

else:
    print("Escolha Invalida")

print("-=--(+)--=-------------=--(+)--=-")
print("-=-=-    Jogo de Batalha    -=-=-")
print("-=--(+)--=-------------=--(+)--=-")
print(" ")
print("Logado como: {}".format(Nome_Player))
print(" ")
print(" 1 - Novo Jogo")
print(" 2 - Continuar")
print(" 3 - Sair")
escolha_jogo = int(input())


batalha(M_Nome, M_Hp, M_Forca, M_Defesa, M_Agilidade, M_Arma, rand, contador)