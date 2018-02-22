# encoding: UTF-8
from Opcoes import salvar_jogo
from time import sleep
from Armas import *
from Armadura import *
from Habilidades import *
from Portal import Portal
from MenusPersonagem import menuPersonagem
from Quest import pousada
from Lojista import Alojista
from Alquimista import alquimista
from Ferreiro import ferreiro
from Arena import torneios
from Pets import pets
from torreChefe import torre

## Testes
from Batalha import *
from Monstros import *
##

#############################################################################################################################

def arena(personagem, nome, inventario, habilidades, itens, bolsa, ponto):
    ponto = len(itens)
    print("\n****************************************************************")
    print("\nGladiador:")
    print("    Bem vindo a Arena. Aqui você poderá enfrentar competidores e outros")
    print("    desafios em troca de dinheiro.")
    if(ponto < 3):
        print("    A Arena só estará disponível a partirdo terceiro andar.")
        sleep(5)
    else:
        torneios(personagem, nome, inventario, habilidades, itens, bolsa)
        
#############################################################################################################################

def cidade_inicial(personagem, inventario, nome, habilidades, itens, bolsa):
    print("\n****************************************************************")
    print("\n\nCidade do Portal\n\n")
    print("****************************************************************\n")
    sleep(2)
    ponto = len(inventario)
    
    if(ponto == 0):
        print("Mago Sábio:")
        print("    Bem vindo a Mundo, %s!" % nome[0])
        sleep(3)
        print("\n    Este mundo foi dividido em cem andares. Cada andar é guardado por um Chefe,")
        print("    o qual você deverá derrotar para avançar. Alguns Chefes ")
        print("    são homens de confiançado Senhor Conquistador, outos são ")
        print("    criaturas monstruosas que estão sobre o porder dele.")
        sleep(7)
        #pets(personagem, nome)
        print("\n    Esta é a Cidade do Portal, o unico lugar seguro que restou.")
        print("    Toda vez que derrotar um Chefe, você será teletransportado ")
        print("    para este local e o Portal dará acesso ao próximo andar.")
        sleep(5)
        print("\n    Fale com o Lojista para receber seus primeiros itens.")
        sleep(2)
        
        
        decisao = "0"
        lojista = "0"
        portal = "0"
        while(decisao != "1" and decisao != "2" and decisao != "3"):
            print("\n****************************************************************")
            decisao = input("\nDecisao: \n1 - Falar com Lojista \n2 - Ir à arena \n3 - Ir ao portal \nR: ")
            
            if(decisao == "2"):
                arena(personagem, nome, inventario, habilidades, itens, bolsa, ponto)
                decisao = "0"
                
            elif(decisao == "3"):
                print("\n****************************************************************")
                if(portal == "0"):
                    print("\nMago Sábio:")
                    print("    Você ainda não pode fazer isso!")
                    sleep(2)
                    decisao = "0"
                else:
                    if(personagem[40] != 4):
                        print("Mago Sábio:")
                        print("    Antes de ir, use seu ponto de habilidade.")
                        print("    Basta escolher o número da habilidade que deseja evoluir e confirmar.")
                        print("    Depois é só escolher um atalho para ela.")
                        sleep(5)
                        
                        evoluir_habilidades(personagem, habilidades, 1)

                    print("\nMago Sábio:")
                    print("    Muito bem, agora você esta pronto para enfrentar o primeiro andar!")
                    sleep(2)
                                        
                    Portal(personagem, nome, inventario, habilidades, itens, ponto, bolsa)
					
            elif(decisao == "1"):
                print("\n****************************************************************")
                if(lojista == "0"):
                    print("\nLojista: ")
                    print("    Olá, vejo que você é novo por aqui. Pegue esses equipamentos iniciais")
                    print("    para te ajudar.")
                    sleep(2)
                    arma = []
                    armadura = []
                    
                    arma_de_aprendiz(arma)
                    equipar_arma(arma, personagem)
                    
                    print("    Durante uma batalha, digite 1 e pressione enter para atacar.")
                    
                    armadura_aprendiz(armadura)
                    equipar_armadura(armadura, personagem)
                    
                    sleep(3)
                    print("    Pegue também algumas poções.")
                    sleep(2)
                    print("\nVocê recebeu poções.")
                    
                    bolsa[3] = bolsa[2]
                    bolsa[7] = bolsa[6]
                    
                    sleep(2)
                    print("\n    Durante a batalha, digite 2 e escolha a opção de Poção que desejar usar.")
                    sleep(2)
                    
                    lojista = "1"
                    
                else:
                    print("Lojista:")
                    print("    Eu já te dei os itens que você precisa, volte quando tiver dinheiro!")
                    sleep(2)
                
                decisao = "0"
                portal = "1"

    ponto = len(inventario)
    
    if(ponto == 1):
        print("Mago Sábio:")
        print("    Muito bem " + nome[0] + " vejo que conseguiu passar do primeiro andar!")
        print("    Com você do nosso lado, eu acredito que podemos vencer este mal.")
        sleep(2)
        print("    Explore um pouco de nossa cidade antes de ir para seu próximo desafio.")
        sleep(4)
	
    if(ponto >= 1):
        decisao = "0"
        while(decisao != "1" and decisao != "2" and decisao != "3" and decisao != "4" and decisao != "5" and decisao != "6" and decisao != "7" and decisao != "8" and decisao != "9" and decisao != "99"):
            decisao = input("\nDecisão \n1 - Menu de personagem \n2 - Lojista \n3 - Arena \n4 - Portal \n5 - Pousada \n6 - Alquimista \n7 - Ferreiro \n8 - Torre dos Chefes \n9 - Salvar \nR: ")
		
            if(decisao == "1"):
                menuPersonagem(personagem, habilidades, itens, nome, bolsa)
                decisao = "0"
			
            elif(decisao == "2"):
                Alojista(personagem, nome, itens, ponto, bolsa)
                decisao = "0"
			
            elif(decisao == "3"):
                arena(personagem, nome, inventario, habilidades, itens, bolsa, ponto)
                decisao = "0"
			
            elif(decisao == "4"):
                Portal(personagem, nome, inventario, habilidades, itens, ponto, bolsa)
                decisao = "0"

            elif(decisao == "5"):
                decisao = pousada(personagem, nome)

            elif(decisao == "6"):
                alquimista(personagem, nome, bolsa)
                decisao = "0"

            elif(decisao == "7"):
                ferreiro(personagem, nome)
                decisao = "0"

            elif(decisao == "8"):
                tentativa = torre(personagem, inventario, habilidades, itens, nome, bolsa)
                decisao = "0"
                
            elif(decisao == "9"):
                decisao2 = "0"

                while(decisao2 != "1" and decisao2 != "2"):
                    decisao2 = input("\nDeseja Salvar o jogo? \n1 - Sim \n2 - Não \nR: ")
                    if(decisao2 == "1"):
                        salvar_jogo(personagem, nome, inventario, habilidades, itens, bolsa)
                    decisao = "0"

            elif(decisao == "99"):
                chefe = []
                mob1 = []
                mob2 = []
                chefeTeste(chefe)
                lobo(mob1)
                lobo(mob2)
                
                batalhaChefe(personagem, chefe,mob1, mob2, habilidades, bolsa, nome)
			
