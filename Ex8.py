valorPi = 3.1415
variavelLitrosUmaLata = 5
precoDaLata = 50.00
ValorMetrosLitros = 3
valorMetrosLatas = variavelLitrosUmaLata * ValorMetrosLitros
variavelAltura = float(input("Digite a altura do cilindro em metros: "))
variavelRaio = float(input("Digite o raio do cilindro em metros: "))

valorBase = valorPi * (variavelRaio ** 2)
valorLateral = (2 * valorPi) * variavelRaio * variavelRaio
valorAreaTotal = ((2 * valorBase) + valorLateral)
numeroDeLatas = valorAreaTotal / valorMetrosLatas
print("Precisara de {} latas para pintar o cilindro.".format(numeroDeLatas))
print("O valor de gasto é de R$:{}".format(numeroDeLatas))
