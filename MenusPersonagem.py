# encoding: UTF-8
from Quest import mostra_status, tomar_pot
from Armas import nome_arma
from Armadura import nome_armadura
from Habilidades import nome_elemento, evoluir_habilidades
from time import sleep

def menuPersonagem(personagem, habilidades, itens, nome, bolsa):
	decisao = "0"
	while(decisao != "1" and decisao != "2" and decisao != "3" and decisao != "4" and decisao != "5"):
		print("\n****************************************************************")
		print("Menu: \n1 - Status \n2 - Equipes \n3 - Poções \n4 - Habilidades \n5 - Voltar")
		decisao = input("R: ")
		
		if(decisao == "1"):
			mostra_status(personagem, nome)
			decisao = "0"
			
		elif(decisao == "2"):
			print("\n****************************************************************")
			print("Arma: " + nome_arma(str(personagem[64])) + " +" + str(personagem[74]))
			print("Dano Físico: %s" % personagem[10])
			print("Dano Mágico: %s" % personagem[11])
			print("Agilidade: %s" % personagem[51])
			print("Destreza: %s" % personagem[52])
			print("Mana Asicional: %s" % personagem[53])
			print("Elemento: " + nome_elemento(int(personagem[57])))
			
			print("\n")
			
			print("Armadura: " + nome_armadura(personagem[65]) + " +" + str(personagem[75]))
			print("Defesa Física: %s" % personagem[12])
			print("Defesa Mágica: %s" % personagem[13])
			print("Elemento: " + nome_elemento(personagem[58]))
			sleep(2)
			
			decisao2 = "0"
			while(decisao2 != "1" and decisao2 != "2" and decisao2 != "3"):
				print("\n****************************************************************")
				print("Menu: \n1 - Trocar Arma \n2 - Trocar Armadura \n3 - Voltar")
				decisao2 = input("R: ")
				
				if(decisao2 == "1"):
					print("\n****************************************************************")
					print("Armas: ")
					for i in range(5):						
						print(str(i + 1) + " - " + nome_arma(str(itens[2 + (9 * i)])))
						
					decisao3 = "0"
					while(decisao3 != "1" and decisao3 != "2" and decisao3 != "3" and decisao3 != "4" and decisao3 != "5"):
						print("\nQual arma você gostaria de ver?")
						decisao3 = input("R: ")
						
						decisao3 = int(decisao3)
						print("\n****************************************************************")
						print("Nome:" + nome_arma(str(itens[2 + (9 * (decisao3 - 1))])))
						print("Dano Físico: %s" % itens[0 + (9 * (decisao3 - 1))])
						print("Dano Mágico: %s" % itens[1 + (9 * (decisao3 - 1))])
						print("Agilidade: %s" % itens[3 + (9 * (decisao3 - 1))])
						print("Destreza: %s" % itens[4 + (9 * (decisao3 - 1))])
						print("Mana Asicional: %s" % itens[5 + (9 * (decisao3 - 1))])
						print("Elemento: " + nome_elemento(int(itens[6 + (9 * (decisao3 - 1))])))
						print("Chance de Status: %s" % itens[8 + (9 * (decisao3 - 1))])
						decisao3 = str(decisao3)
						
						print("\n****************************************************************")
						decisao4 = "0"
						while(decisao4 != "1" and decisao4 != "2"):
							print("Decisão: \n1 - Equipar \n2 - Voltar")
							decisao4 = input("R: ")
							
							if(decisao4 == "1"):                                                               
								temp1 = personagem[10]
								temp2 = personagem[11]
								temp3 = personagem[51]
								temp4 = personagem[52]
								temp5 = personagem[53]
								temp6 = personagem[57]
								temp7 = personagem[64]
								temp8 = personagem[66]
								temp9 = personagem[74]
							
								decisao3 = int(decisao3)
								personagem[10] = itens[0 + (9 * (decisao3 - 1))]
								personagem[11] = itens[1 + (9 * (decisao3 - 1))]
								personagem[51] = itens[3 + (9 * (decisao3 - 1))]
								personagem[52] = itens[4 + (9 * (decisao3 - 1))]
								personagem[53] = itens[5 + (9 * (decisao3 - 1))]
								personagem[57] = itens[6 + (9 * (decisao3 - 1))]
								personagem[64] = itens[2 + (9 * (decisao3 - 1))]
								personagem[66] = itens[8 + (9 * (decisao3 - 1))]
								personagem[74] = itens[65 + (decisao3 - 1)]

								itens[0 + (9 * (decisao3 - 1))] = temp1
								itens[1 + (9 * (decisao3 - 1))] = temp2
								itens[3 + (9 * (decisao3 - 1))] = temp3
								itens[4 + (9 * (decisao3 - 1))] = temp4
								itens[5 + (9 * (decisao3 - 1))] = temp5
								itens[6 + (9 * (decisao3 - 1))] = temp6
								itens[2 + (9 * (decisao3 - 1))] = temp7
								itens[8 + (9 * (decisao3 - 1))] = temp8
								itens[65 + (decisao3 - 1)]  = temp9
								
								decisao3 = str(decisao3)
								
								decisao2 = "0"
								
							elif(decisao4 == "2"):
								decisao2 = "0"
								
								
				elif(decisao2 == "2"):
					print("\n****************************************************************")
					print("Armaduras: ")
					for i in range(5):
						print(str((i + 1)) + " - " + nome_armadura(int(itens[47 + (4 * i)])))
						
					decisao3 = "0"
					while(decisao3 != "1" and decisao3 != "2" and decisao3 != "3" and decisao3 != "4" and decisao3 != "5"):
						print("Qual armadura você gostaria de ver?")
						decisao3 = input("R: ")
						
						decisao3 = int(decisao3)
						print("\n****************************************************************")
						print("%s: " % nome_armadura(itens[47 + (4 * (decisao3 - 1))]))
						print("Defesa Física: %s" % itens[45 + (4 * (decisao3 - 1))])
						print("Defesa Mágica: %s" % itens[46 + (4 * (decisao3 - 1))])
						print("Elemento: " + nome_elemento(int(itens[48 + (4 * (decisao3 - 1))])))
						decisao3 = str(decisao3)
						
						print("\n****************************************************************")
						decisao4 = "0"
						while(decisao4 != "1" and decisao4 != "2"):
							print("Decisão: \n1 - Equipar \n2 - Voltar")
							decisao4 = input("R: ")
							
							if(decisao4 == "1"):
								temp1 = personagem[12]
								temp2 = personagem[13]
								temp3 = personagem[65]
								temp4 = personagem[58]
								temp5 = personagem[75]
							
								decisao3 = int(decisao3)
								personagem[12] = itens[45 + (4 * (decisao3 - 1))]
								personagem[13] = itens[46 + (4 * (decisao3 - 1))]
								personagem[65] = itens[47 + (4 * (decisao3 - 1))]
								personagem[58] = itens[48 + (4 * (decisao3 - 1))]
								personagem[75] = itens[70 + (decisao3 - 1)]

								itens[45 + (4 * (decisao3 - 1))] = temp1
								itens[46 + (4 * (decisao3 - 1))] = temp2
								itens[47 + (4 * (decisao3 - 1))] = temp3
								itens[48 + (4 * (decisao3 - 1))] = temp4
								itens[70 + (decisao3 - 1)] = temp5

								decisao3 = str(decisao3)
								
								decisao2 = "0"
								
							elif(decisao4 == "2"):
								decisao2 = "0"
						
						
				elif(decisao2 == "3"):
					decisao = "0"
				
				
		elif(decisao == "3"):
			tomar_pot(personagem, bolsa)
			decisao = "0"

		elif(decisao == "4"):
                        evoluir_habilidades(personagem, habilidades, 2)
			
		
