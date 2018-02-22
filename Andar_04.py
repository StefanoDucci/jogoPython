# encoding: UTF-8
from Batalha import *
from Monstros import *
from Quest import *
from time import sleep
from Opcoes import salvar_jogo

###############################################################################################################

def sala_do_chefe04(personagem, nome, inventario, habilidades, itens, bolsa):
	print("\n****************************************************************")
	print("\n\n Sala do Carcereiro Mór \n\n")
	print("****************************************************************\n")
	sleep(3)

	print("\nCarcereiro Mór:")
	print("    Então meus guardas não foram capazes de conter essa rebelião ridícula...")
	sleep(3)

	print("\n" + nome[0] + ":")
	print("    Eu não tenho nada a ver com essa rebelião, fui colocado no meio disso.")
	sleep(3)

	print("\nCarcereiro Mór:")
	print("    Foi? Então qual é o seu objetivo vindo até aqui?")
	sleep(3)

	print("\n" + nome[0] + ":")
	print("    Preciso da chave do portal para continuar.")
	sleep(3)

	print("\nCarcereiro Mór:")
	print("    Então toda essa maldita confusão só por causa disto?")
	sleep(3)

	print("\n" + nome[0] + ":")
	print("    Eu já disse que não tenho nada a ver com isso.")
	sleep(3)

	print("\nCarcereiro Mór:")
	print("    Não acredito no que você diz! E também não posso deixar que fique com isso.")
	sleep(3)

	print("\n" + nome[0] + ":")
	print("    Então que assim seja.")
	sleep(3)

	monstro = []
	carcereiro_mor(monstro)

	resultado = batalha(personagem, monstro, habilidades, bolsa)

	if(resultado == 0):
		print("\nCarcereiro Mór:")
		print("    Como um lixo como você chegou até aqui?")
		exit(0)

	print("\n" + nome[0] + ":")
	print("    Preciso descobrir mais sobre este portal, nem todos os chefes parecem gostar disso...")
	sleep(3)

	inventario.append("Chave04")
	
	print("\Chave do 4º Andar adicionado ao inventário")
	sleep(2)
	salvar_jogo(personagem, nome, inventario, habilidades, itens, bolsa)

###############################################################################################################
	
def andar_04(personagem, nome, inventario, habilidades, itens, bolsa):
	chave = [0]
	voltas = [0,0,0,0,0,0]
	print("\n****************************************************************")
	print("\n\n Calabouços \n\n")
	print("****************************************************************\n")
	sleep(3)
	
	print("Vozes distantes:")
	print("    AAAAHHH")
	sleep(2)
	print("\n    Me tirem daqui!")
	sleep(2)
	print("\n    AAAAHHHGG")
	sleep(2)
	print("\n    VOCÊ MATOU ELE!!")
	sleep(2)
	
	print("\n" + nome[0] + ":")
	print("    Este mundo esta um caos, tudo esta desmoronando.")
	sleep(2)
	
	decisao = "0"
	while(decisao != "1" and decisao != "2"):
		print("\nDecisão: \n1 - Oeste \n2 - Tomar Poção")
		decisao = input("R: ")

		if(decisao == "1"):
			print("\n****************************************************************")
			print("\n\n Conjunto de celas A \n\n")
			print("****************************************************************\n")
			sleep(3)

			if(voltas[0] == 0):
                                print("\n" + nome[0] + ":")
                                print("    Ei! Vocês ai! O que esta acontecendo?")
                                sleep(2)
                                
                                print("\n????:")
                                print("    Como você veio parar aqui embaixo?")
                                sleep(2)
                                print("    Não, isso não importa agora, é perfeito.")
                                sleep(2)

                                print("\n" + nome[0] + ":")
                                print("    Desculpe mas acho que não te entendi.")
                                sleep(2)

                                print("\n????:")
                                print("    Rápido, segurem ele, vamos usa-lo de refém.")

                                monstro1 = []
                                monstro2 = []
                                monstro3 = []

                                prisioneiro(monstro1)
                                prisioneiro(monstro2)
                                prisioneiro(monstro3)

                                resultado = batalha_Vs3(personagem, monstro1, monstro2, monstro3, habilidades, bolsa)

                                if(resultado == 0):
                                        print("\nPrisioneiro:")
                                        print("    Vocês não deviam ter usado tanta força, idiotas!")
                                        exit(0)

                                print("\n" + nome[0] + ":")
                                print("    Este lugar é perigoso.")
                                voltas[0] = 1

			decisao2 = "0"
			while(decisao2 != "1" and decisao2 != "2"):
				decisao2 = input("\nDecisão: \n1 - Oeste \n2 - Tomar Poção \nR: ")

				if(decisao2 == "1"):
					print("\n****************************************************************")
					print("\n\n Conjunto de celas B \n\n")
					print("****************************************************************\n")
					sleep(3)

					if(voltas[1] == 0):
                                                print("\n" + nome[0] + ":")
                                                print("    Mais destes caras?")

                                                del monstro1[:]
                                                del monstro2[:]

                                                prisioneiro(monstro1)
                                                prisioneiro(monstro2)

                                                resultado = batalha_Vs2(personagem, monstro1, monstro2, habilidades, bolsa)

                                                if(resultado == "0"):
                                                        print("Você foi morto por prisioneiros.")
                                                        exit(0)
                                                voltas[1] = 1

					decisao3 = "0"
					while(decisao3 != "1" and decisao3 != "2" and decisao3 != "3"):
						decisao3 = input("\nDecisão: \n1 - Sul \n2 - Leste \n3 - Tomar Poção \nR: ")

						if(decisao3 == "1"):
							print("\n****************************************************************")
							print("\n\n Conjunto de celas C \n\n")
							print("****************************************************************\n")
							sleep(3)

							if(voltas[2] == 0):
                                                                print("Guarda:")
                                                                print("    Onde você conseguiu essas roupas?")
                                                                sleep(3)

                                                                print("\n" + nome[0] + ":")
                                                                print("    Ah, um guarda, finalmente! Tem uns caras bem perigosos soltos por aqui.")
                                                                sleep(3)

                                                                print("\nGuarda:")
                                                                print("    Você acha que me engana? Já para a sua cela se não quiser levar uma surra!")
                                                                sleep(3)

                                                                print("\n" + nome[0] + ":")
                                                                print("    Você esta cometendo um engano, não sou um desses...")
                                                                sleep(2)

                                                                print("\nGuarda:")
                                                                print("    Chega! Se você vai continuar com essa história então não temos outra escolha.")
                                                                sleep(3)

                                                                del monstro1[:]
                                                                del monstro2[:]

                                                                guarda(monstro1)
                                                                guarda(monstro2)

                                                                resultado = batalha_Vs2(personagem, monstro1, monstro2, habilidades, bolsa)

                                                                if(resultado == 0):
                                                                        print("\nGuarda:")
                                                                        print("    Os prisioneiros de hoje em dia nem aguentam levar uma surra mais.")
                                                                        exit(0)

                                                                print("\n" + nome[0] + ":")
                                                                print("    Não posso esperar ajuda nem mesmo dos guardas...")
                                                                sleep(2)
                                                                voltas[2] = 1

							decisao4 = "0"
							while(decisao4 != "1" and decisao4 != "2" and decisao4 != "3"):
								decisao4 = input("\nDecisão: \n1 - Sul \n2 - Norte \n3 - Tomar poção \nR: ")

								if(decisao4 == "1"):
									print("\n****************************************************************")
									print("\n\n Conjunto de celas D \n\n")
									print("****************************************************************\n")
									sleep(3)

									if(voltas[3] == 0):
                                                                                print("\n" + nome[0] + ":")
                                                                                print("    Aqui é onde a coisa parace estar mais feia.")
                                                                                sleep(2)

                                                                                print("\nPrisioneiro:")
                                                                                print("    Você! Você é o Carcereiro Mór?")
                                                                                sleep(2)

                                                                                print("\n" + nome[0] + ":")
                                                                                print("    É claro que não.")
                                                                                sleep(2)

                                                                                print("\nPrisioneiro:")
                                                                                print("    Não minta para mim! Eu tenho um refém.")
                                                                                sleep(2)

                                                                                print("\nGuarda-refém")
                                                                                print("    Não é ele! Não é ele! Eu já disse onde ele esta.")
                                                                                sleep(3)

                                                                                print("\nPrisioneiro")
                                                                                print("    Vocês guardas são todos uns mentiros!")
                                                                                sleep(2)

                                                                                print("\nSom cortante")
                                                                                sleep(2)

                                                                                print("\n" + nome[0] + ":")
                                                                                print("    O que você fez?")
                                                                                sleep(2)

                                                                                print("\nPrisioneiro")
                                                                                print("    Você é o próximo!")

                                                                                del monstro1[:]
                                                                                del monstro2[:]
                                                                                del monstro3[:]

                                                                                prisioneiro(monstro1)
                                                                                prisioneiro(monstro2)
                                                                                prisioneiro(monstro3)

                                                                                resultado = batalha_Vs3(personagem, monstro1, monstro2, monstro3, habilidades, bolsa)

                                                                                if(resultado == 0):
                                                                                        print("\nPrisioneiro:")
                                                                                        print("    Matem todos os mentirosos! hahahahaha")
                                                                                        exit(0)

                                                                                del monstro1[:]
                                                                                del monstro2[:]
                                                                                
                                                                                prisioneiro(monstro1)
                                                                                prisioneiro(monstro2)
                                                                                
                                                                                resultado = batalha_Vs2(personagem, monstro1, monstro2, habilidades, bolsa)

                                                                                if(resultado == 0):
                                                                                        print("\nPrisioneiro:")
                                                                                        print("    Matem todos os mentirosos! hahahahaha")
                                                                                        exit(0)


                                                                                print("\n" + nome[0] + ":")
                                                                                print("    Este grupo era grande.")
                                                                                sleep(2)
                                                                                voltas[3] = 1

									decisao5 = "0"
									while(decisao5 != "1" and decisao5 != "2" and decisao5 != "3" and decisao5 != "4"):
										decisao5 = input("\nDecisão: \n1 - Sala do Chefe \n2 - Oeste \n3 - Norte \n4 - Tomar poção \nR: ")

										if(decisao5 == "1"):
											if(chave[0] == 0):
												print("\nA sala do Chefe esta trancada.")
												sleep(2)
												decisao5 = "0"
											else:
												sala_do_chefe04(personagem, nome, inventario, habilidades, itens, bolsa)
												

										elif(decisao5 == "2"):
											print("\n****************************************************************")
											print("\n\n Sala dos Guardas \n\n")
											print("****************************************************************\n")
											sleep(3)

											if(voltas[4] == 0):
                                                                                                print("\nGuarda:")
                                                                                                print("    Então um de vocês é mesmo louco para entrar aqui?")
                                                                                                sleep(2)

                                                                                                print("\n" + nome[0] + ":")
                                                                                                print("    Eu já disse que não sou um deles!")
                                                                                                sleep(2)

                                                                                                print("\nGuarda:")
                                                                                                print("    Não importa quem você é, se você esta aqui não é por um bom motivo!")
                                                                                                sleep(3)

                                                                                                del monstro1[:]
                                                                                                del monstro2[:]
                                                                                                del monstro3[:]

                                                                                                guarda(monstro1)
                                                                                                guarda(monstro2)
                                                                                                guarda(monstro3)

                                                                                                resultado = batalha_Vs3(personagem, monstro1, monstro2, monstro3, habilidades, bolsa)

                                                                                                if(resultado == 0):
                                                                                                        print("\nGuarda:")
                                                                                                        print("    Se isso é tudo o que eles tem, podemos acabar com essa rebelião! Vamos lá homens!")
                                                                                                        exit(0)

                                                                                                print("\n" + nome[0] + ":")
                                                                                                print("    Porcaria de guardas... eu só queria saber sobre o tal Carcereiro Mór.")
                                                                                                sleep(2)
                                                                                                print("    Acho que vou precisar procurar por conta própria.")
                                                                                                sleep(2)
                                                                                                voltas[4] = 1

											decisao6 = "0"
											while(decisao6 != "1" and decisao6 != "2" and decisao6 != "3" and decisao6 != "4"):
												decisao6 = input("\nDecisão: \n1 - Vasculhar a sala \n2 - Sair da sala \n3 - Tomar poção \nR: ")

												if(decisao6 == "1"):
                                                                                                        if(chave[0] == 0):
                                                                                                                print("\nChave da sala do Chefe encontrada")
                                                                                                                chave[0] = 1
                                                                                                                sleep(2)
                                                                                                                decisao6 = "0"
                                                                                                        else:
                                                                                                                print("\n" + nome[0] + ":")
                                                                                                                print("    Não tem mais nada por aqui.")
                                                                                                                sleep(2)
                                                                                                                decisao6 = "0"

												elif(decisao6 == "2"):
                                                                                                        decisao5 = "0"

												elif(decisao6 == "3"):
                                                                                                        tomar_pot(personagem, bolsa)
                                                                                                        decisao6 = "0"

                                                        
											
                                                                                        

										elif(decisao5 == "3"):
                                                                                        decisao4 = "0"

										elif(decisao5 == "4"):
                                                                                        tomar_pot(personagem, bolsa)
                                                                                        decisao5 = "0"
                                                                        

								elif(decisao4 == "2"):
                                                                        decisao3 = "0"

								elif(decisao4 == "3"):
                                                                        tomar_pot(personagem, bolsa)
                                                                        decisao4 = "0"
                                                        

						elif(decisao3 == "2"):
                                                        decisao2 = "0"

						elif(decisao3 == "3"):
                                                        tomar_pot(personagem, bolsa)
                                                        decisao3 = "0"
                                                
				elif(decisao2 == "2"):
                                        tomar_pot(personagem, bolsa)
                                        decisao2 = "0"
		elif(decisao == "2"):
			tomar_pot(personagem, bolsa)
			decisao = "0"
