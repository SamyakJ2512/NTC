#!/usr/bin/python3

import pydes
import pydes96
import sys
import math
import binascii

# Find's a Binary's entropy. 
def find_entropy(Binary) :  

    # Dictionary to store frequency of each character. 
    occurance = dict()

    # List of all characters. 
    List_Binary = list(Binary)

    # Populating the dictionary. 
    for char in Binary : 
        if char in occurance: 
            occurance[char] = occurance[char] + 1

        else : 
            occurance[char] = 0
    
    entropy = 0

    # Find Entropy. 
    for char, val in occurance.items() : 
        
        if val != 0:  
            val = float(val) / len(List_Binary)
            entropy = entropy + val * math.log(val, 2)
    
    entropy = -entropy

    return entropy


# Will check the DesTYpe and generates respective ciphertext. 
def entropy_test(FilePath, DesType, Key) : 

    try: 
        file_object = open(FilePath, 'rb')
    
    except FileNotFoundError: 
        print("File Not Found. ")
        print("Exiting...")
        sys.exit()
    
    plaintext = file_object.read()
    
    # Check the DesType. 
    if DesType == 'des' : 
         d = pydes.des()
         ciphertext = d.encrypt(Key, plaintext)
    
    elif DesType == 'des96' : 
         d = pydes96.des()
         ciphertext = d.encrypt(Key, plaintext)
    
    # Return entropies of plaintext and ciphertext. 
    return find_entropy(plaintext), find_entropy(ciphertext)



# Driver Function. 
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
    
    # Entropy test 
    plaintext_entropy, ciphertext_entropy = entropy_test(FilePath, DesType, Key)

    # Printing output. 
    print("Entropy of Plaintext = ", plaintext_entropy)
    print("Entropy of Ciphertext = ", ciphertext_entropy)

