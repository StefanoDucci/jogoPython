# ecoding: UTF-8

from Batalha import *
from Monstros import *
from Quest import *
from time import sleep
from Opcoes import salvar_jogo
from MenusPersonagem import menuPersonagem


###############################################################################################################

def sala_do_chefe07(personagem, nome, inventario, habilidades, itens, bolsa):
        print("\n****************************************************************")
        print("\n\n Sala do Chefe \n\n")
        print("****************************************************************\n")
        sleep(3)

        print("\nPortas batendo")
        sleep(2)

        print("\nRei:")
        print("    Como ousa entrar aqui assim!")
        sleep(2)

        print("\n" + nome[0] + ":")
        print("    Eu vim atrás da chave do portal que seu amigo Senhor Conquistador te deu!")
        sleep(3)

        print("\nRei:")
        print("    Eu paguei 40 homens para impedir um exército e você matou todos sozinho?")
        sleep(2)
        print("    Bando de incompetentes!!!")
        sleep(2)

        print("\nOlhares nervosos.")
        sleep(2)

        print("\nCapitão da Gurda:")
        print("    Meus homens não cairiam para alguém como ele!")
        sleep(2)

        print("\nLider dos Mercenários:")
        print("    Muito menos os meus! Ele deve ter usado algum truque!")
        sleep(2)

        print("\nRei:")
        print("    Não fiquem ai parados criando desculpas! Matem ele!")
        sleep(2)

        monstro1 = []
        monstro2 = []

        capitao_guarda(monstro1)
        lider_mercenario(monstro2)

        resultado = batalha_Vs2(personagem, monstro1, monstro2, habilidades, bolsa)
        if(resultado == 0):
            print("\nRei:")
            print("    Joguem para os porcos!")
            exit(0)
        else:            
            print("\n" + nome[0] + ":")
            print("    Você não tem mais para onde fugir Rei! Somos só eu e você agora.")
            sleep(2)

        monstro3 = []

        rei(monstro3)

        resultado = batalha(personagem, monstro3, habilidades, bolsa)

        print("\n" + nome[0] + ":")
        print("    Fracote miserável, se escondendo atrás de bons homens!")
        sleep(2)
            
        print("\nVocê recebeu a Chave do 7º andar.")
        sleep(3)

        inventario.append("Chave07")

        print("\nChave do 7º andar adicionada ao inventario.")
        sleep(3)


###############################################################################################################

def mapa(local):
    print("\n        MAPA DO CASTELO\n  N\nO   L\n  S")
    print("            | |")
    print("")
    if(local[12] == 1):
        print("            |X|")
    else:
        print("            | |")
    print("")
    if(local[3] == 1):
        print("| | - | | - |X| - | | - | |")
    elif(local[4] == 1):
        print("| | - | | - | | - |X| - | |")
    elif(local[5] == 1):
        print("| | - | | - | | - | | - |X|")
    elif(local[8] == 1):
        print("| | - |X| - | | - | | - | |")
    elif(local[9] == 1):
        print("|X| - | | - | | - | | - | |")
    else:
        print("| | - | | - | | - | | - | |")
    print("")
    if(local[2] == 1):
        print("| |         |X|         | |")
    elif(local[6] == 1):
        print("| |         | |         |X|")
    elif(local[10] == 1):
        print("|X|         | |         | |")
    else:
        print("| |         | |         | |")
    print("")
    if(local[1] == 1):
        print("| |         |X|         | |")
    elif(local[7] == 1):
        print("| |         | |         |X|")
    elif(local[11] == 1):
        print("|X|         | |         | |")
    else:
        print("| |         | |         | |")
    print("")
    print("            | |")
    


###############################################################################################################

    
def andar_07(personagem, nome, inventario, habilidades, itens, bolsa):
    chave = [0,0]
    voltas = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    local = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    monstro1 = []
    monstro2 = []
    monstro3 = []

    print("\n****************************************************************")
    print("\n\n Entrada do Castelo \n\n")
    print("****************************************************************\n")
    sleep(3)

    print("\n" + nome[0] + ":")
    print("    Um castelo? Não parece um dos grandes...")
    sleep(3)
    print("    Vejamos o que ele tem para nós.")
    sleep(2)

    decisao = "@"
    while(decisao.isalnum() == False):
        print("\nDecisão: \n1 - Entrar no castelo \n2 - Menu do Personagem")
        decisao = input("R: ")

        if(decisao == "1"):
            print("\n****************************************************************")
            print("\n\n Saguão do Castelo \n\n")
            print("****************************************************************\n")

            del local[:]
            local = [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]

            while(voltas[1] == 0):
                print("\nGuarda Real:")
                print("    Quem é você? E o que você quer aqui?")
                sleep(2)

                print("\n" + nome[0] + ":")
                print("    Meu nome é " + nome[0] + " e estou aqui pela chave do portal.")
                sleep(2)

                print("\nGuarda Real")
                print("    Entendo...")
                sleep(2)
                print("    Homens! Matem esse intruso!")
                sleep(2)

                guarda_real(monstro1)
                guarda_real(monstro2)
                guarda_real(monstro3)

                resultado = batalha_Vs3(personagem, monstro1, monstro2, monstro3, habilidades, bolsa)
                if(resultado == 0):
                    print("\nVocê será jogado nas masmorras pelo resto de sua vida.")
                    exit(0)
                else:
                    voltas[1] = 1
                    print("\n" + nome[0] + ":")
                    print("    Esses homens não estão de brincadeira.")
                    sleep(2)


            decisao2 = "@"
            while(decisao2.isalnum() == False):
                print("\nDecisão: \n1 - Norte \n2 - Mapa \n3 - Menu do Personagem")
                decisao2 = input("R: ")

                if(decisao2 == "1"):
                    print("\n****************************************************************")
                    print("\n\n Corredor do Castelo \n\n")
                    print("****************************************************************\n")

                    del local[:]
                    local = [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]

                    while(voltas[2] == 0):
                        print("\n" + nome[0] + ":")
                        print("    Mais uma sala cheia de guardas...")
                        sleep(2)

                        del monstro1[:]
                        del monstro2[:]
                        del monstro3[:]

                        guarda_real(monstro1)
                        guarda_real(monstro2)
                        guarda_real(monstro3)

                        resultado = batalha_Vs3(personagem, monstro1, monstro2, monstro3, habilidades, bolsa)
                        if(resultado == 0):
                            print("\nVocê será jogado nas masmorras pelo resto de sua vida.")
                            exit(0)

                        del monstro1[:]
                        del monstro2[:]
                        del monstro3[:]

                        guarda_real(monstro1)
                        guarda_real(monstro2)
                        guarda_real(monstro3)

                        resultado = batalha_Vs3(personagem, monstro1, monstro2, monstro3, habilidades, bolsa)
                        if(resultado == 0):
                            print("\nVocê será jogado nas masmorras pelo resto de sua vida.")
                            exit(0)

                        else:
                            voltas[2] = 1
                            print("\n" + nome[0] + ":")
                            print("    Esse lugar deve ter umas mil salas, onde o Chefe pode estar?")
                            sleep(3)


                        decisao3 = "@"
                        while(decisao3.isalnum() == False):
                            print("\nDecisão: \n1 - Norte \n2 - Mapa \n3 - Menu do Personagem")
                            decisao3 = input("R: ")

                            if(decisao3 == "1"):
                                print("\n****************************************************************")
                                print("\n\n Centro do Castelo \n\n")
                                print("****************************************************************\n")

                                del local[:]
                                local = [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]

                                while(voltas[3] == 0):
                                    print("\n" + nome[0] + ":")
                                    print("    Parece que tenho outro dilema. ")
                                    sleep(3)

                                    voltas[3] = 1


                                decisao4 = "@"
                                while(decisao4.isalnum() == False):
                                    if(chave[0] == 0 or chave[1] == 0):
                                        print("\nDecisão: \n1 - Leste \n2 - Oeste \n3 - Mapa\n4 - Menu do Personagem")

                                    else:
                                        print("\n" + nome[0] + ":")
                                        print("Eu não tinha visto essa porta aqui antes...")
                                        sleep(2)
                                        print("\nDecisão: \n1 - Leste \n2 - Oeste \n3 - Mapa\n4 - Menu do Personagem \n5 - Norte")
                                        
                                    decisao4 = input("R: ")

                                    if(decisao4 == "1"):
                                        print("\n****************************************************************")
                                        print("\n\n Ala dos Cavaleiros \n\n")
                                        print("****************************************************************\n")

                                        del local[:]
                                        local = [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]

                                        while(voltas[4] == 0):
                                            print("\n" + nome[0] + ":")
                                            print("    Esse rei deve ser muito rico para manter tantos guardas.")
                                            sleep(3)

                                            print("\nCavaleiro Real")
                                            print("    Guardas? Tsc.")
                                            sleep(2)
                                            print("    Nós somos cavaleiros reais!")
                                            print("    E você é um homem morto!")
                                            sleep(4)

                                            del monstro1[:]
                                            del monstro2[:]                                            

                                            cavaleiro_real(monstro1)
                                            cavaleiro_real(monstro2)                                           

                                            resultado = batalha_Vs2(personagem, monstro1, monstro2, habilidades, bolsa)
                                            if(resultado == 0):
                                                print("\nVocê será jogado nas masmorras pelo resto de sua vida.")
                                                exit(0)

                                            else:
                                                voltas[4] = 1
                                                print("\n" + nome[0] + ":")
                                                print("    Não sei não se esse é um bom caminho para continuar...")
                                                sleep(4)


                                        decisao5 = "@"
                                        while(decisao5.isalnum() == False):
                                            print("\nDecisão: \n1 - Leste \n2 - Oeste \n3 - Mapa\n4 - Menu do Personagem")
                                            decisao5 = input("R: ")

                                            if(decisao5 == "1"):
                                                print("\n****************************************************************")
                                                print("\n\n Sala de Treinamento \n\n")
                                                print("****************************************************************\n")

                                                del local[:]
                                                local = [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]

                                                while(voltas[5] == 0):
                                                    print("\n" + nome[0] + ":")
                                                    print("    Não parem por minha causa, estou só de passagem.")
                                                    sleep(2)

                                                    print("\nCavaleiro Real:")
                                                    print("    Vamos ver onde suas gracinhas te levam!")
                                                    sleep(2)

                                                    del monstro1[:]
                                                    del monstro2[:]
                                                    del monstro3[:]

                                                    cavaleiro_real(monstro1)
                                                    cavaleiro_real(monstro2)
                                                    cavaleiro_real(monstro3)

                                                    resultado = batalha_Vs3(personagem, monstro1, monstro2, monstro3, habilidades, bolsa)
                                                    if(resultado == 0):
                                                        print("\nVocê será jogado nas masmorras pelo resto de sua vida.")
                                                        exit(0)

                                                    else:
                                                        voltas[5] = 1
                                                        print("\n" + nome[0] + ":")
                                                        print("    Quantos mais podem ter aqui dentro?")
                                                        sleep(2)

                                                decisao6 = "@"
                                                while(decisao6.isalnum() == False):
                                                    print("\nDecisão: \n1 - Sul \n2 - Oeste \n3 - Mapa\n4 - Menu do Personagem")
                                                    decisao6 = input("R: ")

                                                    if(decisao6 == "1"):
                                                        print("\n****************************************************************")
                                                        print("\n\n Centro de Comando dos Cavaleiros \n\n")
                                                        print("****************************************************************\n")

                                                        del local[:]
                                                        local = [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]

                                                        while(voltas[6] == 0):
                                                            print("Cavaleiro Real:")
                                                            print("    Seu pequeno passeio termina aqui!")
                                                            sleep(2)

                                                            del monstro1[:]
                                                            del monstro2[:]                                                        

                                                            cavaleiro_real(monstro1)
                                                            cavaleiro_real(monstro2)                                                            

                                                            resultado = batalha_Vs2(personagem, monstro1, monstro2, habilidades, bolsa)
                                                            if(resultado == 0):
                                                                print("\nVocê será jogado nas masmorras pelo resto de sua vida.")
                                                                exit(0)

                                                            print("Cavaleiro Real:")
                                                            print("    Que tipo de demonio incansável é você?")
                                                            sleep(2)

                                                            del monstro1[:]
                                                            del monstro2[:]                                                        

                                                            cavaleiro_real(monstro1)
                                                            cavaleiro_real(monstro2)                                                            

                                                            resultado = batalha_Vs2(personagem, monstro1, monstro2, habilidades, bolsa)
                                                            if(resultado == 0):
                                                                print("\nVocê será jogado nas masmorras pelo resto de sua vida.")
                                                                exit(0)

                                                            else:
                                                                print("\n" + nome[0] + ":")
                                                                print("    Eu não aguento muito mais disso.")
                                                                sleep(2)
                                                                voltas[6] = 1

                                                        decisao7 = "@"
                                                        while(decisao7.isalnum() == False):
                                                            print("\nDecisão: \n1 - Sul \n2 - Norte \n3 - Mapa\n4 - Menu do Personagem")
                                                            decisao7 = input("R: ")

                                                            if(decisao7 == "1"):
                                                                print("\n****************************************************************")
                                                                print("\n\n Deposito dos Cavaleiros \n\n")
                                                                print("****************************************************************\n")

                                                                del local[:]
                                                                local = [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]

                                                                if(chave[1] == 0):
                                                                    decisao8 = "@"
                                                                    while(decisao8.isalnum() == False):
                                                                        print("\nDecisão: \n1 - Vasculhar a Sala \n2 - Norte \n3 - Mapa\n4 - Menu do Personagem")
                                                                        decisao8 = input("R: ")

                                                                        if(decisao8 == "1"):
                                                                            recupera_pocao(bolsa)
                                                                            print("\nAlavanca encontrada.")
                                                                            decisao9 = 0
                                                                            while(decisao9 != "1"):
                                                                                print("\nDecisão: \n1 - Ativar alavanca")
                                                                                decisao9 = input("R: ")
                                                                            chave[1] = 1

                                                                        elif(decisao8 == "2"):
                                                                            decisao7 = "@"

                                                                        elif(decisao8 == "3"):
                                                                            mapa(local)
                                                                            decisao8 = "@"

                                                                        elif(decisao8 == "4"):
                                                                            menuPersonagem(personagem, habilidades, itens, nome, bolsa)
                                                                            decisao8 = "@"

                                                                        else:
                                                                            decisao8 = "@"

                                                                if(chave[1] == 1):
                                                                    decisao8 = "@"
                                                                    while(decisao8.isalnum() == False):
                                                                        print("\nDecisão: \n1 - Norte \n2 - Mapa\n3 - Menu do Personagem")
                                                                        decisao8 = input("R: ")                                                                        

                                                                        if(decisao8 == "1"):
                                                                            decisao7 = "@"

                                                                        elif(decisao8 == "2"):
                                                                            mapa(local)
                                                                            decisao8 = "@"

                                                                        elif(decisao8 == "3"):
                                                                            menuPersonagem(personagem, habilidades, itens, nome, bolsa)
                                                                            decisao8 = "@"

                                                                        else:
                                                                            decisao8 = "@"
                                                                    

                                                            elif(decisao7 == "2"):
                                                                decisao6 = "@"

                                                            elif(decisao7 == "3"):
                                                                mapa(local)
                                                                decisao7 = "@"

                                                            elif(decisao7 == "4"):
                                                                menuPersonagem(personagem, habilidades, itens, nome, bolsa)
                                                                decisao7 = "@"

                                                            else:
                                                                decisao7 = "@"
                                                            

                                                    elif(decisao6 == "2"):
                                                        decisao5 = "@"

                                                    elif(decisao6 == "3"):
                                                        mapa(local)
                                                        decisao6 = "@"

                                                    elif(decisao6 == "4"):
                                                        menuPersonagem(personagem, habilidades, itens, nome, bolsa)
                                                        decisao6 = "@"

                                                    else:
                                                        decisao6 = "@"
                                                    

                                            elif(decisao5 == "2"):
                                                decisao4 = "@"

                                            elif(decisao5 == "3"):
                                                mapa(local)
                                                decisao5 = "@"

                                            elif(decisao5 == "4"):
                                                menuPersonagem(personagem, habilidades, itens, nome, bolsa)
                                                decisao5 = "@"

                                            else:
                                                decisao5 = "@"

                                    elif(decisao4 == "2"):
                                        print("\n****************************************************************")
                                        print("\n\n Ala dos Mercenários \n\n")
                                        print("****************************************************************\n")

                                        del local[:]
                                        local = [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]

                                        while(voltas[7] == 0):
                                            print("\n" + nome[0] + ":")
                                            print("    Essa ala do castelo me parece bem mais sombria...")
                                            sleep(2)

                                            print("\nMercenário:")
                                            print("    Ei, você!")
                                            sleep(2)
                                            print("    É você que esta causando confusão no castelo?")
                                            sleep(2)

                                            print("\n" + nome[0] + ":")
                                            print("    Eu só estou atrás da Chave do Portal.")
                                            sleep(2)

                                            print("\nMercenário:")
                                            print("    Ah sim claro, a chave... o motivo de nossa contratação.")
                                            sleep(3)

                                            print("\n" + nome[0] + ":")
                                            print("    Vocês também estão aqui para encontrar a chave?")
                                            sleep(2)

                                            print("\nMercenário:")
                                            print("    Não, para impedir que outros a tenhão!")
                                            sleep(2)

                                            del monstro1[:]
                                            del monstro2[:]
                                            del monstro3[:]

                                            mercenario(monstro1)
                                            mercenario(monstro2)
                                            mercenario(monstro3)

                                            resultado = batalha_Vs3(personagem, monstro1, monstro2, monstro3,habilidades, bolsa)
                                            if(resultado == 0):
                                                print("\nVocê será torturado até a morte.")
                                                exit(0)

                                            else:
                                                print("\n" + nome[0] + ":")
                                                print("    Esses caras são perigosos, eles não tem medo de morrer.")
                                                sleep(2)
                                                voltas[7] = 1

                                        decisao10 = "@"
                                        while(decisao10.isalnum() == False):
                                            print("\nDecisão: \n1 - Oeste \n2 - Leste \n3 - Mapa\n4 - Menu do Personagem")
                                            decisao10 = input("R: ")

                                            if(decisao10 == "1"):
                                                print("\n****************************************************************")
                                                print("\n\n Sala de Tortura \n\n")
                                                print("****************************************************************\n")

                                                del local[:]
                                                local = [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]

                                                while(voltas[8] == 0):
                                                    print("\nPricioneiro:")
                                                    print("    AAHH AAHH EU JÁ FALEI, EU NÃO SEI DE NADA!!!")
                                                    sleep(2)
                                                    print("    NÃO, PORFAVOR, NÃO!")
                                                    sleep(2)
                                                    print("    AHHHH")
                                                    sleep(2)

                                                    print("\nMercenário:")                                                    
                                                    print("    Maldito fracote... não resistiu nem ao terceiro dia...")
                                                    sleep(3)

                                                    print("\n" + nome[0] + ":")
                                                    print("    Qual o propósito disso?")
                                                    sleep(2)

                                                    print("\nMercenário:")
                                                    print("    !!!!")
                                                    sleep(2)
                                                    print("    Você me assustou!")
                                                    sleep(2)
                                                    print("    Mas tudo bem, você era o próximo mesmo...")
                                                    sleep(2)
                                                    print("    Deite na mesa como um bom garoto.")
                                                    sleep(2)

                                                    print("\n" + nome[0] + ":")
                                                    print("    Você é o que eu vou matar primeiro!")
                                                    sleep(2)

                                                    del monstro1[:]
                                                    del monstro2[:]
                                                    del monstro3[:]

                                                    mercenario(monstro1)
                                                    mercenario(monstro2)
                                                    mercenario(monstro3)

                                                    resultado = batalha_Vs3(personagem, monstro1, monstro2, monstro3,habilidades, bolsa)
                                                    if(resultado == 0):
                                                        print("\nVocê será torturado até a morte.")
                                                        exit(0)

                                                    else:
                                                        print("\n" + nome[0] + ":")
                                                        print("    Lixos! Se vendem por algumas moedas...")
                                                        sleep(2)
                                                        voltas[8] = 1


                                                decisao11 = "@"
                                                while(decisao11.isalnum() == False):
                                                    print("\nDecisão: \n1 - Sul \n2 - Leste \n3 - Mapa\n4 - Menu do Personagem")
                                                    decisao11 = input("R: ")

                                                    if(decisao11 == "1"):
                                                        print("\n****************************************************************")
                                                        print("\n\n Sala de Repouso dos Mercenários \n\n")
                                                        print("****************************************************************\n")

                                                        del local[:]
                                                        local = [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]

                                                        while(voltas[9] == 0):
                                                            print("\n" + nome[0] + ":")
                                                            print("    Vocês devem ser os últimos...")
                                                            sleep(2)

                                                            print("\nMercenário:")
                                                            print("    E você, um futuro boneco de arremeço de facas.")
                                                            sleep(2)

                                                            del monstro1[:]
                                                            del monstro2[:]
                                                            
                                                            mercenario(monstro1)
                                                            mercenario(monstro2)                                                           

                                                            resultado = batalha_Vs2(personagem, monstro1, monstro2, habilidades, bolsa)
                                                            if(resultado == 0):
                                                                print("\nVocê será torturado até a morte.")
                                                                exit(0)

                                                            else:
                                                                print("\n" + nome[0] + ":")
                                                                print("    Bom, ainda tem mais uma porta... Esses caras não tem fim.")
                                                                sleep(2)
                                                                voltas[9] = 1


                                                        decisao12 = "@"
                                                        while(decisao12.isalnum() == False):
                                                            print("\nDecisão: \n1 - Sul \n2 - Norte \n3 - Mapa\n4 - Menu do Personagem")
                                                            decisao12 = input("R: ")

                                                            if(decisao12 == "1"):
                                                                print("\n****************************************************************")
                                                                print("\n\n Depósito dos Mercenários \n\n")
                                                                print("****************************************************************\n")

                                                                del local[:]
                                                                local = [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]

                                                                if(chave[0] == 0):
                                                                    decisao13 = "@"
                                                                    while(decisao13.isalnum() == False):
                                                                        print("\nDecisão: \n1 - Vasculhar a Sala \n2 - Norte \n3 - Mapa\n4 - Menu do Personagem")
                                                                        decisao13 = input("R: ")

                                                                        if(decisao13 == "1"):
                                                                            print("\n1000 moedas encontradas.")
                                                                            personagem[56] = personagem[56] + 1000
                                                                            sleep(2)
                                                                            print("\nAlavanca encontrada.")
                                                                            decisao13 = 0
                                                                            while(decisao13 != "1"):
                                                                                print("\nDecisão: \n1 - Ativar alavanca")
                                                                                decisao13 = input("R: ")
                                                                            chave[0] = 1

                                                                        elif(decisao13 == "2"):
                                                                            decisao12 = "@"

                                                                        elif(decisao13 == "3"):
                                                                            mapa(local)
                                                                            decisao13 = "@"

                                                                        elif(decisao13 == "4"):
                                                                            menuPersonagem(personagem, habilidades, itens, nome, bolsa)
                                                                            decisao13 = "@"

                                                                        else:
                                                                            decisao13 = "@"

                                                                if(chave[1] == 1):
                                                                    decisao13 = "@"
                                                                    while(decisao13.isalnum() == False):
                                                                        print("\nDecisão: \n1 - Norte \n2 - Mapa\n3 - Menu do Personagem")
                                                                        decisao13 = input("R: ")                                                                        

                                                                        if(decisao13 == "1"):
                                                                            decisao12 = "@"

                                                                        elif(decisao13 == "2"):
                                                                            mapa(local)
                                                                            decisao13 = "@"

                                                                        elif(decisao13 == "3"):
                                                                            menuPersonagem(personagem, habilidades, itens, nome, bolsa)
                                                                            decisao13 = "@"

                                                                        else:
                                                                            decisao13 = "@"                                                                    
                                                                    

                                                            elif(decisao12 == "2"):
                                                                decisao11 = "@"

                                                            elif(decisao12 == "3"):
                                                                mapa(local)
                                                                decisao12 = "@"

                                                            elif(decisao12 == "4"):
                                                                menuPersonagem(personagem, habilidades, itens, nome, bolsa)
                                                                decisao12 = "@"

                                                            else:
                                                                decisao12 = "@"

                                                            
                                                    elif(decisao11 == "2"):
                                                        decisao10 = "@"

                                                    elif(decisao11 == "3"):
                                                        mapa(local)
                                                        decisao11 = "@"

                                                    elif(decisao11 == "4"):
                                                        menuPersonagem(personagem, habilidades, itens, nome, bolsa)
                                                        decisao11 = "@"

                                                    else:
                                                        decisao11 == "@"
                                                    

                                            elif(decisao10 == "2"):
                                                decisao4 = "@"

                                            elif(decisao10 == "3"):
                                                mapa(local)
                                                decisao10 = "@"

                                            elif(decisao10 == "4"):
                                                menuPersonagem(personagem, habilidades, itens, nome, bolsa)
                                                decisao10 = "@"

                                            else:
                                                decisao10 = "@"
                                                
                                        
                                    elif(decisao4 == "3"):
                                        mapa(local)
                                        decisao4 = "@"

                                    elif(decisao4 == "4"):
                                        menuPersonagem(personagem, habilidades, itens, nome, bolsa)
                                        decisao4 = "@"

                                    elif(decisao4 == "5" and chave[0] == 1 and chave[1] == 1):
                                        print("\n****************************************************************")
                                        print("\n\n Antessala do Rei \n\n")
                                        print("****************************************************************\n")

                                        print("\n" + nome[0] + ":")
                                        print("    Parece que estou chegando a algum lugar afinal.")
                                        sleep(2)

                                        print("\nGuarda de Elite")
                                        print("    Então existe alguém capaz de passar por toda a nossa defesa?")
                                        sleep(3)

                                        print("\n" + nome[0] + ":")
                                        print("    Farei o que for preciso para terminar o que comecei!")
                                        sleep(3)

                                        print("\nGuarda de Elite")
                                        print("    Sinto muito mas nós como guardas pessoais do rei não ")
                                        print("    podemos deixar que passe daqui.")
                                        sleep(4)

                                        print("\n" + nome[0] + ":")
                                        print("    Acho que vocês teram que tentar me impedir então.")
                                        sleep(2)

                                        del monstro1[:]
                                        del monstro2[:]
                                        del monstro3[:]

                                        guarda_elite(monstro1)
                                        guarda_elite(monstro2)
                                        guarda_elite(monstro3)

                                        resultado = batalha_Vs3(personagem, monstro1, monstro2, monstro3,habilidades, bolsa)
                                        if(resultado == 0):
                                            print("\nVocê foi morto pela guarda real.")
                                            exit(0)

                                        else:
                                            print("\n" + nome[0] + ":")
                                            print("    Agora só falta o rei.")
                                            sleep(2)
                                            print("    Mas devo adimitir a força desses guardas.")
                                            sleep(2)

                                        decisao15 = "@"
                                        while(decisao15.isalnum() == False):
                                            print("\nDecisão: \n1 - Sala do Chefe \n2 - Menu do Personagem")
                                            decisao15 = input("R: ")

                                            if(decisao15 == "1"):
                                                sala_do_chefe07(personagem, nome, inventario, habilidades, itens, bolsa)

                                            elif(decisao15 == "2"):
                                                menuPersonagem(personagem, habilidades, itens, nome, bolsa)
                                                decisao15 = "@"

                                            else:
                                                decisao15 = "@"

                                    else:
                                        decisao4 = "@"


                            elif(decisao3 == "2"):
                                mapa(local)
                                decisao3 = "@"

                            elif(decisao3 == "3"):
                                menuPersonagem(personagem, habilidades, itens, nome, bolsa)
                                decisao3 = "@"

                            else:
                                decisao3 = "@"


                elif(decisao2 == "2"):
                    mapa(local)
                    decisao2 = "@"

                elif(decisao2 == "3"):
                    menuPersonagem(personagem, habilidades, itens, nome, bolsa)
                    decisao2 = "@"

                else:
                    decisao2 = "@"


        elif(decisao == "2"):
            menuPersonagem(personagem, habilidades, itens, nome, bolsa)
            decisao = "@"

        else:
            decisao = "@"



