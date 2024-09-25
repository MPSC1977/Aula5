print("\n[1] Sacar \n[2] Extrato \n[0] Sair: \n")

opcao = int(input('Resposta: '))

match opcao:
    case 1:
        print("Sacando...")
    case 2:
        print("Exibindo o extrato...")
    case 0:
        print("Saindo...")
    case _:
        print("Opção inválida!")