"""
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
"""


def  inverter(string):
    inverter =""
    for i in  range(len(string)-1,-1,-1):
        inverter += string[i]
        
    return inverter

texto = input ("digite  uma palavra: ")
texto_invesstido = inverter(texto)
print(f"o texto e {texto} e investido fica {texto_invesstido}")