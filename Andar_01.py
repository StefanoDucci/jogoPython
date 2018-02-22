# encoding: UTF-8
from Batalha import *
from Monstros import *
from Quest import *
from Opcoes import salvar_jogo

###############################################################################################################	

def sala_do_boss01(personagem, inventario, habilidades, itens, nome, bolsa):
    print("\n****************************************************************")
    print("Treinador de féras:")
    print("    Vejo que conseguiu passar por meus bixinhos...")
    sleep(3)
    print("\n" + nome[0] + ":")
    print("    Não se pode chamar aquilo de desafio.")
    sleep(3)
    print("\nTreinador de féras:")
    print("    Muito bem então, mas só atitude não lhe dará essa chave aqui...")
    sleep(3)
    print("    Vejamos o que você pode fazer.")
    sleep(2)
	
    monstro1 = []
    monstro2 = []
    monstro3 = []
	
    javali(monstro1)
    Senhor_do_campo(monstro2)
    lobo(monstro3)
    
	
    resultado = batalha_Vs3(personagem, monstro1, monstro2, monstro3, habilidades, bolsa)
    if(resultado == 0):
        print("Treinador de féras:")
        print("\n\tHahahahaha. Se você não consegue passar nem do primeiro andar, imagine os outros noventa e nove")
        print("\n****************************************************************")   
        exit(0)

    print("\n****************************************************************")      
    print("\n" + nome[0] + ":")    
    print("    O primeiro já foi... Faltam noventa e nove.")
    sleep(3)	
    print("\nVocê recebeu a chave do 1º Andar")
    inventario.append("Chave01")
    sleep(3)
    print("\nChave do 1º Andar adicionado ao inventário")
    sleep(3)
	
    
    salvar_jogo(personagem, nome, inventario, habilidades, itens, bolsa)
    
	
###############################################################################################################	

def centro(personagem, nome, habilidades, inventario, itens, bolsa):
	print("\n****************************************************************")
	print("\n\n Sala do Chefe 01\n\n")
	print("****************************************************************\n")
	sala_do_boss01(personagem, inventario, habilidades, itens, nome, bolsa)


###############################################################################################################	
				
def sudoeste(personagem, nome, habilidades, voltas, bolsa):
	print("\n****************************************************************")
	print("\n\n Parte Sudoeste do Campo\n\n")
	print("****************************************************************\n")
	
	if(voltas[5] == 0):
            print("\n" + nome[0] + ":")
            print("    Acho que sou o inimigo em comum aqui...")
		
            monstro1 = []
            monstro2 = []
		
            lobo(monstro1)
            javali(monstro2)
		
            resultado = batalha_Vs2(personagem, monstro1, monstro2, habilidades, bolsa)
            if(resultado == 0):
                    print("Você foi pisoteado por javalis e comido por lobos")
                    exit(0)
            voltas[5] = 1

###############################################################################################################	
	
def sudeste(personagem, nome, habilidades, voltas, bolsa):
	print("\n****************************************************************")
	print("\n\n Parte Sudeste do Campo\n\n")
	print("****************************************************************\n")
	
	if(voltas[3] == 0):
            print(nome[0] + ":")
            print("    Quanto mais ao Sul eu vou, mais javalis aparecem.")
            sleep(3)
		
	
            monstro1 = []    
            monstro2 = []
            monstro3 = []
		
            javali(monstro1)
            javali(monstro2)
            javali(monstro3)
		
            resultado = batalha_Vs3(personagem, monstro1, monstro2, monstro3, habilidades, bolsa)
            if(resultado == 0):
                print("Você foi pisoteado por javalis.")
                exit(0)
            voltas[3] = 1

###############################################################################################################	
	
def oeste(personagem, nome, habilidades, voltas, bolsa):
	print("\n****************************************************************")
	print("\n\n Parte Oeste do Campo\n\n")
	print("****************************************************************\n")
	sleep(3)
	
	if(voltas[2] == 0):
		print("\n" + nome[0] + ":")
		print("    Essa área parece dominada por lobos.")
		sleep(3)
		
		monstro1 = []    
		monstro2 = []
		monstro3 = []
		
		lobo(monstro1)
		lobo(monstro2)
		lobo(monstro3)
		
		resultado = batalha_Vs3(personagem, monstro1, monstro2, monstro3, habilidades, bolsa)
		if(resultado == 0):
			print("Você foi comido por lobos")
			exit(0)

		print("\n" + nome[0] + ":")
		print("    Para qual lado agora?")
		sleep(2)
		voltas[2] = 1

###############################################################################################################	
		
def leste(personagem, nome, habilidades, voltas, bolsa):
	print("\n****************************************************************")
	print("\n\n Parte Leste do Campo\n\n")
	print("****************************************************************\n")
	
	if(voltas[0] == 0):
		print(nome[0] + ":")
		print("    Ha lobos por toda parte aqui.")
		sleep(3)
		
	
		monstro1 = []
		monstro2 = []
		monstro3 = []
		
		lobo(monstro1)
		lobo(monstro2)
		lobo(monstro3)
		
		resultado = batalha_Vs3(personagem, monstro1, monstro2, monstro3, habilidades, bolsa)
		if(resultado == 0):
			print("Você foi comido por lobos")
			exit(0)
		voltas[0] = 1
		
###############################################################################################################	
		
def andar_01(personagem, nome, inventario, habilidades, itens, bolsa):
    voltas = [0,0,0,0,0,0]
    decisao = "0"
    while(decisao != "1" and decisao != "2" and decisao != "3"):
        print("\n****************************************************************")
        print("\n\n Campo Aberto\n\n")
        print("****************************************************************\n")
        sleep(3)
		
        if(voltas[1] == 0):
            print(nome[0] + ":")
            print("    Somente um campo deserto, nada parece fora do comum...")
            print("    A NÃO SER POR ESSES JAVALIS CORRENDO NA MINHA DIREÇÃO!!!")
            sleep(3)
			
            monstro1 = []
            monstro2 = []
            javali(monstro1)
            javali(monstro2)
			
            resultado = batalha_Vs2(personagem, monstro1, monstro2, habilidades, bolsa)
            if(resultado == 0):
                print("Você morreu pisoteado por Javalis")
                exit(0)			
			
            print("\n" + nome[0] + ":")
            print("    É melhor tomar cuidado daqui para a frente.")
            sleep(3)
            voltas[1] = 1
			
        decisao = "0"
		
        print("\n****************************************************************")
        decisao = input("\nDecisao: \n1 - Ir para Oeste \n2 - Ir para Leste \n3 - Tomar Poção \nR: ")

        if(decisao == "1"):
            oeste(personagem, nome, habilidades, voltas, bolsa)
            
            decisao2 = "0"
            while(decisao2 != "1" and decisao2 != "2" and decisao2 != "3"):
                print("\n****************************************************************")
                decisao2 = input("\nDecisao: \n1 - Seguir para o sul \n2 - Seguir para o leste \n3 - Tomar Poção \nR: ")
                    
                if(decisao2 == "1"):
                    sudoeste(personagem, nome, habilidades, voltas, bolsa)
                        
                    decisao3 = "0"
                    while(decisao3 != "1" and decisao3 != "2" and decisao3 != "3"):
                        print("\n****************************************************************")
                        decisao3 = input("\nDecisao: \n1 - Sala do Chefe \n2 - Seguir para o norte \n3 - Tomar Poção \nR: ")
                            
                        if(decisao3 == "1"):
                            centro(personagem, nome, habilidades, inventario, itens, bolsa)						
						
                        elif(decisao3 == "2"):
                            decisao2 = "0"
						
                        elif(decisao3 == "3"):
                            tomar_pot(personagem, bolsa)
                            decisao3 = "0"
						
                elif(decisao2 == "2"):
                    decisao = "0"
		
                elif(decisao2 == "3"):
                    tomar_pot(personagem, bolsa)
                    decisao2 = "0"
				
        elif(decisao == "2"):
            leste(personagem, nome, habilidades, voltas, bolsa)
			
            decisao4 = "0"
            while(decisao4 != "1" and decisao4 != "2" and decisao4 != "3"):
                print("\n****************************************************************")
                decisao4 = input("\nDecisao: \n1 - Seguir para o sul \n2 - Seguir para o oeste \n3 - Tomar Poção \nR: ")
					
                if(decisao4 == "1"):
                    sudeste(personagem, nome, habilidades, voltas, bolsa)
					
                    decisao5 = "0"
                    while(decisao5 != "1" and decisao5 != "2" and decisao5 != "3"):
                        print("\n****************************************************************")
                        decisao5 = input("\nDecisao: \n1 - Sala do Chefe \n2 - Seguir para o norte \n3 - Tomar Poção \nR: ")
						
                        if(decisao5 == "1"):
                            centro(personagem, nome, habilidades, inventario, itens, bolsa)
						
                        elif(decisao5 == "2"):
                            decisao4 = "0"
						
                        elif(decisao5 == "3"):
                            tomar_pot(personagem, bolsa)
                            decisao5 = "0"
						
						
                elif(decisao4 == "2"):
                    decisao = "0"
				
                elif(decisao4 == "3"):
                    tomar_pot(personagem, bolsa)
                    decisao4 = "0"
					
        elif(decisao == "3"):
            tomar_pot(personagem, bolsa)
            decisao = "0"
