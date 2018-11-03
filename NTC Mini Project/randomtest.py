#!/usr/bin/python3

import pydes
import pydes96
import sys

def bit_array_gen(string) : 

    bitarray = list()

    for char in string : 
        bits = bin(ord(char))[2:]   # Removing the initial '0b' 

        for b in bits : 
            bitarray.append(int(b))

    return bitarray

def count_zero_one(binary) : 

    bitarray = bit_array_gen(binary)

    zero_count = 0
    one_count = 0

    counter = 0
    
    for bit in bitarray : 
        if bit == 0 : 
            zero_count = zero_count + 1
        
        elif bit == 1 : 
            one_count = one_count + 1

    return zero_count, one_count



def random_test_des(FilePath, Key) : 

    try: 
        file_object = open(FilePath, 'rb')
    
    except FileNotFoundError : 
        print("File Not Found.")
        print("Exiting...")
        sys.exit()
    
    # Store the complete binary in the buffer
    plaintext = str(file_object.read())
    
    # Encrypt the plaintext
    d = pydes.des()
    ciphertext = d.encrypt(Key, plaintext, True)

    plaintext_zero_count, plaintext_one_count = count_zero_one(plaintext)
    ciphertext_zero_count, ciphertext_one_count = count_zero_one(ciphertext)

    return plaintext_zero_count, plaintext_one_count, ciphertext_zero_count, ciphertext_one_count


def random_test_des96(FilePath, Key) : 

    try: 
        file_object = open(FilePath, 'rb')
    
    except FileNotFoundError : 
        print("File Not Found.")
        print("Exiting...")
        sys.exit()
    
    # Store the complete binary in the buffer
    plaintext = str(file_object.read())
    
    # Encrypt the plaintext
    d = pydes96.des()
    ciphertext = d.encrypt(Key, plaintext, True)

    plaintext_zero_count, plaintext_one_count = count_zero_one(plaintext)
    ciphertext_zero_count, ciphertext_one_count = count_zero_one(ciphertext)

    return plaintext_zero_count, plaintext_one_count, ciphertext_zero_count, ciphertext_one_count


if __name__ == '__main__' : 

    if len(sys.argv) != 4 : 
        print("Usage: $ ", sys.argv[0], " <FilePath> <DesType> <Key> ")
        sys.exit()
    
    FilePath = sys.argv[1]
    DesType = sys.argv[2]
    Key = sys.argv[3]

    # Check for des validity
    if DesType != 'des' and DesType != 'des96' : 
        print("Wrong DesType entered. ")
        print("Exiting...")
        sys.exit()

    if (DesType == 'des' and len(Key) != 8) or (DesType == 'des96' and len(Key) != 12): 
        print("DesType and Key Length don't match. ")
        print("Exiting...")
        sys.exit()
    
    if DesType == 'des' : 
        plaintext_zero_count, plaintext_one_count, ciphertext_zero_count, ciphertext_one_count = random_test_des(FilePath, Key)
    
    elif DesType == 'des96' : 
        plaintext_zero_count, plaintext_one_count, ciphertext_zero_count, ciphertext_one_count = random_test_des96(FilePath, Key)
    

    print("Details regarding plaintext: ")
    print("zero_count = ", plaintext_zero_count)
    print("one_count = ", plaintext_one_count)
    print("% 0 = ", plaintext_zero_count / (plaintext_zero_count + plaintext_one_count))
    print("% 1 = ", plaintext_one_count / (plaintext_zero_count + plaintext_one_count))

    print("\n")

    print("Details regarding ciphertext: ")
    print("ciphertext_zero_count = ", ciphertext_zero_count)
    print("ciphertext_one_count = ", ciphertext_one_count)
    print("% 0 = ", ciphertext_zero_count / (ciphertext_zero_count + ciphertext_one_count))
    print("% 1 = ", ciphertext_one_count / (ciphertext_zero_count + ciphertext_one_count))
