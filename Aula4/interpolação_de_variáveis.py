nome = "João"
idade = 13
profissao = "Aluno"
linguagem = "Python"

print("Olá, me chamo %s. Eu tenho %d anos de idade, sou %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem ))

print("Olá, me chamo {}. Eu tenho {} anos de idade, sou {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem ))

print("Olá, me chamo {3}. Eu tenho {2} anos de idade, sou {1} e estou matriculado no curso de {0}.".format(nome, idade, profissao, linguagem ))