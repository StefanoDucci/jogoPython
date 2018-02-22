# encoding: UTF-8

def loja_de_armaduras(estoque):
	armadura_leve(estoque)
	armadura_pesada(estoque)
	

def nome_armadura(indice):
	if(indice == 0):
		return "Vazio"
		
	elif(indice == 1):
		return "Armadura de Aprendiz"
	
	elif(indice == 2):
		return "Armadura Pesada"
		
	elif(indice == 3):
		return "Armadura leve"
	
	
def equipar_armadura(armadura, personagem):
	print("\nItem " + nome_armadura(armadura[2]) + " encontrado\n")
	
	personagem[12] = armadura[0]
	personagem[13] = armadura[1]
	personagem[58] = armadura[3]
	personagem[65] = armadura[2]
	
	print("" + nome_armadura(armadura[2]) + " equipada.\n")

			
def armadura_aprendiz(armadura):
	armadura.append(5) # 0 Defesa Fisica
	armadura.append(5) # 1 Defesa Magica
	armadura.append(1) # 2 Nome da armadura
	armadura.append(0) # 3 Elemento
	armadura.append(50)# 4 Preço
	

def armadura_pesada(armadura):
	armadura.append(15) # Defesa Fisica
	armadura.append(15) # Defesa Magica
	armadura.append(2) # Nome da armadura
	armadura.append(0) # Elemento
	armadura.append(50)# Preço
	

def armadura_leve(armadura):
	armadura.append(10) # Defesa Fisica
	armadura.append(10) # Defesa Magica
	armadura.append(3) # Nome da armadura
	armadura.append(0) # Elemento
	armadura.append(30)# Preço
	

	
	
