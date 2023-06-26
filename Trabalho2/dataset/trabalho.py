import RLE, lzw, huffman, arithmetic, ppm, deflate, mtf, bwt

import numpy as np


def main():
    nome_ficheiros= ['bible.txt', 'random.txt', 'finance.csv', 'jquery-3.6.0.js'] 
    entropia(nome_ficheiros)
    sem_transformadas(nome_ficheiros)
    com_BWT(nome_ficheiros)
    com_MTF(nome_ficheiros)    
   
    
def entropia(nome_ficheiros):
    print('Entropia')
    for i in range(len(nome_ficheiros)):
        ficheiro = open(nome_ficheiros[i], 'r')
        P = ficheiro.read()
        print("A entropia do ficheiro", nome_ficheiros[i], "é", calcula_entropia(calcula_ocorrencias(P)))
   
def calcula_ocorrencias(P):
    dic = {}
    no = []
    for i in P:
        if i in dic.keys():
            dic[i] += 1
        else:
            dic.setdefault(i, 1)
    for v in dic.values():
        no.append(v)
    
    return no  

def calcula_entropia(no):
    no = np.copy(no)
    no = no[no > 0]
    prob = no / sum(no) 
    entropia = -np.sum(prob * np.log2(prob))
    return entropia

def sem_transformadas(nome_ficheiros):
    tempo = []
    for i in range(len(nome_ficheiros)):
        tempo.append(0)
    
    RLE.ler_RLE(nome_ficheiros, tempo)
    lzw.ler_LZW(nome_ficheiros, tempo)
    huffman.ler_HUFFMAN(nome_ficheiros, tempo)
    arithmetic.ler_arithmetic(nome_ficheiros, tempo)
    ppm.ler_ppm(nome_ficheiros, tempo)
    deflate.ler_deflate(nome_ficheiros, tempo)
    
def com_BWT(nome_ficheiros):
    nome_bwt = []
    tempo_bwt = []
    for i in range(len(nome_ficheiros)):
        tuplo = bwt.ler_BWT(nome_ficheiros[i])
        nome_bwt.append(tuplo[0])
        tempo_bwt.append(tuplo[1])
    
    RLE.ler_RLE(nome_bwt, tempo_bwt)
    lzw.ler_LZW(nome_bwt, tempo_bwt)
    huffman.ler_HUFFMAN(nome_bwt, tempo_bwt)
    arithmetic.ler_arithmetic(nome_bwt, tempo_bwt)
    ppm.ler_ppm(nome_bwt, tempo_bwt)
    deflate.ler_deflate(nome_bwt, tempo_bwt)
    
def com_MTF(nome_ficheiros):
    nome_mtf = []
    tempo_mtf = []
    for i in range(len(nome_ficheiros)):
        tuplo = mtf.ler_MTF(nome_ficheiros[i])
        nome_mtf.append(tuplo[0])
        tempo_mtf.append(tuplo[1])
    
    RLE.ler_RLE(nome_mtf, tempo_mtf)
    lzw.ler_LZW(nome_mtf, tempo_mtf)
    huffman.ler_HUFFMAN(nome_mtf, tempo_mtf)
    arithmetic.ler_arithmetic(nome_mtf, tempo_mtf)
    ppm.ler_ppm(nome_mtf, tempo_mtf)
    deflate.ler_deflate(nome_mtf, tempo_mtf)
    
    

if __name__ == '__main__':
    main()        