# _*_ coding: utf-8 _*_
#_*_  coding: ASCII _*_
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os as sistema
import os, sys
import colorama 
from colorama import Fore as F
import argparse as arg
import requests as r
sistema.system('cls' if sistema.name == 'nt' else 'reset')
index = r"""
 ____                       _ _         _   _ ____  
/ ___|  ___  ___ _   _ _ __(_) |_ _   _| | | |  _ \ 
\___ \ / _ \/ __| | | | '__| | __| | | | | | | |_) |
 ___) |  __/ (__| |_| | |  | | |_| |_| | |_| |  __/ 
|____/ \___|\___|\__,_|_|  |_|\__|\__, |\___/|_|    
                                  |___/            
Criado por Joas Antonio dos Santos Barbosa
"""
print(index)                          

#TESTE
parser = arg.ArgumentParser(description = "ChatBot by Joas")


parser.add_argument("--chat", action='store_true', help = "Executa o programa")
parser.add_argument("--r", action='store_true', help = 'Remove o Banco de Dados')
param = parser.parse_args()

#########

if param.r:
	
	pasta = str(input('Digite o diretório aonde está o arquivo: '))
	arquivo = str(input('Digite o nome do arquivo que deseja apagar: '))
	diretorio = os.listdir(pasta)
	if arquivo in diretorio:
    		print('---removendo arquivo----')
    		os.remove('{}/{}'.format(pasta, arquivo))
    		print('%s removido da pasta %s' % (pasta, arquivo))
	else:
    		print('este arquivo nao existe')
		
#############

if param.chat:

	bot = ChatBot('Asuna')

convI = ['Oi', 'Ola', 'Tudo bem?', 'Tudo', 'Tudo, e com você?', 'Vou bem', 'Está fazendo oque agora?', 'Nada demais']
convF = ['Gosta de que estilo de música?', 'Eu curto rock e rap', 'Legal eu também curto rock']

bot.set_trainer(ListTrainer)

bot.train(convI)
bot.train(convF)

while True:
	quest = input('Você: ')
	response = bot.get_response(quest)
	if float(response.confidence) > 0.5:
		print('Bot:', response)
	else:
		print('Bot: Eu não entendi :(')
