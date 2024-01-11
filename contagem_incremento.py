print('Contagem de números com incremento\n')
#Feito por Jennifer Lima

num1 = float(input('Digite um número inicial: '))
num2 = float(input('Digite um número final: '))
num3 = float(input('Digite um número de incremento: '))
#Convertido em tipo float para caso o usuário quiser fazer uma contagem de números decimais.

#Tratamento de Erros
if num1 > num2:
    print('ERROR! O número inicial deve ser menor que o final.')
elif num1 == num2:
    print('ERROR! Impossível realizar contagem com números iguais.')
elif num3 < 0:
    print('ERROR! Não será possível somar com o incremento negativo.')

#Função para Contagem
while num1 < num2 and num3 >= 0:
    num1 += num3
    
    #Tratamento de erro sobre exceder o número final
    if num1 > num2:
        print('\nFim da contagem')
    else:
        print(num1)