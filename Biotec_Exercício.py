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

print(complementoDNA("ATCG"))  
print(complementoDNA("AUGC"))  
print(complementoDNA("ATXG"))



#%%
#Crie um programa que recebe uma sequência de DNA e retorna a contagem de cada base nitrogenada.

def contagem_de_base(fita):
    fita = fita.upper()
    Adenosina = 0
    Timina = 0
    Guanina = 0
    Citosina = 0
    Uracila = 0

    bases_validas = {'A', 'T', 'C', 'G', 'U'}
    bases_invalidas = set(fita) - bases_validas
    if bases_invalidas:
        return f'verifique novamente a sequencia de bases nitrogenadas pois {', '. join(bases_invalidas)} não é uma base nitrogenada'
    
    for n in fita:
        if n == 'A':
            Adenosina += 1
        elif n == 'T':
            Timina += 1
        elif n == 'G':
            Guanina += 1
        elif n == 'C':
            Citosina += 1
        elif n == 'U':
            Uracila += 1
    return f'''Adenosina: {Adenosina}
Timina: {Timina}
Guanina: {Guanina}
Citosina: {Citosina}
Uracila: {Uracila}
'''

print(contagem_de_base('AATGCCGT'))







#%%
#Transforme uma sequência de DNA em RNA substituindo T por U.

def ConverterNA(fita):
    fita = fita.upper()
    bases_validas = {'A', 'T', 'G', 'C', 'U'}
    bases_invalidas = set(fita) - bases_validas

    lista = []

    if bases_invalidas:
        return f'verifique novamente a sequencia de bases nitrogenadas pois {', '. join(bases_invalidas)} não é uma base nitrogenada'
    
    if 'T' in fita:
        for n in fita:
            if n == 'T':
                lista.append('U')
            else:
                lista.append(n)
    else:
        for n in fita:
            if n == 'U':
                lista.append('T')
            else:
                lista.append(n)
    return lista

pprint(ConverterNA("ATCG"))  
print(ConverterNA("AUGC"))  
print(ConverterNA("ATXG"))






#%%
#A proporção GC indica a quantidade de Guanina (G) e Citosina (C) em relação ao tamanho total da sequência.

