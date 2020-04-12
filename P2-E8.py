def es_primo(n):
    if n > 1:
        v = True
        for i in range(2, n):
            if (n % i) == 0:
                v = False
                break
    else:
        v = False
    return v

palabra = input('Ingrese una palabra: ')

contadores = {}
for letra in palabra.lower():
    if letra in contadores:
        cont = contadores[letra]
    else:
        cont = 0
    cont = cont + 1
    contadores[letra] = cont

primos = set()
for letra, cont in contadores.items():
    if es_primo(cont):
        primos.add(letra)
    if cont > 1:
        print('La letra \'' + letra + '\' aparece ' + str(cont) + ' veces')
    else:
        print('La letra \'' + letra + '\' aparece 1 vez')
    
print('Las siguientes letras aparecen un numero primo de veces: ' + str(primos))
