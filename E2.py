import os
os.system("cls")

def contraletra (texto,letra):
    for letra in texto:
        if letra.count(texto)==0:
            print(letra)
    return contraletra               


a= contraletra("holamundo", "o")
print(a)

b= contraletra("123456", "2")
print(b)

c= contraletra("lapractica", "a")
print(c)


