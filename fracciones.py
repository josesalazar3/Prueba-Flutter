def fracc(arreglo: list):
    ceros = 0
    menores = 0
    mayores = 0
    for i in arreglo:
        if i == 0:
            ceros = ceros + 1
        elif i > 0:
            mayores = mayores + 1
        else: 
            menores = menores + 1
        
    print(f'positives: {mayores/len(arreglo)}')
    print(f'negatives: {menores/len(arreglo)}')
    print(f'zeros: {ceros/len(arreglo)}')

lista = [-4, 3, -9, 0, 4, 1]
fracc(lista)


        
         