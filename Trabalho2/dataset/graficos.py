# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 22:26:32 2021

@author: HP
"""

import matplotlib.pyplot as plt

import numpy as np

ratio_RLE = [1, 1, 1, 1]
ratio_huffman = [1.824424181, 1.333297779, 1.5512563, 1.568565636]
ratio_lzw = [1.364579066, 0.520034322, 3.504529726, 1.115936257]
ratio_aritmetic = [1.841289569, 1.315443304, 1.543219793, 1.570033459]
ratio_ppm = [4.016863835, 0.914151987, 10.46781649, 3.446019369]
ratio_deflate = [2.546855847, 0.990373569, 15.01532149, 2.542555066]
ratio_MTF_PPM = [4.131364009, 3.727186922, 3.973788972, 3.87686516]
ratio_BWT_RLE = [1.452477769, 1.000009999, 4.293432308, 1.492352321]

barWidth = 0.1
plt.figure(figsize = (10, 5))
tempo_RLE = [1.26353883, 0.03387904, 1.82790899, 0.09184503]
tempo_huffman = [0.95987796, 0.0284574, 1.51949, 0.67985439 ]
tempo_lzw = [0.8240661, 0.0221047, 0.0221047, 0.04380488]
tempo_aritmetic = [28.454261, 0.8381381, 45.585161, 2.24748301]
tempo_ppm = [87.878869, 5.534121, 118.840321, 6.99088811]
tempo_deflate = [0.14804697, 0.00349307, 0.03987812, 0.009869]
tempo_MTF_PPM = [214.617506, 6.11745357, 333.403995, 15.812921]
tempo_BWT_RLE = [9.74310994, 0.24683928, 13.2666859, 0.70176959]

r1 = np.arange(len(ratio_RLE))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
r5 = [x + barWidth for x in r4]
r6 = [x + barWidth for x in r5]
r7 = [x + barWidth for x in r6]
r8 = [x + barWidth for x in r7]

plt.bar(r1,ratio_RLE, color = '#FFA500', width = barWidth, label = 'RLE')
plt.bar(r2,ratio_huffman, color = '#F97306', width = barWidth, label = 'Huffman')
plt.bar(r3,ratio_lzw, color = '#FE420F', width = barWidth, label = 'LZW')
plt.bar(r4,ratio_aritmetic, color = '#FFD700', width = barWidth, label = 'Aritmetic')
plt.bar(r5,ratio_ppm, color = '#DAA520', width = barWidth, label = 'PPM')
plt.bar(r6,ratio_deflate, color = '#FAC205', width = barWidth, label = 'Deflate')
plt.bar(r7,ratio_MTF_PPM, color = '#FF6347', width = barWidth, label = 'MTF + PPM')
plt.bar(r8,ratio_BWT_RLE, color = '#E50000', width = barWidth, label = 'BWT + RLE')

plt.bar(r1,tempo_RLE, color = '#FFA500', width = barWidth, label = 'RLE')
plt.bar(r2,tempo_huffman, color = '#F97306', width = barWidth, label = 'Huffman')
plt.bar(r3,tempo_lzw, color = '#FE420F', width = barWidth, label = 'LZW')
plt.bar(r4,tempo_aritmetic, color = '#FFD700', width = barWidth, label = 'Aritmetic')
plt.bar(r5,tempo_ppm, color = '#DAA520', width = barWidth, label = 'PPM')
plt.bar(r6,tempo_deflate, color = '#FAC205', width = barWidth, label = 'Deflate')
plt.bar(r7,tempo_MTF_PPM, color = '#FF6347', width = barWidth, label = 'MTF + PPM')
plt.bar(r8,tempo_BWT_RLE, color = '#E50000', width = barWidth, label = 'BWT + RLE')
Ficheiros = ['bible.txt', 'random.txt', 'finance.csv', 'jquery-3.6.0.js']

plt.xlabel('Ficheiros')
plt.xticks([r+barWidth for r in range(len(ratio_RLE))], Ficheiros)
plt.ylabel('Ratio')
plt.title('Resultados')
plt.legend()
plt.show()

    
