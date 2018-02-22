# encoding: UTF-8
from Habilidades import nome_habilidade, nome_status, evoluir_habilidades
from random import randint
from time import sleep

###############################################################################################################

def aplica_esquiva(dano, agilidade, destreza, atacante):
	sorteio = randint(1, 100)
	chance = (agilidade - destreza)
	
	if(sorteio <= chance):
		dano = 0
		if(atacante == 1):
			print("\nVocê errou o ataque")
		else:
			print("\nO inimigo errou o ataque")
		return dano
	else:
		return dano

###############################################################################################################

def aplica_dano_status(vidaAlvo, indiceStatus):
			if(indiceStatus == 0):
				return 0
			
			elif(indiceStatus == 1):
				return 5
			
			elif(indiceStatus == 9):
				return 5
			
			elif(indiceStatus == 2):
				return 0
			
###############################################################################################################

def aplica_status(personagem, monstro, indiceStatus, taxaEfeito, atacante):
	sorteio = randint(1,100)

	if(atacante == 1 and sorteio <= taxaEfeito and indiceStatus == 2):
		monstro[11] = indiceStatus
		print("\nO inimigo foi %s" % nome_status(indiceStatus))
		sleep(3)
	
	elif(atacante  == 2 and sorteio <= taxaEfeito and indiceStatus == 2):
		personagem[55] = indiceStatus
		print("\nVocê foi %s" % nome_status(indiceStatus))
		sleep(4)
		
###############################################################################################################

def aplica_elemento(danoPersonagem, elementoPersonagem, elementoMonstro):
	# Super efeito Fogo
	if(elementoPersonagem == 1 and elementoMonstro == 4):
		print("\nSuper Efetivo")
		return danoPersonagem * 2
	elif(elementoPersonagem == 1 and elementoMonstro == 9):
		print("\nSuper Efetivo")
		return danoPersonagem * 2
	# Nao efetivo Fogo
	elif(elementoPersonagem == 1 and elementoMonstro == 2):
		print("\nNão Efetivo")
		return danoPersonagem / 2
	elif(elementoPersonagem == 1 and elementoMonstro == 3):
		print("\nNão Efetivo")
		return danoPersonagem / 2
	elif(elementoPersonagem == 1 and elementoMonstro == 1):
		print("\nNão Efetivo")
		return danoPersonagem / 2
	
	
	# Super efeito Agua
	elif(elementoPersonagem == 2 and elementoMonstro == 1):
		print("\nSuper Efetivo")
		return danoPersonagem * 2
	elif(elementoPersonagem == 2 and elementoMonstro == 3):
		print("\nSuper Efetivo")
		return danoPersonagem * 2
	# Nao efetivo Agua
	elif(elementoPersonagem == 2 and elementoMonstro == 9):
		print("\nNão Efetivo")
		return danoPersonagem / 2
	elif(elementoPersonagem == 2 and elementoMonstro == 2):
		print("\nNão Efetivo")
		return danoPersonagem / 2
	
	# Super efeito Terra
	elif(elementoPersonagem == 3 and elementoMonstro == 1):
		print("\nSuper Efetivo")
		return danoPersonagem * 2
	elif(elementoPersonagem == 3 and elementoMonstro == 5):
		print("\nSuper Efetivo")
		return danoPersonagem * 2
	
	# Nao efetivo Terra
	elif(elementoPersonagem == 3 and elementoMonstro == 9):
		print("\nNão Efetivo")
		return danoPersonagem / 2
	elif(elementoPersonagem == 3 and elementoMonstro == 3):
		print("\nNão Efetivo")
		return danoPersonagem / 2
	
	# Super efeito Vento
	elif(elementoPersonagem == 4 and elementoMonstro == 9):
		print("\nSuper Efetivo")
		return danoPersonagem * 2
		
	# Nao efetivo Vento
	elif(elementoPersonagem == 4 and elementoMonstro == 3):
		print("\nNão Efetivo")
		return danoPersonagem / 2
	elif(elementoPersonagem == 4 and elementoMonstro == 4):
		print("\nNão Efetivo")
		return danoPersonagem / 2
	
	# Super efeito Trovao
	elif(elementoPersonagem == 5 and elementoMonstro == 4):
		print("\nSuper Efetivo")
		return danoPersonagem * 2
	elif(elementoPersonagem == 5 and elementoMonstro == 2):
		print("\nSuper Efetivo")
		return danoPersonagem * 2
	
	# Nao efetivo Trovao
	elif(elementoPersonagem == 5 and elementoMonstro == 3):
		print("\nNão Efetivo")
		return danoPersonagem / 2
	elif(elementoPersonagem == 5 and elementoMonstro == 5):
		print("\nNão Efetivo")
		return danoPersonagem / 2
	
	# Super efeito Luz
	elif(elementoPersonagem == 7 and elementoMonstro == 6):
		print("\nSuper Efetivo")
		return danoPersonagem * 2
	
	# Nao efetivo Luz
	elif(elementoPersonagem == 7 and elementoMonstro == 7):
		print("\nNão Efetivo")
		return danoPersonagem / 2
	
	# Super efeito Trevas
	elif(elementoPersonagem == 6 and elementoMonstro == 7):
		print("\nSuper Efetivo")
		return danoPersonagem * 2
	
	# Nao efetivo Trevas
	elif(elementoPersonagem == 6 and elementoMonstro == 6):
		print("\nNão Efetivo")
		return danoPersonagem / 2
	
	# Super efeito Gelo
	elif(elementoPersonagem == 8 and elementoMonstro == 2):
		print("\nSuper Efetivo")
		return danoPersonagem * 2
	
	# Nao efetivo Gelo
	elif(elementoPersonagem == 8 and elementoMonstro == 1):
		print("\nNão Efetivo")
		return danoPersonagem / 2

	elif(elementoPersonagem == 8 and elementoMonstro == 8):
		print("\nNão Efetivo")
		return danoPersonagem / 2
	
	# Super efeito Floresta
	elif(elementoPersonagem == 9 and elementoMonstro == 2):
		print("\nSuper Efetivo")
		return danoPersonagem * 2
	elif(elementoPersonagem == 9 and elementoMonstro == 3):
		print("\nSuper Efetivo")
		return danoPersonagem * 2
	
	
	# Nao efetivo Floresta
	elif(elementoPersonagem == 9 and elementoMonstro == 1):
		print("\nNão Efetivo")
		return danoPersonagem / 2
	
	elif(elementoPersonagem == 9 and elementoMonstro == 9):
		print("\nNão Efetivo")
		return danoPersonagem / 2
	
	else:
		return danoPersonagem
		
###############################################################################################################
	
def aplica_defesa_magica_monstro(personagem, danoHabilidade, monstro, elementoPersonagem, elementoMonstro):
	if(personagem[40] == 1):
                danoPersonagem = (personagem[5] + personagem[11] + danoHabilidade)
                danoPersonagem = aplica_elemento(danoPersonagem, elementoPersonagem, monstro[6])
                danoPersonagem = danoPersonagem - monstro[4]

	elif(personagem[40] == 2):
                danoPersonagem = (personagem[4] + personagem[10] + danoHabilidade)                
                danoPersonagem = aplica_elemento(danoPersonagem, elementoPersonagem, monstro[6])
                danoPersonagem = danoPersonagem - monstro[3]
                
                taxaCritico = personagem[6] + personagem[52]
                taxaEsquiva = monstro[10]
                danoPersonagem = aplica_esquiva(danoPersonagem, taxaEsquiva, taxaCritico,1)

	elif(personagem[40] == 3):
                danoPersonagem = (personagem[6] + danoHabilidade  + personagem[52] + personagem[10])
                danoPersonagem = aplica_elemento(danoPersonagem, elementoPersonagem, monstro[6])
                danoPersonagem = danoPersonagem - monstro[3]
                
                taxaCritico = personagem[6] + personagem[52]
                taxaEsquiva = monstro[10]
                danoPersonagem = aplica_esquiva(danoPersonagem, taxaEsquiva, taxaCritico,1)

	if(danoPersonagem < 0):
		return 0
	else:
		return danoPersonagem

###############################################################################################################
	
def aplica_critico(dano, taxaCritico, atacante):
	sorteio = randint(1,100)
		
	if(sorteio <= taxaCritico):
		if(atacante == 1):
			print("\n\nVocê deu um Acerto Critico!")
		else:
			print("\n\nVocê recebeu um Acerto Critico!")
		return dano * 2
	else:
		return dano

###############################################################################################################
	
def aplica_defesa_monstro(personagem, monstro):
	taxaCritico = personagem[6] + personagem[52]
	taxaEsquiva = monstro[10]
	dano = personagem[4] + personagem[10]
	
	dano = aplica_esquiva(dano, taxaEsquiva, taxaCritico,1)
	if(dano > 0):
		dano = aplica_critico(dano, taxaCritico,1)
	dano = dano - monstro[3]
		
	if(dano < 0):
		return 0
	else:
		return dano
		
###############################################################################################################		
		
def aplica_defesa(personagem, monstro):
	dano = monstro[2]
	defesa = personagem[8] + personagem[12]
	taxaEsquiva = personagem[7] + personagem[51]
	dano = aplica_esquiva(dano, taxaEsquiva, monstro[15],2)
	if(dano > 0):
		dano = aplica_critico(dano, monstro[8],2)
		if(personagem[55] == 0 and personagem[2] > 0 and personagem[58] != monstro[14]):
                        aplica_status(personagem, monstro, monstro[14], monstro[13], 2)
	
	
	dano = dano - defesa
	if(dano < 0):
		return 0
	else:
		return dano

###############################################################################################################

def aumentar_level(personagem,monstro, habilidades):
	print("****************************************************************")
	personagem[18] = personagem[18] + monstro[5]
	print("Experiência ganha: " + str(monstro[5]) + "\tExperiência atual: " + str(personagem[18]))
                
	personagem[56] = personagem[56] + monstro[12]
	print("Dinheiro ganho: " + str(monstro[12]) + "\tDinheiro atual: " + str(personagem[56]))
	print("\n****************************************************************")
                
	sleep(3)
                
	if(personagem[18] >= (personagem[19] * 100)):
		personagem[18] = personagem[18] - (personagem[19] * 100)
		personagem[19] = personagem[19] + 1
                        
		print("****************************************************************")
		print("Voce subiu para o level " + str(personagem[19]) + " distribua seus pontos de atributo:")
		sleep(2)
		if(personagem[40] != 4):
                        pontos = 5
                        atributos = [0,0,0,0,0,0,0,0]
                        
                        print("\n****************************************************************")
                        print("\nAtributos aumentados: \nVida: \t\t" + str(personagem[0]) + " + " + str((5 * atributos[0])))		
                        print("Mana: \t\t" + str(personagem[1]) + " + " + str((5 * atributos[1])))						
                        print("Dano Físico: \t" + str(personagem[4]) + " + " + str((5 * atributos[2])))						
                        print("Dano Mágico: \t" + str(personagem[5]) + " + " + str((5 * atributos[3])))						
                        print("Defesa Física: \t" + str(personagem[8]) + " + " + str((5 * atributos[4])))						
                        print("Defesa Mágica: \t" + str(personagem[9]) + " + " + str((5 * atributos[5])))
                        print("Agilidade: \t" + str(personagem[7]) + " + " + str((2 * atributos[7])))
                        print("Critico: \t" + str(personagem[6]) + " + " + str((2 * atributos[6])))
                        
                        while(pontos != 0):
                                atributo = int(input("\nPontos para destribuir: %d \n1 - Vida \n2 - Mana \n3 - Dano Físico \n4 - Dano Mágico \n5 - Defesa Física \n6 - Defesa Mágica \n7 - Agilidade \n8 - Chance de Crítico \nR: " % pontos))
                
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
                        
                        evoluir_habilidades(personagem, habilidades, 1)
		else:
                        evoluir_habilidades(personagem, habilidades, 1)
                        personagem[2] = personagem[0]
                        personagem[1] = (personagem[1] + 10)
                        personagem[54] = personagem[1] + personagem[53]
                        personagem[3] = personagem[54]


###############################################################################################################

def personagem_ataca(personagem, monstro, cd):
	dano_personagem = aplica_defesa_monstro(personagem, monstro)
	dano_personagem = aplica_elemento(dano_personagem, personagem[57], monstro[6])
	monstro[0] = monstro[0] - dano_personagem
	print("\nVocê causou: %d de dano" % dano_personagem)
	if(monstro[0] > 0):
                aplica_status(personagem, monstro, personagem[57], personagem[66], 1)

	if(personagem[40] == 4):
                for i in range(5):
                        if(cd[i] != 0):
                                cd[i] = cd[i] - 1
                                

###############################################################################################################

def ataque_monstro(personagem, monstro, habilidades, cont):
	if(monstro[0] > 0):
		if(monstro[11] != 2):
			print("\n****************************************************************")
			dano_monstro = aplica_defesa(personagem, monstro)
			dano_monstro = aplica_elemento(dano_monstro, monstro[6], personagem[58])
			personagem[2] = personagem[2] - int(dano_monstro)
			
			print("\n" + monstro[7] + " causou %d de dano." % dano_monstro)
			sleep(2)			

				
			if(personagem[2] <= 0):
				return 0
			
	elif(monstro[11] == 2):
		print("\n" + monstro[7] + " está congelado")
		cont[0] = cont[0] + 1
		if(cont[0] == 2):
                        print("\n" + monstro[7] + " está livre.")
                        cont[0] = 0
                        monstro[11] = 0
	else:
		aumentar_level(personagem,monstro, habilidades)
		return 1
					
	if(monstro[11] != 0 and monstro[11] != 2 and monstro[0] > 0):
		if(monstro[11] != 2):
			danoStatus = aplica_dano_status(monstro[0], monstro[11])
			monstro[0] = monstro[0] - danoStatus
			print("\n" + str(monstro[7]) + " sofreu " + str(danoStatus) + " de dano por estar " + nome_status(monstro[11]))
			sleep(3)
			if(monstro[0] <= 0):
				aumentar_level(personagem, monstro, habilidades)
				return 1

	
###############################################################################################################

def ataque_monstroV2(personagem, monstro, habilidades, cont):
	if(monstro[0] > 0):
		if(monstro[11] != 2):
			print("\n****************************************************************")
			dano_monstro = aplica_defesa(personagem, monstro)
			dano_monstro = aplica_elemento(dano_monstro, monstro[6], personagem[58])
			personagem[2] = personagem[2] - int(dano_monstro)
			
			print("\n" + monstro[7] + " causou %d de dano." % dano_monstro)
			sleep(2)

			if(personagem[55] == 0):
                                aplica_status(personagem, monstro, monstro[14], monstro[15], 2)

				
			if(personagem[2] <= 0):
				return 0
			
		elif(monstro[11] == 2):
                        print("\n" + monstro[7] + " está congelado")
                        cont[0] = cont[0] + 1
                        if(cont[0] == 2):
                                print("\n" + monstro[7] + " está livre.")
                                cont[0] = 0
                                monstro[11] = 0
	
					
	if(monstro[11] != 0 and monstro[11] != 2 and monstro[0] > 0):
		if(monstro[11] != 2):
			danoStatus = aplica_dano_status(monstro[0], monstro[11])
			monstro[0] = monstro[0] - danoStatus
			print("\n" + str(monstro[7]) + " sofreu " + str(danoStatus) + " de dano por estar " + nome_status(monstro[11]))
			sleep(3)
			if(monstro[0] <= 0):
				aumentar_level(personagem, monstro, habilidades)
				return 1

	
###############################################################################################################


def monstro_vs_monstro(monstroAtaq, monstroDefe):
        dano_ataque = monstroAtaq[2] - monstroDefe[3]
        if(dano_ataque < 0):
                dano_ataque = 0

        monstroDefe[0] = monstroDefe[0] - dano_ataque

        print("\n****************************************************************")
        print(monstroAtaq[7] + " causou " + str(dano_ataque) + " de dano ao " + monstroDefe[7])
        sleep(2)

###############################################################################################################

def usar_habilidade_druida(personagem, resp, habilidades, cd):
        if(resp == 1): #Lobo
                personagem[0] = 30 + (int((30 / 4)) * (habilidades[6] - 1))
                personagem[2] = 30 + (int((30 / 4)) * (habilidades[6] - 1))
                personagem[4] = 15 + (int((15 / 4)) * (habilidades[6] - 1))
                personagem[6] = 5 + (int((5 / 4)) * (habilidades[6] - 1))
                personagem[7] = 5 + (int((5 / 4)) * (habilidades[6] - 1))
                personagem[8] = 5 + (int((5 / 4)) * (habilidades[6] - 1))
                personagem[9] = 5 + (int((5 / 4)) * (habilidades[6] - 1))
                personagem[57] = 5
                cd[0] = 5

        elif(resp == 2): #Urso
                personagem[0] = 60  + (int((60 / 4)) * (habilidades[14] - 1))
                personagem[2] = 60  + (int((60 / 4)) * (habilidades[14] - 1))
                personagem[4] = 5 + (int((5 / 4)) * (habilidades[14] - 1))
                personagem[6] = 2 + (int((2 / 4)) * (habilidades[14] - 1))
                personagem[7] = 0
                personagem[8] = 8 + (int((8 / 4)) * (habilidades[14] - 1))
                personagem[9] = 8 + (int((8 / 4)) * (habilidades[14] - 1))
                personagem[57] = 3
                cd[1] = 5

        elif(resp == 3): #Aguia
                personagem[0] = 25 + (int((25 / 4)) * (habilidades[21] - 1))
                personagem[2] = 25 + (int((25 / 4)) * (habilidades[21] - 1))
                personagem[4] = 10 + (int((10 / 4)) * (habilidades[21] - 1))
                personagem[6] = 20 + (int((20 / 4)) * (habilidades[21] - 1))
                personagem[7] = 10 + (int((10 / 4)) * (habilidades[21] - 1))
                personagem[8] = 5 + (int((5 / 4)) * (habilidades[21] - 1))
                personagem[9] = 5 + (int((5 / 4)) * (habilidades[21] - 1))
                personagem[57] = 4
                cd[2] = 5

        elif(resp == 4): #Tigre
                personagem[0] = 25 + (int((25 / 4)) * (habilidades[30] - 1))
                personagem[2] = 25 + (int((25 / 4)) * (habilidades[30] - 1))
                personagem[4] = 20 + (int((20 / 4)) * (habilidades[30] - 1))
                personagem[6] = 10 + (int((10 / 4)) * (habilidades[30] - 1))
                personagem[7] = 20 + (int((20 / 4)) * (habilidades[30] - 1))
                personagem[8] = 4 + (int((4 / 4)) * (habilidades[30] - 1))
                personagem[9] = 4 + (int((4 / 4)) * (habilidades[30] - 1))
                personagem[57] = 1
                cd[3] = 5


        elif(resp == 5): #Tartaruga
                personagem[0] = 40 + (int((40 / 4)) * (habilidades[38] - 1))
                personagem[2] = 40 + (int((40 / 4)) * (habilidades[38] - 1))
                personagem[4] = 0
                personagem[6] = 0
                personagem[7] = 0
                personagem[8] = 20 + (int((20 / 4)) * (habilidades[38] - 1))
                personagem[9] = 20 + (int((20 / 4)) * (habilidades[38] - 1))
                personagem[57] = 2
                cd[4] = 5


        personagem[3] = personagem[3] - 10

        

        
                

###############################################################################################################

def usar_habilidade(personagem, monstro, resp):
	if(personagem[20 + (4 * (int(resp) - 1))] != 0):
		if(personagem[3] >= personagem[22 + (4 * (resp - 1))] and personagem[3] != 0):
			dano_personagem = aplica_defesa_magica_monstro(personagem, personagem[21 + (4 * (resp - 1))], monstro, personagem[23 + (4 * (resp - 1))], monstro[6])
			monstro[0] = monstro[0] - dano_personagem
			
			print("\nVocê causou: " + str(dano_personagem) + " de dano" + " a " + monstro[7])
			sleep(2)
						
			if(monstro[11] == 0 and monstro[0] > 0):
				aplica_status(personagem, monstro, personagem[41 + (2 * (resp - 1))], personagem[42 + (2 * (resp - 1))], 1)

			return resp
	
		else:
                        print("\nMana insuficiente")
                        sleep(3)
                        return 0

###############################################################################################################
                
def usar_pocao(personagem, resp, bolsa):
	if(resp == "1"):
		if(bolsa[3] > 0):
			personagem[2] = personagem[2] + bolsa[1]
			bolsa[3] = bolsa[3] - 1
			if(personagem[2] >= personagem[0]):
				personagem[2] = personagem[0]
			
			print("\nVocê recuperou: %d de vida" % bolsa[1])
			sleep(2)
			return "1"
						
		else:
			print("\nPoções de vida insuficientes")
			return "@"
			sleep(3)

	elif(resp == "2"):
		if(bolsa[7] > 0):
			personagem[3] = personagem[3] + bolsa[5]
			bolsa[7] = bolsa[7] - 1
			if(personagem[3] >= personagem[54]):
				personagem[3] = personagem[54]
					
			print("\nVocê recuperou: %d de mana" % bolsa[5])
			sleep(2)
			return "2"
			
		else:
			print("\nPoções de mana insuficientes")
			return "@"
			sleep(3)


	elif(resp == "3"):
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
			return "3"
			
		else:
			print("\nPoções hibridas insuficientes")
			return "@"
			sleep(3)


	elif(resp == "4"):
                if(bolsa[14] > 0):
                        if(personagem[55] == 9):
                                print("\nVocê não esta mais envenenado.")
                                bolsa[14] = bolsa[14] - 1
                                personagem[55] = 0
                                return "4"
                                
                        else:
                                print("Você não esta envenenado.")
                                return "@"

                else:
                        print("\nAntidotos insuficientes.")
                        return "@"
                        sleep(3)
	else:
                print("\nEscolha uma opção valida\n")
                sleep(2)
                return "@"

                        
###############################################################################################################

def porcentoVida(vidaMaxima, vidaAtual):
        porcento = vidaAtual * 100

        porcento = porcento / vidaMaxima

        return(int(porcento))


###############################################################################################################

def aplica_defesa_personagem(personagem, habilidadeMonstro):
        dano = habilidadeMonstro[0]

        dano = aplica_elemento(dano, habilidadeMonstro[3], personagem[58])

        if(habilidadeMonstro[1] == 1):
                defesaPersonagem = personagem[8] + personagem[12]

        else:
                defesaPersonagem = personagem[9] + personagem[13]


        dano = dano - defesaPersonagem


        if(dano < 0):
                return 0
        else:
                return dano

        
                
###############################################################################################################

def aplica_dano_monstro(personagem, dano):
        personagem[2] = personagem[2] - dano

        if(personagem[2] < 0):
                personagem[2] = 0


        
###############################################################################################################

def habilidade_chefe(monstros, personagem, indiceHabilidade):
        if(indiceHabilidade == 1):
                dano = aplica_defesa_personagem(personagem, monstros[0][17])
                

        elif(indiceHabilidade == 2):
                dano = aplica_defesa_personagem(personagem, monstros[0][18])

                

        elif(indiceHabilidade == 3):
                dano = aplica_defesa_personagem(personagem, monstros[0][19])


        aplica_dano_monstro(personagem, dano)

        
###############################################################################################################
				
def batalha(personagem, monstro, habilidades, bolsa):
	print("\n****************************************************************")
	print("\n%s apareceu\n" % monstro[7])
	sleep(4)
	
	if(personagem[40] == 4):
                personagem[0] = 1
                personagem[2] = 1
                personagem[4] = 0
                personagem[8] = 0
                
	cd = [0,0,0,0,0]
	cont = [0]
	while(personagem[2] > 0 and monstro[0] > 0):
		resp = "0"
		while (resp != "1" and resp != "2" and resp != "3" and resp != "4"):
			print("****************************************************************")
			print("Inimigo: \nNome:"+ monstro[7] +" \t Vida Inimigo: " + str(monstro[0]))
			print ("\nVocê: \nSua Vida: "+ str(personagem[2]) +" \tPoções de Vida: "+ str(bolsa[3]) +" \nSua Mana: "+ str(personagem[3]) +" \tPoções de Mana: "+ str(bolsa[7]))
			print ("\n1 - Atacar \t\t 2 - Poções \n3 - Habilidade \t\t 4 - Fugir")
			resp = input("\nR: ")
		

		if(resp == "1"):
			personagem_ataca(personagem, monstro, cd)
		
		
		elif(resp == "2"):
			print("****************************************************************")
			resp2 = "0"
			while(resp2 != "1" and resp2 != "2" and resp2 != "3" and resp2 != "4" and resp2 != "5"):	
				print("Pots: \t\t\t\t Restaura: \n1 - Poção de Vida \t\t " + str(bolsa[1]) + " de Vida\n2 - Poção de Mana \t\t " + str(bolsa[5]) + " de Mana \n3 - Poção Hibrida \t\t " + str(bolsa[16]) +" \ " + str(bolsa[17]) + " de V\M \n4 - Antidoto \t\t\t Tira Veneno \n5 - Voltar")
				resp2 = input("R: ")
				if(resp2 == "5"):
                                        resp = "0"
				else:
                                        resp2 = usar_pocao(personagem, resp2, bolsa)

				
			
		elif(resp == "3"):
			if(personagem[40] != 4):
                                print("****************************************************************")
                                print("Habilidades:")
                                print("Nome das Habilidades: \t\tCusto de Mana: ")
                                print("1 - " + str(nome_habilidade(personagem[20])) + " " * (28 - len(nome_habilidade(personagem[20]))) + str(personagem[22]))
                                print("2 - " + str(nome_habilidade(personagem[24])) + " " * (28 - len(nome_habilidade(personagem[24]))) + str(personagem[26]))
                                print("3 - " + str(nome_habilidade(personagem[28])) + " " * (28 - len(nome_habilidade(personagem[28]))) + str(personagem[30]))
                                print("4 - " + str(nome_habilidade(personagem[32])) + " " * (28 - len(nome_habilidade(personagem[32]))) + str(personagem[34]))
                                print("5 - " + str(nome_habilidade(personagem[36])) + " " * (28 - len(nome_habilidade(personagem[36]))) + str(personagem[38]))
                                print("0 - Voltar")
			else:
                                print("****************************************************************")
                                print("Habilidades:")
                                print("Nome das Habilidades: \t\tCusto de Mana: ")
                                print("1 - " + str(nome_habilidade(personagem[20])) + " " * (28 - len(nome_habilidade(personagem[20]))) + str(personagem[22]) + "\tTurnos: " + str(cd[0]))
                                print("2 - " + str(nome_habilidade(personagem[24])) + " " * (28 - len(nome_habilidade(personagem[24]))) + str(personagem[26]) + "\tTurnos: " + str(cd[1]))
                                print("3 - " + str(nome_habilidade(personagem[28])) + " " * (28 - len(nome_habilidade(personagem[28]))) + str(personagem[30]) + "\tTurnos: " + str(cd[2]))
                                print("4 - " + str(nome_habilidade(personagem[32])) + " " * (28 - len(nome_habilidade(personagem[32]))) + str(personagem[34]) + "\tTurnos: " + str(cd[3]))
                                print("5 - " + str(nome_habilidade(personagem[36])) + " " * (28 - len(nome_habilidade(personagem[36]))) + str(personagem[38]) + "\tTurnos: " + str(cd[4]))
                                print("0 - Voltar")
                                
			resp2 = "6"
			while(resp2 != "1" and resp2 != "2" and resp2 != "3" and resp2 != "4" and resp2 != "5" and resp2 != "0"):
                                resp2 = input("R: ")     
                                resp2 = int(resp2)
                                
                                if(resp2 == 1 or resp2 == 2 or resp2 == 3 or resp2 == 4 or resp2 == 5):
                                        if(personagem[40] == 4):
                                                if(personagem[3] >= 10):
                                                        if(cd[resp2 - 1] == 0):
                                                                usar_habilidade_druida(personagem, resp2, habilidades, cd)
                                                                personagem_ataca(personagem, monstro, cd)
                                                        else:
                                                                if(resp2 == 0):
                                                                        resp = "0"

                                                                else:
                                                                        print("\nEsta habilidade esta em tempo de recarga.")
                                                                        resp2 = "6"
                                                                        sleep(2)
                                                else:
                                                        print("\nMana insuficiente.")
                                                        sleep(2)
                                                        resp = "0"
                                        else:
                                                resp2 = usar_habilidade(personagem, monstro, resp2)
                                                
                                                if(personagem[59 + (1 * (resp2 - 1))] == 2):
                                                        resp2 = usar_habilidade(personagem, monstro, resp2)
                                                
                                                if(resp2 == 0):
                                                        print("\nMana Insuficiente")
                                                        resp = "0"
                                                        sleep(2)
                                                else:
                                                        personagem[3] = personagem[3] - personagem[22 + (4 * (resp2 - 1))]
                                        resp2 = str(resp2)		
                                else:
                                        resp2 = "0"
				
		elif(resp == "4"):
			if(monstro1[9] == 0):
                                print("\nVocê Fugiu")
                                sleep(2)
                                return 2
			elif(monstro1[9] == 1):
                                print("\nVocê não pode fugir de lutas contra Chefes.")
                                sleep(3)
                                resp = "0"
			elif(monstro1[9] == 2):
                                print("\nVocê não pode fugir desta luta.")
                                sleep(3)
                                resp = "0"
				
		''' Colocar dano de monstro aqui '''
		resultado = ataque_monstro(personagem, monstro, habilidades, cont)
		if(resultado == 1):
                        return 1
		elif(resultado == 0):
			return 0
		
		if(personagem[2] != 0 and personagem[55] != 0 and personagem[55] != 2):
                        danoStatus = aplica_dano_status(personagem[2], personagem[55])
                        personagem[2] = personagem[2] - danoStatus
                        print("\nVocê sofreu " + str(danoStatus) + " de dano por estar " + nome_status(personagem[55]))
                        sleep(2)

                        if(personagem[2] <= 0):
                                return 0


                                                
###############################################################################################################		

def batalha_Vs2(personagem, monstro1, monstro2, habilidades, bolsa):
	print("\n****************************************************************")
	print("\n" + monstro1[7] + " e " + monstro2[7] + " apareceram.")
	sleep(4)
	
	if(personagem[40] == 4):
                personagem[0] = 1
                personagem[2] = 1
                personagem[4] = 0
                personagem[8] = 0
                
	cd = [0,0,0,0,0]
	retornos = [0,0]
	cont1 = [0]
	cont2 = [0]
	while(personagem[2] > 0 and monstro1[0] > 0 or personagem[2] > 0 and monstro2[0] > 0):
		if(monstro1[0] <= 0):
			monstro1[0] = 0
		if(monstro2[0] <= 0):
			monstro2[0] = 0
		
		resp = "0"
		while (resp != "1" and resp != "2" and resp != "3" and resp != "4"):
			print("****************************************************************")
			print("Inimigo1: \nNome:"+ monstro1[7] +" \t Vida Inimigo: " + str(monstro1[0]))
			print("Inimigo2: \nNome:"+ monstro2[7] +" \t Vida Inimigo: " + str(monstro2[0]))
			print ("\nVocê: \nSua Vida: "+ str(personagem[2]) +" \tPoções de Vida: "+ str(bolsa[3]) +" \nSua Mana: "+ str(personagem[3]) +" \tPoções de Mana: "+ str(bolsa[7]))
			print ("\n1 - Atacar \t\t 2 - Poções \n3 - Habilidade \t\t 4 - Fugir")
			resp = input("\nR: ")
		

			if(resp == "1"):
                                respAtaque = "0"
                                while (respAtaque != "1" and respAtaque != "2"):
                                        print("\nEscolha um oponente para atacar:")
                                        print("Inimigo1: \nNome:"+ monstro1[7] +" \t Vida: " + str(monstro1[0]))
                                        print("Inimigo2: \nNome:"+ monstro2[7] +" \t Vida: " + str(monstro2[0]))
                                        respAtaque = input("R: ")
                                        if(respAtaque == "1" and monstro1[0] > 0):
                                                personagem_ataca(personagem, monstro1, cd)
                                                
                                        elif(respAtaque == "2" and monstro2[0] > 0):
                                                personagem_ataca(personagem, monstro2, cd)
                                        
                                        else:
                                                print("\nEste oponente esta morto, escolha outro.\n")
                                                respAtaque = "0"
                        
			elif(resp == "2"):
				print("****************************************************************")
				resp2 = "0"
				while(resp2 != "1" and resp2 != "2" and resp2 != "3" and resp2 != "4" and resp2 != "5"):	
					print("Pots: \t\t\t\t Restaura: \n1 - Poção de Vida \t\t " + str(bolsa[1]) + " de Vida\n2 - Poção de Mana \t\t " + str(bolsa[5]) + " de Mana \n3 - Poção Hibrida \t\t " + str(bolsa[16]) +" \ " + str(bolsa[17]) + " de V\M \n4 - Antidoto \t\t\t Tira Veneno \n5 - Voltar")
					resp2 = input("R: ")

					if(resp2 == "5"):
                                                resp = "0"
					else:
                                                resp2 = usar_pocao(personagem, resp2, bolsa)

                                        
                                
                     
                
			elif(resp == "3"):
                                if(personagem[40] != 4):
                                        print("****************************************************************")
                                        print("Habilidades:")
                                        print("Nome das Habilidades: \t\tCusto de Mana: ")
                                        print("1 - " + str(nome_habilidade(personagem[20])) + " " * (28 - len(nome_habilidade(personagem[20]))) + str(personagem[22]))
                                        print("2 - " + str(nome_habilidade(personagem[24])) + " " * (28 - len(nome_habilidade(personagem[24]))) + str(personagem[26]))
                                        print("3 - " + str(nome_habilidade(personagem[28])) + " " * (28 - len(nome_habilidade(personagem[28]))) + str(personagem[30]))
                                        print("4 - " + str(nome_habilidade(personagem[32])) + " " * (28 - len(nome_habilidade(personagem[32]))) + str(personagem[34]))
                                        print("5 - " + str(nome_habilidade(personagem[36])) + " " * (28 - len(nome_habilidade(personagem[36]))) + str(personagem[38]))
                                        print("0 - Voltar")
                                else:
                                        print("****************************************************************")
                                        print("Habilidades:")
                                        print("Nome das Habilidades: \t\tCusto de Mana: ")
                                        print("1 - " + str(nome_habilidade(personagem[20])) + " " * (28 - len(nome_habilidade(personagem[20]))) + str(personagem[22]) + "\tTurnos: " + str(cd[0]))
                                        print("2 - " + str(nome_habilidade(personagem[24])) + " " * (28 - len(nome_habilidade(personagem[24]))) + str(personagem[26]) + "\tTurnos: " + str(cd[1]))
                                        print("3 - " + str(nome_habilidade(personagem[28])) + " " * (28 - len(nome_habilidade(personagem[28]))) + str(personagem[30]) + "\tTurnos: " + str(cd[2]))
                                        print("4 - " + str(nome_habilidade(personagem[32])) + " " * (28 - len(nome_habilidade(personagem[32]))) + str(personagem[34]) + "\tTurnos: " + str(cd[3]))
                                        print("5 - " + str(nome_habilidade(personagem[36])) + " " * (28 - len(nome_habilidade(personagem[36]))) + str(personagem[38]) + "\tTurnos: " + str(cd[4]))
                                        print("0 - Voltar")
                                
                                resp2 = "6"
                                while(resp2 != "1" and resp2 != "2" and resp2 != "3" and resp2 != "4" and resp2 != "5" and resp2 != "0"):	
                                        resp2 = input("R: ")
                                        if(resp2 == "0"):
                                                resp = "0"
                                        else:
                                                resp2 = int(resp2)

                                        if(resp2 == 1 or resp2 == 2 or resp2 == 3 or resp2 == 4 or resp2 == 5):
                                                respAtaque = "0"
                                                while (respAtaque != "1" and respAtaque != "2" and resp2 != "0"):                                                
                                                        if(personagem[59 + (1 * (resp2 - 1))] == 1):
                                                                print("\nEscolha um oponente para atacar:")
                                                                print("1 - "+ monstro1[7] +" \t Vida: " + str(monstro1[0]))
                                                                print("2 - "+ monstro2[7] +" \t Vida: " + str(monstro2[0]))                                                        

                                                                respAtaque = input("R: ")
                                                                if(personagem[40] == 4):
                                                                        if(personagem[3] >= 10):
                                                                                if(cd[resp2 - 1] == 0):
                                                                                        if(respAtaque == "1" and monstro1[0] > 0):
                                                                                                usar_habilidade_druida(personagem, resp2, habilidades, cd)
                                                                                                personagem_ataca(personagem, monstro1, cd)
                                                                        
                                                                                        elif(respAtaque == "2" and monstro2[0] > 0):
                                                                                                usar_habilidade_druida(personagem, resp2, habilidades, cd)
                                                                                                personagem_ataca(personagem, monstro2, cd)
                                                                                                                                                                       
                                                                                        else:
                                                                                                print("\nEste oponente esta morto, escolha outro.\n")
                                                                                                respAtaque = "0"
                                                                                else:
                                                                                        if(respAtaque == "0"):
                                                                                           resp = "0"

                                                                                        else:
                                                                                                print("\nEsta habilidade esta em tempo de recarga.")
                                                                                                resp2 = "6"
                                                                                                sleep(2)
                                                                        else:
                                                                                print("\nMana insuficiente.")
                                                                                sleep(2)
                                                                                resp = "0"

                                   
                                                                else:
                                                                        if(respAtaque == "1" and monstro1[0] > 0):
                                                                                resp2 = usar_habilidade(personagem, monstro1, resp2)
                                                        
                                                                        elif(respAtaque == "2" and monstro2[0] > 0):
                                                                                resp2 = usar_habilidade(personagem, monstro2, resp2)
                                                                                                                                        

                                                                        else:
                                                                                print("\nEste oponente esta morto, escolha outro.\n")
                                                                                respAtaque = "0"

                                                        elif(personagem[59 + (1 * (resp2 - 1))] == 2):
                                                                print("\nEscolha um oponente para atacar:")
                                                                print("1 - "+ monstro1[7] +" \t Vida: " + str(monstro1[0]))
                                                                print("2 - "+ monstro2[7] +" \t Vida: " + str(monstro2[0]))
                                                                
                                                                
                                                                respAtaque = input("R: ")
                                                                if(respAtaque == "1" and monstro1[0] > 0):
                                                                        usar_habilidade(personagem, monstro1, resp2)
                                                
                                                                elif(respAtaque == "2" and monstro2[0] > 0):
                                                                        usar_habilidade(personagem, monstro2, resp2)
                                                                
                                                                

                                                                print("\nEscolha outro oponente para atacar:")
                                                                print("1 - "+ monstro1[7] +" \t Vida: " + str(monstro1[0]))
                                                                print("2 - "+ monstro2[7] +" \t Vida: " + str(monstro2[0]))
                                                                

                                                                respAtaque = input("R: ")
                                                                if(respAtaque == "1" and monstro1[0] > 0):
                                                                        usar_habilidade(personagem, monstro1, resp2)
                                                
                                                                elif(respAtaque == "2" and monstro2[0] > 0):
                                                                        usar_habilidade(personagem, monstro2, resp2)
                                                                
                                                                

                                                        elif(personagem[59 + (1 * (resp2 - 1))] == 3):
                                                                usar_habilidade(personagem, monstro1, resp2)
                                                                usar_habilidade(personagem, monstro2, resp2)                                                     
                                                                respAtaque = "1"

                                                        if(resp2 != 0 and personagem[40] != 4):
                                                                personagem[3] = personagem[3] - personagem[22 + (4 * (resp2 - 1))]
                                                                

                                                        resp2 = str(resp2)
                                        else:
                                                respAtaque = "0"
                                        
			elif(resp == "4"):
                                if(monstro1[9] == 0 and monstro2[9] == 0):
                                        print("\nVocê Fugiu")
                                        sleep(2)
                                        return 2
                                elif(monstro1[9] == 1 or monstro2[9] == 1):
                                        print("\nVocê não pode fugir de lutas contra Chefes.")
                                        sleep(3)
                                        resp = "0"
                                elif(monstro1[9] == 2 or monstro2[9] == 2):
                                        print("\nVocê não pode fugir desta luta.")
                                        sleep(3)
                                        resp = "0"
				
		''' Colocar dano de monstro1 aqui '''
		
		if(retornos[0] != 1):
			retorno1 = ataque_monstro(personagem, monstro1, habilidades, cont1)
			if(retorno1 == 0):
				return 0
			elif(retorno1 == 1):
				retornos[0] = 1
		
		if(retornos[1] != 1):
			retorno2 = ataque_monstro(personagem, monstro2, habilidades, cont2)
			if(retorno2 == 0):
				return 0
			elif(retorno2 == 1):
				retornos[1] = 1


		if(personagem[2] != 0 and personagem[55] != 0 and personagem[55] != 2):
                        danoStatus = aplica_dano_status(personagem[2], personagem[55])
                        personagem[2] = personagem[2] - danoStatus
                        print("\nVocê sofreu " + str(danoStatus) + " de dano por estar " + nome_status(personagem[55]))
                        sleep(2)

                        if(personagem[2] <= 0):
                                return 0

	



###############################################################################################################		

		

def batalha_arena_Vs9(personagem, gladiador, habilidades, bolsa):
	print("\n****************************************************************")
	cont = 0
	retornos = [0,0,0]
	cd = [0,0,0,0,0]
	cont1 = [0]
	cont2 = [0]
	cont3 = [0]
	while(personagem[2] > 0 and gladiador[0][0] > 0 or personagem[2] > 0 and gladiador[1][0] > 0 or personagem[2] > 0 and gladiador[2][0] > 0 or personagem[2] > 0 and gladiador[3][0] > 0 or personagem[2] > 0 and gladiador[4][0] > 0 or personagem[2] > 0 and gladiador[5][0] > 0 or personagem[2] > 0 and gladiador[6][0] > 0 or personagem[2] > 0 and gladiador[7][0] > 0 or personagem[2] > 0 and gladiador[8][0] > 0):
		if(gladiador[0][0] <= 0):
			gladiador[0][0] = 0
		if(gladiador[1][0] <= 0):
			gladiador[1][0] = 0
		if(gladiador[2][0] <= 0):
			gladiador[2][0] = 0
		if(gladiador[3][0] <= 0):
			gladiador[3][0] = 0
		if(gladiador[4][0] <= 0):
			gladiador[4][0] = 0
		if(gladiador[5][0] <= 0):
			gladiador[5][0] = 0
		if(gladiador[6][0] <= 0):
			gladiador[6][0] = 0
		if(gladiador[7][0] <= 0):
			gladiador[7][0] = 0
		if(gladiador[8][0] <= 0):
			gladiador[8][0] = 0
		
		
		resp = "0"
		while (resp != "1" and resp != "2" and resp != "3" and resp != "4"):
			print("****************************************************************")
			print("Nome:"+ gladiador[0][7] +" \t Vida: " + str(gladiador[0][0]))
			print("Nome:"+ gladiador[1][7] +" \t Vida: " + str(gladiador[1][0]))
			print("Nome:"+ gladiador[2][7] +" \t Vida: " + str(gladiador[2][0]))
			print("Nome:"+ gladiador[3][7] +" \t Vida: " + str(gladiador[3][0]))
			print("Nome:"+ gladiador[4][7] +" \t Vida: " + str(gladiador[4][0]))
			print("Nome:"+ gladiador[5][7] +" \t Vida: " + str(gladiador[5][0]))
			print("Nome:"+ gladiador[6][7] +" \t Vida: " + str(gladiador[6][0]))
			print("Nome:"+ gladiador[7][7] +" \t Vida: " + str(gladiador[7][0]))
			print("Nome:"+ gladiador[8][7] +" \t Vida: " + str(gladiador[8][0]))
			
			print ("\nVocê: \nSua Vida: "+ str(personagem[2]) +" \tPoções de Vida: "+ str(bolsa[3]) +" \nSua Mana: "+ str(personagem[3]) +" \tPoções de Mana: "+ str(bolsa[7]))
			print ("\n1 - Atacar \t\t 2 - Poções \n3 - Habilidade \t\t 4 - Fugir")
			resp = input("\nR: ")
		

			if(resp == "1"):
                                respAtaque = "0"
                                while (respAtaque != "1" and respAtaque != "2" and respAtaque != "3" and respAtaque != "4" and respAtaque != "5" and respAtaque != "6" and respAtaque != "7" and respAtaque != "8" and respAtaque != "9"):
                                        print("\nEscolha um oponente para atacar:")
                                        print("1 - "+ gladiador[0][7] +" \t Vida: " + str(gladiador[0][0]))
                                        print("2 - "+ gladiador[1][7] +" \t Vida: " + str(gladiador[1][0]))
                                        print("3 - "+ gladiador[2][7] +" \t Vida: " + str(gladiador[2][0]))
                                        print("4 - "+ gladiador[3][7] +" \t Vida: " + str(gladiador[3][0]))
                                        print("5 - "+ gladiador[4][7] +" \t Vida: " + str(gladiador[4][0]))
                                        print("6 - "+ gladiador[5][7] +" \t Vida: " + str(gladiador[5][0]))
                                        print("7 - "+ gladiador[6][7] +" \t Vida: " + str(gladiador[6][0]))
                                        print("8 - "+ gladiador[7][7] +" \t Vida: " + str(gladiador[7][0]))
                                        print("9 - "+ gladiador[8][7] +" \t Vida: " + str(gladiador[8][0]))
			
                                        respAtaque = input("R: ")
                                        if(respAtaque == "1" and gladiador[0][0] > 0):
                                                personagem_ataca(personagem, gladiador[0], cd)
                                                
                                        elif(respAtaque == "2" and gladiador[1][0] > 0):
                                                personagem_ataca(personagem, gladiador[1], cd)
                                        
                                        elif(respAtaque == "3" and gladiador[2][0] > 0):
                                                personagem_ataca(personagem, gladiador[2], cd)

                                        elif(respAtaque == "4" and gladiador[3][0] > 0):
                                                personagem_ataca(personagem, gladiador[3], cd)

                                        elif(respAtaque == "5" and gladiador[4][0] > 0):
                                                personagem_ataca(personagem, gladiador[4], cd)

                                        elif(respAtaque == "6" and gladiador[5][0] > 0):
                                                personagem_ataca(personagem, gladiador[5], cd)

                                        elif(respAtaque == "7" and gladiador[6][0] > 0):
                                                personagem_ataca(personagem, gladiador[6], cd)

                                        elif(respAtaque == "8" and gladiador[7][0] > 0):
                                                personagem_ataca(personagem, gladiador[7], cd)

                                        elif(respAtaque == "9" and gladiador[8][0] > 0):
                                                personagem_ataca(personagem, gladiador[8], cd)
                                        
                                        else:
                                                print("\nEste oponente esta morto, escolha outro.\n")
                                                respAtaque = "0"
                        
			elif(resp == "2"):
                                print("****************************************************************")
                                resp2 = "5"
                                while(resp2 != "1" and resp2 != "2" and resp2 != "0" and resp2 != "3" and resp2 != "4"):	
                                        print("Pots: \t\t\t\t Restaura: \n1 - Poção de Vida \t\t " + str(bolsa[1]) + " de Vida\n2 - Poção de Mana \t\t " + str(bolsa[5]) + " de Mana \n3 - Poção Hibrida \t\t " + str(bolsa[16]) +" \ " + str(bolsa[17]) + " de V\M \n4 - Antidoto \t\t\t Tira Veneno \n0 - Voltar")
                                        resp2 = input("R: ")
                                
                                        resp2 = usar_pocao(personagem, resp2, bolsa)

                                        if(resp2 == "0"):
                                                resp = "0"
                
			elif(resp == "3"):
                                print("****************************************************************")
                                print("Habilidades:")
                                print("Nome das Habilidades: \t\tCusto de Mana: ")
                                print("1 - " + str(nome_habilidade(personagem[20])) + " " * (28 - len(nome_habilidade(personagem[20]))) + str(personagem[22]))
                                print("2 - " + str(nome_habilidade(personagem[24])) + " " * (28 - len(nome_habilidade(personagem[24]))) + str(personagem[26]))
                                print("3 - " + str(nome_habilidade(personagem[28])) + " " * (28 - len(nome_habilidade(personagem[28]))) + str(personagem[30]))
                                print("4 - " + str(nome_habilidade(personagem[32])) + " " * (28 - len(nome_habilidade(personagem[32]))) + str(personagem[34]))
                                print("5 - " + str(nome_habilidade(personagem[36])) + " " * (28 - len(nome_habilidade(personagem[36]))) + str(personagem[38]))
                                print("0 - Voltar")
                                
                                resp2 = "6"
                                while(resp2 != "1" and resp2 != "2" and resp2 != "3" and resp2 != "4" and resp2 != "5" and resp2 != "0"):
                                        resp2 = input("R: ")
                                        if(resp2 == "0"):
                                                resp = "0"
                                        else:
                                                resp2 = int(resp2)
                                        respAtaque = "0"
                                        while (respAtaque != "1" and respAtaque != "2" and respAtaque != "3" and resp2 != "0" and respAtaque != "4" and respAtaque != "5" and respAtaque != "6" and respAtaque != "7" and respAtaque != "8" and respAtaque != "9"):
                                                if(personagem[59 + (1 * (int(resp2) - 1))] == 1):
                                                        print("\nEscolha um oponente para atacar:")
                                                        print("1 - "+ gladiador[0][7] +" \t Vida: " + str(gladiador[0][0]))
                                                        print("2 - "+ gladiador[1][7] +" \t Vida: " + str(gladiador[1][0]))
                                                        print("3 - "+ gladiador[2][7] +" \t Vida: " + str(gladiador[2][0]))
                                                        print("4 - "+ gladiador[3][7] +" \t Vida: " + str(gladiador[3][0]))
                                                        print("5 - "+ gladiador[4][7] +" \t Vida: " + str(gladiador[4][0]))
                                                        print("6 - "+ gladiador[5][7] +" \t Vida: " + str(gladiador[5][0]))
                                                        print("7 - "+ gladiador[6][7] +" \t Vida: " + str(gladiador[6][0]))
                                                        print("8 - "+ gladiador[7][7] +" \t Vida: " + str(gladiador[7][0]))
                                                        print("9 - "+ gladiador[8][7] +" \t Vida: " + str(gladiador[8][0]))
                                                        respAtaque = input("R: ")
                                                        
                                                        if(respAtaque == "1" and gladiador[0][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[0], resp2)
                                        
                                                        elif(respAtaque == "2" and gladiador[1][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[1], resp2)
                                                        
                                                        elif(respAtaque == "3" and gladiador[2][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[2], resp2)

                                                        elif(respAtaque == "4" and gladiador[3][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[3], resp2)

                                                        elif(respAtaque == "5" and gladiador[4][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[4], resp2)

                                                        elif(respAtaque == "6" and gladiador[5][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[5], resp2)

                                                        elif(respAtaque == "7" and gladiador[6][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[6], resp2)

                                                        elif(respAtaque == "8" and gladiador[7][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[7], resp2)

                                                        elif(respAtaque == "9" and gladiador[8][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[8], resp2)

                                                        else:
                                                                print("\nEste oponente esta morto, escolha outro.\n")
                                                                respAtaque = "0"

                                                elif(personagem[59 + (1 * (int(resp2) - 1))] == 2):
                                                        print("\nEscolha um oponente para atacar:")
                                                        print("1 - "+ gladiador[0][7] +" \t Vida: " + str(gladiador[0][0]))
                                                        print("2 - "+ gladiador[1][7] +" \t Vida: " + str(gladiador[1][0]))
                                                        print("3 - "+ gladiador[2][7] +" \t Vida: " + str(gladiador[2][0]))
                                                        print("4 - "+ gladiador[3][7] +" \t Vida: " + str(gladiador[3][0]))
                                                        print("5 - "+ gladiador[4][7] +" \t Vida: " + str(gladiador[4][0]))
                                                        print("6 - "+ gladiador[5][7] +" \t Vida: " + str(gladiador[5][0]))
                                                        print("7 - "+ gladiador[6][7] +" \t Vida: " + str(gladiador[6][0]))
                                                        print("8 - "+ gladiador[7][7] +" \t Vida: " + str(gladiador[7][0]))
                                                        print("9 - "+ gladiador[8][7] +" \t Vida: " + str(gladiador[8][0]))
                                                        respAtaque = input("R: ")
                                                        
                                                        if(respAtaque == "1" and gladiador[0][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[0], resp2)
                                        
                                                        elif(respAtaque == "2" and gladiador[1][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[1], resp2)
                                                        
                                                        elif(respAtaque == "3" and gladiador[2][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[2], resp2)

                                                        elif(respAtaque == "4" and gladiador[3][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[3], resp2)

                                                        elif(respAtaque == "5" and gladiador[4][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[4], resp2)

                                                        elif(respAtaque == "6" and gladiador[5][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[5], resp2)

                                                        elif(respAtaque == "7" and gladiador[6][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[6], resp2)

                                                        elif(respAtaque == "8" and gladiador[7][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[7], resp2)

                                                        elif(respAtaque == "9" and gladiador[8][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[8], resp2)


                                                        print("\nEscolha outro oponente para atacar:")
                                                        print("1 - "+ gladiador[0][7] +" \t Vida: " + str(gladiador[0][0]))
                                                        print("2 - "+ gladiador[1][7] +" \t Vida: " + str(gladiador[1][0]))
                                                        print("3 - "+ gladiador[2][7] +" \t Vida: " + str(gladiador[2][0]))
                                                        print("4 - "+ gladiador[3][7] +" \t Vida: " + str(gladiador[3][0]))
                                                        print("5 - "+ gladiador[4][7] +" \t Vida: " + str(gladiador[4][0]))
                                                        print("6 - "+ gladiador[5][7] +" \t Vida: " + str(gladiador[5][0]))
                                                        print("7 - "+ gladiador[6][7] +" \t Vida: " + str(gladiador[6][0]))
                                                        print("8 - "+ gladiador[7][7] +" \t Vida: " + str(gladiador[7][0]))
                                                        print("9 - "+ gladiador[8][7] +" \t Vida: " + str(gladiador[8][0]))
                                                        respAtaque = input("R: ")
                                                        
                                                        if(respAtaque == "1" and gladiador[0][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[0], resp2)
                                        
                                                        elif(respAtaque == "2" and gladiador[1][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[1], resp2)
                                                        
                                                        elif(respAtaque == "3" and gladiador[2][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[2], resp2)

                                                        elif(respAtaque == "4" and gladiador[3][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[3], resp2)

                                                        elif(respAtaque == "5" and gladiador[4][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[4], resp2)

                                                        elif(respAtaque == "6" and gladiador[5][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[5], resp2)

                                                        elif(respAtaque == "7" and gladiador[6][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[6], resp2)

                                                        elif(respAtaque == "8" and gladiador[7][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[7], resp2)

                                                        elif(respAtaque == "9" and gladiador[8][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[8], resp2)

                                                elif(personagem[59 + (1 * (int(resp2) - 1))] == 3):
                                                        print("\nEscolha outro oponente para atacar:")
                                                        print("1 - "+ gladiador[0][7] +" \t Vida: " + str(gladiador[0][0]))
                                                        print("2 - "+ gladiador[1][7] +" \t Vida: " + str(gladiador[1][0]))
                                                        print("3 - "+ gladiador[2][7] +" \t Vida: " + str(gladiador[2][0]))
                                                        print("4 - "+ gladiador[3][7] +" \t Vida: " + str(gladiador[3][0]))
                                                        print("5 - "+ gladiador[4][7] +" \t Vida: " + str(gladiador[4][0]))
                                                        print("6 - "+ gladiador[5][7] +" \t Vida: " + str(gladiador[5][0]))
                                                        print("7 - "+ gladiador[6][7] +" \t Vida: " + str(gladiador[6][0]))
                                                        print("8 - "+ gladiador[7][7] +" \t Vida: " + str(gladiador[7][0]))
                                                        print("9 - "+ gladiador[8][7] +" \t Vida: " + str(gladiador[8][0]))
                                                        respAtaque = input("R: ")
                                                        
                                                        if(respAtaque == "1" and gladiador[0][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[0], resp2)
                                        
                                                        elif(respAtaque == "2" and gladiador[1][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[1], resp2)
                                                        
                                                        elif(respAtaque == "3" and gladiador[2][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[2], resp2)

                                                        elif(respAtaque == "4" and gladiador[3][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[3], resp2)

                                                        elif(respAtaque == "5" and gladiador[4][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[4], resp2)

                                                        elif(respAtaque == "6" and gladiador[5][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[5], resp2)

                                                        elif(respAtaque == "7" and gladiador[6][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[6], resp2)

                                                        elif(respAtaque == "8" and gladiador[7][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[7], resp2)

                                                        elif(respAtaque == "9" and gladiador[8][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[8], resp2)

                                                        print("\nEscolha outro oponente para atacar:")
                                                        print("1 - "+ gladiador[0][7] +" \t Vida: " + str(gladiador[0][0]))
                                                        print("2 - "+ gladiador[1][7] +" \t Vida: " + str(gladiador[1][0]))
                                                        print("3 - "+ gladiador[2][7] +" \t Vida: " + str(gladiador[2][0]))
                                                        print("4 - "+ gladiador[3][7] +" \t Vida: " + str(gladiador[3][0]))
                                                        print("5 - "+ gladiador[4][7] +" \t Vida: " + str(gladiador[4][0]))
                                                        print("6 - "+ gladiador[5][7] +" \t Vida: " + str(gladiador[5][0]))
                                                        print("7 - "+ gladiador[6][7] +" \t Vida: " + str(gladiador[6][0]))
                                                        print("8 - "+ gladiador[7][7] +" \t Vida: " + str(gladiador[7][0]))
                                                        print("9 - "+ gladiador[8][7] +" \t Vida: " + str(gladiador[8][0]))
                                                        respAtaque = input("R: ")
                                                        
                                                        if(respAtaque == "1" and gladiador[0][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[0], resp2)
                                        
                                                        elif(respAtaque == "2" and gladiador[1][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[1], resp2)
                                                        
                                                        elif(respAtaque == "3" and gladiador[2][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[2], resp2)

                                                        elif(respAtaque == "4" and gladiador[3][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[3], resp2)

                                                        elif(respAtaque == "5" and gladiador[4][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[4], resp2)

                                                        elif(respAtaque == "6" and gladiador[5][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[5], resp2)

                                                        elif(respAtaque == "7" and gladiador[6][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[6], resp2)

                                                        elif(respAtaque == "8" and gladiador[7][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[7], resp2)

                                                        elif(respAtaque == "9" and gladiador[8][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[8], resp2)
                                                                
                                                        print("\nEscolha outro oponente para atacar:")
                                                        print("1 - "+ gladiador[0][7] +" \t Vida: " + str(gladiador[0][0]))
                                                        print("2 - "+ gladiador[1][7] +" \t Vida: " + str(gladiador[1][0]))
                                                        print("3 - "+ gladiador[2][7] +" \t Vida: " + str(gladiador[2][0]))
                                                        print("4 - "+ gladiador[3][7] +" \t Vida: " + str(gladiador[3][0]))
                                                        print("5 - "+ gladiador[4][7] +" \t Vida: " + str(gladiador[4][0]))
                                                        print("6 - "+ gladiador[5][7] +" \t Vida: " + str(gladiador[5][0]))
                                                        print("7 - "+ gladiador[6][7] +" \t Vida: " + str(gladiador[6][0]))
                                                        print("8 - "+ gladiador[7][7] +" \t Vida: " + str(gladiador[7][0]))
                                                        print("9 - "+ gladiador[8][7] +" \t Vida: " + str(gladiador[8][0]))
                                                        respAtaque = input("R: ")
                                                        
                                                        if(respAtaque == "1" and gladiador[0][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[0], resp2)
                                        
                                                        elif(respAtaque == "2" and gladiador[1][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[1], resp2)
                                                        
                                                        elif(respAtaque == "3" and gladiador[2][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[2], resp2)

                                                        elif(respAtaque == "4" and gladiador[3][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[3], resp2)

                                                        elif(respAtaque == "5" and gladiador[4][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[4], resp2)

                                                        elif(respAtaque == "6" and gladiador[5][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[5], resp2)

                                                        elif(respAtaque == "7" and gladiador[6][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[6], resp2)

                                                        elif(respAtaque == "8" and gladiador[7][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[7], resp2)

                                                        elif(respAtaque == "9" and gladiador[8][0] > 0):
                                                                resp2 = usar_habilidade(personagem, gladiador[8], resp2)

                                                                
                                                if(resp2 != 0):
                                                        personagem[3] = personagem[3] - personagem[22 + (4 * (resp2 - 1))]
                                                        

                                                resp2 = str(resp2)
                                                        
                                                        
                                        
			elif(resp == "4"):
                                if(gladiador[0][9] == 0):
                                        print("\nVocê Fugiu")
                                        sleep(2)
                                        return 2
                                elif(gladiador[0][9] == 1):
                                        print("\nVocê não pode fugir de lutas contra Chefes.")
                                        sleep(3)
                                        resp = "0"
                                elif(gladiador[0][9] == 2):
                                        print("\nVocê não pode fugir desta luta.")
                                        sleep(3)
                                        resp = "0"
				
		''' Vez dos Inimigos '''
		contador = 0
		while(contador != 9):
                        sorteio = randint(0, 9)

                        if(gladiador[contador][0] > 0 and gladiador[contador][11] != 2):
                                if(sorteio == 9):
                                        retorno = ataque_monstro(personagem, gladiador[contador], habilidades, cont)
                                        if(retorno == 0):
                                                print("\nVocê é fraco de mais para a arena!")
                                                exit(0)
                                        contador = contador + 1

                                else:
                                        if(gladiador[sorteio][0] > 0): 
                                                monstro_vs_monstro(gladiador[contador], gladiador[sorteio])
                                                contador = contador + 1
                        else:
                                contador = contador + 1
				

		if(personagem[2] >= 0 and personagem[55] != 0 and personagem[55] != 2):
                        danoStatus = aplica_dano_status(personagem[2], personagem[55])
                        personagem[2] = personagem[2] - danoStatus
                        print("\nVocê sofreu " + str(danoStatus) + " de dano por estar " + nome_status(personagem[55]))
                        sleep(2)		



###############################################################################################################	

def batalha_Vs3(personagem, monstro1, monstro2, monstro3, habilidades, bolsa):
	print("\n****************************************************************")
	print("\n" + monstro1[7] + " , " + monstro2[7] + " e " + monstro3[7] + " apareceram.")
	sleep(4)

	if(personagem[40] == 4):
                personagem[0] = 1
                personagem[2] = 1
                personagem[4] = 0
                personagem[8] = 0
                
	cd = [0,0,0,0,0]
	retornos = [0,0,0]
	cont1 = [0]
	cont2 = [0]
	cont3 = [0]
	while(personagem[2] > 0 and monstro1[0] > 0 or personagem[2] > 0 and monstro2[0] > 0 or personagem[2] > 0 and monstro3[0] > 0):
		if(monstro1[0] <= 0):
			monstro1[0] = 0
		if(monstro2[0] <= 0):
			monstro2[0] = 0
		if(monstro3[0] <= 0):
			monstro3[0] = 0
		
		resp = "0"
		while (resp != "1" and resp != "2" and resp != "3" and resp != "4"):
			print("****************************************************************")
			print("Inimigo1: \nNome:"+ monstro1[7] +" \t Vida Inimigo: " + str(monstro1[0]))
			print("Inimigo2: \nNome:"+ monstro2[7] +" \t Vida Inimigo: " + str(monstro2[0]))
			print("Inimigo2: \nNome:"+ monstro3[7] +" \t Vida Inimigo: " + str(monstro3[0]))
			
			print ("\nVocê: \nSua Vida: "+ str(personagem[2]) +" \tPoções de Vida: "+ str(bolsa[3]) +" \nSua Mana: "+ str(personagem[3]) +" \tPoções de Mana: "+ str(bolsa[7]))
			print ("\n1 - Atacar \t\t 2 - Poções \n3 - Habilidade \t\t 4 - Fugir")
			resp = input("\nR: ")
		

			if(resp == "1"):
                                respAtaque = "0"
                                while (respAtaque != "1" and respAtaque != "2" and respAtaque != "3"):
                                        print("\nEscolha um oponente para atacar:")
                                        print("1 -"+ monstro1[7] +" \t Vida: " + str(monstro1[0]))
                                        print("2 -"+ monstro2[7] +" \t Vida: " + str(monstro2[0]))
                                        print("3 -"+ monstro3[7] +" \t Vida: " + str(monstro3[0]))
                                        
                                        respAtaque = input("R: ")
                                        if(respAtaque == "1" and monstro1[0] > 0):
                                                personagem_ataca(personagem, monstro1, cd)
                                                
                                        elif(respAtaque == "2" and monstro2[0] > 0):
                                                personagem_ataca(personagem, monstro2, cd)
                                        
                                        elif(respAtaque == "3" and monstro3[0] > 0):
                                                personagem_ataca(personagem, monstro3, cd)
                                        
                                        else:
                                                print("\nEste oponente esta morto, escolha outro.\n")
                                                respAtaque = "0"
                        
			elif(resp == "2"):
                                print("****************************************************************")
                                resp2 = "0"
                                while(resp2 != "1" and resp2 != "2" and resp2 != "3" and resp2 != "4" and resp2 != "5"):	
                                        print("Pots: \t\t\t\t Restaura: \n1 - Poção de Vida \t\t " + str(bolsa[1]) + " de Vida\n2 - Poção de Mana \t\t " + str(bolsa[5]) + " de Mana \n3 - Poção Hibrida \t\t " + str(bolsa[16]) +" \ " + str(bolsa[17]) + " de V\M \n4 - Antidoto \t\t\t Tira Veneno \n5 - Voltar")
                                        resp2 = input("R: ")

                                        if(resp2 == "5"):
                                                resp = "0"
                                        else:                        
                                                resp2 = usar_pocao(personagem, resp2, bolsa)

                
			elif(resp == "3"):
                                if(personagem[40] != 4):
                                        print("****************************************************************")
                                        print("Habilidades:")
                                        print("Nome das Habilidades: \t\tCusto de Mana: ")
                                        print("1 - " + str(nome_habilidade(personagem[20])) + " " * (28 - len(nome_habilidade(personagem[20]))) + str(personagem[22]))
                                        print("2 - " + str(nome_habilidade(personagem[24])) + " " * (28 - len(nome_habilidade(personagem[24]))) + str(personagem[26]))
                                        print("3 - " + str(nome_habilidade(personagem[28])) + " " * (28 - len(nome_habilidade(personagem[28]))) + str(personagem[30]))
                                        print("4 - " + str(nome_habilidade(personagem[32])) + " " * (28 - len(nome_habilidade(personagem[32]))) + str(personagem[34]))
                                        print("5 - " + str(nome_habilidade(personagem[36])) + " " * (28 - len(nome_habilidade(personagem[36]))) + str(personagem[38]))
                                        print("0 - Voltar")
                                else:
                                        print("****************************************************************")
                                        print("Habilidades:")
                                        print("Nome das Habilidades: \t\tCusto de Mana: ")
                                        print("1 - " + str(nome_habilidade(personagem[20])) + " " * (28 - len(nome_habilidade(personagem[20]))) + str(personagem[22]) + "\tTurnos: " + str(cd[0]))
                                        print("2 - " + str(nome_habilidade(personagem[24])) + " " * (28 - len(nome_habilidade(personagem[24]))) + str(personagem[26]) + "\tTurnos: " + str(cd[1]))
                                        print("3 - " + str(nome_habilidade(personagem[28])) + " " * (28 - len(nome_habilidade(personagem[28]))) + str(personagem[30]) + "\tTurnos: " + str(cd[2]))
                                        print("4 - " + str(nome_habilidade(personagem[32])) + " " * (28 - len(nome_habilidade(personagem[32]))) + str(personagem[34]) + "\tTurnos: " + str(cd[3]))
                                        print("5 - " + str(nome_habilidade(personagem[36])) + " " * (28 - len(nome_habilidade(personagem[36]))) + str(personagem[38]) + "\tTurnos: " + str(cd[4]))
                                        print("0 - Voltar")
                                
                                resp2 = "6"
                                while(resp2 != "1" and resp2 != "2" and resp2 != "3" and resp2 != "4" and resp2 != "5" and resp2 != "0"):	
                                        resp2 = input("R: ")
                                        if(resp2 == "0"):
                                                resp = "0"
                                        else:
                                                resp2 = int(resp2)

                                        if(resp2 == 1 or resp2 == 2 or resp2 == 3 or resp2 == 4 or resp2 == 5):
                                                respAtaque = "0"
                                                while (respAtaque != "1" and respAtaque != "2" and respAtaque != "3" and resp2 != "0"):
                                                        if(personagem[59 + (1 * (resp2 - 1))] == 1):
                                                                print("\nEscolha um oponente para atacar:")
                                                                print("1 - "+ monstro1[7] +" \t Vida: " + str(monstro1[0]))
                                                                print("2 - "+ monstro2[7] +" \t Vida: " + str(monstro2[0]))
                                                                print("3 - "+ monstro3[7] +" \t Vida: " + str(monstro3[0]))

                                                                respAtaque = input("R: ")
                                                                if(personagem[40] == 4):
                                                                        if(personagem[3] >= 10):
                                                                                if(cd[resp2 - 1] == 0):
                                                                                        if(respAtaque == "1" and monstro1[0] > 0):
                                                                                                usar_habilidade_druida(personagem, resp2, habilidades, cd)
                                                                                                personagem_ataca(personagem, monstro1, cd)
                                                                        
                                                                                        elif(respAtaque == "2" and monstro2[0] > 0):
                                                                                                usar_habilidade_druida(personagem, resp2, habilidades, cd)
                                                                                                personagem_ataca(personagem, monstro2, cd)
                                                                                        
                                                                                        elif(respAtaque == "3" and monstro3[0] > 0):
                                                                                                usar_habilidade_druida(personagem, resp2, habilidades, cd)
                                                                                                personagem_ataca(personagem, monstro3, cd)
                                                                                        else:
                                                                                                print("\nEste oponente esta morto, escolha outro.\n")
                                                                                                respAtaque = "0"
                                                                                else:
                                                                                        if(respAtaque == "0"):
                                                                                           resp = "0"

                                                                                        else:
                                                                                                print("\nEsta habilidade esta em tempo de recarga.")
                                                                                                resp2 = "6"
                                                                                                sleep(2)
                                                                        else:
                                                                                print("\nMana insuficiente.")
                                                                                sleep(2)
                                                                                resp = "0"

                                   
                                                                else:                                                                
                                                                        if(respAtaque == "1" and monstro1[0] > 0):
                                                                                resp2 = usar_habilidade(personagem, monstro1, resp2)
                                                        
                                                                        elif(respAtaque == "2" and monstro2[0] > 0):
                                                                                resp2 = usar_habilidade(personagem, monstro2, resp2)
                                                                        
                                                                        elif(respAtaque == "3" and monstro3[0] > 0):
                                                                                resp2 = usar_habilidade(personagem, monstro3, resp2)

                                                                        else:
                                                                                print("\nEste oponente esta morto, escolha outro.\n")
                                                                                respAtaque = "0"

                                                        elif(personagem[59 + (1 * (resp2 - 1))] == 2):
                                                                print("\nEscolha um oponente para atacar:")
                                                                print("1 - "+ monstro1[7] +" \t Vida: " + str(monstro1[0]))
                                                                print("2 - "+ monstro2[7] +" \t Vida: " + str(monstro2[0]))
                                                                print("3 - "+ monstro3[7] +" \t Vida: " + str(monstro3[0]))
                                                                
                                                                respAtaque = input("R: ")
                                                                if(respAtaque == "1" and monstro1[0] > 0):
                                                                        resp2 =  usar_habilidade(personagem, monstro1, resp2)
                                                
                                                                elif(respAtaque == "2" and monstro2[0] > 0):
                                                                        resp2 =  usar_habilidade(personagem, monstro2, resp2)
                                                                
                                                                elif(respAtaque == "3" and monstro3[0] > 0):
                                                                        resp2 =  usar_habilidade(personagem, monstro3, resp2)

                                                                print("\nEscolha outro oponente para atacar:")
                                                                print("1 - "+ monstro1[7] +" \t Vida: " + str(monstro1[0]))
                                                                print("2 - "+ monstro2[7] +" \t Vida: " + str(monstro2[0]))
                                                                print("3 - "+ monstro3[7] +" \t Vida: " + str(monstro3[0]))

                                                                respAtaque = input("R: ")
                                                                if(respAtaque == "1" and monstro1[0] > 0):
                                                                        resp2 =  usar_habilidade(personagem, monstro1, resp2)
                                                
                                                                elif(respAtaque == "2" and monstro2[0] > 0):
                                                                        resp2 =  usar_habilidade(personagem, monstro2, resp2)
                                                                
                                                                elif(respAtaque == "3" and monstro3[0] > 0):
                                                                        resp2 =  usar_habilidade(personagem, monstro3, resp2)

                                                        elif(personagem[59 + (1 * (resp2 - 1))] == 3):
                                                                usar_habilidade(personagem, monstro1, resp2)
                                                                usar_habilidade(personagem, monstro2, resp2)
                                                                resp2 = usar_habilidade(personagem, monstro3, resp2)
                                                                respAtaque = "1"

                                                        if(resp2 != 0 and personagem[40] != 4):
                                                                personagem[3] = personagem[3] - personagem[22 + (4 * (resp2 - 1))]
                                                        else:
                                                                resp = "0"
                                                                

                                                        resp2 = str(resp2)
                                                                
                                        else:
                                                respAtaque = "0"
                                        
			elif(resp == "4"):
                                if(monstro1[9] == 0 and monstro2[9] == 0 and monstro3[9] == 0):
                                        print("\nVocê Fugiu")
                                        sleep(2)
                                        return 2
                                elif(monstro1[9] == 1 or monstro2[9] == 1 or monstro3[9] == 1):
                                        print("\nVocê não pode fugir de lutas contra Chefes.")
                                        sleep(3)
                                        resp = "0"
                                elif(monstro1[9] == 2 or monstro2[9] == 2 or monstro3[9] == 2):
                                        print("\nVocê não pode fugir desta luta.")
                                        sleep(3)
                                        resp = "0"
				
		''' Vez dos Inimigos '''
		
		if(retornos[0] != 1):
			retorno1 = ataque_monstro(personagem, monstro1, habilidades, cont1)
			if(retorno1 == 0):
				return 0
			elif(retorno1 == 1):
				retornos[0] = 1
		
		if(retornos[1] != 1):
			retorno2 = ataque_monstro(personagem, monstro2, habilidades, cont2)
			if(retorno2 == 0):
				return 0
			elif(retorno2 == 1):
				retornos[1] = 1
		
		if(retornos[2] != 1):
			retorno3 = ataque_monstro(personagem, monstro3, habilidades, cont3)
			if(retorno3 == 0):
				return 0
			elif(retorno3 == 1):
				retornos[2] = 1
				

		if(personagem[2] >= 0 and personagem[55] != 0 and personagem[55] != 2):
                        danoStatus = aplica_dano_status(personagem[2], personagem[55])
                        personagem[2] = personagem[2] - danoStatus
                        print("\nVocê sofreu " + str(danoStatus) + " de dano por estar " + nome_status(personagem[55]))
                        sleep(2)

                        if(personagem[2] <= 0):
                                return 0



                        

###############################################################################################################
                        
def batalhaPvP(jogadores):
        print("\n****************************************************************")
        print("\n          " + jogadores[0][1][0] + " vs " + jogadores[1][1][0])
        print("\n****************************************************************")
        sleep(5)

        jogador1 = []
        jogador2 = []

        if(jogadores[0][0][7] > jogadores[1][0][7]):
                jogador1.append(jogadores[0])
                jogador2.append(jogadores[1])

        elif(jogadores[0][0][7] < jogadores[1][0][7]):
                jogador2.append(jogadores[0])
                jogador1.append(jogadores[1])


        cd = [0,0,0,0,0]

        cont1 = [0]
        cont2 = [0]
        cont3 = [0]

        while(jogadores[0][0][2] > 0 and jogadores[1][0][2] > 0):
                vezPersonagem = 0
                while(vezPersonagem == 0):
                        acao = "@"
                        while(acao.isalnum() == False):
                                print("\n****************************************************************")
                                print("---------------------------------------")
                                print("|Jogador 1: " + jogador1[0][1][0] + "|")
                                print("|Vida: " + str(jogador1[0][0][2]) + "   Mana: " + str(jogador1[0][0][3]) + "|")                                            
                                
                                print("---------------------------------------")
                                print("|Jogador 2: " + jogador2[0][1][0] + "|")
                                print("|Vida: " + str(jogador2[0][0][2]) + "   Mana: " + str(jogador2[0][0][3]) + "|")
                                print("---------------------------------------")
                                
                                
                                print("\n1 - Atacar \t 2 - Poções \n3 - Habilidades")
                                acao = input("\nEscolha Jogador 1: ")

                                if(acao == "1"):                                        
                                        dano = (jogador1[0][0][4] + jogador1[0][0][10])
                                        dano = aplica_critico(dano, jogador1[0][0][6], 1)
                                        
                                        dano = (dano) - (jogador2[0][0][8] + jogador2[0][0][12])
                                        
                                        if(dano < 0):
                                                dano = 0
                                        else:
                                                dano = aplica_esquiva(dano, jogador2[0][0][7], jogador1[0][0][6],1)

                                        jogador2[0][0][2] = jogador2[0][0][2] - dano
                                        print("\n" + jogador1[0][1][0] + " causou " + str(dano) + " de dano em " + jogador2[0][1][0])
                                        sleep(4)

                                        vezPersonagem = 1


                                elif(acao == "2"):
                                        print("****************************************************************")
                                        escolhaPocao = "@"
                                        while(escolhaPocao.isalnum() == False):	                                
                                                print("Pots: \t\t\t\t Restaura: \t\t Quantidade: \n1 - Poção de Vida \t\t " + str(bolsa[1]) + " de Vida \t\t " + str(bolsa[3]) + "\\" + str(bolsa[2]) + "\n2 - Poção de Mana \t\t " + str(bolsa[5]) + " de Mana  \t\t " + str(bolsa[7]) + "\\" + str(bolsa[6]) + "\n3 - Poção Hibrida \t\t " + str(bolsa[16]) +" \ " + str(bolsa[17]) + " de V\M  \t " + str(bolsa[19]) + "\\" + str(bolsa[18]) + "\n4 - Antidoto \t\t\t Tira Veneno  \t\t " + str(bolsa[14]) + "\\" + str(bolsa[13]) + "\n0 - Voltar")
                                                escolhaPocao = input("R: ")

                                                if(escolhaPocao == "0"):
                                                        acao = "@"
                                                else:                        
                                                        escolhaPocao = usar_pocao(personagem, escolhaPocao, bolsa)

                                                        if(escolhaPocao != "@"):
                                                                vezPersonagem = 1


                                elif(acao == "3"):
                                        escolhaHabilidade = "@"
                                        while(escolhaHabilidade.isalnum() == False):
                                                if(jogador2[0][0][40] != 4):
                                                        print("****************************************************************")                                        
                                                        print("Nome das Habilidades: \t\tCusto de Mana: \t\tNv Habilidades:")
                                                        print("1 - " + str(nome_habilidade(jogador1[0][0][20])) + " " * (28 - len(nome_habilidade(jogador1[0][0][20]))) + str(jogador1[0][0][22]) + "\t\t\tNv " + str(jogador1[0][0][76]))
                                                        print("2 - " + str(nome_habilidade(jogador1[0][0][24])) + " " * (28 - len(nome_habilidade(jogador1[0][0][24]))) + str(jogador1[0][0][26]) + "\t\t\tNv " + str(jogador1[0][0][77]))
                                                        print("3 - " + str(nome_habilidade(jogador1[0][0][28])) + " " * (28 - len(nome_habilidade(jogador1[0][0][28]))) + str(jogador1[0][0][30]) + "\t\t\tNv " + str(jogador1[0][0][78]))
                                                        print("4 - " + str(nome_habilidade(jogador1[0][0][32])) + " " * (28 - len(nome_habilidade(jogador1[0][0][32]))) + str(jogador1[0][0][34]) + "\t\t\tNv " + str(jogador1[0][0][79]))
                                                        print("5 - " + str(nome_habilidade(jogador1[0][0][36])) + " " * (28 - len(nome_habilidade(jogador1[0][0][36]))) + str(jogador1[0][0][38]) + "\t\t\tNv " + str(jogador1[0][0][80]))
                                                        print("0 - Voltar")                                
                                                        
                                                        escolhaHabilidade = input("\nR: ")

                                                        if(escolhaHabilidade != "1" and escolhaHabilidade != "2" and escolhaHabilidade != "3" and escolhaHabilidade != "4" and escolhaHabilidade != "5" and escolhaHabilidade != "0"):
                                                                print("\nEscolha uma das habilidades")
                                                                sleep(2)
                                                                escolhaHabilidade = "@"

                                                        elif(escolhaHabilidade == "0"):
                                                                acao = "@"

                                                        elif(jogador2[0][0][3] < jogador2[0][0][22 + (4 * (int(escolhaHabilidade) - 1))] and jogador2[0][0][3] != 0):
                                                                print("\nMana insuficiente.")
                                                                sleep(2)
                                                                escolhaHabilidade = "@"

                                                        elif(jogador1[0][0][76 + (1 * (int(escolhaHabilidade) - 1))] == 0):
                                                                print("\nEsta habilidade ainda não foi aprendida.")
                                                                sleep(2)
                                                                escolhaHabilidade = "@"

                                                        else:
                                                                elemento = 23 + (4 * (int(escolhaHabilidade)  - 1))
                                                                
                                                                if(jogador1[0][0][40] == 1):
                                                                        dano = jogador1[0][0][5] + jogador1[0][0][11] + jogador1[0][0][21 + (4 * (int(escolhaHabilidade) - 1))]

                                                                        dano = aplica_elemento(dano, jogador1[0][0][elemento], jogador2[0][0][58])

                                                                        dano = dano - (jogador2[0][0][9] + jogador2[0][0][11])

                                                                        if(dano < 0):
                                                                                dano = 0

                                                                        jogador2[0][0][2] = jogador2[0][0][2] - dano

                                                                        print("\n" + jogador1[0][1][0] + " causou " + str(dano) + " de dano em " + jogador2[0][1][0])
                                                                        sleep(4)

                                                                        vezPersonagem = 1


                                                                if(jogador1[0][0][40] == 2):
                                                                        dano = jogador1[0][0][4] + jogador1[0][0][10] + jogador1[0][0][52] + jogador1[0][0][21 + (4 * (int(escolhaHabilidade) - 1))]

                                                                        dano = aplica_elemento(dano, jogador1[0][0][elemento], jogador2[0][0][58])

                                                                        dano = aplica_critico(dano, jogador1[0][0][6], 1)

                                                                        dano = dano - (jogador2[0][0][8] + jogador2[0][0][10])

                                                                        if(dano < 0):
                                                                                dano = 0

                                                                        jogador2[0][0][2] = jogador2[0][0][2] - dano

                                                                        print("\n" + jogador1[0][1][0] + " causou " + str(dano) + " de dano em " + jogador2[0][1][0])
                                                                        sleep(4)

                                                                        if(jogador1[0][0][59 + (int(escolhaHabilidade) - 1)] == 2):
                                                                                jogador2[0][0][2] = jogador2[0][0][2] - dano

                                                                                print("\n" + jogador1[0][1][0] + " causou " + str(dano) + " de dano em " + jogador2[0][1][0])
                                                                                sleep(4)
                                                                                        

                                                                        vezPersonagem = 1
                                                                        

                                                                if(jogador1[0][0][40] == 3):
                                                                        dano = jogador1[0][0][4] + jogador1[0][0][10] + jogador1[0][0][6] + jogador1[0][0][52] + jogador1[0][0][21 + (4 * (int(escolhaHabilidade) - 1))]

                                                                        dano = aplica_elemento(dano, jogador1[0][0][elemento], jogador2[0][0][58])

                                                                        dano = aplica_critico(dano, jogador1[0][0][6], 1)

                                                                        dano = dano - (jogador2[0][0][8] + jogador2[0][0][10])

                                                                        if(dano < 0):
                                                                                dano = 0
                                                                        

                                                                        jogador2[0][0][2] = jogador2[0][0][2] - dano

                                                                        print("\n" + jogador1[0][1][0] + " causou " + str(dano) + " de dano em " + jogador2[0][1][0])
                                                                        sleep(4)

                                                                        if(jogador1[0][0][59 + (int(escolhaHabilidade) - 1)] == 2):
                                                                                jogador2[0][0][2] = jogador2[0][0][2] - dano

                                                                                print("\n" + jogador1[0][1][0] + " causou " + str(dano) + " de dano em " + jogador2[0][1][0])
                                                                                sleep(4)
                                                                                        

                                                                        vezPersonagem = 1

                                                
                                

                
                vezPersonagem2 = 0
                while(vezPersonagem2 == 0 and jogador2[0][0][2] > 0):
                        acao = "@"
                        while(acao.isalnum() == False):
                                print("\n****************************************************************")
                                print("---------------------------------------")
                                print("|Jogador 1: " + jogador1[0][1][0] + "|")
                                print("|Vida: " + str(jogador1[0][0][2]) + "   Mana: " + str(jogador1[0][0][3]) + "|")                                            
                                
                                print("---------------------------------------")
                                print("|Jogador 2: " + jogador2[0][1][0] + "|")
                                print("|Vida: " + str(jogador2[0][0][2]) + "   Mana: " + str(jogador2[0][0][3]) + "|")
                                print("---------------------------------------")
                                
                                
                                print("\n1 - Atacar \t 2 - Poções \n3 - Habilidades")
                                acao = input("\nEscolha Jogador 2: ")

                                if(acao == "1"):
                                        dano = (jogador2[0][0][4] + jogador2[0][0][10])
                                        dano = aplica_critico(dano, jogador2[0][0][6], 1)
                                        
                                        dano = (dano) - (jogador1[0][0][8] + jogador1[0][0][12])
                                        
                                        if(dano < 0):
                                                dano = 0
                                        else:
                                                dano = aplica_esquiva(dano, jogador1[0][0][7], jogador2[0][0][6],1)

                                        jogador1[0][0][2] = jogador1[0][0][2] - dano
                                        print("\n" + jogador2[0][1][0] + " causou " + str(dano) + " de dano em " + jogador1[0][1][0])
                                        sleep(4)

                                        vezPersonagem2 = 1


                                elif(acao == "2"):
                                        print("****************************************************************")
                                        escolhaPocao = "@"
                                        while(escolhaPocao.isalnum() == False):	                                
                                                print("Pots: \t\t\t\t Restaura: \t\t Quantidade: \n1 - Poção de Vida \t\t " + str(jogador[0][4][1]) + " de Vida \t\t " + str(bolsa[3]) + "\\" + str(bolsa[2]) + "\n2 - Poção de Mana \t\t " + str(bolsa[5]) + " de Mana  \t\t " + str(bolsa[7]) + "\\" + str(bolsa[6]) + "\n3 - Poção Hibrida \t\t " + str(bolsa[16]) +" \ " + str(bolsa[17]) + " de V\M  \t " + str(bolsa[19]) + "\\" + str(bolsa[18]) + "\n4 - Antidoto \t\t\t Tira Veneno  \t\t " + str(bolsa[14]) + "\\" + str(bolsa[13]) + "\n0 - Voltar")
                                                escolhaPocao = input("R: ")

                                                if(escolhaPocao == "0"):
                                                        acao = "@"
                                                else:                        
                                                        escolhaPocao = usar_pocao(personagem, escolhaPocao, bolsa)

                                                        if(escolhaPocao != "@"):
                                                                vezPersonagem = 1


                                elif(acao == "3"):
                                        escolhaHabilidade = "@"
                                        while(escolhaHabilidade.isalnum() == False):
                                                if(jogador2[0][0][40] != 4):
                                                        print("****************************************************************")                                        
                                                        print("Nome das Habilidades: \t\tCusto de Mana: \t\tNv Habilidades:")
                                                        print("1 - " + str(nome_habilidade(jogador2[0][0][20])) + " " * (28 - len(nome_habilidade(jogador2[0][0][20]))) + str(jogador1[0][0][22]) + "\t\t\tNv " + str(jogador2[0][0][76]))
                                                        print("2 - " + str(nome_habilidade(jogador2[0][0][24])) + " " * (28 - len(nome_habilidade(jogador2[0][0][24]))) + str(jogador1[0][0][26]) + "\t\t\tNv " + str(jogador2[0][0][77]))
                                                        print("3 - " + str(nome_habilidade(jogador2[0][0][28])) + " " * (28 - len(nome_habilidade(jogador2[0][0][28]))) + str(jogador1[0][0][30]) + "\t\t\tNv " + str(jogador2[0][0][78]))
                                                        print("4 - " + str(nome_habilidade(jogador2[0][0][32])) + " " * (28 - len(nome_habilidade(jogador2[0][0][32]))) + str(jogador1[0][0][34]) + "\t\t\tNv " + str(jogador2[0][0][79]))
                                                        print("5 - " + str(nome_habilidade(jogador2[0][0][36])) + " " * (28 - len(nome_habilidade(jogador2[0][0][36]))) + str(jogador1[0][0][38]) + "\t\t\tNv " + str(jogador2[0][0][80]))
                                                        print("0 - Voltar")                                
                                                        
                                                        escolhaHabilidade = input("\nR: ")

                                                        if(escolhaHabilidade != "1" and escolhaHabilidade != "2" and escolhaHabilidade != "3" and escolhaHabilidade != "4" and escolhaHabilidade != "5" and escolhaHabilidade != "0"):
                                                                print("\nEscolha uma das habilidades")
                                                                sleep(2)
                                                                escolhaHabilidade = "@"

                                                        elif(escolhaHabilidade == "0"):
                                                                acao = "@"

                                                        elif(jogador2[0][0][3] < jogador2[0][0][22 + (4 * (int(escolhaHabilidade) - 1))] and jogador2[0][0][3] != 0):
                                                                print("\nMana insuficiente.")
                                                                sleep(2)
                                                                escolhaHabilidade = "@"

                                                        elif(jogador2[0][0][76 + (1 * (int(escolhaHabilidade) - 1))] == 0):
                                                                print("\nEsta habilidade ainda não foi aprendida.")
                                                                sleep(2)
                                                                escolhaHabilidade = "@"

                                                        else:
                                                                elemento = 23 + (4 * (int(escolhaHabilidade)  - 1))
                                                                
                                                                if(jogador2[0][0][40] == 1):
                                                                        dano = jogador2[0][0][5] + jogador2[0][0][11] + jogador2[0][0][21 + (4 * (int(escolhaHabilidade) - 1))]

                                                                        dano = aplica_elemento(dano, jogador2[0][0][elemento], jogador1[0][0][58])

                                                                        dano = dano - (jogador1[0][0][9] + jogador1[0][0][11])

                                                                        if(dano < 0):
                                                                                dano = 0

                                                                        jogador1[0][0][2] = jogador1[0][0][2] - dano

                                                                        print("\n" + jogador2[0][1][0] + " causou " + str(dano) + " de dano em " + jogador1[0][1][0])
                                                                        sleep(4)

                                                                        vezPersonagem2 = 1


                                                                if(jogador2[0][0][40] == 2):
                                                                        dano = jogador2[0][0][4] + jogador2[0][0][10] + jogador2[0][0][52] + jogador2[0][0][21 + (4 * (int(escolhaHabilidade) - 1))]

                                                                        dano = aplica_elemento(dano, jogador2[0][0][elemento], jogador1[0][0][58])

                                                                        dano = dano - (jogador1[0][0][8] + jogador1[0][0][10])

                                                                        if(dano < 0):
                                                                                dano = 0

                                                                        jogador1[0][0][2] = jogador1[0][0][2] - dano

                                                                        print("\n" + jogador2[0][1][0] + " causou " + str(dano) + " de dano em " + jogador1[0][1][0])
                                                                        sleep(4)

                                                                        if(jogador2[0][0][59 + (int(escolhaHabilidade) - 1)] == 2):
                                                                                jogador1[0][0][2] = jogador1[0][0][2] - dano

                                                                                print("\n" + jogador2[0][1][0] + " causou " + str(dano) + " de dano em " + jogador1[0][1][0])
                                                                                sleep(4)
                                                                                        

                                                                        vezPersonagem2 = 1
                                                                        

                                                                if(jogador2[0][0][40] == 3):
                                                                        dano = jogador2[0][0][4] + jogador2[0][0][10] + jogador2[0][0][6] + jogador2[0][0][52] + jogador2[0][0][21 + (4 * (int(escolhaHabilidade) - 1))]

                                                                        dano = aplica_elemento(dano, jogador2[0][0][elemento], jogador1[0][0][58])

                                                                        dano = dano - (jogador1[0][0][8] + jogador1[0][0][10])

                                                                        if(dano < 0):
                                                                                dano = 0

                                                                        jogador1[0][0][2] = jogador1[0][0][2] - dano

                                                                        print("\n" + jogador2[0][1][0] + " causou " + str(dano) + " de dano em " + jogador1[0][1][0])
                                                                        sleep(4)

                                                                        if(jogador2[0][0][59 + (int(escolhaHabilidade) - 1)] == 2):
                                                                                jogador1[0][0][2] = jogador1[0][0][2] - dano

                                                                                print("\n" + jogador2[0][1][0] + " causou " + str(dano) + " de dano em " + jogador1[0][1][0])
                                                                                sleep(4)
                                                                                        

                                                                        vezPersonagem2 = 1


###############################################################################################################
                        
def batalhaChefe(personagem, chefe, mob1, mob2, habilidades, bolsa, nome):
        print("\n****************************************************************")
        print("\n          Luta contra: " + chefe[7])
        print("\n****************************************************************")
        sleep(4)
        print(chefe[7] + " trouxe " + mob1[7] + " e " + mob2[7] + " para a luta.")
        sleep(3)

        cd = [0,0,0,0,0]

        tempo_status = 0

        cont1 = [0]
        cont2 = [0]
        cont3 = [0]

        monstros = []
        monstros.append(chefe)
        monstros.append(mob1)
        monstros.append(mob2)

        while(monstros[0][0] > 0 or monstros[1][0] > 0 or monstros[2][0] > 0):
                vezPersonagem = 0

                if(personagem[55] == 2):
                        if(tempo_status == 2):
                                personagem[55] = 0
                                print("\n****************************************************************")
                                print("Você se livrou do congelamento!")
                                sleep(3)
                        else:
                                print("\n****************************************************************")
                                print("\nVocê está congelado!")
                                sleep(4)
                                
                                tempo_status = tempo_status + 1

                                vezPersonagem = 1

                                
                
                while(vezPersonagem == 0):
                        acao = "@"
                        while(acao.isalnum() == False):
                                print("\n****************************************************************")
                                print("---------------------------------------")
                                print("|Chefe: " + chefe[7] + "|")
                                print("|Vida: " + str(monstros[0][0]) + "|")            
                                print("---------------------------------------")            
                                print("|Mob1: " + mob1[7] + ((13 - len(mob1[7])) * " ") + "| Mob2: " + mob2[7] + "|")
                                print("|Vida: " + str(monstros[1][0]) + ((15 - len(mob1[7])) * " ") + "| Vida: " + str(monstros[2][0]) +"|")
                                print("---------------------------------------\n")
                                
                                print("---------------------------------------")
                                print("" + nome[0] + ": \t\t Status: " + nome_status(personagem[55]))
                                print("Vida: " + str(personagem[2]) + "   Mana: " + str(personagem[3]))
                                print("\n1 - Atacar \t 2 - Poções \n3 - Habilidades  4 - Fugir")
                                acao = input("\nR: ")

                                if(acao == "1"):
                                        escolhaAlvo = "@"
                                        while(escolhaAlvo.isalnum() == False):
                                                print("\nEscolha um alvo:")
                                                print("1 - " + monstros[0][7])
                                                print("2 - " + monstros[1][7])
                                                print("3 - " + monstros[2][7])
                                                print("0 - Voltar")

                                                escolhaAlvo = input("\nR: ")

                                                if(escolhaAlvo == "0"):
                                                        acao = "@"

                                                else:
                                                        try:
                                                                if(monstros[int(escolhaAlvo) - 1][0] <= 0):
                                                                        print("\nEste monstro esta morto, escolha outro.")
                                                                        sleep(2)
                                                                        escolhaAlvo = "@"

                                                                else:
                                                                        personagem_ataca(personagem, monstros[int(escolhaAlvo) - 1], cd)

                                                                        if(monstros[int(escolhaAlvo) - 1][0] < 0):
                                                                                print("\n" + monstros[int(escolhaAlvo) - 1][7] + " morreu.")
                                                                                sleep(2)
                                                                                monstros[int(escolhaAlvo) - 1][0] = 0
                                                                                aumentar_level(personagem, monstros[int(escolhaAlvo) - 1], habilidades)

                                                                        vezPersonagem = 1

                                                        except IndexError:
                                                                print("\nEscolha uma opção válida.")
                                                                sleep(2)
                                                                escolhaAlvo = "@"


                                elif(acao == "2"):
                                        print("****************************************************************")
                                        escolhaPocao = "@"
                                        while(escolhaPocao.isalnum() == False):	                                
                                                print("Pots: \t\t\t\t Restaura: \t\t Quantidade: \n1 - Poção de Vida \t\t " + str(bolsa[1]) + " de Vida \t\t " + str(bolsa[3]) + "\\" + str(bolsa[2]) + "\n2 - Poção de Mana \t\t " + str(bolsa[5]) + " de Mana  \t\t " + str(bolsa[7]) + "\\" + str(bolsa[6]) + "\n3 - Poção Hibrida \t\t " + str(bolsa[16]) +" \ " + str(bolsa[17]) + " de V\M  \t " + str(bolsa[19]) + "\\" + str(bolsa[18]) + "\n4 - Antidoto \t\t\t Tira Veneno  \t\t " + str(bolsa[14]) + "\\" + str(bolsa[13]) + "\n0 - Voltar")
                                                escolhaPocao = input("R: ")

                                                if(escolhaPocao == "0"):
                                                        acao = "@"
                                                else:                        
                                                        escolhaPocao = usar_pocao(personagem, escolhaPocao, bolsa)

                                                        if(escolhaPocao != "@"):
                                                                vezPersonagem = 1


                                elif(acao == "3"):
                                        escolhaHabilidade = "@"
                                        while(escolhaHabilidade.isalnum() == False):
                                                if(personagem[40] != 4):
                                                        print("****************************************************************")                                        
                                                        print("Nome das Habilidades: \t\tCusto de Mana: \t\tNv Habilidades:")
                                                        print("1 - " + str(nome_habilidade(personagem[20])) + " " * (28 - len(nome_habilidade(personagem[20]))) + str(personagem[22]) + "\t\t\tNv " + str(habilidades[6]))
                                                        print("2 - " + str(nome_habilidade(personagem[24])) + " " * (28 - len(nome_habilidade(personagem[24]))) + str(personagem[26]) + "\t\t\tNv " + str(habilidades[14]))
                                                        print("3 - " + str(nome_habilidade(personagem[28])) + " " * (28 - len(nome_habilidade(personagem[28]))) + str(personagem[30]) + "\t\t\tNv " + str(habilidades[22]))
                                                        print("4 - " + str(nome_habilidade(personagem[32])) + " " * (28 - len(nome_habilidade(personagem[32]))) + str(personagem[34]) + "\t\t\tNv " + str(habilidades[30]))
                                                        print("5 - " + str(nome_habilidade(personagem[36])) + " " * (28 - len(nome_habilidade(personagem[36]))) + str(personagem[38]) + "\t\t\tNv " + str(habilidades[38]))
                                                        print("0 - Voltar")                                
                                                        
                                                        escolhaHabilidade = input("\nR: ")

                                                        if(escolhaHabilidade != "1" and escolhaHabilidade != "2" and escolhaHabilidade != "3" and escolhaHabilidade != "4" and escolhaHabilidade != "5" and escolhaHabilidade != "0"):
                                                                print("\nEscolha uma das habilidades")
                                                                sleep(2)
                                                                escolhaHabilidade = "@"

                                                        elif(escolhaHabilidade == "0"):
                                                                acao = "@"

                                                        elif(personagem[3] < personagem[22 + (4 * (int(escolhaHabilidade) - 1))] and personagem[3] != 0):
                                                                print("\nMana insuficiente.")
                                                                sleep(2)
                                                                escolhaHabilidade = "@"

                                                        elif(habilidades[6 + (8 * (int(escolhaHabilidade) - 1))] == 0):
                                                                print("\nEsta habilidade ainda não foi aprendida.")
                                                                sleep(2)
                                                                escolhaHabilidade = "@"

                                                        else:
                                                                escolhaAlvo = "@"
                                                                while(escolhaAlvo.isalnum() == False):
                                                                        if(personagem[59 + (int(escolhaHabilidade) - 1)] <= 2):
                                                                                print("****************************************************************")
                                                                                print("\nEscolha um alvo:")
                                                                                print("1 - " + monstros[0][7])
                                                                                print("2 - " + monstros[1][7])
                                                                                print("3 - " + monstros[2][7])
                                                                                print("0 - Voltar")
                                                                                
                                                                                escolhaAlvo = input("\nR: ")

                                                                                if(escolhaAlvo != "1" and escolhaAlvo != "2" and escolhaAlvo != "3" and escolhaAlvo != "0"):
                                                                                        print("\nEscolha um alvo válido.")
                                                                                        sleep(2)
                                                                                        escolhaAlvo = "@"
                                                                                        
                                                                                elif(escolhaAlvo == "0"):
                                                                                        acao = "@"

                                                                                elif(monstros[int(escolhaAlvo) - 1][0] == 0):
                                                                                        print("\nEste alvo esta morto, escolha outro.")
                                                                                        escolhaAlvo = "@"
                                                                                        sleep(2)

                                                                                else:
                                                                                        usar_habilidade(personagem, monstros[int(escolhaAlvo) - 1], int(escolhaHabilidade))

                                                                                        personagem[3] = personagem[3] - personagem[22 + (4 * (int(escolhaHabilidade) - 1))]
                                                                                        
                                                                                        if(monstros[int(escolhaAlvo) - 1][0] < 0):
                                                                                                print("\n" + monstros[int(escolhaAlvo) - 1][7] + " morreu.")
                                                                                                sleep(2)
                                                                                                monstros[int(escolhaAlvo) - 1][0] = 0
                                                                                                aumentar_level(personagem, monstros[int(escolhaAlvo) - 1], habilidades)

                                                                                                vezPersonagem = 1

                                                                                        if(personagem[59 + (int(escolhaHabilidade) - 1)] == 2):
                                                                                                if(monstros[0][0] > 0 or monstros[1][0] > 0 or monstros[2][0] > 0):
                                                                                                        escolhaAlvo = "@"
                                                                                                        while(escolhaAlvo.isalnum() == False):
                                                                                                                print("****************************************************************")
                                                                                                                print("\nEscolha o segundo alvo:")
                                                                                                                print("1 - " + monstros[0][7])
                                                                                                                print("2 - " + monstros[1][7])
                                                                                                                print("3 - " + monstros[2][7])

                                                                                                                escolhaAlvo = input("\nR: ")

                                                                                                                if(escolhaAlvo != "1" and escolhaAlvo != "2" and escolhaAlvo != "3"):
                                                                                                                        print("\nEscolha um alvo válido.")
                                                                                                                        sleep(2)
                                                                                                                        escolhaAlvo = "@"

                                                                                                                elif(monstros[int(escolhaAlvo) - 1][0] == 0):
                                                                                                                        print("\nEste alvo esta morto, escolha outro.")
                                                                                                                        escolhaAlvo = "@"
                                                                                                                        sleep(2)

                                                                                                                else:
                                                                                                                        usar_habilidade(personagem, monstros[int(escolhaAlvo) - 1], int(escolhaHabilidade))
                                                                                                                        vezPersonagem = 1
                                                                                                                        
                                                                                                                        if(monstros[int(escolhaAlvo) - 1][0] < 0):
                                                                                                                                print("\n" + monstros[int(escolhaAlvo) - 1][7] + " morreu.")
                                                                                                                                sleep(2)
                                                                                                                                monstros[int(escolhaAlvo) - 1][0] = 0
                                                                                                                                aumentar_level(personagem, monstros[int(escolhaAlvo) - 1], habilidades)


                                                                        elif(personagem[59 + (int(escolhaHabilidade) - 1)] == 3):
                                                                                if(monstros[0][0] > 0):
                                                                                        usar_habilidade(personagem, monstros[0], int(escolhaHabilidade))
                                                                                        if(monstros[0][0] < 0):
                                                                                                print("\n" + monstros[0][7] + " morreu.")
                                                                                                sleep(2)
                                                                                                monstros[0][0] = 0
                                                                                                aumentar_level(personagem, monstros[0], habilidades)

                                                                                if(monstros[1][0] > 0):
                                                                                        usar_habilidade(personagem, monstros[1], int(escolhaHabilidade))
                                                                                        if(monstros[1][0] < 0):
                                                                                                print("\n" + monstros[1][7] + " morreu.")
                                                                                                sleep(2)
                                                                                                monstros[1][0] = 0
                                                                                                aumentar_level(personagem, monstros[1], habilidades)

                                                                                if(monstros[2][0] > 0):
                                                                                        usar_habilidade(personagem, monstros[2], int(escolhaHabilidade))
                                                                                        if(monstros[2][0] < 0):
                                                                                                print("\n" + monstros[2][7] + " morreu.")
                                                                                                sleep(2)
                                                                                                monstros[2][0] = 0
                                                                                                aumentar_level(personagem, monstros[2], habilidades)
                                                                                                

                                                                                personagem[3] = personagem[3] - personagem[22 + (4 * (int(escolhaHabilidade) - 1))]
                                                                                escolhaAlvo = "0"                                          
                                                                                vezPersonagem = 1

                                                else:
                                                        ataque = 0
                                                        while(ataque == 0):
                                                                try:
                                                                        print("****************************************************************")
                                                                        print("Habilidades:")
                                                                        print("Nome das Habilidades: \t\tCusto de Mana: ")
                                                                        print("1 - " + str(nome_habilidade(personagem[20])) + " " * (28 - len(nome_habilidade(personagem[20]))) + str(personagem[22]) + "\tTurnos: " + str(cd[0]))
                                                                        print("2 - " + str(nome_habilidade(personagem[24])) + " " * (28 - len(nome_habilidade(personagem[24]))) + str(personagem[26]) + "\tTurnos: " + str(cd[1]))
                                                                        print("3 - " + str(nome_habilidade(personagem[28])) + " " * (28 - len(nome_habilidade(personagem[28]))) + str(personagem[30]) + "\tTurnos: " + str(cd[2]))
                                                                        print("4 - " + str(nome_habilidade(personagem[32])) + " " * (28 - len(nome_habilidade(personagem[32]))) + str(personagem[34]) + "\tTurnos: " + str(cd[3]))
                                                                        print("5 - " + str(nome_habilidade(personagem[36])) + " " * (28 - len(nome_habilidade(personagem[36]))) + str(personagem[38]) + "\tTurnos: " + str(cd[4]))
                                                                        print("0 - Voltar")

                                                                        escolhaHabilidade = input("\nR: ")

                                                                        if(escolhaHabilidade == "0"):
                                                                                acao = "@"

                                                                        elif(personagem[3] < personagem[22 + (4 * (int(escolhaHabilidade) - 1))] and personagem[3] != 0):
                                                                                print("\nMana insuficiente.")
                                                                                sleep(2)
                                                                                escolhaHabilidade = "@"

                                                                        else:
                                                                                usar_habilidade_druida(personagem, int(escolhaHabilidade), habilidades, cd)
                                                                                print("****************************************************************")
                                                                                print("\nEscolha um alvo:")
                                                                                print("1 - " + monstros[0][7])
                                                                                print("2 - " + monstros[1][7])
                                                                                print("3 - " + monstros[2][7])
                                                                                print("0 - Voltar")

                                                                                alvoHabilidade = input("\nR: ")
                                                                                
                                                                                personagem_ataca(personagem, monstros[int(alvoHabilidade)], cd)

                                                                                ataque = 1

                                                                                personagem[3] = personagem[3] - personagem[22 + (4 * (int(escolhaHabilidade) - 1))]

                                                                                if(monstros[int(escolhaAlvo) - 1][0] < 0):
                                                                                        print("\n" + monstros[int(escolhaAlvo) - 1][7] + " morreu.")
                                                                                        sleep(2)
                                                                                        monstros[int(escolhaAlvo) - 1][0] = 0
                                                                                        aumentar_level(personagem, monstros[int(escolhaAlvo) - 1], habilidades)

                                                                                        vezPersonagem = 1


                                                                except IndexError:
                                                                        print("Escolha inválida")
                                                                        sleep(2)


                                elif(acao == "4"):
                                        if(monstros[0][9] == 0 and monstros[1][9] == 0 and monstros[2][9] == 0):
                                                print("\nVocê Fugiu")
                                                sleep(2)
                                                return 2
                                        elif(monstros[0][9] == 1 or monstros[1][9] == 1 or monstros[2][9] == 1):
                                                print("\nVocê não pode fugir de lutas contra Chefes.")
                                                sleep(3)
                                                acao = "0"
                                        elif(monstros[0][9] == 2 or monstros[1][9] == 2 or monstros[2][9] == 2):
                                                print("\nVocê não pode fugir desta luta.")
                                                sleep(3)
                                                acao = "0"


                                

                
                vezInimigo = 0
                while(vezInimigo == 0):

                        if(monstros[0][0] > 0):
                                porcento = porcentoVida(monstros[0][16], monstros[0][0])

                                if(porcento >= 1 and porcento <= 10 and monstros[0][19][2] > 0):                                        
                                        habilidade_chefe(monstros[0], personagem, 3)
                                        monstros[0][19][2] = monstros[0][19][2] - 1

                                elif(porcento >= 45 and porcento <= 55 and monstros[0][18][2] > 0):
                                        habilidade_chefe(monstros[0], personagem, 2)
                                        monstros[0][18][2] = monstros[0][18][2] - 1

                                elif(porcento >= 65 and porcento <= 75 and monstros[0][17][2] > 0):
                                        habilidade_chefe(monstros[0], personagem, 1)
                                        monstros[0][17][2] = monstros[0][17][2] - 1

                                else:
                                        ataque = ataque_monstroV2(personagem, monstros[0], habilidades, cont1)
                                
                                
                                if(personagem[2] <= 0):
                                        return 0

                        if(monstros[1][0] > 0):
                                ataque = ataque_monstroV2(personagem, monstros[1], habilidades, cont2)
                                if(personagem[2] <= 0):
                                        return 0

                        if(monstros[2][0] > 0):
                                ataque = ataque_monstroV2(personagem, monstros[2], habilidades, cont3)
                                if(personagem[2] <= 0):
                                        return 0


                                     
                        vezInimigo = 1

