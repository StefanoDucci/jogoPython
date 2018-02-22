# encoding: UTF-8
from time import sleep


def pets(personagem, nome):
    print("\nMago Sábio:")
    print("    Todos nós aqui em Mundo temos um acompanhante para nos ajudar.")
    sleep(2)
    print("    Eu mesmo tenho minha boa e velha companheira Turt.")
    sleep(2)
    print("    Ela já me salvou em várias ocasiões hihi")
    sleep(2)
    print("    Mas isso é outra história...")
    sleep(2)
    print("    Venha comigo ao Viveiro de Criaturas para escolher um magnífico amigo.")
    sleep(3)

    print("\n****************************************************************")
    print("\n\nViveiro de Criaturas\n\n")
    print("****************************************************************\n")
    sleep(2)

    print("\nNewt:")
    print("    Olá grande Sábio, como posso te ajudar hoje?")
    sleep(2)
    print("    Dando uma olhada na velha Turt talvez?")
    sleep(2)
    print("    Ou talvez algumas rações?")
    sleep(2)

    print("\nMago Sábio")
    print("    Ah, não, não... ")
    sleep(2)
    print("    Hoje estou mostrando a cidade para nosso amigo " + nome[0] + " aqui.")
    sleep(2)

    print("\nNewt:")
    print("    Sim claro. Muito bem, muito bem.")
    sleep(2)
    print("    Não aparecem muitos aventureiros por aqui des da chegada do...")
    sleep(3)

    print("\nMago Sábio:")
    print("    Coof coof coof... URhum, acho que não precisamos falar disso por enquanto.")
    sleep(3)

    print("\nNewt:")
    print("    Claro, claro... Bem, no que posso ajudar?")
    sleep(2)

    print("\nMago Sábio:")
    print("    Queremos um companheiro para nosso amigo.")
    sleep(2)

    print("\nNewt")
    print("    Ah sim, é pra já senhor...")
    sleep(2)
    print("    Como você disse que se chama mesmo?")
    sleep(2)

    print("\n" + nome[0] + ":")
    print("    " + nome[0] + ", muito prazer.")
    sleep(2)

    print("\nNewt:")
    print("    O prazer é todo meu!")
    sleep(2)
    print("    Muito bem, vejamos quem nós temos por aqui hoje para você.")
    sleep(3)

    print("\n...")
    sleep(2)
    print("...")
    sleep(2)
    print("...")
    sleep(2)

    print("\nNewt:")
    print("    Sim, sim, aqui estão eles.")
    sleep(2)
    print("    Eu tenho aqui três especimes para o senhor, cada uma de uma parte de nosso mundo.")
    sleep(3)
    print("    Fique avontade para escolher e tirar qualquer dúvida que surgir.")
    sleep(3)


    decisao = "0"
    while(decisao != "1" and decisao != "2" and decisao != "3"):
        print("\nDecisão: \n1 - Salander de Rabo Duplo \n2 - Estufiz Encouraçado \n3 - Florence")
        decisao = input("R: ")

        if(decisao == "1"):
            decisao2 = "0"
            while(decisao2 != "1" and decisao2 != "2" and decisao2 != "3"):
                print("\nDecisão: \n1 - Me fale um pouco sobre este. \n2 - Escolher este como companheiro. \n3 - Voltar")
                decisao2 = input("R: ")

                if(decisao2 == "1"):
                    print("\nNewt:")
                    print("    Ah, está é uma belissima especime de salamandra dos desertos de Mirha.")
                    print("    Dizem que ao chegar na fase adulta, todo o seu corpo se duplica a partir")
                    print("    da segunda cauda.")
                    print("    Tornando ela duas vezes mais perigosa.")
                    print("    Em uma luta, ela te ajudaria a causar dano a seus inimigos.")
                    sleep(10)
                    decisao2 = "0"

                elif(decisao2 == "2"):
                    personagem[67] = 1
                    personagem[68] = 0
                    personagem[69] = 0
                    personagem[70] = 20
                    personagem[71] = 1
                    personagem[72] = 1
                    personagem[73] = 0

                    print("\nNewt:")
                    print("    Uma ótima escolha.")
                    sleep(2)

                elif(decisao2 == "3"):
                    decisao = "0"

        elif(decisao == "2"):
            decisao2 = "0"
            while(decisao2 != "1" and decisao2 != "2" and decisao2 != "3"):
                print("\nDecisão: \n1 - Me fale um pouco sobre este. \n2 - Escolher este como companheiro. \n3 - Voltar")
                decisao2 = input("R: ")

                if(decisao2 == "1"):
                    print("\nNewt:")
                    print("    Este parece pequeno, porém você pode contar com ele para tudo.")
                    print("    O nome vem de sua abilidade de aumentar de tamanho e de sua pele,")
                    print("    que é dura como couro fervido.")
                    print("    Em uma luta, ele recebe por você o dano de seus inimigos.")
                    sleep(10)
                    decisao2 = "0"

                elif(decisao2 == "2"):
                    personagem[67] = 2
                    personagem[68] = 40
                    personagem[69] = 0
                    personagem[70] = 0
                    personagem[71] = 2
                    personagem[72] = 1
                    personagem[73] = 0

                    print("\nNewt:")
                    print("    Uma ótima escolha.")
                    sleep(2)

                elif(decisao2 == "3"):
                    decisao = "0"

        elif(decisao == "3"):
            decisao2 = "0"
            while(decisao2 != "1" and decisao2 != "2" and decisao2 != "3"):
                print("\nDecisão: \n1 - Me fale um pouco sobre este. \n2 - Escolher este como companheiro. \n3 - Voltar")
                decisao2 = input("R: ")

                if(decisao2 == "1"):
                    print("\nNewt:")
                    print("    Essa ai é delicada, mas também não te deixa na mão.")
                    print("    Ela possui propriedades curativas em suas pétalas.")
                    print("    Tornando ela um frasco de poção inesgotável.")
                    print("    Em uma luta, ela cura suas feridas após o ataque inimigo.")
                    sleep(10)
                    decisao2 = "0"

                elif(decisao2 == "2"):
                    personagem[67] = 3
                    personagem[68] = 0
                    personagem[69] = 0
                    personagem[70] = 10
                    personagem[71] = 9
                    personagem[72] = 1
                    personagem[73] = 0

                    print("\nNewt:")
                    print("    Uma ótima escolha.")
                    sleep(2)

                elif(decisao2 == "3"):
                    decisao = "0"


    print("\nNewt:")
    print("    Maravilha, agora só precisamos de um nome para registro.")
    sleep(2)
    nome_pet = input("\nNome: ")

    nome.append(nome_pet)

    print("\nMago Sábio:")
    print("    Muito bem, é hora de continuar.")
    sleep(2)
                    

        


    

    
