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

# Função para calcular o imposto de renda
def calcula_irpf(sal_bruto,num_dependentes,desc_inss):
	# Calcula o valor de desconto por dependetes
	desc_dependentes = num_dependentes * 100

	# Calcula o salário base
	sal_base = sal_bruto - (desc_inss + desc_dependentes)

	# Testa a faixa de desconto em que o funcionário está
	# e atribui o valor à variável desc_irpf
	if(sal_base < 2000):
		desc_irpf = 0
	
	elif(sal_base > 2000 and sal_base < 5000):
		desc_irpf = sal_base * 0.15

	elif(sal_base > 5000):
		desc_irpf = sal_base * 0.275

	return sal_base,desc_dependentes,desc_irpf

# Solicita os dados ao usuário
sal_bruto = float(input("Digite o valor do salario bruto: "))
num_dependentes = int(input("Digite o número de dependentes: "))

# calcula o valor do desconto do INSS e atribui à variável desc_inss 
desc_inss = float(calcula_inss(sal_bruto))

# Calcula o valor do salário base, o desconto por denpendentes
# e o desconto do IRPF 
sal_base,desc_dependentes,desc_irpf = calcula_irpf(sal_bruto,num_dependentes,desc_inss)

# Calcula salário líquido e atribui à variável sal_liquido
sal_liquido = sal_bruto - (desc_inss + desc_dependentes + desc_irpf)

# imprime o bilhete de pagamento
print("Salário bruto: R$ %.2f"%(sal_bruto))
print("Desconto do INSS: R$ %.2f"%(desc_inss))
print("Desconto por dependentes: R$ %.2f"%(desc_dependentes))
print("Desconto IRPF: R$ %.2f"%(desc_irpf))
print("Salário líquido: R$ %.2f"%(sal_liquido))
