import matplotlib.pyplot as plt

import matplotlib.image as mpimg

import scipy.io.wavfile as spiowf

import numpy as np

from huffmancodec import HuffmanCodec

import math

def main():
    file = input('Introduza o nome do fiheiro: ')
    if(file.endswith('txt') == 1):                    
          fich = open(file, 'r')
          texto = fich.read()
          P = []
          trata_texto(texto,P)
          fich.close()
    
    elif(file.endswith('bmp') == 1):
        P = mpimg.imread(file)                                 
        if P.ndim > 2:                                  
            P = P[:,:,0]
        P = P.flatten() 
    
    elif(file.endswith('wav') == 1):
        [fs, P] =spiowf.read(file)
        if P.ndim > 1:                                  
            P = P[:,0]
        P = P.flatten()
     
    no = histograma(P, file)
    
    H, prob = entropia(no)
    print('Entropia: ', H,' bits por símbolo')
    
    codec = HuffmanCodec.from_data(P)
    symbols,lenghts = codec.get_code_len()
    med = media(prob, lenghts)
    print("Média: ", med , "bits por símbolo")
    var = variancia(prob, med, lenghts)
    print("Variância: ", var)
    
    entropia_agrupada = agrupamento_simbolos(P, file)
    print("Entropia agrupada:",entropia_agrupada)
    
    print()
    exercicio6a()
    print()
    exercicio6b()
    print()
    exercicio6c()
    
##---------------------Q1--------------------------      
def histograma(P, file):
    A, no = np.unique(P, return_counts = True)     
    plt.bar(A, no)                                  
    plt.title(file[:-4])
    plt.xlabel("Alfabeto")
    plt.ylabel("Número ocorrências")
    return no

##---------------------Q2--------------------------   
def entropia(no):
    no = no[no > 0]                                
    H = 0
    prob = no / sum(no)
    H = - np.sum(prob * np.log2(prob))
    return H, prob

##---------------------Q3-------------------------- 
def trata_texto(texto, P):
    for i in texto:
        if (64 < ord(i) < 91 or 96 < ord(i) < 123):
            P.append(i)                             

##---------------------Q4-------------------------- 
def media(prob, lenghts):
    media = np.sum(prob * lenghts)                
    return media

def variancia(prob, med, lenghts):
    var = np.sum(prob * (lenghts - med)**2)        
    return var

##---------------------Q5-------------------------- 
def agrupamento_simbolos(P, file):
    if (type(P[0]) == str):                         
        for i in range(len(P)):
            P[i] = ord(P[i])                       
        P = np.asarray(P)                         
            
    if((len(P) % 2) == 0):                       
       size = int(len(P)/2)
                      
    else:                                          
       size = int((len(P)-1)/2)
       P = P[:-1]
       
    P = P.reshape(size, 2)                       
    P1 = np.empty(size)                            
    for i in range(size):
       P1[i] = (P[i][0]* len(P)) + P[i][1]         
       
    no = np.unique(P1, return_counts = True)[1]

    entropia_agrupada = entropia(no)[0]                            
    
    return entropia_agrupada / 2
    
   
##---------------------Q6-------------------------- 
#Entropia
def entropia2(X):
    unique, count = np.unique(X, return_counts=True, axis=0)
    prob = count / len(X)
    H = -np.sum(prob * np.log2(prob))
    return H

#Informação Mútua
def info_mutua(X, Y):
    return entropia2(X) + entropia2(Y) - entropia_conjunta(X,Y)

#Entropia Conjunta
def entropia_conjunta(X,Y):
    XY = np.c_[X,Y]
    return entropia2(XY)

#Função retorna a fonte do ficheiro
def ler_audio(query, target):
    P_query =spiowf.read(query)[1]
    if(P_query.ndim > 1):
        P_query = P_query[:,0]
    P_target =spiowf.read(target)[1]
    if(P_target.ndim > 1):
        P_target = P_target[:,0]
    return P_query, P_target

#Função genérica para o exercício 6b e 6c
def inf_mutua6(P_query, P_target):
    
    inicio = 0
    tam = len(P_query)
    passo = tam/4
    passo = math.ceil(passo)
    
    new_tam = (len(P_target) - len(P_query) + 1) / passo
    new_tam = math.ceil(new_tam)
    infMutua = np.zeros(new_tam)
    count = 0
    
    inicio_max = len(P_target) - len(P_query) + 1
    
    while (inicio < inicio_max):
        nova = P_target[inicio:tam]
        
        if (len(P_query) == len(nova)):
            I= info_mutua(P_query, nova)
            infMutua[count]=I
            
        count += 1
        inicio += passo
        tam += passo
        
    return infMutua

##---------------------Q6a-------------------------
def exercicio6a():
    query = np.array([2, 6, 4, 10, 5, 9, 5, 8, 0, 8])
    target = np.array([6, 8, 9, 7, 2, 4, 9, 9, 4, 9, 1, 4, 8, 0, 1, 2, 2, 6, 3, 2, 0,
              7, 4, 9, 5, 4, 8, 5, 2, 7, 8, 0, 7, 4, 8, 5, 7, 4, 3, 2, 2, 7,
              3, 5, 2, 7, 4, 9, 9, 6])
    passo = 1
    inf_mutua6a(query, target, passo)
    
def inf_mutua6a(query, target, passo):
    inicio=0
    tam = len(query)
    
    new_tam = (int)((len(target) - len(query) + 1)/passo)
    new_tam = math.ceil(new_tam)
    infMutua = np.zeros(new_tam)
    count=0
    
    inicio_max = len(target) - len(query) + 1
    
    while (inicio < inicio_max):
        new_target = target[inicio : tam]
        
        if (len(query) == len(new_target)):
            I = info_mutua(query, new_target)
            infMutua[count] = I 
        
        count += 1
        inicio += passo
        tam += passo
        
    print("Informação mútua:" ) 
    print(infMutua)

##---------------------Q6b-------------------------- 
def exercicio6b():
    P_query1, P_target1 = ler_audio("guitarSolo.wav", "target01 - repeat.wav")
    P_query2, P_target2 = ler_audio("guitarSolo.wav", "target02 - repeatNoise.wav")
    graf1 = inf_mutua6(P_query1, P_target1)
    graf2 = inf_mutua6(P_query2, P_target2)
    x = plt.subplots()[1]
    print("Informação mútua de guitarSolo.wav e target01 - repeat.wav ", graf1)
    x.plot(graf1)
    print("Informação mútua de guitarSolo.wav e target02 – repeatNoise.wav", graf2)
    x.plot(graf2)

##---------------------Q6c-------------------------- 
def exercicio6c():
    query = "guitarSolo.wav"
    for i in range(1,8):
        song = "Song0" + str(i)+".wav"
        print("Song0" + str(i)+".wav")
        P_query, P_target = ler_audio(query, song)
        infMutua= inf_mutua6(P_query, P_target)
        IM_max = infMutua.max()
        print("Informação mútua máxima: ", IM_max,"\n")

    
if __name__ == "__main__":
    main()