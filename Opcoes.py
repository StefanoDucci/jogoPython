# encoding: UTF-8
def salvar_jogo(personagem, nome, inventario, habilidades, itens, bolsa):
	''' Salva Configuração do personagem '''
	savesP = open(nome[0] + "_save_personagem.txt","w")
	
	for i in range(len(personagem)):
		savesP.write(str(personagem[i]) + ";")
	
	savesP.close()
	
	''' Salva Informações do Jogador '''
	savesJ = open(nome[0] + "_save_jogador.txt", "w")
	for i in range(len(nome)):
		savesJ.write(str(nome[i]) + ";")
	savesJ.close()
	
	''' Salva as Habilidades do jogador '''
	savesH = open(nome[0] + "_save_habilidades.txt", "w")
	
	for j in range(len(habilidades)):
		savesH.write(str(habilidades[j]) + ";")
	
	savesH.close()
	

	''' Salva o Inventário do jogador '''
	savesI = open(nome[0] + "_save_inventario.txt", "w")
	
	for j in range(len(inventario)):
		savesI.write(str(inventario[j]) + ";")
	
	savesI.close()
	
	''' Salva os Itens do jogador '''
	savesIt = open(nome[0] + "_save_itens.txt", "w")
	
	for j in range(len(itens)):
		savesIt.write(str(itens[j]) + ";")
	
	savesIt.close()

	''' Salva Bolsa do jogador '''
	savesB = open(nome[0] + "_save_bolsa.txt", "w")
	
	for j in range(len(bolsa)):
		savesB.write(str(bolsa[j]) + ";")
	
	savesB.close()
	
	print("\n****************************************************************")
	print("\nJogo salvo com sucesso!\n")
	print("\n****************************************************************\n")


###############################################################################################################
	
def carregar_jogo(personagem, nome, inventario, habilidades, itens, ponto, bolsa):
	
	
	loadP = open(nome[0] + "_save_personagem.txt","r")
	dadosP = loadP.readline()
	loadP.close()
	
	loadI = open(nome[0] + "_save_inventario.txt","r")
	dadosI = loadI.readline()
	loadI.close()
	
	loadH = open(nome[0] + "_save_habilidades.txt","r")
	dadosH = loadH.readline()
	loadH.close()
	
	loadIt = open(nome[0] + "_save_itens.txt","r")
	dadosIt = loadIt.readline()
	loadIt.close()

	loadB = open(nome[0] + "_save_bolsa.txt","r")
	dadosB = loadB.readline()
	loadB.close()

	loadJ = open(nome[0] + "_save_jogador.txt","r")
	dadosJ = loadJ.readline()
	loadJ.close()
	
	''' Load Nomes personagem '''
	elementosJ = dadosJ.split(';')
	elementosJ.remove('')
	
	
	del nome[:]
	for i in range(len(elementosJ)):
		nome.append(elementosJ[i])
		
		


	''' Load Personagem personagem '''
	elementosP = dadosP.split(';')
	elementosP.remove('')
	
	
	del personagem[:]
	for i in range(len(elementosP)):
		personagem.append(int(elementosP[i]))

	''' Load Inventario personagem '''
	elementosI = dadosI.split(';')
	elementosI.remove('')
	
	
	ponto = len(elementosI)
	
	del inventario[:]
	for i in range(ponto):
		inventario.append(str(elementosI[i]))
	
	''' Load Habilidades personagem '''
	elementosH = dadosH.split(';')
	elementosH.remove('')	
	
	del habilidades[:]
	for i in range(len(elementosH)):
		habilidades.append(int(elementosH[i]))
	
	''' Load Habilidades personagem '''
	elementosIt = dadosIt.split(';')
	elementosIt.remove('')	
	
	del itens[:]
	for i in range(len(elementosIt)):
		itens.append(int(elementosIt[i]))

	''' Load Bolsa personagem '''
	elementosB = dadosB.split(';')
	elementosB.remove('')	
	
	del bolsa[:]
	for i in range(len(elementosB)):
		bolsa.append(int(elementosB[i]))
	
	
	
	return ponto
	
	
	
	
###############################################################################################################

