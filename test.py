import unittest 
import os
from modules.HuffmanAlgorithm import HuffmanCompressor
path ="sample_1.txt"
huffman_instance =HuffmanCompressor(path=path)

class TestHuffmanAlgorithm(unittest.TestCase):

    def test_frequency_count(self):

        self.assertDictEqual(huffman_instance.frequency_count(), {'a': 4, 'b': 7, 'd': 5, 'e': 7, 'h': 5, 'g': 3, 'q': 3, 'w': 2, 'r': 1, 't': 1}

)
    
    def test_generate_encoded_text(self):
        huffman_instance.make_heap(huffman_instance.frequency_count())
        huffman_instance.heap_merger()
        huffman_instance.make_codes()

        self.assertEqual(huffman_instance.generate_encoded_text(), '01001001001000000000000000100100100100100111111111111111101101101101101110111011101110011001100011001101111110111001111'
)
    def test_pad_encoded_text(self):
        huffman_instance.make_heap(huffman_instance.frequency_count())
        huffman_instance.heap_merger()
        huffman_instance.make_codes()
       
        self.assertEqual(huffman_instance.pad_encoded_text( huffman_instance.generate_encoded_text()),'00000001010010010010000000000000001001001001001001111111111111111011011011011011101110111011100110011000110011011111101110011110'
)

    def test_byte_array(self):
        huffman_instance.make_heap(huffman_instance.frequency_count())
        huffman_instance.heap_merger()
        huffman_instance.make_codes()
        encoded_text=huffman_instance.generate_encoded_text()
        padded_text=huffman_instance.pad_encoded_text(encoded_text)
        self.assertEqual(huffman_instance.get_byte_array(padded_text),bytearray(b'\x01I \x00$\x92\x7f\xff\xb6\xdb\xbb\xb9\x98\xcd\xfb\x9e'))


    def test_file_size(self):
        self.assertEqual(huffman_instance.file_size(path=path),38)  

    def test_remove_padding(self):
        huffman_instance.make_heap(huffman_instance.frequency_count())
        huffman_instance.heap_merger()
        huffman_instance.make_codes()
        encoded_text=huffman_instance.generate_encoded_text()
        padded_text=huffman_instance.pad_encoded_text(encoded_text)
        self.assertEqual(huffman_instance.remove_padding(padded_text),'01001001001000000000000000100100100100100111111111111111101101101101101110111011101110011001100011001101111110111001111')
    

    def test_read_file(self):
        self.assertEqual(huffman_instance.read_file(path=path),'aaaabbbbbbbdddddeeeeehhhhhgggqqqwweert')


    def test_compress_text(self):
        self.assertEqual(huffman_instance.read_file(huffman_instance.compress()),huffman_instance.read_file(
            path="sample_1.bin"))
         
    def test_decompress(self):
        self.assertEqual(huffman_instance.read_file( huffman_instance.decompress(huffman_instance.compress())),huffman_instance.read_file(
            path="sample_1.txt")) 


    def test_decode_text(self):
        huffman_instance.make_heap(huffman_instance.frequency_count())
        huffman_instance.heap_merger()
        huffman_instance.make_codes()
        encoded_text=huffman_instance.generate_encoded_text()

        self.assertEqual(huffman_instance.read_file(huffman_instance.decode_text(encoded_text=encoded_text)),huffman_instance.read_file(path=path))

    def test_compression_ratio(self):
        self.assertEqual(huffman_instance.compression_ratio(decompress_file_path="sample_1.txt",compresss_file_path=huffman_instance.compress()),0.42105263157894735)  




if __name__ == "__main__":
     unittest.main() 