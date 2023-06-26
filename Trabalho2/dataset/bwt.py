from time import time

def ler_BWT(nome_ficheiros):
    inicio_tempo = time()
    
    string_bwt = BWT(nome_ficheiros)
    
    novo_nome = 'BWT_' + nome_ficheiros
    novo_ficheiro = open(novo_nome, 'w')
    
    novo_ficheiro.write(string_bwt)
    total_time_bwt = time() - inicio_tempo
    
    return novo_nome, total_time_bwt

##https://github.com/aaroncoyner/bwt

def BWT(nome_ficheiros):
    BUF = 10000
    write = ''
    fich = open(nome_ficheiros, 'r')
    
    while True:
        sequence = fich.read(BUF)
        if not sequence:
            break
        sequence += '$'
        table = [sequence[index:] + sequence[:index] for index, _ in enumerate(sequence)]
        table.sort()
        bwt = [rotation[-1] for rotation in table]
        bwt = ''.join(bwt) 
        write += bwt
    
    return write