import random
from re import S  #Utilizamos a classe random.

def adivinhar():
    numero_secreto = random.randint(1, 10)  #Definimos o número secreto com o método randint no range de 1 até 15.
    numero_usuario = 0
    tentativa = 1
    win = False
    
    
    #Mostramos essa mensagem na tela
    print('\n\nEsse é o game de adivinhar o número, você tem 3 tentativa para acertar o número de 1 até 15.\nBoa sorte!!\n')
    
    #Aqui começa nosso loop, enquanto o número for diferente e o número de tentativas for menor ou igual a 3.
    while numero_usuario != numero_secreto and tentativa <= 3:                                             
        print(f'Essa é a sua tentativa de Nº {tentativa}.')      #Mostramos ao usuário qual o número da tentativa dele.
        
        
        try:
            numero_usuario = int(input('Qual o número secreto?  '))  #Pedimos que ele tente acertar o número secreto.
            
            if numero_usuario == numero_secreto:  #Se o usuário acerta o número.
                print('\nParabéns! Você acertou!\n')
                win = True
                break
            else:                                 #Se o usuário erra o número, validamos se o número digitado é maior ou menor que o número secreto.
                if numero_usuario > numero_secreto:
                    print('\nInfelizmente você errou, seu número é maior do que o número secreto.\n')
                else:
                    print('\nInfelizmente você errou, seu número é menor do que o número secreto.\n')
                
            tentativa+=1  #Adicionamos +1 a tentativa.
        
        #Se o jogador digitar um valor que não seja número inteiro.    
        except ValueError:  
            print('\nDigite um valor válido!!!\n')
    
    
    
    #Caso o jogador tenha perdido o jogo.        
    if win == False:
        print('\nInfelizmente você perdeu, tente novamente!!\n')
    else:
        pass      
        

                        
adivinhar()