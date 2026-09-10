n = int(input("Digite um número: "))
for i in range(n):
    for j in range(n-i):
        print("*", end="")
    print()