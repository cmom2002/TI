import zlib

import os

from time import time

import base64


def ler_deflate(nome_ficheiros, tempo):
    print("Deflate")
    for i in range(len(nome_ficheiros)):
        print(nome_ficheiros[i])
        inicio_tempo = time()
        
        ficheiro = open(nome_ficheiros[i], 'rb')
        string = ficheiro.read()
        
        string_deflate = deflate_and_base64_encode(string)
        
        novo_nome = 'Deflate_' + nome_ficheiros[i]
        novo_ficheiro = open(novo_nome, 'wb')
        novo_ficheiro.write(string_deflate)
        
        tamanho_original = os.path.getsize(nome_ficheiros[i])
        tamanho_final = os.path.getsize(novo_nome)
        ratio = tamanho_original/tamanho_final
        total_time_huffman = time() - inicio_tempo + tempo[i]
        print("Tamanho original do ficheiro ", nome_ficheiros[i], ": ", tamanho_original)
        print("Tamanho final do ficheiro ", novo_nome, ": ", tamanho_final)
        print("Tempo de compressão: ", total_time_huffman)
        print("Ratio de compressão: ", ratio, " :1")
        print()
    print('---------------------------------------------------------------')

##https://stackoverflow.com/questions/1089662/python-inflate-and-deflate-implementations

def deflate_and_base64_encode( string_val ):
    zlibbed_str = zlib.compress( string_val )
    compressed_string = zlibbed_str[2:-4]
    return base64.b64encode( compressed_string )

def decode_base64_and_inflate( b64string ):
    decoded_data = base64.b64decode( b64string )
    return zlib.decompress( decoded_data , -15)