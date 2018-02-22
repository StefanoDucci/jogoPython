def cria_personagem_generico(personagem, classe):
    del personagem [:]
        
    personagem.append(30) # VidaMax          0
    personagem.append(5) # ManaMax           1
    personagem.append(30) # VidaAtual        2
    personagem.append(0) # ManaAtual         3
        
    personagem.append(0)  # DanoFisico        4
    personagem.append(0)  # DanoMagico        5
    personagem.append(0)  # TaxaAcertoCtit    6
    personagem.append(0)  # TaxaEsquiva       7
        
    personagem.append(0)  # Defesa            8
    personagem.append(0)  # DefesaMagica      9
        
    personagem.append(0) #ArmaDanoFisiico    10
    personagem.append(0) #ArmaDanoMagico     11
        
    personagem.append(0) # Armadura          12
    personagem.append(0) # DefMagica         13

    personagem.append(5) # PoçãoVidaMax          14
    personagem.append(5) # PoçãoManaMax          15
    personagem.append(0) # PoçãoVidaAtual        16
    personagem.append(0) # PoçãoManaAtual        17

    personagem.append(0) # XP                    18
    personagem.append(1) # Level                 19
        
    personagem.append(0) # Indice Habilidade1    20
    personagem.append(0) # Dano Habilidade1      21
    personagem.append(0) # CustoHabilidade1      22
    personagem.append(0) # ElementoHabilidade1   23
        
    personagem.append(0) # Indice Habilidade2    24
    personagem.append(0) # Dano Habilidade2      25
    personagem.append(0) # CustoHabilidade2      26
    personagem.append(0) # ElementoHabilidade2   27
        
    personagem.append(0) # Indice Habilidade3    28
    personagem.append(0) # Dano Habilidade3      29
    personagem.append(0) # CustoHabilidade3      30
    personagem.append(0) # ElementoHabilidade3   31
        
    personagem.append(0) # Indice Habilidade4    32
    personagem.append(0) # Dano Habilidade4      33
    personagem.append(0) # CustoHabilidade4      34
    personagem.append(0) # ElementoHabilidade4   35
        
    personagem.append(0) # Indice Habilidade5    36
    personagem.append(0) # Dano Habilidade5      37
    personagem.append(0) # CustoHabilidade5      38
    personagem.append(0) # ElementoHabilidade5   39
        
    personagem.append(classe) # Classe           40
        
    personagem.append(0) # StatusHabilidade 1    41
    personagem.append(0) # ChanceStatusHabi 1    42
        
    personagem.append(0) # StatusHabilidade 2    43
    personagem.append(0) # ChanceStatusHabi 2    44
        
    personagem.append(0) # StatusHabilidade 3    45
    personagem.append(0) # ChanceStatusHabi 3    46
        
    personagem.append(0) # StatusHabilidade 4    47
    personagem.append(0) # ChanceStatusHabi 4    48
        
    personagem.append(0) # StatusHabilidade 5    49
    personagem.append(0) # ChanceStatusHabi 5    50
    
    personagem.append(0) # AgilidadeDaArma       51
    personagem.append(0) # DestrezaArma          52
    personagem.append(0) # ManaArma              53
    personagem.append(0) # ManaMaxima2           54
    
    personagem.append(0) # StatusEmBatalha       55
    
    personagem.append(0) # Dinheiro              56
    
    personagem.append(0) # Elemento Arma         57
    personagem.append(0) # Elemento Armadura     58
    
    personagem.append(0) # NumeroInimigosHab1    59
    personagem.append(0) # NumeroInimigosHab2    60
    personagem.append(0) # NumeroInimigosHab3    61
    personagem.append(0) # NumeroInimigosHab4    62
    personagem.append(0) # NumeroInimigosHab5    63
    
    personagem.append(0) # NomeArma	         64
    personagem.append(0) # NomeArmadura          65

    personagem.append(0) # ChanceStatusArma      66

    
    personagem.append(0) # Tipo de Pet           67
    personagem.append(0) # Vida do Pet           68
    personagem.append(0) # Defesa do Pet         69
    personagem.append(0) # Dano do Pet           70
    personagem.append(0) # Elemento do Pet       71
    personagem.append(0) # Level do Pet          72
    personagem.append(0) # Exp do Pet            73

    personagem.append(0) # Nivel da Arma         74
    personagem.append(0) # Nivel da Armadura     75

    personagem.append(0) # Nivel Habilidade1     76
    personagem.append(0) # Nivel Habilidade2     77
    personagem.append(0) # Nivel Habilidade3     78
    personagem.append(0) # Nivel Habilidade4     79
    personagem.append(0) # Nivel Habilidade5     80

    personagem.append(0) # DanoFisicoArmaMao2    81
    personagem.append(0) # DanoMagicoArmaMao2    82
    personagem.append(0) # ElementoArmaMao2      83
    personagem.append(0) # StatusArmaMao2        84
    personagem.append(0) # ChanceStatusMao2      85
    personagem.append(0) # LevelArmaMao2         86
    personagem.append(0) # NomeArmaMao2          87
    personagem.append(0) # AgilidadeArmaMao2     88
    personagem.append(0) # DestrezaArmaMao2      89
    personagem.append(0) # ManaArmaMao2          90
    personagem.append(0) # DefesaArmaMao2        91

    
    

    

def altera_status_por_classe(personagem):
    if(personagem[40] == 1):
        personagem[0] = 25 # VidaMaxima
        personagem[1] = 30 # ManaMaxima
        personagem[2] = 25 # VidaAtual
        personagem[3] = 30 # ManaAtual
        personagem[4] = 0  # DanoFisico
        personagem[5] = 10  # DanoMagico
        personagem[6] = 0  # Destreza
        personagem[7] = 0  # Agilidade
        personagem[8] = 5  # DefesaFisica
        personagem[9] = 10  # DefesaMagica
        personagem[54] = personagem[1] + personagem[53]
        

    elif(personagem[40] == 2):
        personagem[0] = 30 # VidaMaxima
        personagem[1] = 20 # ManaMaxima
        personagem[2] = 30 # VidaAtual
        personagem[3] = 20 # ManaAtual
        personagem[4] = 10  # DanoFisico
        personagem[5] = 0  # DanoMagico
        personagem[6] = 2  # Destreza
        personagem[7] = 2  # Agilidade
        personagem[8] = 10  # DefesaFisica
        personagem[9] = 5  # DefesaMagica
        personagem[12] = 5 # DefesaFisicaArmadura
        personagem[54] = personagem[1] + personagem[53]
        
        
    elif(personagem[40] == 3):
        personagem[0] = 25 # VidaMaxima
        personagem[1] = 25 # ManaMaxima
        personagem[2] = 25 # VidaAtual
        personagem[3] = 25 # ManaAtual
        personagem[4] = 10 # DanoFisico
        personagem[5] = 0  # DanoMagico
        personagem[6] = 15 # Destreza
        personagem[7] = 15 # Agilidade
        personagem[8] = 5  # DefesaFisica
        personagem[9] = 5  # DefesaMagica
        personagem[54] = personagem[1] + personagem[53]

    
    elif(personagem[40] == 4):
        personagem[0] = 1 # VidaMaxima
        personagem[1] = 30 # ManaMaxima
        personagem[2] = 1 # VidaAtual
        personagem[3] = 30 # ManaAtual
        personagem[54] = personagem[1] + personagem[53]
        personagem[20] = 16
        personagem[24] = 17
        personagem[28] = 18
        personagem[32] = 19
        personagem[36] = 20
        
        personagem[59] = 1
        personagem[60] = 1
        personagem[61] = 1
        personagem[62] = 1
        personagem[63] = 1
        
        personagem[22] = 10
        personagem[26] = 10
        personagem[30] = 10
        personagem[34] = 10
        personagem[38] = 10

        


def nome_classe(classe):
	if(classe == 1):
		return "Mago"
	
	if(classe == 2):
		return "Guerreiro"
	
	if(classe == 3):
		return "Gatuno"

	if(classe == 4):
		return "Druida"

	
