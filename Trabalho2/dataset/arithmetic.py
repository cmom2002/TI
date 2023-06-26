import contextlib

import biblio_arithmetic

import os

from time import time


def ler_arithmetic(nome_ficheiros, tempo):
    print("Arithmetic")
    for i in range(len(nome_ficheiros)):
       inicio_tempo = time()
       
       novo_nome = "aritmetic_" + nome_ficheiros[i]
       freqs = get_frequencies(nome_ficheiros[i])
       freqs.increment(256) 
        	
       with open(nome_ficheiros[i], "rb") as inp, \
          contextlib.closing(biblio_arithmetic.BitOutputStream(open(novo_nome, "wb"))) as bitout:
        	 write_frequencies(bitout, freqs)
        	 compress(freqs, inp, bitout)
             
       tamanho_original = os.path.getsize(nome_ficheiros[i])
       tamanho_final = os.path.getsize(novo_nome)
       ratio = tamanho_original/tamanho_final
       total_time_lz77 = time() - inicio_tempo + tempo[i]
       
       print("Tamanho original do ficheiro ", nome_ficheiros[i], ": ", tamanho_original)
       print("Tamanho final do ficheiro ", novo_nome, ": ", tamanho_final)
       print("Tempo de compressão: ", total_time_lz77)
       print("Ratio de compressão: ", ratio, " :1")
       print()
    print('---------------------------------------------------------------')

##https://github.com/nayuki/Reference-arithmetic-coding/blob/master/python/arithmetic-compress.py

def get_frequencies(filepath):
	freqs = biblio_arithmetic.SimpleFrequencyTable([0] * 257)
	with open(filepath, "rb") as input:
		while True:
			b = input.read(1)
			if len(b) == 0:
				break
			freqs.increment(b[0])
	return freqs


def write_frequencies(bitout, freqs):
	for i in range(256):
		write_int(bitout, 32, freqs.get(i))


def compress(freqs, inp, bitout):
	enc = biblio_arithmetic.ArithmeticEncoder(32, bitout)
	while True:
		symbol = inp.read(1)
		if len(symbol) == 0:
			break
		enc.write(freqs, symbol[0])
	enc.write(freqs, 256)  
	enc.finish()  

##https://github.com/nayuki/Reference-arithmetic-coding/blob/master/python/arithmetic-decompress.py

def write_int(bitout, numbits, value):
	for i in reversed(range(numbits)):
		bitout.write((value >> i) & 1)  
        
def read_frequencies(bitin):
	def read_int(n):
		result = 0
		for _ in range(n):
			result = (result << 1) | bitin.read_no_eof() 
		return result
	
	freqs = [read_int(32) for _ in range(256)]
	freqs.append(1)  # EOF symbol
	return biblio_arithmetic.SimpleFrequencyTable(freqs)


def decompress(freqs, bitin, out):
	dec = biblio_arithmetic.ArithmeticDecoder(32, bitin)
	while True:
		symbol = dec.read(freqs)
		if symbol == 256:  
			break
		out.write(bytes((symbol,)))