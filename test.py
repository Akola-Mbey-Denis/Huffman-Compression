import unittest 
import os
from modules.HuffmanAlgorithm import HuffmanCompressor
path =os.environ.get('SAMPLE_TEXT')
huffman_instance =HuffmanCompressor(path=path)

class TestHuffmanAlgorithm(unittest.TestCase):

    def test_frequency_count(self):

        self.assertDictEqual(huffman_instance.frequency_count(text=path ),{'/': 1, 'h': 1, 'o': 1, 'm': 1, 'e': 1, 'd': 1, 'n': 1, 'i': 1, 's': 1, 'D': 1, 'k': 1, 't': 1, 'p': 1, 'H': 1, 'u': 1, 'f': 1, 'a': 1, '_': 1, 'l': 1, 'c': 1, 'r': 1, '1': 1, '.': 1, 'x': 1}
)
    
    def test_generate_encoded_text(self):
        huffman_instance.make_heap(huffman_instance.frequency_count(text=path))
        huffman_instance.heap_merger()
        huffman_instance.make_codes()

        self.assertEqual(huffman_instance.generate_encoded_text(path),'110001011011001010110111110001110110111100101111111110110000100101111111010000000011001001011000011010011100011000101011010110010101000001110011111011110000110111111101111010100001111001010100101110010111111101111011111110011001011000111101010101010010000110111101000111110110000110100000'
)
    def test_pad_encoded_text(self):
        huffman_instance.make_heap(huffman_instance.frequency_count(text=path))
        huffman_instance.heap_merger()
        huffman_instance.make_codes()
       
        self.assertEqual(huffman_instance.pad_encoded_text( huffman_instance.generate_encoded_text(path)),'0000100011000101101100101011011111000111011011110010111111111011000010010111111101000000001100100101100001101001110001100010101101011001010100000111001111101111000011011111110111101010000111100101010010111001011111110111101111111001100101100011110101010101001000011011110100011111011000011010000000000000'
)

    def test_byte_array(self):
        huffman_instance.make_heap(huffman_instance.frequency_count(text=path))
        huffman_instance.heap_merger()
        huffman_instance.make_codes()
        encoded_text=huffman_instance.generate_encoded_text(path)
        padded_text=huffman_instance.pad_encoded_text(encoded_text)
        self.assertEqual(huffman_instance.get_byte_array(padded_text),bytearray(b'\x08\xc5\xb2\xb7\xc7o/\xfb\t\x7f@2Xi\xc6+YPs\xef\r\xfd\xea\x1eT\xb9\x7f{\xf9\x96=U!\xbd\x1fa\xa0\x00'))


    def test_file_size(self):
        self.assertEqual(huffman_instance.file_size(path=path),38)  

    def test_remove_padding(self):
        huffman_instance.make_heap(huffman_instance.frequency_count(text=path))
        huffman_instance.heap_merger()
        huffman_instance.make_codes()
        encoded_text=huffman_instance.generate_encoded_text(path)
        padded_text=huffman_instance.pad_encoded_text(encoded_text)
        self.assertEqual(huffman_instance.remove_padding(padded_text),'110001011011001010110111110001110110111100101111111110110000100101111111010000000011001001011000011010011100011000101011010110010101000001110011111011110000110111111101111010100001111001010100101110010111111101111011111110011001011000111101010101010010000110111101000111110110000110100000')
    

    def test_read_file(self):
        self.assertEqual(huffman_instance.read_file(path=path),'aaaabbbbbbbdddddeeeeehhhhhgggqqqwweert')


    def test_compress_text(self):
        self.assertEqual(huffman_instance.read_file(huffman_instance.compress()),huffman_instance.read_file(
            path="/home/denis/Desktop/Huffman_lossless_compression/sample_1.bin"))
         
    def test_decompress(self):
        self.assertEqual(huffman_instance.read_file( huffman_instance.decompress(huffman_instance.compress())),huffman_instance.read_file(
            path="/home/denis/Desktop/Huffman_lossless_compression/sample_1.txt")) 


    def test_decode_text(self):
        huffman_instance.make_heap(huffman_instance.frequency_count(text=path))
        huffman_instance.heap_merger()
        huffman_instance.make_codes()
        encoded_text=huffman_instance.generate_encoded_text(path)

        self.assertEqual(huffman_instance.read_file(huffman_instance.decode_text(encoded_text=encoded_text)),huffman_instance.read_file(path=path))

    def test_compression_ratio(self):
        self.assertEqual(huffman_instance.compression_ratio(decompress_file_path="/home/denis/Desktop/Huffman_lossless_compression/sample_1.txt",compresss_file_path=huffman_instance.compress()),17/38)  




if __name__ == "__main__":
     unittest.main()