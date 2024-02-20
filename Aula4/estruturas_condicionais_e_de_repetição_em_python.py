saldo = 2000.0
saque =float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("valor sacado!")
    print("retire o seu dinehiro na boca do caixa")
    
#if saldo < saque:
else:
    print("você não pode sacar o dinheiro")



opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))

elif opcao == 2:
    print("Exibindo o extrato....")
else:
    sys.exit("Opção inválida")