p1=(int(input("Primeira palavra:")))
p2=(int(input("Segunda palavra:")))
p3=(int(input("Terceira palavra:")))

if p1 == "invertebrado":
    if p2 =="inseto":
        if p3 == "hematofago":
            print("pulga")
        elif p3 == "herbivoro":
            print("lagarta")
    elif p2 == "anelidio":
        if p3 == "hematofogo":
            print("sanguessuga")
        elif p3 == "onivoro":
            print("minhoca")
elif p1 == "vertebrado":
    if p2 =="mamifero":
            if p3 == "herbivoro":
                print("vaca")
            elif p3 == "onivoro":
                print("homem")
    elif p2 == "ave":
            if p3 == "carnivoro":
                print("aguia")
            elif p3 == "onivoro":
                print("pomba")




a = int(input("digite um numero de lados:"))

if a == 3:
     print ("3")
     print("triângulo")
elif a == 4:
     print ("4")
     print("quadrado")
elif a == 5:
     print ("5")
     print("pentágono")
elif a == 6:
     print ("6")
     print("hexágono")
elif a == 7:
     print ("7")
     print("heptágono")
elif a == 11:
     print("11")
     print("Erro!")
elif a == 15:
     print("15")
     print("Erro!")