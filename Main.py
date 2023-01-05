from Batalha import batalha, Hp, M_Nome, M_Hp, M_Forca, M_Defesa, M_Agilidade, M_Arma, rand, contador
from time import sleep
import os

print("-=--(+)--=-------------=--(+)--=-")
print("-=-=-    Jogo de Batalha    -=-=-")
print("-=--(+)--=-------------=--(+)--=-")
print(" ")
print(" 1 - Novo Jogo")
print(" 2 - Continuar")
print(" 3 - Sair")
escolha_jogo = int(input())


batalha(M_Nome, M_Hp, M_Forca, M_Defesa, M_Agilidade, M_Arma, rand, contador)