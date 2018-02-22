# encoding: UTF-8
from Classes import *
from Opcoes import *
from Cidade_Inicial import *
from Habilidades import *
from Itens import *
from Bolsa import criar_bolsa
from pvp import *

###############################################################################################################

def novo_jogo():
    personagem = []
    inventario = []
    habilidades = []
    itens = []
    classe = 0
    bolsa = []
    nome = []
    load = ''
    print("****************************************************************")
    print("\nCriação de Personagem")
    while(load.isalnum() == False):
        load = input("Escolha um nome para seu personagem \nNome: ")
        if(load.isalnum() == False):
            print("Por favor, escolha um nome contendo apenas letras e números.")
        else:
            nome.append(load)
            break
    while(classe != "1" and classe != "2" and classe != "3" and classe != "4"):
        classe = input("\nEscolha uma classe: \n1 - Mago \n2 - Guerreiro \n3 - Gatuno \n4 - Druida \nR: ")
        
        if(classe != "1" and classe != "2" and classe != "3" and classe != "4"):
            print("\nPor favor, informe uma classe entre 1 e 4")
        else:
            classe = int(classe)    
            break
    
        
    cria_personagem_generico(personagem, classe)
    altera_status_por_classe(personagem)
    
    cria_arvore_habilidade(habilidades, personagem)
    
    cria_bolca_itens(itens)
    criar_bolsa(bolsa)
	
    salvar_jogo(personagem, nome, inventario, habilidades, itens, bolsa)
    cidade_inicial(personagem, inventario, nome, habilidades, itens, bolsa)
        
###############################################################################################################

def inicio():
    personagem = []
    inventario = []
    habilidades = []
    itens = []
    bolsa = []
    nome = []
    ponto = 0
    
    resp = input("1 - Novo Jogo \n2 - Jogo Salvo \n3 - PvP\nR: ")
    while(resp != "1" and resp != "2" and resp != "3"):
        print("\nSistema: Informe apenas números entre 1 e 2.")
        resp = input("\nR: ")
    
    resp = int(resp)
    
    if(resp == 1):
        novo_jogo()
    elif(resp == 2):
        load = input("Informe o nome do personagem salvo: ")
        nome.append(load)
        carregar_jogo(personagem, nome, inventario, habilidades, itens, ponto, bolsa)
        cidade_inicial(personagem, inventario, nome, habilidades, itens, bolsa)

    elif(resp == 3):
        load = input("Informe o nome do primeiro jogador: ")
        nome.append(load)
        carregar_jogo(personagem, nome, inventario, habilidades, itens, ponto, bolsa)

        personagem2 = []
        inventario2 = []
        habilidades2 = []
        itens2 = []
        bolsa2 = []
        nome2 = []
        
        load2 = input("Informe o nome do segundo jogador: ")
        nome2.append(load2)
        carregar_jogo(personagem2, nome2, inventario2, habilidades2, itens2, ponto, bolsa2)

        jogador1 = []
        jogador2 = []
        jogadores = []
        
        jogador1.append(personagem)
        jogador1.append(nome)
        jogador1.append(inventario)
        jogador1.append(habilidades)
        jogador1.append(bolsa)
        
        jogador2.append(personagem2)
        jogador2.append(nome2)
        jogador2.append(inventario2)
        jogador2.append(habilidades2)
        jogador2.append(bolsa2)

        jogadores.append(jogador1)
        jogadores.append(jogador2)

        pvp(jogadores)
        

inicio()
