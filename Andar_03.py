# encoding: UTF-8
from Batalha import *
from Monstros import *
from Quest import *
from time import sleep
from Opcoes import salvar_jogo

###############################################################################################################

def sala_do_boss03(personagem, nome, inventario, habilidades, itens, bolsa):
	print("\n****************************************************************")
	print("\n\n Cabine do Capitão \n\n")
	print("****************************************************************\n")
	sleep(3)

	print("\nCapitão:")
	print("    Então você conseguiu derrotar meus homens e montar minha chave?")
	sleep(3)
	print("    Impressionante... Mas você acaba aqui!")
	sleep(3)
	
	monstro = []	
	Capitao(monstro)
	
	resultado = batalha(personagem, monstro, habilidades, bolsa)
	if(resultado == 0):
		print("\nCapitão:")
		print("    Tirem esse lixo daqui homens! E tragem meu rum!")
		exit(0)

	else:
		print("\n" + nome[0] + ":")
		print("    Este emblema foi bem merecido... os chefes estão ficando fotes.")
		sleep(3)
		
		inventario.append("Chave03")
		
		print("\Chave do 3º Andar adicionado ao inventário")
		sleep(2)
		salvar_jogo(personagem, nome, inventario, habilidades, itens, bolsa)


###############################################################################################################

def estibordo(personagem, nome, habilidades, chaves, bolsa):
	print("\nMarinheiro:")
	print("    Aaarrg!")
	sleep(3)	
	
	print("\nMarujo:")
	print("    Vocês acham que sou apenas um pirata como os outros?")
	sleep(2)
	print("    Eu sou um verdadeiro Marujo! Com M de Macho!")
	sleep(2)
	print("    Venham quantos quiserem seus frutinhas!")
	sleep(2)
	print("    Ahh, veja o que temos aqui... Quanto tempo você vai durar?")
	sleep(3)
	
	monstro = []	
	marujo(monstro)
	
	resultado = batalha(personagem, monstro, habilidades, bolsa)
	if(resultado == 0):
		print("\Marujo:")
		print("    Hahahaha Esse era o mais forte de vocês? Vocês me enojam!")
		exit(0)
	
	elif(resultado == 2):
		print("\Marujo:")
		print("    Lambedor de peixe! Volte aqui e eu acabo com você!")
		sleep(3)
	
	else:
		print("\n" + nome[0] + ":")
		print("    Parece que você não era tudo isso afinal...")
		sleep(2)
		print("    Vamos ver o que você tem para mim.")
		sleep(3)

		chaves[2] = 1
		
		print("\nFragmento de chave encontrado.")
		chaves[2] = 1
		sleep(3)
	
###############################################################################################################

def bombordo(personagem, nome, habilidades, chaves, bolsa):
	print("\nPirata:")
	print("    Aaarrg!")
	sleep(3)
	
	print("\nMarinheiro:")
	print("    Este foi o último deste lado do navio.")
	sleep(3)
	
	print("\nMarinheiro:")
	print("    A não, ainda sobrou um rato aqui.")
	sleep(3)
	
	print("\n" + nome[0] + ":")
	print("    Eu? Mas eu não sou um...")
	sleep(3)
	
	print("\nMarinheiro:")
	print("    Não venha com desculpas, morra de uma vez!")
	sleep(3)
	
	monstro1 = []
	monstro2 = []
	monstro3 = []
	
	marinheiro(monstro1)
	marinheiro(monstro2)
	marinheiro(monstro3)
	
	resultado = batalha_Vs3(personagem, monstro1, monstro2, monstro3, habilidades, bolsa)
	if(resultado == 0):
		print("\nMarinheiro:")
		print("    Vamos homens, nenhum pirata sai vivo hoje!")
		exit(0)
	
	elif(resultado == 2):
		print("Marinheiro:")
		print("    Não deixem ele fugir! Atrás dele!")
		sleep(3)
	
	else:
		print("\n" + nome[0] + ":")
		print("    Não tenho aliados em lugar nenhum.")
		print("    Mas pelo menos esses deixaram alguma coisa para trás.")
		sleep(4)

		chaves[1] = 1
		
		print("\nFragmento de chave encontrado")
		chaves[1] = 1
		sleep(2)
		
###############################################################################################################

def cozinha(personagem, nome, habilidades, chaves, bolsa):	
	print("Cozinheiro:")
	print("    Saia já da minha cozinha seu verme!")
	sleep(3)
	
	monstro = []	
	cozinheiro(monstro)
	
	resultado = batalha(personagem, monstro, habilidades, bolsa)
	if(resultado == 0):
		print("\nCozinheiro:")
		print("    Vou te cortar em pedacinhos e servir aos meus gatos.")
		exit(0)
	
	elif(resultado == 2):
		print("\nCozinheiro:")
		print("    Covarde! Volte pro buraco de onde você saíu!")
		sleep(3)
	
	else:
		print("\n" + nome[0] + ":")
		print("    O que é isso no pescoço dele?")
		sleep(3)

		chaves[0] = 1
		
		print("\nFragmento de chave encontrado.")
		chaves[0] = 1
		sleep(3)
		
###############################################################################################################

def andar_03(personagem, nome, inventario, habilidades, itens, bolsa):
	chaves = [0,0,0]
	
	print("\n****************************************************************")
	print("\nCapitão:")
	print("    Vamos homens! Defendam esse navio com suas vidas!")
	sleep(3)
	print("\nPorta batendo.")
	sleep(2)
	
	print("\nPiratas:")
	print("    EEEHHH, matem todos os marinheiros!")
	sleep(3)
	
	print("\n" + nome[0] + ":")
	print("    Uma batalha maritima? Onde mais esse portal pode me levar?")
	sleep(3)
	
	print("\nPiratas:")
	print("    Ei! Você! Esta na hora de andar na prancha!")
	sleep(3)
	
	monstro1 = []
	monstro2 = []
	
	pirata(monstro1)
	pirata(monstro2)
	
	resultado = batalha_Vs2(personagem, monstro1, monstro2, habilidades, bolsa)
	if(resultado == 0):
		print("Piratas:")
		print("    Tesc, mais um que vira comida de peixe.")
		exit(0)
	
	elif(resultado == 2):
		print("Piratas:")
		print("    Covarde! Venha e lute como homem!")
		sleep(3)
	
	decisao = "0"
	while(decisao != "1" and decisao != "2" and decisao != "3" and decisao != "4" and decisao != "5"):
		print("\n****************************************************************")
		print("\n\n Convés do Navio \n\n")
		print("****************************************************************\n")
		sleep(3)
		
		print("\nDecisão: \n1 - Norte \n2 - Sala do Chefe \n3 - Leste \n4 - Oeste \n5 - Tomar poção")
		decisao = input("R: ")
		
		if(decisao == "1"):
			print("\n****************************************************************")
			print("\n\n Cozinha \n\n")
			print("****************************************************************\n")
			sleep(3)
			if(chaves[0] == 0):
				cozinha(personagem, nome, habilidades, chaves, bolsa)
				
			
			print("\n" + nome[0] + ":")
			print("    Não tem mais nada por aqui, melhor continuar.")
			sleep(3)	
			decisao = "0"
			
		elif(decisao == "2"):
			if(chaves != [1,1,1]):
				print("\n****************************************************************")
				print("A porta do Chefe do andar esta trancanda.")
				decisao = "0"
				sleep(2)
                                
			elif(chaves == [1,1,1]):
				sala_do_boss03(personagem, nome, inventario, habilidades, itens, bolsa)
				
		elif(decisao == "3"):
			print("\n****************************************************************")
			print("\n\n Bombordo do Navio \n\n")
			print("****************************************************************\n")
			sleep(3)
			if(chaves[1] == 0):
				bombordo(personagem, nome, habilidades, chaves, bolsa)
				

			print("\n" + nome[0] + ":")
			print("    Não tem mais nada por aqui, melhor continuar.")
			sleep(3)
			decisao = "0"
			
			
		elif(decisao == "4"):
			
			print("\n****************************************************************")
			print("\n\n Estibordo do Navio \n\n")
			print("****************************************************************\n")
			sleep(3)
			if(chaves[2] == 0):
				estibordo(personagem, nome, habilidades, chaves, bolsa)
				
			elif(chaves[2] == 1):	
				print("\n" + nome[0] + ":")
				print("    Não tem mais nada por aqui, melhor continuar.")
				sleep(3)
			decisao = "0"
			
		elif(decisao == "5"):
			tomar_pot(personagem, bolsa)
			decisao = "0"
			
			
	
