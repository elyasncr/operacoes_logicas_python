"""
Estruturas Lógicas: and (e), or (ou), not (não), is (é)

Operadores unários:
    - not,
Operadores binários:
    - and, or, is

Regras de funcionamento:
Para o 'and', ambos os valores precisam ser true
para o 'or', um ou outro valor precisa ser true
para o 'not', o valor do booleano é invertido, ou seja, se for true, vira false, se for false vira true
para o 'is', o valor é comparado com um segundo.


"""
ativo = True
logado = False

if ativo:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')
else:
    print('Bem-vindo usuário')


print(ativo is True)