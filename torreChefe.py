# ecoding: UTF-8
from Batalha import *
from Monstros import *
from Quest import *
from Opcoes import salvar_jogo

###############################################################################################################	

def dobro(monstro):
    monstro[0] = monstro[0] * 2
    monstro[1] = monstro[1] * 2
    monstro[2] = monstro[2] * 2
    monstro[3] = monstro[3] * 2
    monstro[4] = monstro[4] * 2
    monstro[8] = monstro[8] * 2
    monstro[10] = monstro[10] * 2
    monstro[13] = monstro[13] * 2
    monstro[15] = monstro[15] * 2

def torre(personagem, inventario, habilidades, itens, nome, bolsa):

    print("\n****************************************************************")
    print("Mago Sábio:")
    print("    Parce que você esta procurando por desafios maiores " + nome[0] + ".")
    sleep(2)
    print("    Muito bem, essa é a torre dos 100 Chefes,")
    print("    nela você poderá desafiar todos os chefes")
    print("    que você já derrotou em sequência.")
    print("    Porém, com o dobro da força!")
    print("    Boa sorte! Você vai precisar.")
    sleep(5)

    ponto = len(inventario)
    
    monstro1 = []
    monstro2 = []
    monstro3 = []
    
    if(ponto >= 1):
            
        javali(monstro1)
        Senhor_do_campo(monstro2)
        lobo(monstro3)

        dobro(monstro1)
        dobro(monstro2)
        dobro(monstro3)
            
        resultado = batalha_Vs3(personagem, monstro1, monstro2, monstro3, habilidades, bolsa)
        if(resultado == 0):
            return 1


    if(ponto >= 2):
        del monstro1[:]
        del monstro2[:]
        del monstro3[:]

        rato(monstro1)
        Crocodilo_gigante(monstro2)
        lesma(monstro3)

        dobro(monstro1)
        dobro(monstro2)
        dobro(monstro3)
        
        resultado = batalha_Vs3(personagem, monstro1, monstro2, monstro3, habilidades, bolsa)
        if(resultado == 0):
                return 2



    if(ponto >= 3):
        del monstro1[:]
        del monstro2[:]
        del monstro3[:]

        marujo(monstro1)
        Capitao(monstro2)
        marujo(monstro3)

        dobro(monstro1)
        dobro(monstro2)
        dobro(monstro3)
        
        resultado = batalha_Vs3(personagem, monstro1, monstro2, monstro3, habilidades, bolsa)
        if(resultado == 0):
                return 3


    if(ponto >= 4):
        del monstro1[:]
        del monstro2[:]
        del monstro3[:]

        guarda(monstro1)
        carcereiro_mor(monstro2)
        guarda(monstro3)

        dobro(monstro1)
        dobro(monstro2)
        dobro(monstro3)
        
        resultado = batalha_Vs3(personagem, monstro1, monstro2, monstro3, habilidades, bolsa)
        if(resultado == 0):
                return 4


    if(ponto >= 5):
        del monstro1[:]
        del monstro2[:]
        del monstro3[:]

        necromante(monstro1)
        demonio(monstro2)
        necromante(monstro3)

        dobro(monstro1)
        dobro(monstro2)
        dobro(monstro3)
        
        resultado = batalha_Vs3(personagem, monstro1, monstro2, monstro3, habilidades, bolsa)
        if(resultado == 0):
                return 5



    if(ponto >= 6):
        del monstro1[:]
        del monstro2[:]
        del monstro3[:]

        anaconda(monstro1)
        rainha_serpente(monstro2)
        anaconda(monstro3)

        dobro(monstro1)
        dobro(monstro2)
        dobro(monstro3)
        
        resultado = batalha_Vs3(personagem, monstro1, monstro2, monstro3, habilidades, bolsa)
        if(resultado == 0):
                return 6

            
    if(ponto >= 7):
        del monstro1[:]
        del monstro2[:]
        del monstro3[:]

        lider_mercenario(monstro1)
        rei(monstro2)
        capitao_guarda(monstro3)

        dobro(monstro1)
        dobro(monstro2)
        dobro(monstro3)
        
        resultado = batalha_Vs3(personagem, monstro1, monstro2, monstro3, habilidades, bolsa)
        if(resultado == 0):
                return 7


    if(ponto >= 8):
        del monstro1[:]
        del monstro2[:]
        del monstro3[:]

        ladrao(monstro1)
        Chafe_ladroes(monstro2)
        ladrao(monstro3)

        dobro(monstro1)
        dobro(monstro2)
        dobro(monstro3)
        
        resultado = batalha_Vs3(personagem, monstro1, monstro2, monstro3, habilidades, bolsa)
        if(resultado == 0):
                return 7 
