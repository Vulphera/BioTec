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


print(complemento_fita("ATCG"))  
print(complemento_fita("AUGC"))  
print(complemento_fita("ATXG"))

#%%
#Crie um programa que recebe uma sequência de DNA e retorna a contagem de cada base nitrogenada.

def contagem_de_base(fita):
    fita = fita.upper()
    contagem = {'A': 0, 'T': 0, 'G': 0, 'C': 0, 'U': 0}

    bases_validas = {'A', 'T', 'C', 'G', 'U'}
    bases_invalidas = set(fita) - bases_validas
    if bases_invalidas:
        return f'verifique novamente a sequencia de bases nitrogenadas pois {', '. join(bases_invalidas)} não é uma base nitrogenada'
    
    for n in fita:
        if n in contagem:
            contagem[n] += 1
    resultado = '\n'.join(f'{base}: {contagem[base]}' for base in contagem)

    return resultado

print(contagem_de_base('AATGCCGT'))

#%%

def ConverterNA(fita):
    fita = fita.upper()
    bases_validas = {'A', 'T', 'C', 'G', 'U'}
    bases_invalidas = set(fita) - bases_validas

    if bases_invalidas:
        return f'Verifique novamente a sequencia de bases nitrogenadas pois {', '.join(bases_invalidas)} não é uma base nitrogenada'
    
    if 'T' in fita:
        resultado = ''.join('U' if n == 'T' else n for n in fita)
    else:
        resultado = ''.join('T' if n == 'U' else n for n in fita)

    return resultado

print(ConverterNA("ATCG"))  
print(ConverterNA("AUGC"))  
print(ConverterNA("ATXG"))

# %%


