import os
os.system('cls')

print(30*'=')
# turno = int(input('Informe o número do turno :'))

# match turno:
#     case 1:
#         print('Manhã!')
#     case 2:
#         print('Tarde!')
#     case 3:
#         print('Noite!')
#     case _:
#         print('Turno inválido!')

# mes = int(input('Informe um número para descobrir o mês correspondente :'))

# match mes:
#     case 1:
#         print('Janeiro')
#     case 2:
#         print('Fevereiro')
#     case 3:
#         print('Março')
#     case 4:
#         print('Abril')
#     case 5:
#         print('Maio')
#     case 6:
#         print('Junho')
#     case _:
#         print('Digite entre 1 e 6!')

# print("\n[1] Chinês \n[2] Italiano \n[3] Mexicano \n[4] Vegetariano: \n")
# rest = int(input('Informe seu restaurante de preferência e receba uma recomendação :'))

# match rest:
#     case 1:
#         print('Que tal um Yakisoba?')
#     case 2:
#         print('Que tal uma macarronada?')
#     case 3:
#         print('O que acha de um Taco?')
#     case 4:
#         print('O que acha de uma salada?')
#     case _:
#         print('Opção inválida!')

opcao1 = int(input('Informe um número :'))
print(f'A opção que você escolheu foi {opcao1}')

opcao2 = int(input('Informe um número entre 1 e 4 : '))

print("\n[1] Soma 1 ao valor inicial \n[2] Subtrai 1 do valor inicial \n[3] Lista os valores escolhidos \n[4] Sair: \n")

match opcao2:
    case 1:
        print(f'Sua escolha resultou em: {opcao1 + 1}')
    case 2:
        print(f'Sua escolha resultou em: {opcao1 - 1}')
    case 3:
        print(f'Suas escolhas foram: {opcao1} e {opcao2}')
    case 4:
        print('Saindo...')
    case _:
        print('Opção Inválida!')
