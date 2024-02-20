saldo, saque = (100, 50)
status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao relizar o saque")