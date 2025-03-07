#%%
#Escreva um programa que recebe uma sequência de DNA e retorna o fio complementar (A ↔ T, C ↔ G).


def complementoDNA(fita):
    fita = fita.upper()
    complemento = []
    base = 0
    for n in fita:
        base += 1
        if n == 'A':
            complemento.append('T')
        elif n == 'T':
            complemento.append('A')
        elif n == 'C':
            complemento.append('G')
        elif n == 'G':
            complemento.append('C')
        elif n == 'U':
            return 'A fita apresentada é parte de um RNA'
        else:
            return f'A base nitrogenada {n} foi digitada de forma errada, por favor verifique: a base {base} '
            #futuramente inserir qual das bases foi digitada de forma errada
    return ''.join(complemento)

print(complementoDNA('ATCG'))



#%%
#Crie um programa que recebe uma sequência de DNA e retorna a contagem de cada base nitrogenada.


#%%
#Transforme uma sequência de DNA em RNA substituindo T por U.

#%%
#A proporção GC indica a quantidade de Guanina (G) e Citosina (C) em relação ao tamanho total da sequência.

