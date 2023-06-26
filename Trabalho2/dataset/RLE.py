import os
 
from time import time


def ler_RLE(nome_ficheiros, tempo):
    print("RLE")
    lista = []
    for i in range(len(nome_ficheiros)):
        inicio_tempo = time()
        print(nome_ficheiros[i])
        
        ficheiro = open(nome_ficheiros[i], 'r')
        string = ficheiro.read()     
        novo_nome = 'RLE_' + nome_ficheiros[i]
        
        novo_ficheiro = open(novo_nome, 'w')
        string_rle = RLE_compressao(string)
        novo_ficheiro.write(string_rle)
        
        tamanho_original = os.path.getsize(nome_ficheiros[i])
        tamanho_final = os.path.getsize(novo_nome)
        ratio = tamanho_original/tamanho_final
        
        total_time_RLE = time() - inicio_tempo + tempo[i]
        lista.append([ratio, total_time_RLE])
        print("Tamanho original do ficheiro ", nome_ficheiros[i], ": ", tamanho_original)
        print("Tamanho final do ficheiro ", novo_nome, ": ", tamanho_final)
        print("Tempo de compressão: ", total_time_RLE)
        print("Ratio de compressão: ", ratio, " :1")
        print()
    print('---------------------------------------------------------------')
    return lista

##feito por n
    
def RLE_compressao(string):      
    
    new_string = ''
    flag = '#'
    count = 0
    for i in range(len(string) - 1):
        if (string[i] == string[i + 1]):        
            count += 1
            
        if(string[i] != string[i + 1] or i == (len(string) - 2)):
            if count > 2:
                new_string += flag
                new_string += string[i]
                new_string += str(count + 1)
            else:
                new_string += (string[i] * (count + 1))
            
            count = 0
            
        if(string[i] != string[i + 1] and i == (len(string) - 2)):
           new_string += string[i + 1]
    
    return new_string

def RLE_descompressao(string):
    flag = '#'
    
    new_string = ''
    i = 0
    while(i <= len(string)-1 ):
        new_num = ''
        j = 2
        if(string[i] == flag):
            while (string[i + j].isdigit()):
                new_num += string[i + j]
                j += 1
                if(i + j)>=len(string): break
            new_string += (int)(new_num)*string[i+1]
            i += j

        else:
            new_string += string[i]
            i+=1
    return new_string
        

