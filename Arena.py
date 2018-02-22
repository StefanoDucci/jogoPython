# encoding: UTF-8
from Batalha import *
from Monstros import *
from Quest import *
from time import sleep
from Opcoes import salvar_jogo
from MenusPersonagem import menuPersonagem
from random import randint

###############################################################################################################

def homem_vs_fera(personagem, nome, habilidades, itens, bolsa):
        print("\nLocutor:")
        print("    Eeeeesta na hora Arena!")
        sleep(2)

        print("\nPlatéia:")
        print("    Yeeeeeaaaahhhh!!!")
        sleep(2)

        print("\nLocutor:")
        print("    Hoje teremos um de nossos jogos mais sangrentos!")
        sleep(3)
        print("    Hoje é dia de Homem Vs Féra!")
        sleep(2)

        
        print("\nLocutor:")
        print("    O nosso desafiante de hoje se chama %s, deem as boas vindas para ele!" % nome[0])
        sleep(3)

        print("\nLocutor:")
        print("    Vamos ao sorteio.")
        sleep(2)
        print("    Pegue um papel do saco um.")
        sleep(2)

        monstro1 = []
        monstro2 = []
        monstro3 = []
        
        sorteioFera = randint(1, 5)

        if(sorteioFera == 1):
                print("\nLocutor:")
                print("    Leões? Classico.")
                sleep(2)
                leao(monstro1)
                leao(monstro2)
                leao(monstro3)

        elif(sorteioFera == 2):
                print("\nLocutor:")
                print("    Urso? Essa vai ser dificíl.")
                sleep(2)
                urso(monstro1)
                urso(monstro2)
                urso(monstro3)

        elif(sorteioFera == 3):
                print("\nLocutor:")
                print("    Hienas? Parece que temos um sortudo entre nós.")
                sleep(2)
                hiena(monstro1)
                hiena(monstro2)
                hiena(monstro3)

        elif(sorteioFera == 4):
                print("\nLocutor:")
                print("    O Gigante? Isso vai ser bom.")
                sleep(2)
                gigante(monstro1)

        elif(sorteioFera == 5):
                print("\nLocutor:")
                print("    Touro? Eu começaria a correr se fosse você.")
                sleep(2)
                touro(monstro1)
                touro(monstro2)
                touro(monstro3)
        
        
        sorteioNume = randint(1, 3)

        if(sorteioFera != 4):
                print("\nLocutor:")
                print("    Agora retire um número do saco dois.")
                sleep(2)

        elif(sorteioFera == 4):
                print("\nLocutor:")
                print("    Bom, como só temos um gigante... Vamos a parte boa!")
                sleep(3)
               


        if(sorteioNume == 1 or sorteioFera == 4):
                if(sorteioFera == 3):
                        print("    Tragam a %s" % monstro1[7])
                        sleep(2)
                else:
                        print("    Tragam o %s" % monstro1[7])
                        sleep(2)
                resultado = batalha(personagem, monstro1, habilidades, bolsa)

        elif(sorteioNume == 2):
                if(sorteioFera == 3):
                        print("    Tragam as " + monstro1[7] + "s")
                        sleep(2)
                else:
                        print("    Tragam os " + monstro1[7] + "s")
                        sleep(2)
                resultado = batalha_Vs2(personagem, monstro1, monstro2, habilidades, bolsa)

        elif(sorteioNume == 3):
                if(sorteioFera == 3):
                        print("    Tragam as " + monstro1[7] + "s")
                        sleep(2)
                else:
                        print("    Tragam os " + monstro1[7] + "s")
                        sleep(2)
                resultado = batalha_Vs3(personagem, monstro1, monstro2, monstro3, habilidades, bolsa)

        if(resultado == 0):
                print("\n    Você é fraco de mais para a arena!")
                exit(0)

        

###############################################################################################################

def ultimo_homem(personagem, nome, habilidades, itens, bolsa):
        print("\nLocutor:")
        print("    Eeeeesta na hora Arena!")
        sleep(2)

        print("\nPlatéia:")
        print("    Yeeeeeaaaahhhh!!!")
        sleep(2)

        print("\nLocutor:")
        print("    Hoje teremos o jogo favorito de vocês! Último Homem em Pé!!!")
        sleep(2)

        print("\nPlatéia:")
        print("    Começem de uma vez!!!")
        sleep(2)
        print("    Eu quero ver sangue!")
        sleep(2)

        print("\nLocutor:")
        print("    Que assim seja então! Tragam os competidores!!!")
        sleep(2)


        
        gladiadores = []
        monstro1 = []
        monstro2 = []
        monstro3 = []
        monstro4 = []
        monstro5 = []
        monstro6 = []
        monstro7 = []
        monstro8 = []
        monstro9 = []

        gladiador1(monstro1)
        gladiador2(monstro2)
        gladiador3(monstro3)
        gladiador4(monstro4)
        gladiador5(monstro5)
        gladiador6(monstro6)
        gladiador7(monstro7)
        gladiador8(monstro8)
        gladiador9(monstro9)

        gladiadores.append(monstro1)
        gladiadores.append(monstro2)
        gladiadores.append(monstro3)
        gladiadores.append(monstro4)
        gladiadores.append(monstro5)
        gladiadores.append(monstro6)
        gladiadores.append(monstro7)
        gladiadores.append(monstro8)
        gladiadores.append(monstro9)
        

        batalha_arena_Vs9(personagem, gladiadores, habilidades, bolsa)
        
        

###############################################################################################################

def melhor_dos_melhores(personagem, nome, habilidades, itens, bolsa):
        print("C1 ---								 	-- C9")
        print("      |								       |")
        print("      |								       |")
        print("       -- VB1 ---					      -- VB5 --")
        print("      |		  |					     |         |")
        print("      |		  |					     |         |")
        print("C2 ---		  |					     |          -- C10")
        print(" 		   -- VB9  ---                    --- VB11 --")
        print("C3 ---		  |	      |			 |           |          -- C11")
        print("      |		  |	      |			 |           |         |")
        print("      |		  |	      |			 |           |         |")
        print("       -- VB2 ---	      |			 |            -- VB6 --")
        print("      |			      |			 |        	       |")
        print("     |			      |			 |       	       |")
        print("C4 ---			      |			 |	 		-- C12")
        print("                                -- VB13 - VB14 --")
        print("C5 ---			      |			 |       		-- C13")
        print("      |			      |			 |      	       |")
        print("      |			      |			 |       	       |")
        print(" 	-- VB3 ---	      |			 |            -- VB7 --")
        print("      |		  |	      |			 |           |         |")
        print("      |		  |	      |			 |           |         |")
        print("C6 ---		  |	      |			 |           |  	-- C14")
        print(" 		   -- VB10 ---			  --- VB12 --")
        print("C7 ---		  |					     |  	-- C15")
        print("      |		  |					     |         |")
        print("      |		  |					     |         |")
        print(" 	-- VB4 ---					      -- VB8 --")
        print("      |								       |")
        print("      |								       |")
        print("C8 ---								 	-- C16")
        

###############################################################################################################

def torneios(personagem, nome, inventario, habilidades, itens, bolsa):
	print("\n****************************************************************")
	print("\n\n Saguão da Arena \n\n")
	print("****************************************************************\n")
	sleep(3)

	print("Recepcionista:")
	print("    Olá %s, seja bem vindo a Arena, aqui você poderá enfrentar os mais fortes adversários para ganhar os melhores prêmios." % nome[0])
	sleep(3)
	print("    Por favor, escolha em qual dos torneios você gostaria de se inscrever.")
	sleep(2)

	decisao = "0"
	while(decisao != "1" and decisao != "2" and decisao != "3" and decisao != "4"):
                print("\nTorneios: \t\t\tRecompensa:")
                print("1 - Homem Vs Fera \t\t500 moedas")
                print("2 - Último homem em pé \t\t1000 moedas")
                print("3 - O melhor dos melhores \t2000 moedas")
                print("4 - Voltar")
                decisao = input("R: ")

                if(decisao == "1"):
                        decisao2 = "0"
                        while(decisao2 != "1" and decisao2 != "2"):
                                decisao2 = input("\nDecisão: \n1 - Ver descrição do torneio \n2 - Participar do torneio \n3 - Voltar \nR: ")
                                if(decisao2 == "1"):
                                        print("\nO torneio Homem Vs Fera consiste em:")
                                        print("Sortear um papel com o nome da fera que você irá enfrentar.")
                                        print("Sortear o número de feras que serão colocadas na arena.")
                                        print("Ser o único a sair com vida da arena.")
                                        decisao2 = "0"
                                        sleep(5)

                                elif(decisao2 == "2"):
                                        print("\nRecepcionista:")
                                        print("    Boa sorte!")
                                        sleep(2)
                                        homem_vs_fera(personagem, nome, habilidades, itens, bolsa)
                                        print("\nRecepcionista:")
                                        print("    Parabéns! Aqui esta seu prêmio. ")
                                        sleep(2)
                                        print("\nVocê recebeu 500 moedas.")
                                        sleep(2)
                                        personagem[56] = personagem[56] + 500
                                        print("\nRecepcionista:")
                                        print("    Espero velo por aqui mais vezes.")
                                        sleep(2)

                                elif(decisao2 == "3"):
                                        decisao = "0"

                elif(decisao == "2"):
                        decisao2 = "0"
                        while(decisao2 != "1" and decisao2 != "2"):
                                decisao2 = input("\nDecisão: \n1 - Ver descrição do torneio \n2 - Participar do torneio \n3 - Voltar \nR: ")
                                if(decisao2 == "1"):
                                        print("\nO torneio Último Homem em Pé consiste em:")
                                        print("Dez homems entrarão na arena.")
                                        print("Somente um sairá vivo.")
                                        decisao2 = "0"
                                        sleep(5)
                                elif(decisao2 == "2"):
                                        print("\nRecepcionista:")
                                        print("    Boa sorte!")
                                        sleep(2)
                                        ultimo_homem(personagem, nome, habilidades, itens, bolsa)
                                        print("\nRecepcionista:")
                                        print("    Parabéns! Aqui esta seu prêmio. ")
                                        sleep(2)
                                        print("\nVocê recebeu 1000 moedas.")
                                        sleep(2)
                                        personagem[56] = personagem[56] + 1000
                                        print("\nRecepcionista:")
                                        print("    Espero velo por aqui mais vezes.")
                                        sleep(2)

                                elif(decisao2 == "3"):
                                        decisao = "0"


                elif(decisao == "3"):
                        print("\nRecepcionista:")
                        print("    Boa sorte!")
                        sleep(2)
                        melhor_dos_melhores(personagem, nome, habilidades, itens, bolsa)
                        decisao = "0"

                elif(decisao == "4"):
                        print("\nRecepsionista:")
                        print("    Espero vê-lo em preve.")
                        sleep(2)

	
