# encoding: UTF-8
from Batalha import *
from Monstros import *
from Quest import *
from Opcoes import salvar_jogo
from MenusPersonagem import menuPersonagem

###############################################################################################################	

def sala_do_boss02(personagem, nome, inventario, habilidades, itens, bolsa):
        print("\n****************************************************************")
        print("\n\n Sala do Chefe 02\n\n")
        print("****************************************************************\n")

        print("\n" + nome[0] + ":")
        print("    O cheiro de sangue esta mais forte aqui.")
        sleep(2)
        print("    Mario!?")
        sleep(2)

        print("\nMario:")
        print("    Coof Coof")
        sleep(2)

        print("\n" + nome[0] + ":")
        print("    Você ainda esta vivo? O que aconteceu? Todo este sague...")
        sleep(2)

        print("\nMario:")
        print("    Eu te avisei sobre a criatura! Agora já é tarde para mim!")
        sleep(2)
        print("    Coof, coof")
        sleep(2)
        print("    Mas se você correr, você ainda pode se salvar! Corra %s corra!" % nome[0])
        sleep(2)
        print("\nUltimo suspiro.")
        sleep(2)
        
        print("\n" + nome[0] + ":")
        print("    Nãaao! Eu causei isso!")
        sleep(2)

        print("\nCrocodilo Gigante:")
        print("    Aaarrrrr!!")
        sleep(2)

        print("\n" + nome[0] + ":")
        print("    Maldito! Você pagará pelo que fez!")
        sleep(2)
	
        monstro = []
        Crocodilo_gigante(monstro)
	
        resultado = batalha(personagem, monstro, habilidades, bolsa)
        if(resultado == 0):
                exit(0)

        else:
                print("\n" + nome[0] + ":")
                print("    Parece que meu trabalho acabou por aqui.")
                sleep(2)
                print("    Levarei esta morte comigo para me lembrar o pelo que estou lutando.")
                sleep(2)
                print("\nVocê encontrou a chave do 2º andar")
                sleep(2)
                inventario.append("Chave02")
                print("Chave do 2º andar adicionada ao inventário")
                sleep(2)
                salvar_jogo(personagem, nome, inventario, habilidades, itens, bolsa)

###############################################################################################################	

def sala_controle(personagem, nome, habilidades, chave, condicao, voltas, bolsa):
	print("\n****************************************************************")
	print("\n\n Sala abandonada\n\n")
	print("****************************************************************\n")
	if(voltas[4] == 0):
		monstro1 = []
		monstro2 = []
		monstro3 = []
				
		morcego(monstro1)
		morcego(monstro2)
		morcego(monstro3)
		
		resultado = batalha_Vs3(personagem, monstro1, monstro2, monstro3, habilidades, bolsa)
		
		
		del monstro1[:]
		del monstro2[:]
		del monstro3[:]
		
		rato(monstro1)
		morcego(monstro2)
		rato(monstro3)
		
		resultado = batalha_Vs3(personagem, monstro1, monstro2, monstro3, habilidades, bolsa)
		if(resultado == 0):
			print("\nVocê morreu!")
			exit(0)
		
		
		if(condicao[0] == 0):
			print("\n****************************************************************")
			print("\n" + nome[0] + ":")
			print("    Parece ser uma especie de sala de controle...")
		
		elif(condicao[0] == 1):
			print("\n****************************************************************")
			print("\n" + nome[0] + ":")
			print("    A sala de controle deve ser aqui...")
	
		voltas[4] = 1
	
	decisao = "0"
	while(decisao != "1" and decisao != "2"):
		print("\nDecisão: \n1 - Usar a alavanca \n2 - Seguir sem usar a alavanca")
		decisao = input("R: ")
		
		if(decisao == "1"):
			print("\nUma porta se abriu em algum lugar.\n")
			sleep(2)
			print("Barulho sinistro: AAAAAARRRRRRRR!!!")
			sleep(2)
			print(nome[0] + ":")
			print("    Que barulho foi este?")
			sleep(2)
			chave[0] = 1
			
###############################################################################################################	

def tunel_sul(personagem, nome, habilidades, voltas, bolsa):
	print("\n****************************************************************")
	print("\n\n Túnel Sul\n\n")
	print("****************************************************************\n")
	if(voltas[3] == 0):
		monstro1 = []
		monstro2 = []
		monstro3 = []
				
		rato(monstro1)
		rato(monstro2)
		rato(monstro3)
					
		resultado = batalha_Vs3(personagem, monstro1, monstro2, monstro3, habilidades, bolsa)
		if(resultado == 0):
			print("\nVocê morreu!")
			exit(0)
		
		voltas[3] = 1
		
###############################################################################################################	

def tunel_esquerdo(personagem, nome, habilidades, voltas, bolsa):
	print("\n****************************************************************")
	print("\n\n Túnel Esquerdo\n\n")
	print("****************************************************************\n")
	if(voltas[1] == 0):
                print(nome[0] + ":")
                print("    Estou vendo uma luz a frente...")                
                sleep(2)

                decisao = "@"
                while(decisao.isalnum() == False):
                        try:
                                print("\nDecisão: ")
                                print("1 - Investigar")
                                print("2 - Não investigar")
                                decisao = input("\nR: ")

                                if(decisao == "1"):
                                        print("\n" + nome[0] + ":")
                                        print("    Quem esta ai?")
                                        sleep(2)

                                        print("\n????")
                                        print("    Eu é que pergunto, quem é você?")
                                        sleep(2)

                                        print("\n" + nome[0] + ":")
                                        print("    Me chamo %s, estou em busca da segunda chave do portal!" % nome[0])
                                        sleep(2)

                                        print("\n????")
                                        print("    Porque não disse logo? Me chamo Mario, cuido destes esgotos a ")
                                        sleep(2)
                                        print("    40 anos. Já vi muitos de vocês passaram por aqui!")
                                        sleep(2)

                                        print("\n" + nome[0] + ":")
                                        print("    40 anos? Então o Sr pode me dizer onde encontrar a chave?")
                                        sleep(2)

                                        print("\nMario:")
                                        print("    Só posso lhe dizer o mesmo que disse para os outros, não ande por ai sozinho")
                                        sleep(2)
                                        print("    uma criatura monstruosa caminha por estes túneis.")
                                        sleep(2)

                                        print("\n" + nome[0] + ":")
                                        print("    Pode deixar, eu sei me cuidar.")
                                        sleep(2)

                                        print("\nMario:")
                                        print("    Depois não diga que eu não avisei.")
                                        sleep(2)
                                        print("    Mas já que esta por aqui, você poderia eliminar os monstros para mim?")
                                        sleep(2)

                                        print("\n" + nome[0] + ":")
                                        print("    Claro! Nos vemos por ai.")
                                        sleep(2)

                                else:
                                        return 0

                        except IndexError:
                                print("\nEscolha uma opção válida")
                                sleep(2)
                                decisao = "@"
                
                monstro1 = []
                monstro2 = []
				
                besouro(monstro1)
                besouro(monstro2)
					
                resultado = batalha_Vs2(personagem, monstro1, monstro2, habilidades, bolsa)
                if(resultado == 0):
                        print("\nVocê morreu!")
                        exit(0)
			
                voltas[1] = 1
		
###############################################################################################################	

def tunel_esquerdo_N2(personagem, nome, habilidades, voltas, bolsa):
	print("\n****************************************************************")
	print("\n\n Túnel Esquerdo N2\n\n")
	print("****************************************************************\n")
	if(voltas[2] == 0):
		monstro1 = []
		monstro2 = []
		monstro3 = []
				
		lesma(monstro1)
		lesma(monstro2)
		lesma(monstro3)
					
		resultado = batalha_Vs3(personagem, monstro1, monstro2, monstro3, habilidades, bolsa)
		if(resultado == 0):
			print("\nVocê morreu!")
			exit(0)
		
		voltas[2] = 1
	
###############################################################################################################	

def andar_02(personagem, nome, inventario, habilidades, itens, bolsa):
        voltas = [0,0,0,0,0,0]
        chave = [0]
        condicao = [0]
        decisao = "0"
        contador = 0
        while(decisao != "1"):
                print("\n****************************************************************")
                print("\n\n Esgotos \n\n")
                print("****************************************************************\n")
                sleep(3)
                if(voltas[0] == 0):	
                        print(nome[0] + ":")
                        print("    Não consigo ver nada! E este cheiro, parece que mataram alguém aqui!")
                        print("    Esta tão escuro que nem consigo ver um passo a minha frente...")
                        sleep(4)
			
                        decisao = input("\nDecisão: \n1 - Tatear pelo escuro \nR: ")
                        decisao2 = "0"
                        while(decisao2 != "1"):
                                decisao2 = input("\nDecisão: \n1 - Tatear pelo escuro \nR: ")
				
                                if(decisao == "1"):
                                        print("\nTocha encontrada.")
			
                        print("\n" + nome[0] + ":")
                        print("    Ótimo, uma tocha. Vamos ver o que estou perdendo.")
                        sleep(3)
                        print("\nRuidos de tocha acendendo")
                        sleep(2)
                        print("\n    Um esgoto? Que som é esse?")
                        sleep(3)
			
                        monstro1 = []
                        monstro2 = []
                        monstro3 = []
				
                        morcego(monstro1)
                        morcego(monstro2)
                        morcego(monstro3)
				
				
                        resultado = batalha_Vs3(personagem, monstro1, monstro2, monstro3, habilidades, bolsa)
                        if(resultado == 0):
                                print("Você morreu!")
                                exit(0)

                        elif(resultado == 1):
                                print(nome + ":")
                                print("    Criaturas malditas.")
		
		
        decisao2 = "0"
        while(decisao2 != "1" and decisao2 != "2" and decisao2 != "3"):
                print("\nDecisão: \n1 - Oeste \n2 - Sul \n3 - Menu Personagem")
                decisao2 = input("R: ")
		
                if(decisao2 == "1"):
                        resposta = tunel_esquerdo(personagem, nome, habilidades, voltas, bolsa)
                        if(resposta == 0):
                                decisao2 = "0"
			
                        decisao3 = "0"
                        while(decisao3 != "1" and decisao3 != "2" and decisao3 != "3" and decisao3 != "4" and decisao2 == "1"):
                                if(chave[0] == 1 and contador == 0):
                                        print("\nRastro de sangue encontrado.")
                                        sleep(2)
                                        print("\n" + nome[0] + ":")
                                        print("    Será que todo esse sangue tem relação com aquele barulho?")
                                        sleep(2)
                                        print("    Espero que o Mario esteja bem.")
                                        sleep(2)

                                        print("\n????")
                                        print("    AAAHHHH")
                                        sleep(2)

                                        print("\n" + nome[0] + ":")
                                        print("    Um grito? Devo me apressar!")
                                        sleep(2)

                                        contador = 1
                                                
                                print("Decisão: \n1 - Oeste \n2 - Sul \n3 - Leste \n4 - Menu Personagem")
                                decisao3 = input("R: ")
				
                                if(decisao3 == "1"):
                                        tunel_esquerdo_N2(personagem, nome, habilidades, voltas, bolsa)
					
                                        decisao6 = "0"
                                        while(decisao6 != "1"):
                                                print("\n" + nome[0] + ":")
                                                print("    Sem saída")
                                                print("\nDecisão: \n1 - Leste")
                                                decisao6 = input("R: ")
						
                                                if(decisao6 == "1"):
                                                        decisao3 = "0"
					
                                elif(decisao3 == "2"):
                                        sala_controle(personagem, nome, habilidades, chave, condicao, voltas, bolsa)
                                        
					
                                        decisao4 = "0"
                                        while(decisao4 != "1" and decisao4 != "2"):
                                                print("Decisão: \n1 - Norte \n2 - Tomar Poção")
                                                decisao4 = input("R: ")
						
                                                if(decisao4 == "1"):
                                                        decisao3 = "0"
						
                                                elif(decisao4 == "2"):
                                                        tomar_pot(personagem, bolsa)
                                                        decisao4 = "0"
						
                                elif(decisao3 == "3"):
                                        decisao2 = "0"

                                elif(decisao3 == "4"):
                                        menuPersonagem(personagem, habilidades, itens, nome, bolsa)
                                        decisao3 = "0"
					
                elif(decisao2 == "2"):
                        tunel_sul(personagem, nome, habilidades, voltas, bolsa)
			
                        decisao5 = "0"
                        while(decisao5 != "1" and decisao5 != "2" and decisao5 != "3"):
                                print("\nDecisão: \n1 - Norte \n2 - Sala do Chefe \n3 - Menu  Personagem")
                                decisao5 = input("R: ")
				
                                if(decisao5 == "1"):
                                        decisao2 = "0"
					
                                elif(decisao5 == "2"):
                                        if(chave[0] != 1):
                                                print("\nA porta do Chefe esta fechada.")
                                                sleep(2)
                                                print("\nEncontre o sistema de controle para abri-la")
                                                sleep(2)
                                                condicao[0] = 1
                                                decisao5 = "0"
						
                                        else:
                                                sala_do_boss02(personagem, nome, inventario, habilidades, itens, bolsa)
                                                
                                elif(decisao5 == "3"):
                                        menuPersonagem(personagem, habilidades, itens, nome, bolsa)
                                        decisao5 = "0"

                elif(decisao2 == "3"):
                        menuPersonagem(personagem, habilidades, itens, nome, bolsa)
                        decisao2 = "0"
		
		
		
		
			
