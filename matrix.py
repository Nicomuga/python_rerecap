#Objetivo: dibujar una linea diagonal en un cuadrado 10 x 10

# El siguiente codigo imprime una matriz 10 x 10

for i in range(1,11):
    row= ""
    for j in range(1,11):
        if i==j or i+j == 11:
            row += "*"
        else:
            row += "-"
    print(row)