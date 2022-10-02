import random

#Definimos a classe jogo.
class jogo:
    def __init__(self, escolha_ia, escolha_user):
        self.escolha_ia = escolha_ia
        self.escolha_user = escolha_user
        
    #Criamos o método jogar, com todas as validações.        
    def jogar(self):    
        if self.escolha_user=='PEDRA' and self.escolha_ia== 'TESOURA':
            print(f'Você ganhou! A {self.escolha_user} ganha da {self.escolha_ia}')
        elif self.escolha_user=='PAPEL' and self.escolha_ia== 'PEDRA':
            print(f'Você ganhou! O {self.escolha_user} ganha da {self.escolha_ia}')
        elif self.escolha_user=='TESOURA' and self.escolha_ia== 'PAPEL':
            print(f'Você ganhou! A {self.escolha_user} ganha do {self.escolha_ia}')
        
        elif self.escolha_ia=='PEDRA' and self.escolha_user== 'TESOURA':
            print(f'Você perdeu! A {self.escolha_ia} ganha da {self.escolha_user}')
        elif self.escolha_ia=='PAPEL' and self.escolha_user== 'PEDRA':
            print(f'Você perdeu! O {self.escolha_ia} ganha da {self.escolha_user}')
        elif self.escolha_ia=='TESOURA' and self.escolha_user== 'PAPEL':
            print(f'Você perdeu! A {self.escolha_ia} ganha do {self.escolha_user}')
            
        else:
            print('\nDeu empate.\n')

#Game loop.
jogar = True
while jogar == True:
    ppt=['Pedra', 'Papel', 'Tesoura'] 
    #Definimos o valor da máquina com o método random.choice         
    escolha_ia = str(random.choice(ppt).upper())
    
    #Jogador define Pedra, Papel ou Tesoura.
    escolha_user = str(input('Escolha Pedra, Papel ou Tesoura: ').upper())
    
    #Verifica se o jogador digitou Pedra, Papel ou Tesoura.    
    if escolha_user != 'PEDRA' and escolha_user != 'PAPEL' and escolha_user != 'TESOURA':
        print('\nDigite Pedra, Papel ou Tesoura.\n')
    else:
        #Se o jogador digitou corretamente os valores, instanciamos um objeto a partir da classe criada.    
        jogoppt = jogo(escolha_ia, escolha_user)
        #Chamamos o objeto com o método jogar.
        jogoppt.jogar() 
        
        #Verificar se o jogador quer jogar novamente ou não.
        try:    
            jogar = int(input('\n\nSe quiser jogar novamente aperte 1, para sair aperte qualquer outro número: '))
            if jogar == 1:
                jogar = True
            else:
                jogar = False
        except ValueError:
            print('Digite 1 para jogar novamente ou outro número para deixar de jogar.')
    
            
    
    
    
            

        
        
    
        



            




       
         
            
    
            
            
        
        
        