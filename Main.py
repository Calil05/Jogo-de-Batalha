from Batalha import batalha, Hp, M_Nome, M_Hp, M_Forca, M_Defesa, M_Agilidade, M_Arma, rand, contador
from time import sleep
import os

print("-=--(+)--=-------------=--(+)--=-")
print("-=-=-    Jogo de Batalha    -=-=-")
print("-=--(+)--=-------------=--(+)--=-")
print(" ")
print("---------------------------------")
print("- Prescione Enter pra Iniciar! - ")
print("---------------------------------")
input("")
sleep(0.5)
os.system('cls') or None


batalha(M_Nome, M_Hp, M_Forca, M_Defesa, M_Agilidade, M_Arma, rand, contador)