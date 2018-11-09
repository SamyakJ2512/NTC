#!/usr/bin/env python3

import pydes
from struct import *

def bit_array_gen(binary) : 

    byte_array = list()
    bitarray = list()
    list_binary = list(binary)

    for char in list_binary : 
        if type(char) != int : 
            
            char = bytes(char.encode('utf-8'))
            char = str(char)[1:]    # Removed the first byte. 

            # If char is a character - 1 byte
            if len(char) == 1: 
                char = 
            
                
            else : 
                unpack('H', char)
            
            print(char)

        #bit_char = bin(int(char))

    
    #print(byte_array)

    return bitarray


if __name__ == '__main__' : 

    file_object = open("./test_files/ls", 'rb')
    plaintext = file_object.read()

    d = pydes.des()
    ciphertext = d.encrypt('12345678', plaintext)

    plaintext = list(plaintext)
    ciphertext = list(ciphertext)

    plaintext_bitarray = bit_array_gen(plaintext)
    ciphertext_bitarray = bit_array_gen(ciphertext)
    

