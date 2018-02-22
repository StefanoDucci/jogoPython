# encoding: UTF-8
from Batalha import *
from Monstros import *
from Quest import *
from time import sleep
from Opcoes import salvar_jogo
from MenusPersonagem import menuPersonagem

###############################################################################################################

def sala_do_chefe06(personagem, nome, inventario, habilidades, itens, bolsa):
        print("\n****************************************************************")
        print("\n\n Sala do Chefe \n\n")
        print("****************************************************************\n")
        sleep(3)

        print("\n" + nome[0] + ":")
        print("    Essa sala é enorme!")
        sleep(2)

        print("\nRainha Serpente:")
        print("    Quem se atreve a atrapalhar o meu desssscanço?")
        sleep(2)
        print("    Você é tão inocente para entrar aqui asssssim?")
        sleep(2)

        print("\n" + nome[0] + ":")
        print("    Estou atrás da chave do portal.")
        sleep(2)

        print("\nRainha Serpente:")
        print("    Vocêsss tolosss não se canssssam de morrer por isssso? Sisisisi")
        sleep(2)

        print("\n" + nome[0] + ":")
        print("    Desculpe, mas eu não pretendo morrer!")
        sleep(2)

        print("\nRainha Serpente:")
        print("    Sisisisi. Venham meusss bebesss, é hora do jantar!")
        sleep(2)

        monstro1 = []
        monstro2 = []
        monstro3 = []

        anaconda(monstro1)
        rainha_serpente(monstro2)
        anaconda(monstro3)

        resultado = batalha_Vs3(personagem, monstro1, monstro2, monstro3, habilidades, bolsa)
        if(resultado == 0):
                print("\nRainha Serpente:")
                print("    Sisisisi. Não deixem sobrar nada filhasss!")
                exit(0)


        print("\n" + nome[0] + ":")
        print("    A força dessa rainha era enorme, vou precisar de treinamento para continuar avançando!")
        sleep(2)

        print("\nVocê recebeu a Chave do 6º andar.")
        sleep(3)

        inventario.append("Chave06")

        print("\nChave do 6º andar adicionada ao inventario.")
        sleep(3)


def andar_06(personagem, nome, inventario, habilidades, itens, bolsa):
    chave = [0]
    voltas = [0,0,0,0,0]
    monstro1 = []
    monstro2 = []
    monstro3 = []

    print("\n****************************************************************")
    print("\n\n Entrada da Caverna \n\n")
    print("****************************************************************\n")
    sleep(3)

    print("\n" + nome[0] + ":")
    print("    Somente uma caverna a vista, ela parece descer bem fundo, não vejo nada alem de escuridão.")
    sleep(3)
    print("    Por sorte eu mantive esta tocha sempre por perto...")
    sleep(2)

    decisao = "@"
    while(decisao.isalnum() == False):
        print("\nDecisão: \n1 - Entrar na caverna \n2 - Menu de Personagem")
        decisao = input("R: ")

        if(decisao == "1"):
            decisao2 = "@"
            while(decisao2.isalnum() == False):
                print("\n****************************************************************")
                print("\n\n Bifurcação \n\n")
                print("****************************************************************\n")
                sleep(2)
                
                print("\nDecisão: \n1 - Norte \n2 - Sul \n3 - Menu de Personagem")
                decisao2 = input("R: ")

                if(decisao2 == "1"):
                    print("\n****************************************************************")
                    print("\n\n Norte da Caverna \n\n")
                    print("****************************************************************\n")
                    sleep(2)

                    while(voltas[0] == 0):                            
                        print("\n" + nome[0] + ":")
                        print("    Essa não... cobras...")
                        sleep(2)

                        del monstro1[:]
                        del monstro2[:]
                        del monstro3[:]

                        serpente(monstro1)
                        serpente(monstro2)
                        serpente(monstro3)

                        resultado = batalha_Vs3(personagem, monstro1, monstro2, monstro3, habilidades, bolsa)
                        if(resultado == 0):
                                print("\nVocê será lentamente devorado por serpentes.")
                                exit(0)
                        else:
                                voltas[0] = 1
                            

                    decisao3 = "@"
                    while(decisao3.isalnum() == False):
                        print("\nDecisão: \n1 - Oeste \n2 - Sul \n3 - Menu de Personagem")
                        decisao3 = input("R: ")

                        if(decisao3 == "1"):
                            decisao4 = "@"
                            while(decisao4.isalnum() == False):
                                print("\n****************************************************************")
                                print("\n\n Noroeste da Caverna \n\n")
                                print("****************************************************************\n")
                                sleep(2)

                                while(voltas[1] == 0):                            
                                        print("\n" + nome[0] + ":")
                                        print("    Que barulho de ossos quebrando é esse...?")
                                        sleep(2)
                                        print("    OLHA O TAMANHO DESSA COBRA!!!")
                                        sleep(2)

                                        del monstro1[:]
                                        
                                        anaconda(monstro1)
                                        
                                        resultado = batalha(personagem, monstro1, habilidades, bolsa)
                                        if(resultado == 0):
                                                print("\nVocê foi engolido inteiro.")
                                                exit(0)
                                        else:
                                                voltas[1] = 1

                                print("\nDecisão: \n1 - Oeste \n2 - Leste \n3 - Meu de Personagem")
                                decisao4 = input("R: ")

                                if(decisao4 == "1"):
                                    decisao5 = "@"
                                    while(decisao5.isalnum() == False):
                                        print("\n****************************************************************")
                                        print("\n\n Extremo Noroeste da Caverna \n\n")
                                        print("****************************************************************\n")
                                        sleep(2)

                                        if(voltas[2] == 0):
                                                print("\n" + nome[0] + ":")
                                                print("    Essa parece ser a última sala...")
                                                sleep(2)

                                                print("\nGuardiões de Pedra:")
                                                print("    Não de mas nenhum passo, mortal!")
                                                sleep(2)
                                                print("    Essa caverna pertence a Rainha Serpente, suma daqui!")
                                                sleep(2)

                                                print("\n" + nome[0] + ":")
                                                print("    Não posso, eu preciso ir até o final disso.")
                                                sleep(2)

                                                print("\nGuardiões de Pedra:")
                                                print("    Não deixaremos que toque na jóia de nossa Rainha.")
                                                sleep(2)

                                                del monstro1[:]
                                                del monstro2[:]

                                                guardiao_pedra(monstro1)
                                                guardiao_pedra(monstro2)

                                                resultado = batalha(personagem, monstro1, habilidades, bolsa)
                                                if(resultado == 0):
                                                        print("\nGuardião de Pedra:")
                                                        print("    Ninguém passara!")
                                                        sleep(2)
                                                        exit(0)
                                                        
                                                resultado = batalha(personagem, monstro2, habilidades, bolsa)
                                                if(resultado == 0):
                                                        print("\nGuardião de Pedra:")
                                                        print("    Ninguém passara!")
                                                        sleep(2)
                                                        exit(0)

                                                print("\n" + nome[0] + ":")
                                                print("    Esses caras eram durões...")
                                                voltas[2] = 1
                                                sleep(2)
                                        
                                        if(chave[0] == 0):
                                                print("\n****************************************************************")
                                                print("\nDecisão: \n1 - Pegar Jóia \n2 - Leste \n3 - Menu de Personagem")
                                                decisao5 = input("R: ")

                                                if(decisao5 == "1"):
                                                    chave[0] = 1                                                    

                                                elif(decisao5 == "2"):
                                                    decisao4 = "@"

                                                elif(decisao5 == "3"):
                                                    menuPersonagem(personagem, habilidades, itens, nome, bolsa)
                                                    decisao5 = "@"

                                                else:
                                                    decisao5 = "@"
                                                    print("\n\nSistema: Por favor, escolha somente números em suas decisões.\n\n")
                                                    sleep(3)
                                                    
                                        if(chave[0] == 1):
                                                print("\n****************************************************************")
                                                print("\nDecisão: \n1 - Leste \n2 - Menu de Personagem")
                                                decisao5 = input("R: ")

                                                if(decisao5 == "1"):
                                                    decisao4 = "@"

                                                elif(decisao5 == "2"):
                                                    menuPersonagem(personagem, habilidades, itens, nome, bolsa)
                                                    decisao5 = "@"

                                                else:
                                                    decisao5 = "@"
                                                    print("\n\nSistema: Por favor, escolha somente números em suas decisões.\n\n")
                                                    sleep(3)
                                                                                

                                elif(decisao4 == "2"):
                                    decisao3 = "@"

                                elif(decisao4 == "3"):
                                    menuPersonagem(personagem, habilidades, itens, nome, bolsa)
                                    decisao4 = "@"

                                else:
                                    decisao4 = "@"
                                    print("\n\nSistema: Por favor, escolha somente números em suas decisões.\n\n")
                                    sleep(3)

                        elif(decisao3 == "2"):
                            decisao2 = "@"

                        elif(decisao3 == "3"):
                            menuPersonagem(personagem, habilidades, itens, nome, bolsa)
                            decisao3 = "@"

                        else:
                            decisao3 = "@"
                            print("\n\nSistema: Por favor, escolha somente números em suas decisões.\n\n")
                            sleep(3)
                            

                elif(decisao2 == "2"):
                    decisao6 = "@"
                    while(decisao6.isalnum() == False):
                        print("\n****************************************************************")
                        print("\n\n Sul da Caverna \n\n")
                        print("****************************************************************\n")
                        sleep(2)

                        while(voltas[3] == 0):                            
                                print("\n" + nome[0] + ":")
                                print("    Já estou começando a odiar cobras!")
                                sleep(2)

                                del monstro1[:]
                                del monstro2[:]
                                del monstro3[:]

                                vibora(monstro1)
                                vibora(monstro2)
                                vibora(monstro3)

                                resultado = batalha_Vs3(personagem, monstro1, monstro2, monstro3, habilidades, bolsa)
                                if(resultado == 0):
                                        print("\nVocê será lentamente devorado por viboras.")
                                        exit(0)
                                else:
                                        voltas[3] = 1
                        
                        print("\nDecisão: \n1 - Oeste \n2 - Norte \n3 - Menu de Personagem")
                        decisao6 = input("R: ")

                        if(decisao6 == "1"):            
                            decisao7 = "@"
                            while(decisao7.isalnum() == False):
                                print("\n****************************************************************")
                                print("\n\n Suldoeste da Caverna \n\n")
                                print("****************************************************************\n")
                                sleep(2)

                                while(voltas[4] == 0):                            
                                        print("\n" + nome[0] + ":")
                                        print("    Claro... o que mais teria aqui?")
                                        sleep(2)

                                        del monstro1[:]
                                        del monstro2[:]
                                        del monstro3[:]

                                        vibora(monstro1)
                                        vibora(monstro2)
                                        vibora(monstro3)

                                        resultado = batalha_Vs3(personagem, monstro1, monstro2, monstro3, habilidades, bolsa)
                                        if(resultado == 0):
                                                print("\nVocê será lentamente devorado por viboras.")
                                                exit(0)
                                        else:
                                                voltas[4] = 1
                                
                                print("\nDecisão: \n1 - Sala do Chefe \n2 - Leste \n3 - Menu de Personagem")
                                decisao7 = input("R: ")

                                if(decisao7 == "1"):
                                    if(chave[0] == 1):
                                        decisao8 = "@"
                                        while(decisao8.isalnum() == False):
                                            print("\nDecisão: \n1 - Colocar Jóia \n2 - Voltar")
                                            decisao8 = input("R: ")

                                            if(decisao8 == "1"):
                                                sala_do_chefe06(personagem, nome, inventario, habilidades, itens, bolsa)

                                            elif(decisao8 == "2"):
                                                decisao7 = "@"

                                            else:
                                                decisao8 = "@"
                                                print("\n\nSistema: Por favor, escolha somente números em suas decisões.\n\n")
                                                sleep(3)
                                                                                    
                                    else:
                                        print("\n" + nome[0] + ":")
                                        print("    Parece que esta faltando algo nesta porta.")
                                        sleep(3)
                                        decisao7 = "@"

                                elif(decisao7 == "2"):
                                    decisao6 = "@"

                                elif(decisao7 == "3"):
                                    menuPersonagem(personagem, habilidades, itens, nome, bolsa)
                                    decisao7 = "@"

                                else:
                                    decisao7 = "@"
                                    print("\n\nSistema: Por favor, escolha somente números em suas decisões.\n\n")
                                    sleep(3)
                                    

                        elif(decisao6 == "2"):
                            decisao2 = "@"

                        elif(decisao6 == "3"):
                            menuPersonagem(personagem, habilidades, itens, nome, bolsa)
                            decisao6 = "@"

                        else:
                            decisao6 = "@"
                            print("\n\nSistema: Por favor, escolha somente números em suas decisões.\n\n")
                            sleep(3)
                        

                elif(decisao2 == "3"):
                    menuPersonagem(personagem, habilidades, itens, nome, bolsa)
                    decisao2 = "@"

                else:
                    decisao2 = "@"
                    print("\n\nSistema: Por favor, escolha somente números em suas decisões.\n\n")
                    sleep(3)
            

        elif(decisao == "2"):
            menuPersonagem(personagem, habilidades, itens, nome, bolsa)
            decisao = "@"

        else:
            decisao = "@"
            print("\n\nSistema: Por favor, escolha somente números em suas decisões.\n\n")
            sleep(3)
