import os
 
from time import time


def ler_LZW(nome_ficheiros, tempo):
    print("LZW")
    for i in range(len(nome_ficheiros)):
        print(nome_ficheiros[i])
        inicio_tempo = time()
        ficheiro = open(nome_ficheiros[i], 'r')
        string = ficheiro.read()
        
        string_LZW = LZW_compressao(string)
        
        novo_nome = 'LZW_' + nome_ficheiros[i]
        novo_ficheiro = open(novo_nome, 'w')
        novo_ficheiro.write(string_LZW)
   
        tamanho_original = os.path.getsize(nome_ficheiros[i])
        tamanho_final = os.path.getsize(novo_nome)
        ratio = tamanho_original/tamanho_final
        total_time_LZW = time() - inicio_tempo + tempo[i]
        
        print("Tamanho original do ficheiro ", nome_ficheiros[i], ": ", tamanho_original)
        print("Tamanho final do ficheiro ", novo_nome, ": ", tamanho_final)
        print("Tempo de compressão: ", total_time_LZW)
        print("Ratio de compressão: ", ratio, " :1")
        print()
    print('---------------------------------------------------------------')
    

##https://titanwolf.org/Network/Articles/Article?AID=f23d21ef-679b-4b3e-b86a-34eba1c736ce    

def LZW_compressao(text):
    
    dict_size = 256
    dictionary = dict((chr(i), i) for i in range(dict_size))
 
    w = ""
    result = []
    for c in text:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            dictionary[wc] = dict_size
            dict_size += 1
            w = c
 
    if w:
        result.append(dictionary[w])
    
    string = ''
    for i in result:
        string += str(i)
    
    return string

def LZW_descompressao(text):
    """Decompress a list of output ks to a string."""
    from io import StringIO
 
    # Build the dictionary.
    dict_size = 256
    dictionary = dict((i, chr(i)) for i in range(dict_size))
    
    result = StringIO()
    w = chr(text.pop(0))
    result.write(w)
    for k in text:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed k: %s' % k)
        result.write(entry)
 
        dictionary[dict_size] = w + entry[0]
        dict_size += 1
 
        w = entry
    return result.getvalue()
