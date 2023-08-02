operacao = input("Digite a operação:\n1 - Depósito\n2 - Saque\n3 - Extrato\n4 - Sair\n\n")
saldo = 100
lista_depositos = []
lista_saques = []
saque_permitido_no_dia = 500
while operacao != 4:
    if operacao == "1":
        deposito = float(input("Digite o valor do depósito: "))
        while deposito <= 0:
            print("Valor inválido!")
            deposito = float(input("Digite o valor do depósito: "))
        saldo = saldo + deposito
        lista_depositos.append(deposito)
        print("Deposito realizado com sucesso!\n")
        operacao = input("Deseja realizar outra opeção?\n1 - Depósito\n2 - Saque\n3 - Extrato\n4 - Sair\n\n")
    elif operacao == "2":
        saque = float(input("Digite o valor do saque: "))
        while saque <= 0:
            print("Valor inválido! Saques devem ser maiores que zero.")
            saque = float(input("Digite o valor do saque: "))
        while saque > saldo:
            print(f'Saldo insuficiente! Seu saldo é de R${saldo:,.2f}')
            saque = float(input("Digite o valor do saque: "))
        saque_permitido_no_dia -= saque
        if saque_permitido_no_dia <= 0:
            print(f'Valor de saque não permitido, saque máximo permitido é de R${saque_permitido_no_dia + saque:,.2f}\n')
            operacao = input("Deseja realizar outra opeção?\n1 - Depósito\n3 - Extrato\n4 - Sair\n\n")
        saldo = saldo - saque
        lista_saques.append(saque)
        print("Saque realizado com sucesso!\n")
        operacao = input("Deseja realizar outra opeção?\n1 - Depósito\n2 - Saque\n3 - Extrato\n4 - Sair\n\n")
    elif operacao == "3":
        print(f'{"Saque":>5}   {"Depósito":>12}')
        maior_lista = max(len(lista_saques), len(lista_depositos))
        for i in range(maior_lista):
            if i >= len(lista_saques) and i < len(lista_depositos):
                print(f'{"-":>5}   {lista_depositos[i]:^12,.2f}')
            elif i >= len(lista_depositos) and i < len(lista_saques):
                print(f'{lista_saques[i]:>5,.2f}   {"-":>12}')
            else:
                print(f'{lista_saques[i]:>5,.2f}   {lista_depositos[i]:>12,.2f}')
        operacao = input("Deseja realizar outra opeção?\n1 - Depósito\n2 - Saque\n3 - Extrato\n4 - Sair\n\n")
    elif operacao == "4":
        print("Obrigado!")
        break
    else:
        print("Operação inválida!")
        operacao = input("Digite a operação:\n1 - Depósito\n2 - Saque\n3 - Extrato\n4 - Sair\n\n")
