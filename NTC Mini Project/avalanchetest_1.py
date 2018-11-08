#!/usr/bin/python3

import pydes
import pydes96
import sys

# Converts data into bitarray
def bit_array_gen(string) : 

    bitarray = list()

    for char in string : 
        bits = bin(ord(char))[2:]   # Removing the initial '0b' 

        for b in bits : 
            bitarray.append(int(b))

    return bitarray


# Find a NULL Byte and add something such that we get the required change in bits. 
# This routine does not work for normal user-input strings. 
def change_bits(data, n) : 

    data = list(data)

    counter = 0
    bit_count = 0

    quotient = n  / 8
    remainder = n / 8

    while counter < len(data) and bit_count < n : 
       
        while quotient != 0 : 
            
            if data[counter] == '\x00' : 
                data[counter] = '\xff'
                bit_count = bit_count + 8
                quotient = quotient - 1
            
            counter = counter + 1
            if counter == len(data) - 1 : 
                return bytes(data)

            bit_count = bit_count + 8

        if data[counter] == '\x00' : 
            data[counter] = 2**remainder
            bit_count = bit_count + remainder

        counter = counter + 1
    
    return bytes(data)


# This routine finds the hamming distance between 2 binaries. It assumes that the 2 binaries are equal in length. 
def find_hamming_distance(binary1, binary2) : 

    bitarray1 = bit_array_gen(binary1)
    bitarray2 = bit_array_gen(binary2)

    hamming_distance = 0

    for x in range(0, len(bitarray1)) : 
        
        if bitarray1[x] != bitarray2[x] : 
            hamming_distance = hamming_distance + 1
    
    return hamming_distance
        


# This routine will do avalanche test on plaintext bits. 
# Currently testing for change in 1, 2, 3 bits. 
def avalanche_test_on_message(FilePath, DesType, Key) : 

    try: 
        file_object = open(FilePath, 'rb')
    
    except FileNotFoundError:
        print("File Not Found. ")
        print("Exitting...")
        sys.exit()
    
    if DesType == 'des' : 
        d = pydes.des()
    
    elif DesType == 'des96' : 
        d = pydes96.des()
    

    print("Reading and encrypting original plaintext. ")
    # Original Plaintext
    plaintext_0 = file_object.read()
    ciphertext_0 = d.encrypt(Key, plaintext_0)
    print(plaintext_0, ciphertext_0)

    print("Reading and encrypting plaintext with 1 bit difference")
    # Changing 1 bit. 
    plaintext_1 = change_bits(plaintext_0, 1)
    ciphertext_1 = d.encrypt(Key, plaintext_1)
    print(plaintext_1, ciphertext_1)

    # print("Reading and Encrypting plaintext with 2 bits difference")
    # # Changing 2 bits. 
    # plaintext_2 = change_bits(plaintext_0, 2)
    # ciphertext_2 = d.encrypt(Key, plaintext_2, False)
    # print(len(plaintext_2), len(ciphertext_2))
    # print("Reading and Encrypting plaintext with 3 bits difference")
    # # Changing 3 bits. 
    # plaintext_3 = change_bits(plaintext_0, 3)
    # ciphertext_3 = d.encrypt(Key, plaintext_3, False)
    # print(len(plaintext_3), len(ciphertext_3))

    # hamming_distance_01 = find_hamming_distance(ciphertext_0, ciphertext_1)
    # hamming_distance_02 = find_hamming_distance(ciphertext_0, ciphertext_2)
    # hamming_distance_03 = find_hamming_distance(ciphertext_0, ciphertext_3)

    # print(hamming_distance_01, hamming_distance_02, hamming_distance_03)


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

    # Avalanche test on plaintext bits. 
    avalanche_test_on_message(FilePath, DesType, Key)


