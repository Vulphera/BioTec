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
    def complementoDNA(self, format = False):
        if self.erro:
            return self.erro
        pares = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
        complemento = f'Fio principal:{self.fita}\nFio complementar:'if format else ''
        complemento += ''.join(pares[n] for n in self.fita)
        
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
    def ConverterNA(self, format = False):
        if self.erro:
            return self.erro
        
        resultado = f'Fio principal:{self.fita}\nFio convertido:' if format else ''

        if 'T' in self.fita:
            resultado += ''.join('U' if n == 'T' else n for n in self.fita)
        if 'U' in self.fita:
            resultado += ''.join('T' if n == 'U' else n for n in self.fita)
        
        return resultado

    #A proporção GC indica a quantidade de Guanina (G) e Citosina (C) em relação ao tamanho total da sequência.
    def propGC(self):
        if self.erro:
            return self.erro
        
        gc_total = sum(self.fita.count(base) for base in 'GC')
        total = len(self.fita)

        proportionGC = (gc_total / total) * 100
        return f'{proportionGC:.3f} '


    #Os códons de início e fim são fundamentais na tradução do RNA em proteínas. No DNA, o códon de início é sempre ATG, enquanto os códons de parada podem ser TAA, TAG ou TGA.
    #Crie um programa que identifique onde um gene começa e onde ele termina em uma sequência de DNA.
    def find_codon(self):
        if self.erro:
            return self.erro
        
        codon_inicio = 'ATG'
        codon_fim = {'TAA', 'TAG', 'TGA'}
        codons = []

        for cod in range(len(self.fita) - 2):
            trecho = self.fita[cod:cod+3]
            if trecho == codon_inicio:
                codons.append(f'Códon de início na posição {cod+1}')
            elif trecho in codon_fim:
                codons.append(f'Códon de parada na posição {cod+1}')

        return '\n'.join(codons) if codons else 'nenhum códon encontrado'
   

fita = LeitorNA("CGGATGCGTAGGTAATGACCTAG")
print(fita.complementoDNA())
print(fita.complementoDNA(format = True))
print(fita.contagem_de_base())
print(fita.contagem_de_base(format = True))
print(fita.ConverterNA())
print(fita.ConverterNA(format = True))
print(fita.propGC())
print(fita.find_codon())