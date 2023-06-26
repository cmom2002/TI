import contextlib

import biblio_arithmetic

import os

from time import time

MODEL_ORDER = 3


def ler_ppm(nome_ficheiros, tempo):
    print("Ppm")
    for i in range(len(nome_ficheiros)):
       print(nome_ficheiros[i])
       inicio_tempo = time()

       novo_nome = "ppm_" + nome_ficheiros[i]
    	
       with open(nome_ficheiros[i], "rb") as inp, \
           contextlib.closing(biblio_arithmetic.BitOutputStream(open(novo_nome, "wb"))) as bitout:
           compress(inp, bitout)
       
       tamanho_original = os.path.getsize(nome_ficheiros[i])
       tamanho_final = os.path.getsize(novo_nome)
       ratio = tamanho_original/tamanho_final
       total_time_ppm = time() - inicio_tempo + tempo[i]
       print("Tamanho original do ficheiro ", nome_ficheiros[i], ": ", tamanho_original)
       print("Tamanho final do ficheiro ", novo_nome, ": ", tamanho_final)
       print("Tempo de compressão: ", total_time_ppm)
       print("Ratio de compressão: ", ratio, " :1")
       print()
    print('---------------------------------------------------------------')

##https://github.com/nayuki/Reference-arithmetic-coding/blob/master/python/ppm-compress.py


def compress(inp, bitout):

	enc = biblio_arithmetic.ArithmeticEncoder(32, bitout)
	model = PpmModel(MODEL_ORDER, 257, 256)
	history = []
	
	while True:
		symbol = inp.read(1)
		if len(symbol) == 0:
			break
		symbol = symbol[0]
		encode_symbol(model, history, symbol, enc)
		model.increment_contexts(history, symbol)
		
		if model.model_order >= 1:
			if len(history) == model.model_order:
				history.pop()
			history.insert(0, symbol)
	
	encode_symbol(model, history, 256, enc)  # EOF
	enc.finish()  


def encode_symbol(model, history, symbol, enc):
	
	for order in reversed(range(len(history) + 1)):
		ctx = model.root_context
		for sym in history[ : order]:
			assert ctx.subcontexts is not None
			ctx = ctx.subcontexts[sym]
			if ctx is None:
				break
		else:  
			if symbol != 256 and ctx.frequencies.get(symbol) > 0:
				enc.write(ctx.frequencies, symbol)
				return
			enc.write(ctx.frequencies, 256)
	enc.write(model.order_minus1_freqs, symbol)


##https://github.com/nayuki/Reference-arithmetic-coding/blob/master/python/ppmmodel.py

class PpmModel:
	
	def __init__(self, order, symbollimit, escapesymbol):
		if order < -1 or symbollimit <= 0 or not (0 <= escapesymbol < symbollimit):
			raise ValueError()
		self.model_order = order
		self.symbol_limit = symbollimit
		self.escape_symbol = escapesymbol
		
		if order >= 0:
			self.root_context = PpmModel.Context(symbollimit, order >= 1)
			self.root_context.frequencies.increment(escapesymbol)
		else:
			self.root_context = None
		self.order_minus1_freqs = biblio_arithmetic.FlatFrequencyTable(symbollimit)
	
	
	def increment_contexts(self, history, symbol):
		if self.model_order == -1:
			return
		if len(history) > self.model_order or not (0 <= symbol < self.symbol_limit):
			raise ValueError()
		
		ctx = self.root_context
		ctx.frequencies.increment(symbol)
		for (i, sym) in enumerate(history):
			subctxs = ctx.subcontexts
			assert subctxs is not None
			
			if subctxs[sym] is None:
				subctxs[sym] = PpmModel.Context(self.symbol_limit, i + 1 < self.model_order)
				subctxs[sym].frequencies.increment(self.escape_symbol)
			ctx = subctxs[sym]
			ctx.frequencies.increment(symbol)
	
	
	
	# Helper structure
	class Context:
		
		def __init__(self, symbols, hassubctx):
			self.frequencies = biblio_arithmetic.SimpleFrequencyTable([0] * symbols)
			self.subcontexts = ([None] * symbols) if hassubctx else None

