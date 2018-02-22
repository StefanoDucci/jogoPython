# encoding: UTF-8

from time import sleep

def ferreiro(personagem, nome):
    print("\n****************************************************************")
    print("\nLoja do Ferreiro")
    print("\n****************************************************************\n")
    sleep(2)

    print("Ferreiro:")
    print("    Olá " + nome[0] + " o que posso fazer por você hoje?")
    sleep(2)

    decisao = "0"
    while(decisao != "1" and decisao != "2" and decisao != "3"):
        decisao = input("\nDecisão: \n1 - Melhorar arma \n2 - Melhorar armadura \n3 - Voltar \nR: ")

        if(decisao == "1"):
            decisao2 = "0"
            while(decisao2 != "1" and decisao2 != "2" and decisao2 != "3" and decisao2 != "4" and decisao2 != "5"):
                decisao2 = input("\nDecisão: \n1 - Aumentar dano fisíco \n2 - Aumentar dano mágico \n3 - Mudar elemento \n4 - Melhorar chances de Status \n5 - Voltar \nR: ")

                if(decisao2 == "1"):
                    decisao3 = "0"
                    while(decisao3 != "1" and decisao3 != "2"):
                        decisao3 = input("\nDecisão: \n1 - Pagar 1000 moedas para melhorar sua arma? \n2 - Voltar \nR: ")

                        if(decisao3 == "1"):
                            if(personagem[56] >= 1000):
                                if((personagem[74] + 1) > 10):
                                    print("\nEsta arma não pode mais ser aprimorada.")
                                    sleep(3)
                                else:
                                    personagem[56] = personagem[56] - 1000
                                    personagem[10] = personagem[10] + int(personagem[10] / 10)
                                    print("\nVocê gastou 1000 moedas.")
                                    print("\nVocê tem %d moedas."  % personagem[56])
                                    sleep(2)
                                    decisao2 = "0"
                                    personagem[74] = personagem[74] + 1
                            else:
                                print("\nMoedas insuficientes.")
                                sleep(2)
                                decisao2 = "0"

                        elif(decisao3 == "2"):
                            decisao2 = "0"


                if(decisao2 == "2"):
                    decisao3 = "0"
                    while(decisao3 != "1" and decisao3 != "2"):
                        decisao3 = input("\nDecisão: \n1 - Pagar 1000 moedas para melhorar sua arma? \n2 - Voltar \nR: ")

                        if(decisao3 == "1"):
                            if(personagem[56] >= 1000):
                                if((personagem[74] + 1) > 10):
                                    print("\nEsta arma não pode mais ser melhorada.")
                                    sleep(2)
                                else:                                    
                                    personagem[56] = personagem[56] - 1000
                                    personagem[11] = personagem[11] + int(personagem[11] / 10)
                                    print("\nVocê gastou 1000 moedas.")
                                    print("\nVocê tem %d moedas."  % personagem[56])
                                    sleep(2)
                                    decisao2 = "0"
                                    personagem[74] = personagem[74] + 1
                            else:
                                print("\nMoedas insuficientes.")
                                sleep(2)
                                decisao2 = "0"

                        elif(decisao3 == "2"):
                            decisao2 = "0"


                if(decisao2 == "3"):
                    decisao3 = "0"
                    while(decisao3 != "1" and decisao3 != "2"):
                        decisao3 = input("\nDecisão: \n1 - Pagar 5000 moedas para melhorar sua arma? \n2 - Voltar \nR: ")

                        if(decisao3 == "1"):
                            if(personagem[56] >= 5000):
                                decisao4 = "0"
                                while(decisao4 != "1" and decisao4 != "2" and decisao4 != "3"):
                                    decisao4 = input("\nEscolha o elemento: \nDecisão: \n1 - Fogo \n2 - Floresta \n3 - Voltar")

                                    if(decisao4 == "1"):
                                        personagem[56] = personagem[56] - 5000
                                        personagem[57] = 1
                                        print("\nVocê gastou 5000 moedas.")
                                        print("\nVocê tem %d moedas."  % personagem[56])
                                        sleep(2)
                                        decisao3 = "0"

                                    elif(decisao4 == "2"):
                                        personagem[56] = personagem[56] - 5000
                                        personagem[57] = 9
                                        print("\nVocê gastou 5000 moedas.")
                                        print("\nVocê tem %d moedas."  % personagem[56])
                                        sleep(2)
                                        decisao3 = "0"

                                    elif(decisao4 == "3"):
                                        decisao3 = "0"
                                
                            else:
                                print("\nMoedas insuficientes.")
                                sleep(2)
                                decisao2 = "0"
                                
                        if(decisao3 == "2"):
                            decisao2 = "0"


                elif(decisao2 == "4"):
                    decisao3 = "0"
                    while(decisao3 != "1" and decisao3 != "2"):
                        decisao3 = input("\nDecisão: \n1 - Pagar 1000 moedas para melhorar sua arma? \n2 - Voltar \nR: ")

                        if(decisao3 == "1"):
                            if(personagem[56] >= 1000):
                                personagem[66] = personagem[66] + int(personagem[66] / 10)
                                print("\nVocê gastou 1000 moedas.")
                                print("\nVocê tem %d moedas."  % personagem[56])
                                sleep(2)
                                decisao2 = "0"

                            else:
                                print("\nMoedas insuficientes.")
                                sleep(2)
                                decisao2 = "0"

                elif(decisao2 == "5"):
                    decisao = "0"


        elif(decisao == "2"):
            decisao2 = "0"
            while(decisao2 != "1" and decisao2 != "2" and decisao2 != "3" and decisao2 != "4"):
                decisao2 = input("\nDecisão: \n1 - Aumentar defesa fisíca \n2 - Aumentar defesa mágica \n3 - Mudar elemento \n4 - Voltar \nR: ")
                if(decisao2 == "1"):
                    decisao3 = "0"
                    while(decisao3 != "1" and decisao3 != "2"):
                        decisao3 = input("\nDecisão: \n1 - Pagar 1000 moedas para melhorar sua arma? \n2 - Voltar \nR: ")

                        if(decisao3 == "1"):
                            if(personagem[56] >= 1000):
                                if((personagem[75] + 1) > 10):
                                    print("\nEsta armadura não pode mais ser melhorada.")
                                    sleep(3)
                                else:
                                    personagem[56] = personagem[56] - 1000
                                    personagem[12] = personagem[12] + int(personagem[12] / 10)
                                    print("\nVocê gastou 1000 moedas.")
                                    print("\nVocê tem %d moedas."  % personagem[56])
                                    sleep(2)
                                    decisao2 = "0"
                                    personagem[75] = personagem[75] + 1
                            else:
                                print("\nMoedas insuficientes.")
                                sleep(2)
                                decisao2 = "0"

                        elif(decisao3 == "2"):
                            decisao2 = "0"


                if(decisao2 == "2"):
                    decisao3 = "0"
                    while(decisao3 != "1" and decisao3 != "2"):
                        decisao3 = input("\nDecisão: \n1 - Pagar 1000 moedas para melhorar sua arma? \n2 - Voltar \nR: ")

                        if(decisao3 == "1"):
                            if(personagem[56] >= 1000):
                                if((personagem[75] + 1) > 10):
                                    print("\nEsta armadura não pode mais ser melhorada.")
                                    sleep(3)
                                else:
                                    personagem[56] = personagem[56] - 1000
                                    personagem[13] = personagem[13] + int(personagem[13] / 10)
                                    print("\nVocê gastou 1000 moedas.")
                                    print("\nVocê tem %d moedas."  % personagem[56])
                                    sleep(2)
                                    decisao2 = "0"
                                    personagem[75] = personagem[75] + 1
                            else:
                                print("\nMoedas insuficientes.")
                                sleep(2)
                                decisao2 = "0"

                        elif(decisao3 == "2"):
                            decisao2 = "0"


                elif(decisao2 == "3"):
                    decisao3 = "0"
                    while(decisao3 != "1" and decisao3 != "2"):
                        decisao3 = input("\nDecisão: \n1 - Pagar 5000 moedas para melhorar sua armadura? \n2 - Voltar \nR: ")

                        if(decisao3 == "1"):
                            if(personagem[56] >= 5000):
                                decisao4 = "0"
                                while(decisao4 != "1" and decisao4 != "2" and decisao4 != "3"):
                                    decisao4 = input("\nEscolha o elemento: \nDecisão: \n1 - Fogo \n2 - Floresta \n3 - Voltar \nR: ")

                                    if(decisao4 == "1"):
                                        if(personagem[58] == 1):
                                            print("\nEstá armadura já é do elemento fogo.")
                                            decisao4 = "0"
                                        else:
                                            personagem[56] = personagem[56] - 5000
                                            personagem[58] = 1
                                            print("\nVocê gastou 5000 moedas.")
                                            print("\nVocê tem %d moedas."  % personagem[56])
                                            sleep(2)
                                            decisao3 = "0"

                                    elif(decisao4 == "2"):
                                        if(personagem[58] == 9):
                                            print("\nEstá armadura já é do elemento floresta.")
                                            decisao4 = "0"

                                        else:
                                            personagem[56] = personagem[56] - 5000
                                            personagem[58] = 9
                                            print("\nVocê gastou 5000 moedas.")
                                            print("\nVocê tem %d moedas."  % personagem[56])
                                            sleep(2)
                                            decisao3 = "0"

                                    elif(decisao4 == "3"):
                                        decisao3 = "0"
                                
                            else:
                                print("\nMoedas insuficientes.")
                                sleep(2)
                                decisao2 = "0"
                                
                        if(decisao3 == "2"):
                            decisao2 = "0"


                elif(decisao2 == "4"):
                    decisao = "0"

        elif(decisao == "3"):
            print("\nFerreiro:")
            print("    Volte quando quiser ser mais forte.")
            sleep(2)
