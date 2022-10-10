from random import randint
import mysql.connector

# ARQUIVO APENAS PARA TESTE E VIZUALIZAÇÃO DA FUNCIONALIDADE DA LOJA

con = mysql.connector.connect(host='localhost',database='jogo_batalha',username='root',password='masterkey')

rand = randint(1,5)
rand2 = randint(1,5)

Moedas = 50

if con.is_connected():

    cursor = con.cursor()
    cursor.execute("select item_Nome from items where item_code = %s", (rand,))
    item_Nome = cursor.fetchone()
    cursor.execute("select item_Preco from items where item_code = %s", (rand,))
    item_Preco = cursor.fetchone()
    cursor.execute("select item_Descricao from items where item_code = %s", (rand,))
    item_Descricao = cursor.fetchone()

    cursor = con.cursor()
    cursor.execute("select item_Nome from items where item_code = %s", (rand2,))
    item2_Nome = cursor.fetchone()
    cursor.execute("select item_Preco from items where item_code = %s", (rand2,))
    item2_Preco = cursor.fetchone()
    cursor.execute("select item_Descricao from items where item_code = %s", (rand2,))
    item2_Descricao = cursor.fetchone()
  
a = "."
item_Nome = ''.join(x for x in item_Nome if x not in a)    
item_Nome = item_Nome.replace(',','.')

i_preco = [str(i) for i in item_Preco] 
item_Preco = str("".join(i_preco))
item_Preco = int(item_Preco)

b = "."
item_Descricao = ''.join(x for x in item_Descricao if x not in b)    
item_Descricao = item_Descricao.replace(',','.')

a2 = "."
item2_Nome = ''.join(x for x in item2_Nome if x not in a2)    
item2_Nome = item2_Nome.replace(',','.')

i2_preco = [str(i) for i in item2_Preco] 
item2_Preco = str("".join(i2_preco))
item2_Preco = int(item2_Preco)

b2 = "."
item2_Descricao = ''.join(x for x in item2_Descricao if x not in b2)    
item2_Descricao = item2_Descricao.replace(',','.')

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print(" -=- Bem Vindo a Loja -=- ")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("Moedas : {}".format(Moedas))
print(" ")
print(" Deseja comprar algo? ") 
print(" ")
print("1 - {}".format(item_Nome))
print("------------------------")
print(item_Descricao)
print("Preco: {} moedas".format(item_Preco))
print(" ")
print("2 - {}".format(item2_Nome))
print("------------------------")
print(item2_Descricao)
print("Preco: {} moedas".format(item2_Preco))
print(" ")
print("3 - Não comprar nada")
compra = int(input())

if compra == 1:
    if Moedas >= item_Preco:
        print("{} adiquirido!".format(item_Nome))
        Moedas = Moedas - item_Preco
    else:
        print("Você não possui moedas o suficiente")

if compra == 2:
    if Moedas >= item2_Preco:
        print("{} adiquirido!".format(item2_Nome))
        Moedas = Moedas - item2_Preco
    else:
        print("Você não possui moedas o suficiente")

if compra == 3:
    print("Não comprou nada!")