"""
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
"""

import json

def calcular_menor(dados):
    menor = dados[0]
    for valor in dados:
        if valor < menor:
            menor = valor
    return menor

def calcular_maior(dados):
    
    maior = dados[0]
    for valor in dados:
        if valor> maior:
            maior = valor
    return maior

with open("dados.json","r") as arquivo:
    dados = json.load(arquivo)
    
dias_uteis =[dia["valor"] for dia in dados if dia ["valor"]>0]

menor_fatura = calcular_menor(dias_uteis)
maior_fatura = calcular_maior(dias_uteis)
media_fatura = sum (dias_uteis)/len(dias_uteis)
dias_acima_da_media =sum(1 for valor in dias_uteis if valor > media_fatura)
        
print(f"Menor faturamento: R${menor_fatura:.2f}")
print(f"Maior faturamento: R${maior_fatura:.2f}")
print(f"Número de dias acima da media; {dias_acima_da_media}")