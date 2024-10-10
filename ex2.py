#2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’,
#  seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

def verifica_a(string):
    return string.lower().count('a')

string = input("Digite uma string: ")
if verifica_a(string):
    print(f"A letra 'a' aparece {verifica_a(string)} vezes na string")
else:
    print("A letra 'a' não aparece na string")