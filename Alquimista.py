# encoding: UTF-8

from time import sleep

def alquimista(personagem, nome, bolsa):
    print("\n****************************************************************")
    print("\nLoja de Alquimia")
    print("\n****************************************************************\n")
    sleep(2)

    print("Alquimista:")
    print("    Olá %s, seja bem vindo a loja de alquimia." % nome[0])

    
    decisao = "0"
    while(decisao != "1" and decisao != "2" and decisao != "3"):
        print("\nOpções: \n1 - Melhorar poção de vida \n2 - Melhorar poção de mana \n3 - Voltar")
        decisao = input("\nR: ")

        if(decisao == "1"):
            decisao2 = "0"
            while(decisao2 != "1" and decisao2 != "2"):
                print("\nOpção: \t Suas moedas: " + str(personagem[56]) + "\n1 - Pagar %d moedas para melhorar a poção? \n2 - Voltar" % (bolsa[0] * 1000))
                decisao2 = input("R: ")

                if(decisao2 == "1"):
                    if(bolsa[0] * 1000 <= personagem[56]):
                        personagem[56] = personagem[56] - (bolsa[0] * 1000)
                        bolsa[0] = bolsa[0] + 1
                        bolsa[1] = bolsa[1] + int(bolsa[1] / 4)
                        decisao = "0"
                    else:
                        print("\nMoedas insuficientes.")
                        sleep(2)
                        decisao = "0"
                elif(decisao2 == "2"):
                    decisao = "0"

        elif(decisao == "2"):
            decisao2 = "0"
            while(decisao2 != "1" and decisao2 != "2"):
                print("\nOpção: \t Suas moedas: " + str(personagem[56]) + "\n1 - Pagar %d moedas para melhorar a poção? \n2 - Voltar" % (bolsa[4] * 1000))
                decisao2 = input("R: ")
                if(decisao2 == "1"):
                    if(bolsa[4] * 1000 <= personagem[56]):
                        personagem[56] = personagem[56] - (bolsa[4] * 1000)
                        bolsa[4] = bolsa[4] + 1
                        bolsa[5] = bolsa[5] + int(bolsa[5] / 4) 
                        decisao = "0"
                    else:
                        print("\nMoedas insuficientes.")
                        sleep(2)
                        decisao = "0"

                elif(decisao2 == "2"):
                        decisao = "0"


        elif(decisao == "3"):
            print("\nALquimista:")
            print("    Volte quando quiser poções melhores.")
            sleep(2)
        
