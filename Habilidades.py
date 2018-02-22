# encoding: UTF-8
from time import sleep
'''
Elementos:
0 - Neutro
1 - Fogo
2 - Agua
3 - Terra
4 - Vento
5 - Trovao
6 - Trevas
7 - Luz
8 - Gelo
9 - Floresta
'''

def nome_elemento(indice):
	if(indice == 0):
		return "Neutro"
	
	if(indice == 1):
		return "Fogo"
	
	if(indice == 2):
		return "Água"
	
	if(indice == 3):
		return "Terra"
	
	if(indice == 4):
		return "Vento"
	
	if(indice == 5):
		return "Trovão"
	
	if(indice == 6):
		return "Trevas"
	
	if(indice == 7):
		return "Luz"
	
	if(indice == 8):
		return "Gelo"
	
	if(indice == 9):
		return "Floresta"
	
###############################################################################################


def nome_habilidade(indice):
	if(indice == 0):
		return "Habilidade Vazia"
	
	if(indice == 1):
		return "Bola de Fogo"
	
	if(indice == 2):
		return "Golpe Flamejante"
	
	if(indice == 3):
		return "Congelar"
	
	if(indice == 4):
		return "Golpe certeiro"
	
	if(indice == 5):
		return "Terremoto"
	
	if(indice == 6):
		return "Fissura"
	
	if(indice == 7):
		return "Arremeçar facas"
	
	if(indice == 8):
		return "Envenenar"
	
	if(indice == 9):
		return "Corte das Sombras"
	
	if(indice == 10):
		return "Relâmpago"
	
	if(indice == 11):
		return "Tornado"
	
	if(indice == 12):
		return "Impacto Explosivo"
	
	if(indice == 13):
		return "Estocada"

	if(indice == 14):
                return "Golpe Duplo"

	if(indice == 15):
		return "Armadilha"
	
	if(indice == 16):
		return "Lobo"

	if(indice == 17):
		return "Urso"

	if(indice == 18):
		return "Aguia"

	if(indice == 19):
		return "Tigre"

	if(indice == 20):
		return "Tartaruga"

	if(indice == 21):
		return "Brasas"
	
	if(indice == 22):
		return "Distorção Arcana"	
	
	
	
	
###############################################################################################


def evoluir_habilidades(personagem, habilidades, condicao):
	if(condicao == 1):	
		print("\nEscolha uma habilidade para evoluir: ")
	else:
		print("\nEscolha uma habilidade para por em seus atalhos:")
	cont = 0
	cont2 = 6
	cont3 = 2
	cont4 = 7
	for i in range(int(len(habilidades) / 8)):
		print(str(i + 1) + " - " + nome_habilidade(habilidades[cont]) + ' ' * ((18 - len(nome_habilidade(habilidades[cont])))) + "Nv " + str(habilidades[cont2]) + "\t Custo - " + str(habilidades[cont3]) + "\t Número de Alvos - " + str(habilidades[cont4]))
		cont = cont + 8
		cont2 = cont2 + 8
		cont3 = cont3 + 8
		cont4 = cont4 + 8
                
	decisao = "0"
	while(decisao != "1" and decisao != "2" and decisao != "3" and decisao != "4" and decisao != "5" and decisao != "6"):
		decisao = input("\nR: ")
		
		if(condicao == 1):
			if((habilidades[6 + (8 * (int(decisao) - 1))] + 1) > 10):
                                print("\nEsta habilidade já esta em seu nível máximo, escolha outra.")
                                sleep(3)
			else:
                                habilidades[6 + (8 * (int(decisao) - 1))] = habilidades[6 + (8 * (int(decisao) - 1))] + 1
		if(condicao == 2):
                        if(habilidades[6 + (8 * (int(decisao) - 1))] == 0):
                                print("\nEsta habilidade ainda não foi evoluida, escolha outra.")
                                decisao = "0"
	if(personagem[40] != 4):
                habilidadeUp = []
                decisao = int(decisao)
                
                for i in range(8):
                        habilidadeUp.append(habilidades[i + (8 * (decisao - 1))])


                decisao = "0"
                while(decisao != "1" and decisao != "2" and decisao != "3" and decisao != "4" and decisao != "5"):
                        print("\nEm qual posição você gostaria de deixar esta habilidade? ")
                        
                        print("Nome das Habilidades: \t\tCusto de Mana:  \t Sua Mana: %s" % str(personagem[3]))
                        print("1 - " + str(nome_habilidade(personagem[20])) + " " * (28 - len(nome_habilidade(personagem[20]))) + str(personagem[22]))
                        print("2 - " + str(nome_habilidade(personagem[24])) + " " * (28 - len(nome_habilidade(personagem[24]))) + str(personagem[26]))
                        print("3 - " + str(nome_habilidade(personagem[28])) + " " * (28 - len(nome_habilidade(personagem[28]))) + str(personagem[30]))
                        print("4 - " + str(nome_habilidade(personagem[32])) + " " * (28 - len(nome_habilidade(personagem[32]))) + str(personagem[34]))
                        print("5 - " + str(nome_habilidade(personagem[36])) + " " * (28 - len(nome_habilidade(personagem[36]))) + str(personagem[38]))
                        '''
                        cont1 = 20
                        cont2 = 22
                        for i in range(len(habilidades) / 8):
                                print(str(i + 1) + " - " + str(nome_habilidade(personagem[cont1])) + " " * (28 - len(nome_habilidade(personagem[cont1]))) + str(personagem[cont2]))
                                cont1 = cont1 + 4
                                cont2 = cont2 + 4
                        '''
                        decisao = input("\nR: ")

                decisao = int(decisao)
                
                personagem[20 + (4 * (decisao - 1))] = habilidadeUp[0]
                personagem[21 + (4 * (decisao - 1))] = habilidadeUp[1] + (int((habilidadeUp[1] / 4)) * habilidadeUp[6])
                personagem[22 + (4 * (decisao - 1))] = habilidadeUp[2]
                personagem[23 + (4 * (decisao - 1))] = habilidadeUp[3]
                personagem[41 + (2 * (decisao - 1))] = habilidadeUp[4]
                personagem[42 + (2 * (decisao - 1))] = habilidadeUp[5]
                personagem[59 + (1 * (decisao - 1))] = habilidadeUp[7]
                personagem[76 + (1 * (decisao - 1))] = habilidadeUp[6]
                
                
	
	
###############################################################################################

def cria_arvore_habilidade(habilidades, personagem):
	if(personagem[40] == 1):
		bola_de_fogo(habilidades)
		congelar(habilidades)
		terremoto(habilidades)
		relampago(habilidades)
		tornado(habilidades)
		distorcao_arcana(habilidades)
	
	if(personagem[40] == 2):
		golpe_flamejante(habilidades)
		golpe_rapido(habilidades)
		fissura(habilidades)
		impacto_explosivo(habilidades)
		estocada(habilidades)

	if(personagem[40] == 3):
		arremeca_faca(habilidades)
		envenenar(habilidades)
		corte_das_sombras(habilidades)
		corteDuplo(habilidades)
		armadilha(habilidades)
		brasa(habilidades)
		

	if(personagem[40] == 4):
		hab_lobo(habilidades)
		hab_urso(habilidades)
		hab_aguia(habilidades)
		hab_tigre(habilidades)
		hab_tartaruga(habilidades)

		
	
###############################################################################################


def nome_status(indice):
	if(indice == 1):
		return "Queimando"
	
	if(indice == 2):
		return "Congelado"
	
	if(indice == 9):
		return "Envenenado"

	if(indice == 8):
                return "Molhado"

	if(indice == 0):
                return " "

###############################################################################################


def bola_de_fogo(habilidade):
	habilidade.append(1) # Indice			0
	habilidade.append(10) # DanoMagico		1
	habilidade.append(5) # CustoMana		2
	habilidade.append(1) # ElementoFogo		3
	habilidade.append(1) # Status			4
	habilidade.append(10) # ChanceStatus	5
	habilidade.append(0) # LevelHabilidade	6
	habilidade.append(1) # NumeroInimigos	7


def golpe_flamejante(habilidade):
	habilidade.append(2) # Indice
	habilidade.append(15) # DanoMagico
	habilidade.append(5) # CustoMana
	habilidade.append(1) # ElementoFogo
	habilidade.append(1) # Status
	habilidade.append(10) # ChanceStatus
	habilidade.append(0) # LevelHabilidade
	habilidade.append(1) # NumeroInimigos	7
	


def congelar(habilidade):
	habilidade.append(3) # Indice
	habilidade.append(20) # DanoMagico
	habilidade.append(15) # CustoMana
	habilidade.append(8) # ElementoGelo
	habilidade.append(2) # Status
	habilidade.append(20) # ChanceStatus
	habilidade.append(0) # LevelHabilidade
	habilidade.append(1) # NumeroInimigos	7
	

def golpe_rapido(habilidade):
	habilidade.append(4) # Indice
	habilidade.append(30) # DanoMagico
	habilidade.append(15) # CustoMana
	habilidade.append(0) # ElementoNeutro
	habilidade.append(0) # Status
	habilidade.append(0) # ChanceStatus
	habilidade.append(0) # LevelHabilidade
	habilidade.append(1) # NumeroInimigos	7
	
		
def terremoto(habilidade):
	habilidade.append(5) # Indice
	habilidade.append(30) # DanoMagico
	habilidade.append(40) # CustoMana
	habilidade.append(3) # ElementoTerra
	habilidade.append(0) # Status
	habilidade.append(0) # ChanceStatus
	habilidade.append(0) # LevelHabilidade
	habilidade.append(3) # NumeroInimigos	7
	

def fissura(habilidade):
	habilidade.append(6) # Indice
	habilidade.append(20) # DanoMagico
	habilidade.append(30) # CustoMana
	habilidade.append(3) # ElementoTerra
	habilidade.append(0) # Status
	habilidade.append(0) # ChanceStatus
	habilidade.append(0) # LevelHabilidade
	habilidade.append(3) # NumeroInimigos	7
	


def arremeca_faca(habilidade):
	habilidade.append(7) # Indice
	habilidade.append(15) # DanoMagico
	habilidade.append(10) # CustoMana
	habilidade.append(0) # Elemento
	habilidade.append(0) # Status
	habilidade.append(0) # ChanceStatus
	habilidade.append(0) # LevelHabilidade
	habilidade.append(3) # NumeroInimigos	7
	
	
def envenenar(habilidade):
	habilidade.append(8) # Indice
	habilidade.append(25) # DanoMagico
	habilidade.append(20) # CustoMana
	habilidade.append(0) # Elemento
	habilidade.append(9) # Status
	habilidade.append(50) # ChanceStatus
	habilidade.append(0) # LevelHabilidade
	habilidade.append(1) # NumeroInimigos	7
	
	
def corte_das_sombras(habilidade):
	habilidade.append(9) # Indice
	habilidade.append(100) # DanoMagico
	habilidade.append(40) # CustoMana
	habilidade.append(6) # ElementoTrevas
	habilidade.append(0) # Status
	habilidade.append(0) # ChanceStatus
	habilidade.append(0) # LevelHabilidade
	habilidade.append(1) # NumeroInimigos	7

	
def relampago(habilidade):
	habilidade.append(10) # Indice
	habilidade.append(20) # DanoMagico
	habilidade.append(15) # CustoMana
	habilidade.append(10) # ElementoRaio
	habilidade.append(0) # Status
	habilidade.append(0) # ChanceStatus
	habilidade.append(0) # LevelHabilidade
	habilidade.append(1) # NumeroInimigos	7


def tornado(habilidade):
	habilidade.append(11) # Indice
	habilidade.append(20) # DanoMagico
	habilidade.append(30) # CustoMana
	habilidade.append(4) # ElementoRaio
	habilidade.append(0) # Status
	habilidade.append(0) # ChanceStatus
	habilidade.append(0) # LevelHabilidade
	habilidade.append(3) # NumeroInimigos	7


def impacto_explosivo(habilidade):
	habilidade.append(12) # Indice
	habilidade.append(20) # DanoMagico
	habilidade.append(20) # CustoMana
	habilidade.append(0) # ElementoRaio
	habilidade.append(0) # Status
	habilidade.append(0) # ChanceStatus
	habilidade.append(0) # LevelHabilidade
	habilidade.append(2) # NumeroInimigos	7

	
def estocada(habilidade):
	habilidade.append(13) # Indice
	habilidade.append(40) # DanoMagico
	habilidade.append(20) # CustoMana
	habilidade.append(0) # ElementoRaio
	habilidade.append(0) # Status
	habilidade.append(0) # ChanceStatus
	habilidade.append(0) # LevelHabilidade
	habilidade.append(1) # NumeroInimigos	7


def corteDuplo(habilidade):
	habilidade.append(14) # Indice
	habilidade.append(10) # DanoMagico
	habilidade.append(10) # CustoMana
	habilidade.append(0) # Elemento
	habilidade.append(0) # Status
	habilidade.append(0) # ChanceStatus
	habilidade.append(0) # LevelHabilidade
	habilidade.append(2) # NumeroInimigos	7

def armadilha(habilidade):
	habilidade.append(15) # Indice
	habilidade.append(40) # DanoMagico
	habilidade.append(30) # CustoMana
	habilidade.append(0) # ElementoRaio
	habilidade.append(2) # Status
	habilidade.append(30) # ChanceStatus
	habilidade.append(0) # LevelHabilidade
	habilidade.append(1) # NumeroInimigos	7


def hab_lobo(habilidade):
	habilidade.append(16) # Indice
	habilidade.append(0) # DanoMagico
	habilidade.append(10) # CustoMana
	habilidade.append(0) # ElementoRaio
	habilidade.append(0) # Status
	habilidade.append(0) # ChanceStatus
	habilidade.append(1) # LevelHabilidade
	habilidade.append(1) # NumeroInimigos

def hab_urso(habilidade):
	habilidade.append(17) # Indice
	habilidade.append(0) # DanoMagico
	habilidade.append(10) # CustoMana
	habilidade.append(0) # ElementoRaio
	habilidade.append(0) # Status
	habilidade.append(0) # ChanceStatus
	habilidade.append(1) # LevelHabilidade
	habilidade.append(1) # NumeroInimigos

def hab_aguia(habilidade):
	habilidade.append(18) # Indice
	habilidade.append(0) # DanoMagico
	habilidade.append(10) # CustoMana
	habilidade.append(0) # ElementoRaio
	habilidade.append(0) # Status
	habilidade.append(0) # ChanceStatus
	habilidade.append(1) # LevelHabilidade
	habilidade.append(1) # NumeroInimigos

def hab_tigre(habilidade):
	habilidade.append(19) # Indice
	habilidade.append(0) # DanoMagico
	habilidade.append(10) # CustoMana
	habilidade.append(0) # ElementoRaio
	habilidade.append(0) # Status
	habilidade.append(0) # ChanceStatus
	habilidade.append(1) # LevelHabilidade
	habilidade.append(1) # NumeroInimigos

def hab_tartaruga(habilidade):
	habilidade.append(20) # Indice
	habilidade.append(0) # DanoMagico
	habilidade.append(10) # CustoMana
	habilidade.append(0) # ElementoRaio
	habilidade.append(0) # Status
	habilidade.append(0) # ChanceStatus
	habilidade.append(1) # LevelHabilidade
	habilidade.append(1) # NumeroInimigos


def brasa(habilidade):
	habilidade.append(21) # Indice
	habilidade.append(30) # DanoMagico
	habilidade.append(30) # CustoMana
	habilidade.append(1) # Elemento
	habilidade.append(1) # Status
	habilidade.append(30) # ChanceStatus
	habilidade.append(0) # LevelHabilidade
	habilidade.append(2) # NumeroInimigos	7


def distorcao_arcana(habilidade):
	habilidade.append(22) # Indice
	habilidade.append(15) # DanoMagico
	habilidade.append(15) # CustoMana
	habilidade.append(0) # Elemento
	habilidade.append(0) # Status
	habilidade.append(0) # ChanceStatus
	habilidade.append(0) # LevelHabilidade
	habilidade.append(3) # NumeroInimigos	7





	
