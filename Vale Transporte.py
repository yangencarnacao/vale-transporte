# n = int(input('Digite um numero: '))
# print("O dobro do {} é {}".format(n, n * 2))
# print("O triplo de {} é {}".format(n, n * 3))
# print("A raiz quadrada de {} é {:.0f}".format(n, pow(n, (1/2))))

#valorPassagem = float(input('Qual é o valor da sua passagem? '))
#diasTrabalhados = int(input('Quantos dias voce trabalhou? '))
#passagemIdaVolta = int(diasTrabalhados * 2)
#valorPagoPassagem = int(input('Quanto pagaram de passagem? '))
#print(f'Foram pagos {passagemIdaVolta // valorPassagem} dias de passagem')
#if valorPagoPassagem > passagemIdaVolta:
#    faltamPagar = int(valorPagoPassagem - passagemIdaVolta)
#else:
#    faltamPagar = int(passagemIdaVolta - valorPagoPassagem)
#print(f'Faltam te pagar {faltamPagar} reais')

valorPassagem: float = float(input('Qual é o valor da passagem? '))
valorDepositado = float(input('Quanto depositaram de passagem? '))
diasTrabahados = int(input('Quantos dias voce trabalhou presencialmente? '))
diasIdaVolta = int(diasTrabahados * 2)
print(f'Foram pagos {int(valorDepositado // valorPassagem) // 2} dias de passagem')
valorDevido = diasTrabahados * valorPassagem
faltamPagar = input(f'Faltam pagar {valorDepositado - valorDevido} reais')
# if valorDevido <= diasTrabahados:
#    print(f'Faltam te pagar {valorDevido - valorDepositado} reais')
# else:
#    pass
# print(f'Voce foi pago {valorDepositado - valorDevido :.2f} reais a mais de passagem')

