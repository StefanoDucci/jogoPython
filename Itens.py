# encoding: UTF-8

def cria_bolca_itens(itens):
	itens.append(0) #DanoFisicoArma1	0
	itens.append(0) #DanoMagicoArma1	1
	itens.append(0) #NomeArma1		2
	itens.append(0) #AgilidadeArma1		3
	itens.append(0) #DestrezaArma1		4
	itens.append(0) #ManaArma1		5
	itens.append(0) #ElementoArma1		6
	itens.append(0) #precoArma1		7
	itens.append(0) #ChanceStatus		8
	
	itens.append(0) #DanoFisicoArma2	9
	itens.append(0) #DanoMagicoArma2	10
	itens.append(0) #NomeArma2		11
	itens.append(0) #AgilidadeArma2		12
	itens.append(0) #DestrezaArma2		13
	itens.append(0) #ManaArma2		14
	itens.append(0) #ElementoArma2		15
	itens.append(0) #precoArma2		16
	itens.append(0) #ChanceStatus		17
	
	itens.append(0) #DanoFisicoArma3	18
	itens.append(0) #DanoMagicoArma3	19
	itens.append(0) #NomeArma3		20
	itens.append(0) #AgilidadeArma3		21
	itens.append(0) #DestrezaArma3		22
	itens.append(0) #ManaArma3		23
	itens.append(0) #ElementoArma3		24
	itens.append(0) #precoArma3		25
	itens.append(0) #ChanceStatus		26
	
	itens.append(0) #DanoFisicoArma4	27
	itens.append(0) #DanoMagicoArma4	28
	itens.append(0) #NomeArma4		29
	itens.append(0) #AgilidadeArma4		30
	itens.append(0) #DestrezaArma4		31
	itens.append(0) #ManaArma4		32
	itens.append(0) #ElementoArma4		33
	itens.append(0) #precoArma4		34
	itens.append(0) #ChanceStatus		35
	
	itens.append(0) #DanoFisicoArma5	36
	itens.append(0) #DanoMagicoArma5	37
	itens.append(0) #NomeArma5		38
	itens.append(0) #AgilidadeArma5		39
	itens.append(0) #DestrezaArma5		40
	itens.append(0) #ManaArma5		41
	itens.append(0) #ElementoArma5		42
	itens.append(0) #precoArma5		43
	itens.append(0) #ChanceStatus		44
	

	
	itens.append(0) #DefesaFisicaArmadura1	45
	itens.append(0) #DefesaMagicaArmadura1	46
	itens.append(0) #NomeArmadura1		47
	itens.append(0) #ElementoArmadura1	48
	
	itens.append(0) #DefesaFisicaArmadura2	49
	itens.append(0) #DefesaMagicaArmadura2	50
	itens.append(0) #NomeArmadura2		51
	itens.append(0) #ElementoArmadura2	52
	
	itens.append(0) #DefesaFisicaArmadura3	53
	itens.append(0) #DefesaMagicaArmadura3	54
	itens.append(0) #NomeArmadura3		55
	itens.append(0) #ElementoArmadura3	56
	
	itens.append(0) #DefesaFisicaArmadura4	57
	itens.append(0) #DefesaMagicaArmadura4	58
	itens.append(0) #NomeArmadura4		59
	itens.append(0) #ElementoArmadura4	60
	
	itens.append(0) #DefesaFisicaArmadura5	61
	itens.append(0) #DefesaMagicaArmadura5	62
	itens.append(0) #NomeArmadura5		63
	itens.append(0) #ElementoArmadura5	64
	


	itens.append(0) #LevelArma1             65
	itens.append(0) #LevelArma2             66
	itens.append(0) #LevelArma3             67
	itens.append(0) #LevelArma4             68
	itens.append(0) #LevelArma5             69

	itens.append(0) #LevelArmadura1         70
	itens.append(0) #LevelArmadura2         71
	itens.append(0) #LevelArmadura3         72
	itens.append(0) #LevelArmadura4         73
	itens.append(0) #LevelArmadura5         74




def add_item_bolsa(itens, item):
        if(itens[0] == 0):
                start = 0

        elif(itens[9] == 0):
                start = 9

        elif(itens[18] == 0):   
                start = 18

        elif(itens[27] == 0):
                start = 27
                
        elif(itens[36] == 0):
                start = 36


        itens[start] = item[0]
        itens[start + 1] = str(item[1])
        itens[start + 2] = str(item[2])
        itens[start + 3] = str(item[3])
        itens[start + 4] = str(item[4])
        itens[start + 5] = str(item[5])
        itens[start + 6] = str(item[6])
        itens[start + 7] = str(item[7])
        itens[start + 8] = str(item[8])


def add_armadura_bolsa(itens, item):
        if(itens[45] == 0):
                start = 45

        elif(itens[49] == 0):
                start = 49

        elif(itens[53] == 0):   
                start = 53

        elif(itens[57] == 0):
                start = 57
                
        elif(itens[61] == 0):
                start = 61

        itens[start] = item[0]
        itens[start + 1] = str(item[1])
        itens[start + 2] = str(item[2])
        itens[start + 3] = str(item[3])


        
                
	
