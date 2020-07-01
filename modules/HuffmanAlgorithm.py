import heapq
import os 
from .heap import HeapNode

class HuffmanCompressor:
    def __init__(self,path):
        self.path=path
        self.heap=[]
        self.codes={}
        self.reverse_mapping={}

    def frequency_count(self):
        ''''
         computes the frequency of each unique character in the text
         returns a dictionary containing the unique characters and their
         frequency counts.


        '''
        file=open(file=self.path,mode="r") 
        
        if file:
            text=file.read()
             
            frequency={}

            for ch in text:
                if not ch in frequency:
                    frequency[ch]=0
                frequency[ch]+=1 
            return frequency
        else:
            pass
        file.close()


    def  make_heap(self,frequency):
        '''
        Receives a dictionary containing the frequency count of each unique character in
        the text file.

        ''' 
        for key in frequency:
            node = HeapNode(key,frequency[key])
            heapq.heappush(self.heap,node)

    def heap_merger(self):
        '''
        combines two heap nodes to form a new node

        '''
        while len(self.heap)>1:
            node_1=heapq.heappop(self.heap)
            node_2=heapq.heappop(self.heap)
            merged_node =HeapNode(None,node_1.freq +node_2.freq)
            merged_node.left =node_1
            merged_node.right =node_2
            heapq.heappush(self.heap, merged_node)


    def codes_generate(self,root,current_code):
        '''Assigns code 0 to left child and 1 to the right child of every heap node

        '''
        if(root == None):
                return

        if(root.char != None):
            self.codes[root.char] = current_code
            self.reverse_mapping[current_code] = root.char
            return

        self.codes_generate(root.left, current_code + "0")
        self.codes_generate(root.right, current_code + "1") 


    def make_codes(self):
        
        root = heapq.heappop(self.heap)
        current_code = ""
        self.codes_generate(root, current_code)




    def generate_encoded_text(self):
        encoded_text=""
        file = open(file=self.path,mode="r") 
        
        if file:
            try:
                text=file.read()        
                

                for ch in text:
                    encoded_text+=self.codes[ch]
                     
                return encoded_text
            except EnvironmentError as error:
                pass  
        else:
            pass 
        file.close()   
           

    def pad_encoded_text(self, encoded_text):
        extra_padding = 8 - len(encoded_text) % 8
        for i in range(extra_padding):
            encoded_text += "0"

        padded_info = "{0:08b}".format(extra_padding)
        encoded_text = padded_info + encoded_text
        return encoded_text


    def get_byte_array(self, padded_encoded_text):
        if(len(padded_encoded_text) % 8 != 0):
            print("Encoded text not padded properly")
            exit(0)

        b = bytearray()
        for i in range(0, len(padded_encoded_text), 8):
            byte = padded_encoded_text[i:i+8]
            b.append(int(byte, 2))
        return b



    def compress(self):
        filename, file_extension = os.path.splitext(self.path)
        output_path = filename + ".bin"

        with open(self.path, 'r+') as file, open(output_path, 'wb') as output:
            text = file.read()
            text = text.rstrip()

            frequency = self.frequency_count ()
            self.make_heap(frequency)
            self.heap_merger()
            self.make_codes()

            encoded_text = self.generate_encoded_text()
            padded_encoded_text = self.pad_encoded_text(encoded_text)

            b = self.get_byte_array(padded_encoded_text)
            output.write(bytes(b))
            output.close()

         
        return output_path

    """ functions for decompression: """
     
    def remove_padding(self, padded_encoded_text):
        padded_info = padded_encoded_text[:8]
        extra_padding = int(padded_info, 2)

        padded_encoded_text = padded_encoded_text[8:] 
        encoded_text = padded_encoded_text[:-1*extra_padding]

        return encoded_text

    def decode_text(self, encoded_text):
        current_code = ""
        decoded_text = ""

        for bit in encoded_text:
            current_code += bit
            if(current_code in self.reverse_mapping):
                character = self.reverse_mapping[current_code]
                decoded_text += character
                current_code = ""

        return decoded_text


    def decompress(self, input_path):
        filename, file_extension = os.path.splitext(self.path)
        output_path = filename + "_decompressed" + ".txt"

        with open(input_path, 'rb') as file, open(output_path, 'w') as output:
            bit_string = ""

            byte = file.read(1) 
            while(byte != "" and len(byte)>0):
                 
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8, '0')
                bit_string += bits
                byte = file.read(1)

            encoded_text = self.remove_padding(bit_string)

            decompressed_text = self.decode_text(encoded_text)
            
            output.write(decompressed_text)

         
        return output_path

    def  file_size(self,path):
        '''
        returns the size of the file
        '''
        
        file_info =os.stat(path=path)
        return file_info.st_size

    def read_file(self,path):
        '''
        Read the content of a file 
        '''
        with open(self.path, 'r+') as file:
            text = file.read()   
        return text  

    def compression_ratio(self,decompress_file_path,compresss_file_path):
        return (self.file_size(path=compresss_file_path)/self.file_size(path=decompress_file_path))       

     









