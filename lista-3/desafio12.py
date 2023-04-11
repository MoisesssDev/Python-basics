salario = 1000
aumento = 0.015 # 1,5% de aumento em 2011

for ano in range(2011, 2018):
    salario += salario * aumento

for ano in range(2018, 2023):
    aumento *= 2
    salario += salario * aumento
print( round(salario, 2))
