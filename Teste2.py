from Teste_Batalha import batalha, Hp, M_Nome, M_Hp, M_Forca, M_Defesa, M_Agilidade, M_Arma, rand, contador
from time import sleep
import os

print("-=--(+)--=-------------=--(+)--=-")
print("-=-=-    Jogo de Batalha    -=-=-")
print("-=--(+)--=-------------=--(+)--=-")
print(" ")
print(" 1 - Criar Conta")
print(" 2 - Login ")
escolha_inicial = int(input())


batalha(M_Nome, M_Hp, M_Forca, M_Defesa, M_Agilidade, M_Arma, rand, contador)