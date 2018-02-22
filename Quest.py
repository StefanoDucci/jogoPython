# encoding: UTF-8
from time import sleep


def nome_classe(classe):
	if(classe == 1):
		return "Mago"
	
	if(classe == 2):
		return "Guerreiro"
	
	if(classe == 3):
		return "Gatuno"

	if(classe == 4):
		return "Druida"

	

		
def recupera_pocao(bolsa):
	bolsa[3] = bolsa[2]
	bolsa[7] = bolsa[6]
	
	print("\nPoções Recuperadas\n")
	sleep(2)
	

def quest_completa(personagem, xp):
	personagem[18] = personagem[18] + xp
	print("\nExperiencia Atual: %s" % personagem[18])
	if(personagem[18] >= (personagem[19] * 100)):
		personagem[18] = personagem[18] - (personagem[19] * 100)
		personagem[19] = personagem[19] + 1
			
		print("****************************************************************")
		print("Voce subiu para o level " + str(personagem[19]) + " distribua seus ponstos de atributo: ")
		sleep(2)
		pontos = 5
		atributos = [0,0,0,0,0,0,0,0]

		print("\nAtributos aumentados: \nVida: \t\t" + str(personagem[0]) + " + " + str((5 * atributos[0])))		
		print("Mana: \t\t" + str(personagem[1]) + " + " + str((5 * atributos[1])))						
		print("Dano Físico: \t" + str(personagem[4]) + " + " + str((5 * atributos[2])))						
		print("Dano Mágico: \t" + str(personagem[5]) + " + " + str((5 * atributos[3])))						
		print("Defesa Física: \t" + str(personagem[8]) + " + " + str((5 * atributos[4])))						
		print("Defesa Mágica: \t" + str(personagem[9]) + " + " + str((5 * atributos[5])))
		print("Agilidade: \t" + str(personagem[7]) + " + " + str((2 * atributos[7])))
		print("Critico: \t" + str(personagem[6]) + " + " + str((2 * atributos[6])))
		
		while(pontos != 0):
			atributo = int(input("\nPontos para destribuir: %d \n1 - Vida \n2 - Mana \n3 - Dano Fiísico \n4 - Dano Mágico \n5 - Defesa Física \n6 - Defesa Mágica \n7 - Agilidade \n8 - Chance de Crítico \nR: " % pontos))
	
			quantidade_pontos = input("\nInforme a quantidade de pontos para este atibuto: ")
			while(quantidade_pontos != "0" and quantidade_pontos != "1" and quantidade_pontos != "2" and quantidade_pontos != "3" and quantidade_pontos != "4" and quantidade_pontos != "5"):
				print("\nSistema: Informe apenas valores númericos de 0 a 5 para destribuição de atributos\n")
				sleep(5)
				quantidade_pontos = input("\nInforme a quantidade de pontos para este atibuto: ")
	
			quantidade_pontos = int(quantidade_pontos)
			verifica = pontos - quantidade_pontos
				
			if(verifica < 0):
				print("\nA quantidade de pontos atribuidos não pode ser maior que a quantidade disponível")
				sleep(4)
		
			elif(verifica >= 0):
				pontos = pontos - quantidade_pontos

				if(atributo == 1):
					atributos[0] = atributos[0] + quantidade_pontos
		
				elif(atributo == 2):
					atributos[1] = atributos[1] + quantidade_pontos

				elif(atributo == 3):
					atributos[2] = atributos[2] + quantidade_pontos
		
				elif(atributo == 4):
					atributos[3] = atributos[3] + quantidade_pontos

				elif(atributo == 5):
					atributos[4] = atributos[4] + quantidade_pontos
		
				elif(atributo == 6):
					atributos[5] = atributos[5] + quantidade_pontos

				elif(atributo == 7):
					atributos[6] = atributos[6] + quantidade_pontos

				elif(atributo == 8):
					atributos[7] = atributos[7] + quantidade_pontos

				print("\n****************************************************************")
				print("\nAtributos aumentados: \nVida: \t\t" + str(personagem[0]) + " + " + str((5 * atributos[0])))		
				print("Mana: \t\t" + str(personagem[1]) + " + " + str((5 * atributos[1])))						
				print("Dano Físico: \t" + str(personagem[4]) + " + " + str((3 * atributos[2])))						
				print("Dano Mágico: \t" + str(personagem[5]) + " + " + str((3 * atributos[3])))						
				print("Defesa Física: \t" + str(personagem[8]) + " + " + str((2 * atributos[4])))						
				print("Defesa Mágica: \t" + str(personagem[9]) + " + " + str((2 * atributos[5])))
				print("Agilidade: \t" + str(personagem[7]) + " + " + str((3 * atributos[6])))
				print("Critico: \t" + str(personagem[6]) + " + " + str((3 * atributos[7])))
				
		personagem[0] = personagem[0] + (5 * atributos[0])
		personagem[1] = personagem[1] + (5 * atributos[1])
		personagem[4] = personagem[4] + (3 * atributos[2])
		personagem[5] = personagem[5] + (3 * atributos[3])
		personagem[8] = personagem[8] + (2 * atributos[4])
		personagem[9] = personagem[9] + (2 * atributos[5])
		personagem[7] = personagem[7] + (2 * atributos[6])
		personagem[6] = personagem[6] + (2 * atributos[7])
		personagem[54] = personagem[1] + personagem[53]

		personagem[2] = personagem[0]
		personagem[3] = personagem[54]


		

def descansar(personagem):
	personagem[2] = personagem[0]
	personagem[3] = personagem[54]
	personagem[55] = 0
	sleep(2)
	print("\nVida e mana recuperados\n")
	print("****************************************************************\n")
	sleep(1)
	

def pousada(personagem, nome):
	print("****************************************************************")
	print("Mary:")
	print("    Olá " + nome[0] + " seja bem vindo a nossa pousada!")
	sleep(3)
	print("    Você gostaria de alugar uma cama por 10 moedas?")
	decisao = "0"
	while(decisao != "1" and decisao != "2"):
                decisao = input("\nDecisão: \n1 - Sim \n2 - Não \nR: ")

                if(decisao == "2"):
                        return "0"
                elif(decisao == "1"):
                        print("\nVocê gastou 10 moedas")
                        personagem[56] = personagem[56] - 10
                        print("\nVocê tem %d moedas" % personagem[56])
                        descansar(personagem)
                        print("Mary:")
                        print("    Volte sempre!")
                        sleep(2)
                        return "0"


def mostra_status(personagem, nome):
	print("\n****************************************************************")
	print("Nome: " + nome[0] + "\tClasse: " + nome_classe(personagem[40]))
	print("Moedas: %d \n" % personagem[56])
	print("Level: %d" % personagem[19])
	print("Experiência atual: %d" % personagem[18])
	print("Experiência para aumentar de level: " + str((personagem[19] * 100) - personagem[18]) + "\n")
	print("Vida Máxima: " + str(personagem[0]) + " \tVida Atual: " + str(personagem[2]))
	print("Mana Máxima: " + str(personagem[1]) + "(+" + str(personagem[53]) + ")" + " \tMana Atual: " + str(personagem[3]) + "\n")
	print("Agilidade: " + str(personagem[7]) + "(+" + str(personagem[51]) + ")")
	print("Destreza: " + str(personagem[6]) + "(+" + str(personagem[52]) + ")")
	print("Dano Físico: " + str(personagem[4]) + "(+" + str(personagem[10]) + ")")
	print("Dano Mágico: " + str(personagem[5]) + "(+" + str(personagem[11]) + ")")
	print("Defesa Física: " + str(personagem[8]) + "(+" + str(personagem[12]) + ")")
	print("Defesa Mágica: " + str(personagem[9]) + "(+" + str(personagem[13]) + ")")
	print("\n****************************************************************")
	sleep(5)
	
	
	
def tomar_pot(personagem, bolsa):
	print("\n")
	print("****************************************************************")
	print("Vida Máxima: " + str(personagem[0]) + " \tVida Atual: " + str(personagem[2]))
	print("Mana Máxima: " + str(personagem[54]) + " \tMana Atual: " + str(personagem[3]))
	print("Poções de vida: " + str(bolsa[3]) + " \tPoções de mana: " + str(bolsa[7]))
	print("Poções Hibridas: " + str(bolsa[19]))
	print("Antidotos: " + str(bolsa[14]))
	print("\n")

	decisao = "0"
	while(decisao != "1" and decisao != "2" and decisao != "3" and decisao != "4" and decisao != "5"):
		decisao = input("\nDecisao: \n1 - Poção de Vida \n2 - Poção de Mana \n3 - Poção Hibrida \n4 - Antidoto \n5 - Voltar \nR: ")
	
		if(decisao == "1"):
                        if(bolsa[3] > 0):
                                personagem[2] = personagem[2] + bolsa[1]
                                bolsa[3] = bolsa[3] - 1
                                if(personagem[2] >= personagem[0]):
                                        personagem[2] = personagem[0]

                                print("\nVocê recuperou " + str(bolsa[1]) + " de vida")
                                decisao = "0"
                        else:
                                print("Poções de vida insuficientes")
                                decisao = "0"

		elif(decisao == "2"):
                        if(bolsa[7] > 0):
                                personagem[3] = personagem[3] + bolsa[5]
                                bolsa[7] = bolsa[7] - 1
                                if(personagem[3] >= personagem[54]):
                                        personagem[3] = personagem[54]
                                        
                                print("\nVocê recuperou " + str(bolsa[5]) + " de mana")
                                decisao = "0"
                        else:
                                print("Poções de mana insuficientes")
                                decisao = "0"

		elif(decisao == "3"):
                        if(bolsa[19] > 0):
                                personagem[2] = personagem[2] + bolsa[16]
                                personagem[3] = personagem[3] + bolsa[17]
                                bolsa[19] = bolsa[19] - 1
                                if(personagem[3] >= personagem[54]):
                                        personagem[3] = personagem[54]
                                if(personagem[2] >= personagem[0]):
                                        personagem[2] = personagem[0]
                                
                                print("\nVocê recuperou: %d de vida" % bolsa[16])	
                                print("\nVocê recuperou: %d de mana" % bolsa[17])
                                sleep(2)
                                decisao = "0"
                                
                        else:
                                print("\nPoções hibridas insuficientes")
                                decisao = "0"
                                sleep(3)


		elif(decisao == "4"):
                        if(bolsa[14] > 0):
                                if(personagem[55] == 9):
                                        print("\nVocê não esta mais envenenado.")
                                        bolsa[14] = bolsa[14] - 1
                                        personagem[55] = 0
                                        decisao = "0"
                                        
                                else:
                                        print("Você não esta envenenado.")
                                        decisao = "0"

                        else:
                                print("\nAntidotos insuficientes.")
                                decisao = "0"
                                sleep(3)



	
