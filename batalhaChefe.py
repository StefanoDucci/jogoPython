# ecoding: UTF-8
from time import sleep


###############################################################################################################

def personagem_ataca(personagem, monstro, cd):
	dano_personagem = aplica_defesa_monstro(personagem, monstro)
	dano_personagem = aplica_elemento(dano_personagem, personagem[57], monstro[6])
	monstro[0] = monstro[0] - dano_personagem
	print("\nVocê causou: %d de dano" % dano_personagem)
	if(monstro[0] > 0):
                aplica_status(personagem, monstro, personagem[57], personagem[66], 1)

	if(personagem[40] == 4):
                for i in range(5):
                        if(cd[i] != 0):
                                cd[i] = cd[i] - 1


    
###############################################################################################################

                                
def batalhaChefe(personagem, chefe,mob1, mob2, habilidades, bolsa, nome):
    print("\n****************************************************************")
    print("\nLuta contra: " + chefe[7])
    print(chefe[7] + " trouxe " + mob1[7] + " e " + mob2[7] + " para a luta.")
    sleep(4)

    cd = [0,0,0,0,0]

    monstros = []
    monstros.append(chefe)
    monstros.append(mob1)
    monstros.append(mob2)

    while(personagem[2] >= 0 and monstros[0][0] >= 0 and monstros[1][0] >=0 and monstros[2][0] >= 0):
        vezPersonagem = 0
        while(vezPersonagem == 0):
            acao = "@"
            while(acao.isalnum() == False):
                print("\n****************************************************************")
                print("---------------------------------------")
                print("|Chefe: " + chefe[7] + "|")
                print("|Vida: " + str(monstros[0][0]) + "   Mana: " + str(chefe[1]) + "|")            
                print("---------------------------------------")            
                print("|Mob1: " + mob1[7] + ((13 - len(mob1[7])) * " ") + "| Mob2: " + mob2[7] + "|")
                print("|Vida: " + str(monstros[1][0]) + ((15 - len(mob1[7])) * " ") + "| Vida: " + str(monstros[2][0]) +"|")
                print("---------------------------------------\n")
                
                print("---------------------------------------")
                print("" + nome[0] + ":")
                print("Vida: " + str(personagem[2]) + "   Mana: " + str(personagem[3]))
                print("\n1 - Atacar \t 2 - Poções \n3 - Habilidades  4 - Fugir")
                acao = input("\nR: ")

                if(acao == "1"):
                    escolhaInimigo = "@"
                    while(escolhaInimigo.isalnum() == False):
                        while True:
                            try:
                                print("---------------------------------------\n")
                                print("Escolha um inimigo para atacar:\n")
                                print("1 - " + chefe[7])
                                print("2 - " + mob1[7])
                                print("3 - " + mob2[7])
                                print("0 - Voltar")

                                escolhaInimigo = input("\nR: ")

                                if(escolhaInimigo == "0"):
                                    acao = "@"
                                    break
                                else:
                                    personagem_ataca(personagem, monstros[int(escolhaInimigo) - 1], cd)

                            except IndexError:
                                print("\nPor favor, informe somente valores validos!")
                                sleep(2)

           

            exit(0)
