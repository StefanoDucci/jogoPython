# encoding: UTF-8

from Andar_01 import andar_01
from Andar_02 import andar_02
from Andar_03 import andar_03
from Andar_04 import andar_04
from Andar_05 import andar_05
from Andar_06 import andar_06
from Andar_07 import andar_07
from Andar_08 import andar_08


from Batalha import *
from Monstros import *



'''        
	chefe  = []
	mob1  = []
	mob2  = []

	Chafe_teste(chefe)
	ladrao(mob1)
	ladrao(mob2)

	batalhaChefe(personagem, chefe, mob1, mob2, habilidades, bolsa, nome)

'''


def Portal(personagem, nome, inventario, habilidades, itens, ponto, bolsa):

	ponto = len(inventario)
	if(ponto == 0):
		andar_01(personagem, nome, inventario, habilidades, itens, bolsa)
			
	if(ponto == 1):
		andar_02(personagem, nome, inventario, habilidades, itens, bolsa)
	
	if(ponto == 2):
		andar_03(personagem, nome, inventario, habilidades, itens, bolsa)
	
	if(ponto == 3):
		andar_04(personagem, nome, inventario, habilidades, itens, bolsa)
		
	if(ponto == 4):
		andar_05(personagem, nome, inventario, habilidades, itens, bolsa)
	
	if(ponto == 5):
		andar_06(personagem, nome, inventario, habilidades, itens, bolsa)

	if(ponto == 6):
		andar_07(personagem, nome, inventario, habilidades, itens, bolsa)

	if(ponto == 7):
		andar_08(personagem, nome, inventario, habilidades, itens, bolsa)
		
