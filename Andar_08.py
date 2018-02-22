# ecoding: UTF-8

from Batalha import *
from Monstros import *
from Quest import *
from time import sleep
from Opcoes import salvar_jogo
from MenusPersonagem import menuPersonagem

###############################################################################

def mapa(local):
    print("\n        MAPA DO DESERTO \n  N\nO   L\n  S")
    if(local[0] == 1):
        print("            |X|")
    else:
        print("            | |")
    print("")

    if(local[1] == 1):
        print("      | | - |x| - | | - | | - | | - | |")
    elif(local[2] == 1):
        print("      | | - | | - |X| - | | - | | - | |")
    elif(local[3] == 1):
        print("      | | - | | - | | - |x| - | | - | |")
    elif(local[4] == 1):
        print("      | | - | | - | | - | | - |X| - | |")
    elif(local[5] == 1):
        print("      | | - | | - | | - | | - | | - |X|")
    elif(local[7] == 1):
        print("      |X| - | | - | | - | | - | | - | |")
    else:
        print("      | | - | | - | | - | | - | | - | |")
    print("")
    if(local[6] == 1):
        print("                                    |X|")
    else:
        print("                                    | |")


###############################################################################

def andar_08(personagem, nome, inventario, habilidades, itens, bolsa):
    chave = [0]
    voltas = [0,0,0,0,0,0,0,0]
    local = [0,0,0,0,0,0,0,0]
    monstro1 = []
    monstro2 = []
    monstro3 = []

    print("\n****************************************************************")
    print("\n" + nome[0] + ":")
    print("    Um deserto? Posso ver um ponto brilhante daqui.")
    sleep(2)
    print("    O que é isso enfiado na areia...")
    sleep(2)
    print("    Parece uma placa...")
    sleep(2)

    decisao = "@"
    while(decisao != "1"):
        print("\n****************************************************************")
        print("\nDecisão: \n1 - Limpar e ler a placa")
        decisao = input("R: ")

    print("\nPlaca:")
    print("    Território dos landrões do deserto. Fique longe!")
    sleep(2)

    print("\n" + nome[0] + ":")
    print("    Ladrões? Materei todos!")
    sleep(2)

    decisao2 = "@"
    while(decisao2.isalnum() == False):
        del local[:]
        local = [1,0,0,0,0,0,0,0]
        
        print("\n****************************************************************")
        print("Decisão: \n1 - Entrar no território dos ladrões \n2 - Mapa \n3 - Menu do Personagem")
        decisao2 = input("R: ")

        if(decisao2 == "1"):
            print("\n****************************************************************")
            print("                     Território dos Ladrões")                            
            print("\n****************************************************************")
            sleep(2)
                
            if(voltas[0] == 0):
                print("\n****************************************************************")
                print("\nLadrão:")
                print("     Ei você, me entregue tudo que você tem!")
                sleep(2)

                print("\n" + nome[0] + ":")
                print("     Tente tirar de mim, seu verme!")
                sleep(2)

                del monstro1[:]
                del monstro2[:]

                ladrao(monstro1)
                ladrao(monstro2)

                resultado = batalha_Vs2(personagem, monstro1, monstro2, habilidades, bolsa)

                if(resultado == 0):
                    print("\nLadrão:")
                    print("     Cheio de marra, pra nada...")
                    sleep(2)
                    exit(0)

                voltas[0] = 1
                            

            decisao3 = "@"
            while(decisao3.isalnum() == False):                                
                del local[:]
                local = [0,1,0,0,0,0,0,0]
                
                print("\n****************************************************************")
                print("\nDecisão: ")
                print("1 - Oeste \n2 - Leste \n3 - Mapa \n4 - Menu do Personagem")
                decisao3 = input("\nR: ")                            

                if(decisao3 == "1"):
                    print("\n****************************************************************")
                    print("                     Zona de Ventanias")
                    print("\n****************************************************************")
                    sleep(2)
                    
                    if(chave[0] == 0):
                        print("\n" + nome[0] + ":")
                        print("     Não consigo enchergar nada!! É melhor eu voltar.")
                        sleep(2)
                        decisao3 = "@"

                    else:
                        print("\n****************************************************************")
                        print("\n" + nome[0] + ":")
                        print("     Agora consigo ver, preciso agradecer a Minerva na volta.")
                        sleep(4)

                        decisao9 = "@"
                        while(decisao9.isalnum() == False):                                
                            del local[:]
                            local = [0,0,0,0,0,0,0,1]
                            
                            print("\n****************************************************************")
                            print("\nDecisão: ")
                            print("1 - Descer o alçapão \n2 - Leste \n3 - Mapa \n4 - Menu do Personagem")
                            decisao9 = input("\nR: ")

                            if(decisao9 == "1"):                                
                                print("\n****************************************************************")
                                print("\nHistoria:")
                                print("     As escadas me levaram a um tipo de camâra subterrânea.")
                                sleep(4)
                                print("     Depois de algum tempo seguindo um rio, me deparei com ")
                                sleep(4)
                                print("     quem só poderia ser o Chefe deste lugar.")
                                sleep(4)
                                
                                print("\n" + nome[0] + ":")
                                print("     Então é aqui que você andou se escondendo este tempo todo?")
                                sleep(4)

                                print("\nChefe dos Ladrões:")
                                print("     Este problema com a água não me deixa sair muito...")
                                sleep(3)
                                print("     glup glup glup glup")
                                sleep(3)
                                print("     AAHH, não posso ficar sem ela.")
                                sleep(3)

                                print("\n" + nome[0] + ":")
                                print("     Eu vim aqui pela Chave do Portal, de ela para mim.")                            
                                sleep(4)

                                print("\nChefe fos Ladrões:")
                                print("     Sinto muito mas, tenho mais medo do Senhor Conquistador do que de você!")
                                sleep(5)

                                print("\n" + nome[0] + ":")
                                print("     Vamos a luta então...")
                                sleep(4)

                                del monstro1[:]
                                del monstro2[:]
                                del monstro3[:]

                                ladrao(monstro1)
                                Chafe_ladroes(monstro2)
                                ladrao(monstro3)

                                resultado = batalha_Vs3(personagem, monstro1, monstro2, monstro3, habilidades, bolsa)
                                if(resultado == 0):
                                    print("\n****************************************************************")
                                    print("\nChefe dos Ladrões:")
                                    print("     Tirem esse lixo daqui!")
                                    sleep(4)

                                    exit(0)

                                else:
                                    
                                    inventario.append("Chave08")
                                    
                                    print("\Chave do 8º Andar adicionado ao inventário")
                                    sleep(2)
                                    salvar_jogo(personagem, nome, inventario, habilidades, itens, bolsa)


                            elif(decisao9 == "2"):
                                decisao3 = "@"

                            elif(decisao9 == "3"):
                                mapa(local)
                                decisao9 = "@"

                            elif(decisao9 == "4"):
                                menuPersonagem(personagem, habilidades, itens, nome, bolsa)
                                decisao9 = "@"
                                

                elif(decisao3 == "2"):
                    print("\n****************************************************************")
                    print("                     Estrada de Areia")
                    print("\n****************************************************************")
                    sleep(2)

                    if(voltas[1] == 0):
                        print("\n" + nome[0] + ":")
                        print("     Estradas costumam ser cheias de ladrões, ótimo!")
                        sleep(2)
                        
                        del monstro1[:]
                        del monstro2[:]
                        del monstro3[:]

                        ladrao(monstro1)
                        ladrao(monstro2)
                        ladrao(monstro3)

                        resultado = batalha_Vs3(personagem, monstro1, monstro2, monstro3, habilidades, bolsa)

                        if(resultado == 0):
                            print("\nLadrão:")
                            print("     Cheio de marra, pra nada...")
                            sleep(2)
                            exit(0)
                        voltas[1] = 1

                    decisao4 = "@"
                    while(decisao4.isalnum() == False):                                
                        del local[:]
                        local = [0,0,1,0,0,0,0,0]
                        
                        print("\n****************************************************************")
                        print("\nDecisão: ")
                        print("1 - Oeste \n2 - Leste \n3 - Mapa \n4 - Menu do Personagem")
                        decisao4 = input("\nR: ")

                        if(decisao4 == "1"):
                            decisao3 = "@"

                        elif(decisao4 == "2"):
                            print("\n****************************************************************")
                            print("                     Vila Abandonada")
                            print("\n****************************************************************")
                            sleep(2)

                            if(voltas[2] == 0):
                                print("\n" + nome[0] + ":")
                                print("     Oquê será que acontenceu nesta vila? Onde estão todos?")
                                sleep(2)

                                print("\nLadrão:")
                                print("     Ei forasteiro! Não percebeu que este território é nosso?")
                                sleep(2)

                                print("\n" + nome[0] + ":")
                                print("     Mais moscas zunindo no meu ouvido?")
                                sleep(2)

                                print("\nLadrão:")
                                print("     Do que você nos chamou? Já tiramos vidas por menos!")
                                sleep(2)

                                print("\nAmbiente:")
                                print("     Tremor desconhecido.")
                                sleep(2)

                                print("\n" + nome[0] + ":")
                                print("     Que tremor foi esse? Isso é obra de vocês?")
                                sleep(2)

                                print("\nLadrão:")
                                print("     Claro que não!")
                                sleep(2)

                                print("\nHistoria:")
                                print("     Um escorpião gigante surge de um burado na areia!")
                                sleep(3)
                                print("     Com um golpe rápido de sua garra ele corta um ladrão ao meio.")
                                sleep(3)
                                print("     E com um golpe de seu ferrão, ele paralisa o outro.")
                                sleep(3)

                                print("\n" + nome[0] + ":")
                                print("     Ei! Essas presas eram minhas! Você pagara por isso!")
                                sleep(2)

                                print("\nHistoria:")
                                print("     Após um novo movimento de cauda do escorpião,")
                                sleep(3)
                                print("     uma mancha de sangue se forma em nossa armadura.")
                                sleep(3)

                                print("\n" + nome[0] + ":")
                                print("     Desgrçado! Ah... Você... voc... v...")
                                sleep(2)

                                print("\nHistoria:")
                                print("     Escuridão.")
                                sleep(10)

                                print("\n\n\n\n" + nome[0] + ":")
                                print("     OQUE???!!")
                                sleep(2)
                                print("     AH, minha cabeça!")
                                sleep(2)
                                print("     Que lugar é esse?")
                                sleep(2)

                                print("\nVelha:")
                                print("     Ei você ai! Não se mexa tanto, vai abrir os pontos!")
                                sleep(3)

                                print("\n" + nome[0] + ":")
                                print("     Ahn? Quem esta ai? Exijo que mostre-se!")
                                sleep(2)

                                print("\nVelha")
                                print("     Dentro de minha cabana quem faz exigências sou eu!")
                                sleep(2)
                                print("     E estou mandondo que você volte a se deitar!")
                                sleep(2)

                                print("\n" + nome[0] + ":")
                                print("     Quem você pensa que é para falar comigo assim?")
                                sleep(2)

                                print("\nVelha:")
                                print("     Me chamo Minerva, e acabo de salvar a sua vida miserável!")
                                sleep(2)

                                print("\nHistoria:")
                                print("     Depois de nos acalmar, tivemos uma conversa sobre o que havia acontecido.")
                                sleep(4)

                                print("\n" + nome[0] + ":")
                                print("     Desculpe meus modos, obrigado por ter me salvado.")
                                sleep(2)

                                print("\nMinerva:")
                                print("     Era o minimo que eu podia fazer por alguém que esta lutando contra o portal.")
                                sleep(4)

                                print("\n" + nome[0] + ":")
                                print("     Sobre isso, o que você pode me dizer sobre a chave deste andar?")
                                sleep(4)

                                print("\nMinerva:")
                                print("     Tudo o que sei é que ela esta escondida em um alçapão no meio do deserto.")
                                sleep(5)
                                print("     Aquele que o escorpião levou tem a chave. Ele era o imediato do Chefe.")
                                sleep(5)

                                print("\n" + nome[0] + ":")
                                print("     Então devo me apressar antes que aquele monstro coma minha chave.")
                                sleep(5)

                                print("\nMinerva:")
                                print("     Antes de ir, leve com você estes oculos de proteção, te ajudará na busca.")
                                sleep(5)

                                print("\nHistoria:")
                                print("     Minerva coloca os oculos em nosso bolso.")
                                sleep(3)

                                decisaoConversa = "@"
                                while(decisaoConversa != "1" and decisaoConversa != "2"):
                                    print("\n****************************************************************")
                                    print("\nDecisão: ")
                                    print("1 - Ir atrás da chave \n2 - Continuar a conversa")
                                    decisaoConversa = input("\nR: ")

                                    if(decisaoConversa == "2"):
                                        print("\nMinerva:")
                                        print("     Aquela criatura pode parecer forte, mas ela possui um ponto fraco.")
                                        sleep(4)

                                        print("\n" + nome[0] + ":")
                                        print("     Qual?")
                                        sleep(2)

                                        print("\nMinerva:")
                                        print("     Em sua ultima luta contra o Chefe, ela saiu com uma rachadura em suas costas.")
                                        sleep(5)

                                        print("\n" + nome[0] + ":")
                                        print("     Obrigado, me lembrarei disso.")
                                        sleep(2)

                                        print("\nMinerva:")
                                        print("     De agora em diante, não deixe que sua causa lhe suba a cabeça.")
                                        sleep(5)
                                        print("     Eu não estarei la para te salvar na próxima!")
                                        sleep(3)

                                        print("\n" + nome[0] + ":")
                                        print("     Não acontecerá novamente.")
                                        sleep(3)

                                    elif(decisaoConversa == "1"):
                                        print("\n" + nome[0] + ":")
                                        print("     Preciso ir. Obrigado por tudo.")
                                        sleep(3)                                        

                            voltas[2] = 1
                                                                        

                            decisao5 = "@"
                            while(decisao5.isalnum() == False):     
                                del local[:]
                                local = [0,0,0,1,0,0,0,0]
                                
                                print("\n****************************************************************")
                                print("\nDecisão: ")
                                print("1 - Oeste \n2 - Leste \n3 - Mapa \n4 - Menu do Personagem")
                                decisao5 = input("\nR: ")

                                if(decisao5 == "1"):
                                    decisao4 = "@"

                                elif(decisao5 == "2"):
                                    print("\n****************************************************************")
                                    print("                         Oasis")                            
                                    print("\n****************************************************************")
                                    sleep(2)

                                    if(voltas[3] == 0):
                                        print("\n" + nome[0] + ":")
                                        print("     Finalmente um pouco de água no meio deste inferno.")
                                        sleep(2)
                                        print("     Só preciso me livrar destas criaturas primeiro.")
                                        sleep(2)
                                        if(decisaoConversa == "2"):
                                            print("      Com calma desta vez!")
                                            sleep(3)

                                        del monstro1[:]
                                        del monstro2[:]
                                        del monstro3[:]

                                        lagarto(monstro1)
                                        lagarto(monstro2)
                                        lagarto(monstro3)

                                        resultado = batalha_Vs3(personagem, monstro1, monstro2, monstro3, habilidades, bolsa)

                                        if(resultado == 0):                                            
                                            print("     Você foi comigo por lagartos.")
                                            sleep(2)
                                            exit(0)

                                    voltas[3] = 1

                                    decisao6 = "@"
                                    while(decisao6.isalnum() == False):                                
                                        del local[:]
                                        local = [0,0,0,0,1,0,0,0]
                                        
                                        print("\n****************************************************************")
                                        print("\nDecisão: ")
                                        print("1 - Oeste \n2 - Leste \n3 - Mapa \n4 - Menu do Personagem")
                                        decisao6 = input("\nR: ")

                                        if(decisao6 == "1"):
                                            decisao5 = "@"

                                        elif(decisao6 == "2"):
                                            print("\n****************************************************************")
                                            print("                     Ninho do Escorpião")                            
                                            print("\n****************************************************************")
                                            sleep(2)

                                            if(voltas[4] == 0):
                                                print("\n" + nome[0] + ":")
                                                print("     Crias daquele monstro?")
                                                sleep(2)

                                                del monstro1[:]
                                                del monstro2[:]
                                                
                                                filhote_escorpiao(monstro1)
                                                filhote_escorpiao(monstro2)                                               

                                                resultado = batalha_Vs2(personagem, monstro1, monstro2, habilidades, bolsa)

                                                if(resultado == 0):                                            
                                                    print("     Você servira de alimento para crias.")
                                                    sleep(2)
                                                    exit(0)

                                                print("\n****************************************************************")
                                                print("\n" + nome[0] + ":")
                                                print("     Mais crias?")
                                                sleep(4)


                                                del monstro1[:]
                                                del monstro2[:]
                                                
                                                filhote_escorpiao(monstro1)
                                                filhote_escorpiao(monstro2)                                               

                                                resultado = batalha_Vs2(personagem, monstro1, monstro2, habilidades, bolsa)

                                                if(resultado == 0):                                            
                                                    print("     Você servira de alimento para crias.")
                                                    sleep(2)
                                                    exit(0)

                                                print("\n****************************************************************")
                                                print("\n" + nome[0] + ":")
                                                print("     Foram todas...")
                                                sleep(4)


                                            voltas[4] = 1

                                            decisao7 = "@"
                                            while(decisao7.isalnum() == False):                                
                                                del local[:]
                                                local = [0,0,0,0,0,1,0,0]
                                                
                                                print("\n****************************************************************")
                                                print("\nDecisão: ")
                                                print("1 - Oeste \n2 - Sul \n3 - Mapa \n4 - Menu do Personagem")
                                                decisao7 = input("\nR: ")

                                                if(decisao7 == "1"):
                                                    decisao6 = "@"

                                                elif(decisao7 == "2"):
                                                    print("\n****************************************************************")
                                                    print("                 Caverna da Mãe Escorpião")                            
                                                    print("\n****************************************************************")
                                                    sleep(2)
                                                    
                                                    if(voltas[5] == 0):
                                                        print("\n" + nome[0] + ":")
                                                        print("     Finalmente nos escontramos.")
                                                        sleep(4)

                                                        del monstro1[:]
                                                        del monstro2[:]
                                                        del monstro3[:]
                                                        
                                                        ponto_fraco_escorpiao(monstro1)
                                                        escorpiao_gigante(monstro2)
                                                        escorpiao_gigante2(monstro3)

                                                        if(decisaoConversa == "2"):

                                                            resultado = batalha(personagem, monstro1, habilidades, bolsa)
                                                            if(resultado == 0):
                                                                print("     Você será comida para as próximas crias.")
                                                                sleep(2)
                                                                exit(0)

                                                            resultado = batalha(personagem, monstro2, habilidades, bolsa)
                                                            if(resultado == 0):
                                                                print("     Você será comida para as próximas crias.")
                                                                sleep(2)
                                                                exit(0)

                                                        else:
                                                            resultado = batalha(personagem, monstro3, habilidades, bolsa)
                                                            if(resultado == 0):
                                                                print("     Você será comida para as próximas crias.")
                                                                sleep(2)
                                                                exit(0)

                                                        print("\n****************************************************************")
                                                        print("\n" + nome[0] + ":")
                                                        print("     Finalmente acabou.")
                                                        sleep(4)
                                                        print("     Preciso achar aquela maldita chave.")
                                                        sleep(3)

                                                        print("\nHistoria:")
                                                        print("     Após algum tempo procurando entre entranhas e ossos,")
                                                        sleep(4)
                                                        print("     Encontramos a chave para a sala do Chefe.")
                                                        sleep(3)
                                                        chave[0] = 1

                                                        voltas[5] = 1

                                                    
                                                    decisao8 = "@"
                                                    while(decisao8.isalnum() == False):                                
                                                        del local[:]
                                                        local = [0,0,0,0,0,0,1,0]
                                                        
                                                        print("\n****************************************************************")
                                                        print("\nDecisão: ")
                                                        print("1 - Norte \n2 - Mapa \n3 - Menu do Personagem")
                                                        decisao8 = input("\nR: ")

                                                        if(decisao8 == "1"):
                                                            decisao7 = "@"

                                                        elif(decisao8 == "2"):
                                                            mapa(local)
                                                            decisao8 = "@"

                                                        elif(decisao8 == "3"):
                                                            menuPersonagem(personagem, habilidades, itens, nome, bolsa)
                                                            decisao8 = "@"


                                                elif(decisao7 == "3"):
                                                    mapa(local)
                                                    decisao7 = "@"

                                                elif(decisao7 == "4"):
                                                    menuPersonagem(personagem, habilidades, itens, nome, bolsa)
                                                    decisao7 = "@"
                                                    

                                        elif(decisao6 == "3"):
                                            mapa(local)
                                            decisao6 = "@"

                                        elif(decisao6 == "4"):
                                            menuPersonagem(personagem, habilidades, itens, nome, bolsa)
                                            decisao6 = "@"
                                        

                                elif(decisao5 == "3"):
                                    mapa(local)
                                    decisao5 = "@"

                                elif(decisao5 == "4"):
                                    menuPersonagem(personagem, habilidades, itens, nome, bolsa)
                                    decisao5 = "@"
                                                            

                        elif(decisao4 == "3"):
                            mapa(local)
                            decisao4 = "@"

                        elif(decisao4 == "4"):
                            menuPersonagem(personagem, habilidades, itens, nome, bolsa)
                            decisao4 = "@"

                    
                    
                elif(decisao3 == "3"):
                    mapa(local)
                    decisao3 = "@"

                elif(decisao3 == "4"):
                    menuPersonagem(personagem, habilidades, itens, nome, bolsa)
                    decisao3 = "@"
                


        elif(decisao2 == "2"):
            mapa(local)
            decisao2 = "@"
            
        elif(decisao2 == "3"):
            menuPersonagem(personagem, habilidades, itens, nome, bolsa)
            decisao2 = "@"

             
