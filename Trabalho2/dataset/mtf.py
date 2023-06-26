from time import time

SYMBOLTABLE = [chr(i) for i in range(255)]


def ler_MTF(nome_ficheiros):
    inicio_tempo = time()
    
    ficheiro = open(nome_ficheiros, 'r')
    string = ficheiro.read()
    
    list_mtf = MTF_compressao(string)
    string_mtf = ''
    for i in list_mtf:
        string_mtf += str(i)
        string_mtf += ' '
        
    novo_nome = 'MTF_' + nome_ficheiros       
    novo_ficheiro = open(novo_nome, 'w')
    novo_ficheiro.write(string_mtf)
    
    total_time_bwt = time() - inicio_tempo

    return novo_nome, total_time_bwt
    
##https://titanwolf.org/Network/Articles/Article?AID=2fb527a4-b1a2-4e05-8f56-ad861e0f480e

def MTF_compressao(string):
    sequence, pad = [], SYMBOLTABLE[::]
    for char in string:
        indx = pad.index(char)
        sequence.append(indx)
        pad = [pad.pop(indx)] + pad
    return sequence

def MTF_decode(sequence):
    chars, pad = [], SYMBOLTABLE[::]
    for indx in sequence:
        char = pad[indx]
        chars.append(char)
        chars.append(' ')
        pad = [pad.pop(indx)] + pad
    return ''.join(chars)   


