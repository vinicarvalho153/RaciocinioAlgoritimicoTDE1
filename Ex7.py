VariavelHora = int(input("Digite as hora: "))
variavelMinutos = int(input("Digite os minutos: "))
variavelSegundos = int(input("Digite os segundos: "))
variavelHoraMinutos = VariavelHora * 60
minutosTotal = variavelHoraMinutos + variavelMinutos
minutosSegundos = minutosTotal * 60
totalSegundos = minutosSegundos + variavelSegundos
print("Ja passou {} minutos desde o início do dia.".format(minutosTotal))
print("Passaram {} segundos desde o início do dia." .format(totalSegundos))
