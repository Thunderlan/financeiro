#!/usr/bin/python
# -*- coding: utf-8 -*-

# Função para calcular o salario bruto
def calcula_inss(sal_bruto):
	# atribui o percentual de desconto à variável percent_desc
	percent_desc = 0.11

	# calcula o valor do desconto e atribui à variável desc_inss
	desc_inss = sal_bruto * percent_desc

	# retorna desc_inss
	return desc_inss

# Solicita os dados ao usuário
sal_bruto = float(input("Digite o valor do salario bruto: "))
num_dependentes = int(input("Digite o número de dependentes: "))

# calcula o valor do desconto do INSS e atribui à variável desc_inss 
desc_inss = float(calcula_inss(sal_bruto))

# imprime o valor do desconto
print("Desconto do INSS: R$ %.2f"%(desc_inss))

