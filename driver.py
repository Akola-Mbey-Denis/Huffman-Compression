import os
from modules.HuffmanAlgorithm import HuffmanCompressor
huffman_instance = HuffmanCompressor(path=os.environ.get('SAMPLE_TEXT'))
h=huffman_instance.compress()
huffman_instance.decompress(input_path=h) 
 
 