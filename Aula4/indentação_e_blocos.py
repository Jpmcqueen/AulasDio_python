def sacar(valor) -> None:
    saldo = 50

    if saldo >= valor:
      print("valor sacado!")
      print("retire o seu dinehiro na boca do caixa")
    
    if saldo < valor:  
       print("você não pode sacar o dinheiro")
    
    print("obrigado por ser nosso cliente, tenha um bom dia")
    

sacar(100)
