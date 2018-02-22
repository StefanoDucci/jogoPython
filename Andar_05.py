# encoding: UTF-8
from Batalha import *
from Monstros import *
from Quest import *
from time import sleep
from Opcoes import salvar_jogo
from MenusPersonagem import menuPersonagem

###############################################################################################################

def sala_do_chefe05(personagem, nome, inventario, habilidades, itens, bolsa):
	print("\n****************************************************************")
	print("\n\n Sala do Chefe \n\n")
	print("****************************************************************\n")
	sleep(3)

	print("Rrruuuuuurrrrr")
	sleep(2)

	print("\n" + nome[0] + ":")
	print("    Que tipo de criatura é essa?")
	sleep(3)

	monstro = []

	demonio(monstro)

	resultado = batalha(personagem, monstro, habilidades, bolsa)

	if(resultado == 0):
                print("\nSua alma foi aprisionada para sempre")
                sleep(2)
                exit(0)

	print("\n" + nome[0] + ":")
	print("    Não acredito que sai vivo dessa...")
	sleep(2)
	print("    Esta na hora de ter uma conversa com o Mago Sábio.")
	sleep(2)

	print("\nVocê recebeu a Chave do 5º andar.")
	sleep(3)

	inventario.append("Chave05")

	print("\nChave do 5º andar adicionada ao inventario.")
	sleep(3)



###############################################################################################################

def andar_05(personagem, nome, inventario, habilidades, itens, bolsa):
	chave = [0,0]
	voltas = [0,0,0,0,0,0]
	
	monstro1 = []
	monstro2 = []
	monstro3 = []

	
        
	print("\n****************************************************************")
	print("\n\n Cemitério \n\n")
	print("****************************************************************\n")
	sleep(3)

	print("\n" + nome[0] + ":")
	print("    Brrr")
	sleep(2)
	print("    Mas de onde está vindo esse frio? Estamos no meio do verão.")
	sleep(2)

	decisao = "0"
	while(decisao != "1" and decisao != "2"):
		decisao = input("\nDecisão: \n1 - Entrar no cemitério \n2 - Menu de Personagem \nR: ")

		if(decisao == "1"):
			print("\n****************************************************************")
			print("\n\n Centro do Cemitério \n\n")
			print("****************************************************************\n")
			sleep(3)

			print("\n" + nome[0] + ":")
			print("    Que tipo de bruxaria é essa?")
			sleep(3)

			print("\nNecromante:")
			print("    O que? Mas quem é você? E como você passou por nossa barreira na entrada?")
			sleep(3)

			print("\n" + nome[0] + ":")
			print("    Que barreira? Eu fui transportado aqui para dentro.")
			sleep(3)

			print("\nNecromante:")
			print("    Então você só pode ser o tal " + nome_classe(personagem[40]) + " que esta tentando vencer o jogo do mestre.")
			sleep(3)

			print("\n" + nome[0] + ":")
			print("    Então isso é um jogo para vocês?")
			sleep(3)

			print("\nNecromante:")
			print("    Uahahaha. Mas é claro, brincar com este mundo é a nossa maior diversão.")
			sleep(3)

			print("\n" + nome[0] + ":")
			print("    Não vou deixar que façam isso!")
			sleep(3)

			print("\nPLAFT")
			sleep(3)

			print("\n" + nome[0] + ":")
			print("    Mas o que? Outra barreira?")
			sleep(3)
			print("    Espere, eu consigo ver as linhas de energia...")
			sleep(3)
			print("    Se eu destruir as fontes vocês não terão como terminar este ritual!")
			sleep(3)

			decisao2 = "0"
			while(decisao2 != "1" and decisao2 != "2" and decisao2 != "3" and decisao2 != "4"):
				decisao2 = input("\nDecisão: \n1 - Oste \n2 - Leste \n3 - Sala do Chefe \n4 - Menu Personagem \nR: ")

				if(decisao2 == "1"):
                                        print("\n****************************************************************")
                                        print("\n\n Oeste do Cemitério \n\n")
                                        print("****************************************************************\n")

                                        if(voltas[1] == 0):
                                                if(voltas[3] == 0):
                                                        print("Cleck Cleck Cleck")
                                                        sleep(2)

                                                        print("\n" + nome[0] + ":")
                                                        print("    Que barulho é esse?")
                                                        sleep(2)
                                                        print("    Os tumulos estão...")
                                                        sleep(2)
                                                        print("    Estão...")
                                                        sleep(2)
                                                        print("    Se abrindo!!!")
                                                        sleep(2)
                                                        
                                                elif(voltas[3] == 1):
                                                        print("\n" + nome[0] + ":")
                                                        print("    Deste lado também?")

                                                del monstro1[:]
                                                del monstro2[:]
                                                del monstro3[:]

                                                esqueleto(monstro1)
                                                esqueleto(monstro2)
                                                esqueleto(monstro3)

                                                resultado = batalha_Vs3(personagem, monstro1, monstro2, monstro3, habilidades, bolsa)

                                                if(resultado == 0):
                                                        print("\nVocê morreu soterrado por ossos.")
                                                        sleep(2)
                                                        exit(0)

                                                print("\n" + nome[0] + ":")
                                                print("    Esse lugar é um pedaço do próprio inferno.")
                                                voltas[1] = 1

                                        decisao3 = "0"
                                        while(decisao3 != "1" and decisao3 != "2" and decisao3 != "3"):
                                                decisao3 = input("\nDecisão: \n1 - Oeste \n2 - Leste \n3 - Menu Personagem \nR: ")

                                                if(decisao3 == "1"):
                                                        print("\n****************************************************************")
                                                        print("\n\n Extremo Oeste do Cemitério \n\n")
                                                        print("****************************************************************\n")
                                                        sleep(3)

                                                        if(voltas[2] == 0):
                                                                del monstro1[:]
                                                                del monstro2[:]

                                                                zumbi(monstro1)
                                                                zumbi(monstro2)

                                                                resultado = batalha_Vs2(personagem, monstro1, monstro2, habilidades, bolsa)

                                                                if(resultado == 0):
                                                                        print("\nVocê se tornou parte do exercito zumbi.")
                                                                        sleep(2)
                                                                        exit(0)

                                                                if(voltas[2] == 0 and voltas[4] == 0):
                                                                        print("\n" + nome[0] + ":")
                                                                        print("    Parece que esta é a fonte de poder.")
                                                                        sleep(2)

                                                                elif(voltas[2] == 0 and voltas[4] == 1):
                                                                        print("\n" + nome[0] + ":")
                                                                        print("    Esta é a ultima fonte de poder.")
                                                                        sleep(2)

                                                                voltas[2] = 1

                                                        decisao4 = "0"
                                                        while(decisao4 != "1" and decisao4 != "2"):
                                                                if(chave[0] == 0):
                                                                        decisao4 = input("\nDecisão: \n1 - Destuir o altar \n2 - Voltar \nR: ")
                                                                elif(chave[0] == 1):
                                                                        print("\nEste altar já está destruido.")
                                                                        sleep(2)
                                                                        decisao4 = input("\n1 - Voltar \nR: ")

                                                                if(decisao4 == "1" and chave[0] == 0):
                                                                        print("\nO Altar Direito foi destruido.")
                                                                        sleep(2)
                                                                        chave[0] = 1
                                                                        decisao4 = "0"

                                                                elif(decisao4 == "2" or decisao4 == "1" and chave[0] == 1):
                                                                        decisao3 = "0"
                                                                                

                                                elif(decisao3 == "2"):
                                                        decisao2 = "0"


                                                elif(decisao3 == "3"):
                                                        menuPersonagem(personagem, habilidades, itens, nome, bolsa)
                                                        decisao3 = "0"
                                        


				elif(decisao2 == "2"):
                                        print("\n****************************************************************")
                                        print("\n\n Leste do Cemitério \n\n")
                                        print("****************************************************************\n")

                                        if(voltas[3] == 0):
                                                if(voltas[1] == 0):
                                                        print("Cleck Cleck Cleck")
                                                        sleep(2)

                                                        print("\n" + nome[0] + ":")
                                                        print("    Que barulho é esse?")
                                                        sleep(2)
                                                        print("    Os tumulos estão...")
                                                        sleep(2)
                                                        print("    Estão...")
                                                        sleep(2)
                                                        print("    Se abrindo!!!")
                                                        sleep(2)
                                                        
                                                elif(voltas[1] == 1):
                                                        print("\n" + nome[0] + ":")
                                                        print("    Deste lado também?")

                                                del monstro1[:]
                                                del monstro2[:]
                                                del monstro3[:]

                                                esqueleto(monstro1)
                                                esqueleto(monstro2)
                                                esqueleto(monstro3)

                                                resultado = batalha_Vs3(personagem, monstro1, monstro2, monstro3, habilidades, bolsa)

                                                if(resultado == 0):
                                                        print("\nVocê morreu soterrado por ossos.")
                                                        sleep(2)
                                                        exit(0)

                                                print("\n" + nome[0] + ":")
                                                print("    Esse lugar é um pedaço do próprio inferno.")
                                                voltas[3] = 1

                                        decisao5 = "0"
                                        while(decisao5 != "1" and decisao5 != "2" and decisao5 != "3"):
                                                decisao5 = input("\nDecisão: \n1 - Leste \n2 - Oeste \n3 - Menu Personagem \nR: ")

                                                if(decisao5 == "1"):
                                                        print("\n****************************************************************")
                                                        print("\n\n Extremo Leste do Cemitério \n\n")
                                                        print("****************************************************************\n")
                                                        sleep(3)

                                                        if(voltas[4] == 0):
                                                                del monstro1[:]
                                                                del monstro2[:]

                                                                zumbi(monstro1)
                                                                zumbi(monstro2)

                                                                resultado = batalha_Vs2(personagem, monstro1, monstro2, habilidades, bolsa)

                                                                if(resultado == 0):
                                                                        print("\nVocê se tornou parte do exercito zumbi.")
                                                                        sleep(2)
                                                                        exit(0)

                                                                if(voltas[2] == 0 and voltas[4] == 0):
                                                                        print("\n" + nome[0] + ":")
                                                                        print("    Parece que esta é a fonte de poder.")
                                                                        sleep(2)

                                                                elif(voltas[2] == 0 and voltas[4] == 1):
                                                                        print("\n" + nome[0] + ":")
                                                                        print("    Esta é a ultima fonte de poder.")
                                                                        sleep(2)

                                                                voltas[4] = 1

                                                        decisao6 = "0"
                                                        while(decisao6 != "1" and decisao6 != "2"):
                                                                if(chave[1] == 0):
                                                                        decisao6 = input("\nDecisão: \n1 - Destuir o altar \n2 - Voltar \nR: ")
                                                                elif(chave[1] == 1):
                                                                        print("\nEste altar já está destruido.")
                                                                        sleep(2)
                                                                        decisao6 = input("\n1 - Voltar \nR: ")

                                                                if(decisao6 == "1" and chave[1] == 0):
                                                                        print("\nO Altar Esquerdo foi destruido.")
                                                                        sleep(2)
                                                                        chave[1] = 1
                                                                        decisao6 = "0"

                                                                elif(decisao6 == "2" or decisao6 == "1" and chave[1] == 1):
                                                                        decisao5 = "0"
                                                                                

                                                elif(decisao5 == "2"):
                                                        decisao2 = "0"


                                                elif(decisao5 == "3"):
                                                        menuPersonagem(personagem, habilidades, itens, nome, bolsa)
                                                        decisao5 = "0"
                                        

				elif(decisao2 == "3"):
                                        if(chave[0] == 1 and chave[1] == 1):
                                                print("\n" + nome[0] + ":")
                                                print("    Eu destrui ambas as fontes de poder, agora é a vez de vocês.")
                                                sleep(3)

                                                print("\nNecromante:")
                                                print("    Já é tarde seu tolo! Nosso ritual está quase completo!")
                                                sleep(2)

                                                print("\n" + nome[0] + ":")
                                                print("    Eu mato vocês dois antes disso.")
                                                sleep(2)

                                                del monstro1[:]
                                                del monstro2[:]
                                                del monstro3[:]

                                                necromante(monstro2)
                                                esqueleto(monstro1)
                                                zumbi(monstro3)

                                                resultado = batalha_Vs3(personagem, monstro1, monstro2, monstro3, habilidades, bolsa)

                                                if(resultado == 0):
                                                        print("\nNecromante:")
                                                        print("    Tolo, ninguém pode nos impedir!")
                                                        sleep(2)
                                                        exit(0)

                                                print("\n" + nome[0] + ":")
                                                print("    Só falta um.")
                                                sleep(2)

                                                del monstro1[:]
                                                del monstro2[:]
                                                del monstro3[:]

                                                necromante(monstro2)
                                                esqueleto(monstro1)
                                                zumbi(monstro3)

                                                resultado = batalha_Vs3(personagem, monstro1, monstro2, monstro3, habilidades, bolsa)

                                                if(resultado == 0):
                                                        print("\nNecromante:")
                                                        print("    Tolo, ninguém pode nos impedir!")
                                                        sleep(2)
                                                        exit(0)

                                                print("\n" + nome[0] + ":")
                                                print("    Droga! Me estendi de mais. Tem algo saindo desse maldito pentagrama.")
                                                sleep(2)

                                                decisao7 = "0"
                                                while(decisao7 != "1" and decisao7 != "2"):
                                                        decisao7 = input("\nDecisão: \n1 - Seguir em direção a morte certa \n2 - Se preparar para a morte certa \nR: ")

                                                        if(decisao7 == "1"):
                                                                sala_do_chefe05(personagem, nome, inventario, habilidades, itens, bolsa)

                                                        elif(decisao7 == "2"):
                                                                menuPersonagem(personagem, habilidades, itens, nome, bolsa)
                                                                decisao7 = "0"

                                        else:
                                                print("\nEsta sala esta selada pelo poder dos necromantes.")
                                                sleep(2)
                                                decisao2 = "0"
                                                
				elif(decisao2 == "4"):
                                        menuPersonagem(personagem, habilidades, itens, nome, bolsa)
                                        decisao2 = "0"
                            

		elif(decisao == "2"):
			menuPersonagem(personagem, habilidades, itens, nome, bolsa)
			decisao = "0"
            
