#!/usr/bin/python3

import pydes
import pydes96
import sys


# Converts data into bitarray
def bit_array_gen(binary) : 

    bitarray = list()
    string = str(binary)

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

    print(len(bitarray1), len(bitarray2))

    hamming_distance = 0

    for x in range(0, min(len(bitarray1), len(bitarray2))) : 
        print(bitarray1[x], bitarray2[x])

        if bitarray1[x] != bitarray2[x] : 
            print(bitarray1[x], bitarray2[x])
            hamming_distance = hamming_distance + 1

    return hamming_distance
        

def avalanche_test_on_key(FilePath, DesType, Key0, Key1, Key2, Key3) : 

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
    if len(plaintext_0) % 8 != 0 : 
        x = len(plaintext_0) - len(plaintext_0) % 8
        plaintext_0 = plaintext_0[:x]
    ciphertext_0 = d.encrypt(Key0, plaintext_0)
    #print(plaintext_0, ciphertext_0)
    file_object.close()

    ciphertext_1 = d.encrypt(Key1, plaintext_0)
    ciphertext_2 = d.encrypt(Key2, plaintext_0)
    ciphertext_3 = d.encrypt(Key3, plaintext_0)

    hamming_distance_01 = find_hamming_distance(ciphertext_0, ciphertext_1)
    hamming_distance_02 = find_hamming_distance(ciphertext_0, ciphertext_2)
    hamming_distance_03 = find_hamming_distance(ciphertext_0, ciphertext_3)

    return hamming_distance_01, hamming_distance_02, hamming_distance_03


# This routine will do avalanche test on plaintext bits. 
# Currently testing for change in 1, 2, 3 bits. 
def avalanche_test_on_message(FilePath, DesType, Key) : 

    try: 
        file_object = open('./test_files/ls', 'rb')
    
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
    #print(plaintext_0, ciphertext_0)
    file_object.close()

    print("Reading and encrypting plaintext with 1 bit difference")
    # Changing 1 bit. 
    file_object = open('./test_files/ls_1', 'rb')
    plaintext_1 = file_object.read()
    # plaintext_1 = change_bits(plaintext_0, 1)
    if len(plaintext_1) % 8 != 0 : 
       x = len(plaintext_1) - len(plaintext_1) % 8
       plaintext_1 = plaintext_1[:x]
    #print(plaintext_1, ciphertext_1)
    ciphertext_1 = d.encrypt(Key, plaintext_1)
    file_object.close()

    print("Reading and Encrypting plaintext with 2 bits difference")
    # Changing 2 bits. 
    file_object = open('./test_files/ls_2', 'rb')
    plaintext_2 = file_object.read()
    # plaintext_2 = change_bits(plaintext_0, 2)
    if len(plaintext_2) % 8 != 0 : 
       x = len(plaintext_2) - len(plaintext_2) % 8
       plaintext_2 = plaintext_2[:x]
    ciphertext_2 = d.encrypt(Key, plaintext_2)
    #print(plaintext_2, ciphertext_2)
    file_object.close()

    print("Reading and Encrypting plaintext with 3 bits difference")
    # Changing 3 bits. 
    file_object = open('./test_files/ls_3', 'rb')
    plaintext_3 = file_object.read()
    # plaintext_3 = change_bits(plaintext_0, 3)
    if len(plaintext_3) % 8 != 0 : 
       x = len(plaintext_3) - len(plaintext_3) % 8
       plaintext_3 = plaintext_3[:x]
    ciphertext_3 = d.encrypt(Key, plaintext_3)
    #print(plaintext_3, ciphertext_3)
    file_object.close()

    hamming_distance_01 = find_hamming_distance(ciphertext_0, ciphertext_1)
    hamming_distance_02 = find_hamming_distance(ciphertext_0, ciphertext_2)
    hamming_distance_03 = find_hamming_distance(ciphertext_0, ciphertext_3)

    return hamming_distance_01, hamming_distance_02, hamming_distance_03


# Driver function. 
if __name__ == '__main__' : 

    if len(sys.argv) != 4 and len(sys.argv) != 7: 
        
        print("Usage: $ ", sys.argv[0], " <FilePath> <DesType> <message / key>")
        sys.exit()

    FilePath = sys.argv[1]
    DesType = sys.argv[2]
    TestType = sys.argv[3]

    # Check for des validity
    if DesType != 'des' and DesType != 'des96' : 
        print("Wrong DesType entered. ")
        print("Exiting...")
        sys.exit()

    # if (DesType == 'des' and len(Key) != 8) or (DesType == 'des96' and len(Key) != 12): 
    #     print("DesType and Key Length don't match. ")
    #     print("Exiting...")
    #     sys.exit()

    # Avalanche test on plaintext bits.
    if TestType == 'message' : 
        print("Enter Key: ", end = '')
        Key = input()
        hamming_distance_01, hamming_distance_02, hamming_distance_03 = avalanche_test_on_message(FilePath, DesType, Key)
    
    # Avalanche test on key bits. 
    elif TestType == 'key' : 
        print("Enter Key0: ", end = '')
        Key0 = input()
        print("Enter Key1: ", end = '')
        Key1 = input()
        print("Enter Key2: ", end = '')
        Key2 = input()
        print("Enter Key3: ", end = '')
        Key3 = input()
        hamming_distance_01, hamming_distance_02, hamming_distance_03 = avalanche_test_on_key(FilePath, DesType, Key0, Key1, Key2, Key3)
     
    
    print("Hamming Distance between encrypt(plaintext) and encrypt(plaintext_1bit = ", hamming_distance_01)
    print("Hamming Distance between encrypt(plaintext) and encrypt(plaintext_2bit) = ", hamming_distance_02)
    print("Hamming Distance between encrypt(plaintext) and encrypt(plaintext_3bit) = ", hamming_distance_03)

    


