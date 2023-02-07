def jugar(dado1: int, dado2: int, dado3: int):
  
  lista = [dado1, dado2, dado3]

  ocurrencias = lista.count(dado1)

  match ocurrencias:
    case 2: # Si son 2 números iguales, deberás retornar el número multiplicado por 2
      resultado = dado1*2
    case 3: # Si recibes 3 dados con el mismo número, deberás retornar el número multiplicado por 3
      resultado = dado1*3
    case _: # Si no hay número iguales, deberás retornar el número más grande de ellos
      resultado = max(lista)

  return resultado

print(jugar(1,1,2))
