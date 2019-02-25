generator = (i ** 2 for i in range(10) if i % 2 == 0)
print(next(generator)) #saída 0
print(next(generator)) #saída 4
print(next(generator)) #saída 16
print(next(generator)) #saída 36
print(next(generator)) #saída 64
print(next(generator)) #Erro!