# encoding: UTF-8

def nome_arma(indice):
	if(indice == "0"):
		return "Espaço Vazio"
		
	if(indice == "1"):
		return "Arma de aprendiz"
		
	if(indice == "2"):
		return "Cajado Arcano"
	
	if(indice == "3"):
		return "Espada Longa"
		
	if(indice == "4"):
		return "Adaga envenenada"

	if(indice == "5"):
                return "Colar Espiritual"

	if(indice == "6"):
                return "Adaga Gumy"
        
	if(indice == "7"):
                return "Espada Curva"

	if(indice == "8"):
                return "Cajado da Destruição"
        
	
	
def equipar_arma(arma, personagem):
	personagem[10] = arma[0]
	personagem[11] = arma[1]
	personagem[51] = arma[3]
	personagem[52] = arma[4]
	personagem[53] = arma[5]
	personagem[57] = arma[6]
	personagem[64] = arma[2]
	personagem[66] = arma[8]
	
	print("Arma " + nome_arma(str(arma[2])) + " equipada\n")


def loja_de_armas(estoque_armas):
	cajado_arcano(estoque_armas)
	cajado_da_destruicao(estoque_armas)
	
	espada_longa(estoque_armas)
	espada_curva(estoque_armas)
	
	adaga_envenenada(estoque_armas)
	adaga_gumy(estoque_armas)
	
	colar_espiritual(estoque_armas)
	
	
	


def arma_de_aprendiz(arma):
	arma.append(5) #0 Dano Fisico
	arma.append(5) #1 Dano Magico
	arma.append(1) #2 Nome da arma
	arma.append(0) #3 Agilidade Arma
	arma.append(0) #4 Destreza Arma
	arma.append(0) #5 Mana Arma
	arma.append(0) #6 Elemento
	arma.append(50)#7 Preço
	arma.append(0) #8 ChanceStatus
	arma.append(0) #9 Classe de Uso
	
	

def cajado_arcano(arma):
	arma.append(10) # Dano Fisico
	arma.append(15) # Dano Magico
	arma.append(2) # Nome da arma
	arma.append(0) # Agilidade Arma
	arma.append(0) # Destreza Arma
	arma.append(5) # Mana Arma
	arma.append(0) # Elemento
	arma.append(50) # Preço
	arma.append(0) # ChanceStatus
	arma.append(1) # Classe de Uso
	
	

def espada_longa(arma):
	arma.append(15) # Dano Fisico
	arma.append(10) # Dano Magico
	arma.append(3) # Nome da arma
	arma.append(2) # Agilidade Arma
	arma.append(2) # Destreza Arma
	arma.append(0) # Mana Arma
	arma.append(0) # Elemento
	arma.append(50) # Preço
	arma.append(0) # ChanceStatus
	arma.append(2) # Classe de Uso
	


def adaga_envenenada(arma):
	arma.append(10) # Dano Fisico
	arma.append(10) # Dano Magico
	arma.append(4) # Nome da arma
	arma.append(10) # Agilidade Arma
	arma.append(10) # Destreza Arma
	arma.append(0) # Mana Arma
	arma.append(9) # Elemento
	arma.append(50) # Preço
	arma.append(10) # ChanceStatus
	arma.append(3) # Classe de Uso

	
	 
def colar_espiritual(arma):
	arma.append(10) # Dano Fisico
	arma.append(0) # Dano Magico
	arma.append(5) # Nome da arma
	arma.append(0) # Agilidade Arma
	arma.append(0) # Destreza Arma
	arma.append(0) # Mana Arma
	arma.append(0) # Elemento
	arma.append(50) # Preço
	arma.append(0) # ChanceStatus
	arma.append(4) # Classe de Uso




def adaga_gumy(arma):
	arma.append(20) # Dano Fisico
	arma.append(0) # Dano Magico
	arma.append(6) # Nome da arma
	arma.append(20) # Agilidade Arma
	arma.append(20) # Destreza Arma
	arma.append(0) # Mana Arma
	arma.append(0) # Elemento
	arma.append(500) # Preço
	arma.append(0) # ChanceStatus
	arma.append(3) # Classe de Uso


def espada_curva(arma):
	arma.append(30) # Dano Fisico
	arma.append(0) # Dano Magico
	arma.append(7) # Nome da arma
	arma.append(5) # Agilidade Arma
	arma.append(5) # Destreza Arma
	arma.append(0) # Mana Arma
	arma.append(0) # Elemento
	arma.append(500) # Preço
	arma.append(0) # ChanceStatus
	arma.append(2) # Classe de Uso


def cajado_da_destruicao(arma):
	arma.append(20) # Dano Fisico
	arma.append(30) # Dano Magico
	arma.append(8) # Nome da arma
	arma.append(0) # Agilidade Arma
	arma.append(0) # Destreza Arma
	arma.append(20) # Mana Arma
	arma.append(0) # Elemento
	arma.append(500) # Preço
	arma.append(0) # ChanceStatus
	arma.append(1) # Classe de Uso

