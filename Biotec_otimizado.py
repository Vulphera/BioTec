#%%
#Escreva um programa que recebe uma sequência de DNA e retorna o fio complementar (A ↔ T, C ↔ G).


def complemento_fita(fita):
    fita = fita.upper()
    complemento = []
    bases_validas = {'A', 'T', 'C', 'G', 'U'}
    bases_invalidas = set(fita) - bases_validas

    if bases_invalidas:
        return f'Bases inválidas encontradas: {', '.join(bases_invalidas)}. Verifique a sequência'
    if 'U' in fita:
        return 'A fita apresentada é parte de um RNA'
    
    pares = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    complemento = ''.join(pares[n] for n in fita)
    return complemento


print(complemento_fita(input("Digite uma sequência de bases nitrogenadas: ")))

#%%
#Crie um programa que recebe uma sequência de DNA e retorna a contagem de cada base nitrogenada.