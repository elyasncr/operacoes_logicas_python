"""
Loop for
Loop -> Estrutura de repetição.
For -> Uma dessas estruturas.

C ou Java

for(int i = 0; i<10; i++){
    //execução do loop
}

Python

for item in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis:
- String
    nome = 'elyas'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros= range(1, 10)

"""

nome = 'elyas'
lista = [1, 3, 5, 7, 9]
numero = range(1, 10)
"""
#Exemplo de For 1:
for letra in nome:
    print(letra)

#Exemplo de For 2:
for numero in lista:
    print(numero)

#Exemplo de For 3 (Iterando sobre um Range)

range(valor_inicial, valor_final)

obs: o valor final não é incluido
ex: range(1, 10)
entra: (1,2,3,4,5,6,7,8,9) mas não entra o 10.

#Exemplo de for 4
for numero in range(1, 10):
    print(numero)
enumerate:
((0, 'e'), (1, 'l'), (2, 'y'), (3, 'a'), (4, 's')
for indice, letra in enumerate(nome):
    print(nome(indice))

for _, letra in enumerate(nome):
    print(letra)
        obs: quando não precisamos de um valor, podemos descartá-lo utilizando um underline (_)

for i, v, in enumerate(nome):
    print(nome[i])

for _, letra in enumerate(nome):
    print(letra)
#Exemplo de FOR 5

qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0
for n in range(1, qtd):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma= soma + num
print(f'A soma é {soma}')
"""

# original: U+1F63B
# modificado: U0001F63B
emoji = 'U0001F60D'
for x in range(3):
    for num in range(1, 11):
        print('\U0001F60D' * num)