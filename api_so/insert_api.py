from connectAuto import *
import mysql.connector
from credentials import usr, pswd
from functools import reduce


print('='*10, 'NBA Cadastro', '='*10)

try: 

    continuar = True

    while(continuar):

        nome= str(input('Qual o nome do jogador? \n'))
        altura= float(input('Qual a altura? (m) \n'))
        posicao= str(input('Qual a posição do jogador? \n'))
        numeroCamisa= int(input('Qual o número da camisa? \n'))
        team= str(input('Qual o time do jogador? \n'))

        insert_db(nome, altura, posicao, numeroCamisa, team)

        resposta = str(input('Deseja cadastrar mais jogadores? (S/N) \n').lower())
        
        while(resposta != "n" and resposta != "s"):
            print('Resposta inválida')
            resposta = str(input('Deseja cadastrar mais jogadores? (S/N) \n').lower())
            
        if (resposta == "n"): 
            continuar = False
        
except KeyboardInterrupt:
    pass    


