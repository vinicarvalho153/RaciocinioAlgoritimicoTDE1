inserirValorProduto = float(input("Digite o valor do produto: "))
valorComJuros = inserirValorProduto + (inserirValorProduto * 0.05)
valorParcelaComJuros = valorComJuros / 3
valorParcelaSemJuros = inserirValorProduto / 2
variavelValorVista = inserirValorProduto - (inserirValorProduto * 0.05)
print("3x com juros sai com o valor de R${}".format(valorComJuros), " com parcelas de R${}".format(valorParcelaComJuros))
print("2x sem juros sai com o valor de R${}".format(valorParcelaSemJuros))
print("Á vista sai com um desconto de R${}".format(variavelValorVista))