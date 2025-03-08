#%%
class LeitorNA:
    def __init__(self, fita):
    
        self.fita = fita.upper()
        self.contagem = {'A': 0, 'T': 0, 'G': 0, 'C': 0, 'U': 0}
        erro = self.validar_fita()
        if erro:
            self.erro = erro
        else:
            self.erro = None

    def validar_fita(self):
        fita = self.fita
        bases_validas = {'A', 'T', 'C', 'G', 'U'}
        bases_invalidas = set(fita) - bases_validas
        if bases_invalidas:
            return(f"Verifique novamente a sequência de bases nitrogenadas, pois {', '.join(bases_invalidas)} não é uma base válida.")
    
        elif {'T', 'U'}.issubset(fita):
            return ValueError("Algo está errado, pois a fita contém tanto Timina (T) quanto Uracila (U). Logo, não pode ser nem DNA nem RNA.")


    #Escreva um programa que recebe uma sequência de DNA e retorna o fio complementar (A ↔ T, C ↔ G).
    def complementoDNA(self):
        if self.erro:
            return self.erro
        pares = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
        complemento = ''.join(pares[n] for n in self.fita)

        return complemento
    
    #Crie um programa que recebe uma sequência de DNA e retorna a contagem de cada base nitrogenada.
    def contagem_de_base(self, format = False):
        if self.erro:
            return self.erro
        
        if format:
            return '\n'.join(f'{base}: {self.contagem[base]}' for base in self.contagem)
        else:
            for n in self.fita:
                self.contagem[n] += 1
            return self.contagem
            
    #Transforme uma sequência de DNA em RNA substituindo T por U.
    def ConverterNA(self):
        if self.erro:
            return self.erro
        if 'T' in self.fita:
            resultado = ''.join('U' if n == 'T' else n for n in self.fita)
        if 'U' in self.fita:
            resultado = ''.join('T' if n == 'U' else n for n in self.fita)
        
        return resultado

#%%
#A proporção GC indica a quantidade de Guanina (G) e Citosina (C) em relação ao tamanho total da sequência.

def propGC(fita):
    fita = fita.upper()
    bases_validas = {'A', 'T', 'G', 'C', 'U'}
    bases_invalidas = set(fita) - bases_validas
    if bases_invalidas:
        return f'verifique novamente a sequencia de bases nitrogenadas pois {', '. join(bases_invalidas)} não é uma base nitrogenada'
    
    if {'T', 'U'}.issubset(fita):
        return 'Algo está errado pois existem ambas Timina e Uracila nesta fita, logo não é nem DNA nem RNA'
    
    contagem = {'A': 0, 'T': 0, 'G': 0, 'C': 0, 'U': 0}

    for n in fita:
        contagem[n] += 1
        

    proportionGC = ((contagem['G'] + contagem['C']) / (sum(contagem.values()))) * 100
    return f'{proportionGC:.3f} '

print(propGC("ATCGGC"))
# %%
#Os códons de início e fim são fundamentais na tradução do RNA em proteínas. No DNA, o códon de início é sempre ATG, enquanto os códons de parada podem ser TAA, TAG ou TGA.
#Crie um programa que identifique onde um gene começa e onde ele termina em uma sequência de DNA.

#%%
fita = LeitorNA("AATGCCTG")
print(fita.complementoDNA())
print(fita.contagem_de_base())
print(fita.contagem_de_base(format = True))
print(fita.ConverterNA())