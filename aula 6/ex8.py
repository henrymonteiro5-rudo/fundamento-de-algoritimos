n = int(input("Digite um número: "))
i = 2
while i < n:
    if n % i == 0:
        break
    i += 1
else:
    print(n)