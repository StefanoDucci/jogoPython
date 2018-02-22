# encoding: UTF-8
from Armas import *
from Habilidades import nome_elemento
from time import sleep
from Armadura import nome_armadura, loja_de_armaduras
from Quest import nome_classe
from Itens import add_item_bolsa, add_armadura_bolsa

def Alojista(personagem, nome, itens, ponto, bolsa):
	loja = ["1", "2", "3"]
	estoque = []
	conf = 1
	
	if(personagem[56] <= 200):
		print("\n****************************************************************")
		print("\nLojista:")
		print("    Hum, vejo que não tem muito dinheiro...")
		print("    De uma olhada mas tente não quebrar nada...")
		sleep(2)
	
	elif(personagem[56] <= 1000):
		print("\n****************************************************************")
		print("\nLojista:")
		print("    Parece que alguém começou a fazer dinheiro!")
		print("    Quem sabe você não encontra uma nova arma aqui.")
		sleep(2)
	
	
	elif(personagem[56] > 1000):
		print("\n****************************************************************")
		print("\nLojista:")
		print("    Hora, vamos, vamos, não fique parado!")
		print("    Tenho certeza que podemos achar um destino para todas essas moedas.")
		sleep(2)
	
	
	
	decisao = "0"
	while(decisao != "1" and decisao != "2" and decisao != "3" and decisao != "4"):
		print("\n****************************************************************")
		print("Loja: \tSuas Moedas: %d \n" % personagem[56])
		print("1 - Armas")
		print("2 - Armaduras")
		print("3 - Poções")
		print("4 - Voltar")
		
		decisao = input("R: ")
		
		if(decisao == "1"):
			del estoque[:]
			loja_de_armas(estoque)
			
			decisao2 = "@"
			while(decisao2.isalnum() == False):
                                print("\n****************************************************************")
                                print("Catalogo de Armas:")
                                for i in range(int(len(estoque) / 10)):
                                        print(str(i + 1) + " - " + nome_arma(str(estoque[2 + (10 * i)])))
                                print("0 - Voltar")

                                decisao2 = input("\nQual arma você gostaria de ver? \nR: ")

                                if(decisao2 == "0"):
                                        decisao = "0"
                                else:
                                        try:                                        
                                                print("\n****************************************************************")
                                                print("Nome: " + nome_arma(str(estoque[2 + (10 * (int(decisao2) - 1))])))
                                                print("Dano Fisico: " + str(estoque[0 + (10 * (int(decisao2) - 1))]))
                                                print("Dano Mágico: " + str(estoque[1 + (10 * (int(decisao2) - 1))]))
                                                print("Elemento: " + str(estoque[6 + (10 * (int(decisao2) - 1))]))
                                                print("Chance de Status: " + str(estoque[8 + (10 * (int(decisao2) - 1))]))
                                                print("Agilidade: " + str(estoque[3 + (10 * (int(decisao2) - 1))]))
                                                print("Destreza: " + str(estoque[4 + (10 * (int(decisao2) - 1))]))
                                                print("Mana: " + str(estoque[5 + (10 * (int(decisao2) - 1))]))             
                                                print("Preço: " + str(estoque[7 + (10 * (int(decisao2) - 1))]))
                                                print("Classe: " + nome_classe(estoque[9 + (10 * (int(decisao2) - 1))]))
                                                

                                                print("\n****************************************************************")
                                                print("Lojista: \nVocê gostaria de comprar?")                                        

                                                comprar = "@"
                                                while(comprar.isalnum() == False):
                                                        comprar = input("1 - Sim \n2 - Não \nR: ")

                                                        if(comprar == "1"):
                                                                if(estoque[9 + (10 * (int(decisao2) - 1))] == personagem[40]):
                                                                        if(personagem[56] > estoque[7 + (10 * (int(decisao2) - 1))]):
                                                                                personagem[56] = personagem[56] - estoque[7 + (10 * (int(decisao2) - 1))]

                                                                                item = []
                                                                                item.append(estoque[0 + (10 * (int(decisao2) - 1))])
                                                                                item.append(estoque[1 + (10 * (int(decisao2) - 1))])
                                                                                item.append(estoque[2 + (10 * (int(decisao2) - 1))])                                                                                
                                                                                item.append(estoque[3 + (10 * (int(decisao2) - 1))])
                                                                                item.append(estoque[4 + (10 * (int(decisao2) - 1))])
                                                                                item.append(estoque[5 + (10 * (int(decisao2) - 1))])
                                                                                item.append(estoque[6 + (10 * (int(decisao2) - 1))])
                                                                                item.append(estoque[7 + (10 * (int(decisao2) - 1))])
                                                                                item.append(estoque[8 + (10 * (int(decisao2) - 1))])                                                                        

                                                                                add_item_bolsa(itens, item)

                                                                                print("\nItem adicionado a bolsa.")
                                                                                sleep(3)
                                                                                decisao = "0"
                                                                                
                                                                        else:
                                                                                print("\nLojista: \n      Parece que você não tem tanto dinheiro quanto pensa...")
                                                                                sleep(3)
                                                                                decisao2 = "@"                                                                

                                                                else:
                                                                        print("\nLojista: \n      Esta arma não pertence a sua classe.")
                                                                        sleep(4)
                                                                        decisao2 = "@"

                                                        elif(comprar == "2"):
                                                                decisao2 = "@"
                                                        else:
                                                                print("\nEscolha um opição válida.")
                                                                sleep(4)
                                                                comprar = "@"

                                        except IndexError:
                                                print("\nEsta arma não está na lista.")
                                                sleep(2)
                                                decisao2 = "@"
                                        

		elif(decisao == "2"):
			del estoque[:]
			loja_de_armaduras(estoque)

			decisao2 = "@"
			while(decisao2.isalnum() == False):
                                print("\n****************************************************************")
                                print("Catalogo de Armas:")
                                for i in range(int(len(estoque) / 5)):
                                        print(str(i + 1) + " - " + nome_armadura(estoque[2 + (5 * i)]))
                                print("0 - Voltar")

                                decisao2 = input("\nQual armadura você gostaria de ver? \nR: ")

                                if(decisao2 == "0"):
                                        decisao = "0"

                                else:
                                        try:                                        
                                                print("\n****************************************************************")
                                                print("Nome: " + nome_arma(str(estoque[2 + (5 * (int(decisao2) - 1))])))
                                                print("Defesa Fisico: " + str(estoque[0 + (5 * (int(decisao2) - 1))]))
                                                print("Defesa Mágico: " + str(estoque[1 + (5 * (int(decisao2) - 1))]))
                                                print("Elemento: " + str(estoque[3 + (5 * (int(decisao2) - 1))]))
                                                print("Preço: " + str(estoque[4 + (5 * (int(decisao2) - 1))]))

                                                

                                                print("\n****************************************************************")
                                                print("Lojista: \nVocê gostaria de comprar?")                                        

                                                comprar = "@"
                                                while(comprar.isalnum() == False):
                                                        comprar = input("1 - Sim \n2 - Não \nR: ")

                                                        if(comprar == "1"):
                                                                
                                                                if(personagem[56] > estoque[4 + (5 * (int(decisao2) - 1))]):
                                                                        personagem[56] = personagem[56] - estoque[4 + (5 * (int(decisao2) - 1))]

                                                                        item = []
                                                                        item.append(estoque[0 + (5 * (int(decisao2) - 1))])
                                                                        item.append(estoque[1 + (5 * (int(decisao2) - 1))])
                                                                        item.append(estoque[2 + (5 * (int(decisao2) - 1))])                                                                                
                                                                        item.append(estoque[3 + (5 * (int(decisao2) - 1))])                                                                                                                                                                        

                                                                        add_armadura_bolsa(itens, item)

                                                                        print("\nItem adicionado a bolsa.")
                                                                        sleep(3)
                                                                        decisao = "0"
                                                                                
                                                                else:
                                                                        print("\nLojista: \n      Parece que você não tem tanto dinheiro quanto pensa...")
                                                                        sleep(3)
                                                                        decisao2 = "@"                                                                

                                                               

                                                        elif(comprar == "2"):
                                                                decisao2 = "@"
                                                        else:
                                                                print("\nEscolha um opição válida.")
                                                                sleep(4)
                                                                comprar = "@"

                                        except IndexError:
                                                print("\nEsta armadura não está na lista.")
                                                sleep(2)
                                                decisao2 = "@"
                                        
                                
                                                      
		elif(decisao == "3"):
			decisao2 = "0"
			while(decisao2 != "1" and decisao2 != "2" and decisao2 != "3" and decisao2 != "4" and decisao2 != "5"):
				print("\n****************************************************************")
				print("Suas poções de vida: %d" % bolsa[3])
				print("Suas poções de mana: %d" % bolsa[7])
				print("Suas poções hibridas: %d" % bolsa[19])
				print("Seus antidotos: %d" % bolsa[14])
				print("\nQual poção você deseja comprar: \tSuas Moedas: %d" % personagem[56])
				print("1 - Poção de Vida \t Custo: 30 moedas")
				print("2 - Poção e Mana \t Custo: 20 moedas")
				print("3 - Poção Hibrida \t Custo: 50 moedas")
				print("4 - Antidoto \t\t Custo: 20 moedas")
				print("5 - Voltar")
				decisao2 = input("\nR: ")

				if(decisao2 == "1"):
					quantidade = int(input("\nQuantidade: "))

					if(personagem[56] < quantidade * 30):
						print("Moedas insuficientes.")
						conf = 0
						decisao2 = "0"
					else:
						conf = 1
                                                
					if(quantidade > bolsa[2] - bolsa[3] and conf == 1):
						print("\nVocê só pode carregar %d poções de vida atualmente" % bolsa[2])
						sleep(2)
						decisao2 = "0"
					elif(quantidade <= bolsa[2] - bolsa[3] and conf == 1):
						bolsa[3] = bolsa[3] + quantidade
						personagem[56] = personagem[56] - (quantidade * 30)
						decisao2 = "0"

				elif(decisao2 == "2"):
					quantidade = int(input("\nQuantidade:"))

					if(personagem[56] < quantidade * 20):
						print("Moedas insuficientes.")
						conf = 0
						decisao2 = "0"
					else:
						conf = 1
                                                
					if(quantidade > bolsa[6] - bolsa[7] and conf == 1):
						print("\nVocê só pode carregar %d poções de mana atualmente" % bolsa[6])
						sleep(2)
						decisao2 = "3"
					elif(quantidade <= bolsa[6] - bolsa[7] and conf == 1):
						bolsa[7] = bolsa[7] + quantidade
						personagem[56] = personagem[56] - (quantidade * 20)
						print("Suas Moedas: %d" % personagem[56])
						decisao2 = "0"

				elif(decisao2 == "3"):
					quantidade = int(input("\nQuantidade:"))

					if(personagem[56] < quantidade * 50):
						print("Moedas insuficientes.")
						conf = 0
						decisao2 = "0"
					else:
						conf = 1
                                                
					if(quantidade > bolsa[18] - bolsa[19] and conf == 1):
						print("\nVocê só pode carregar %d poções hibridas atualmente" % bolsa[18])
						sleep(2)
						decisao2 = "3"
					elif(quantidade <= bolsa[18] - bolsa[19] and conf == 1):
						bolsa[19] = bolsa[19] + quantidade
						personagem[56] = personagem[56] - (quantidade * 50)
						print("Suas Moedas: %d" % personagem[56])
						decisao2 = "0"

				elif(decisao2 == "4"):
					quantidade = int(input("\nQuantidade:"))

					if(personagem[56] < quantidade * 20):
						print("Moedas insuficientes.")
						conf = 0
						decisao2 = "0"
					else:
						conf = 1
                                                
					if(quantidade > bolsa[13] - bolsa[14] and conf == 1):
						print("\nVocê só pode carregar %d poções de mana atualmente" % bolsa[13])
						sleep(2)
						decisao2 = "3"
					elif(quantidade <= bolsa[13] - bolsa[14] and conf == 1):
						bolsa[14] = bolsa[14] + quantidade
						personagem[56] = personagem[56] - (quantidade * 20)
						print("Suas Moedas: %d" % personagem[56])
						decisao2 = "0"

				elif(decisao2 == "5"):
					decisao = "0"

		elif(decisao == "4"):
			print("\nVolte sempre!")
			sleep(2)
