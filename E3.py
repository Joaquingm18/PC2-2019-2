import os
os.system("cls")

a=[]
b=[]
c=[]
cant1=0
cant2=0
while len(a)<5 and len(b)<5 and len(c)<5:

    nombre=input("Ingrese su nombre: ")
    a.append(nombre)
    sexo = input("Ingrese su sexo: ")
    if sexo=="masculino" or sexo =="femenino":
        b.append(sexo)
        if sexo=="masculino":
            cant1= cant1+1
        else:
            cant2=cant2+1    
    else:
        print("Especifique sexo ya sea masculino o femenino. ")        
    edad = int(input("Ingrese su edad: "))
    if edad >=5 and edad <=17:
        c.append(edad)
    else:
        print("Edad no en rango. ")    
        
z=0
for i in c:
    z=s+i
z=z/5
print("Las personas inscritas son: ")
print(a)
print(b)
print(c)
print("")
print("La cantidad de hombres son:"+ str(cant1))
print("")
print("La cantidad de mujeres son:"+ str(cant2))
print("")
print("La edad promedio de personas registradas son: "+ str(z))
