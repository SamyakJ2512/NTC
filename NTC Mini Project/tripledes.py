#!/usr/bin/python3

import pydes
import sys

def tripledes(FilePath, Key0, Key1, Key2) : 

    try : 
        file_object = open(FilePath, 'rb')

    except FileNotFoundError: 
        print("File Not Found. ")
        print("Exitting...")
        sys.exit()

    plaintext = str(file_object.read())

    if len(plaintext) % 8 != 0 : 
        plaintext = plaintext + (8 - (len(plaintext) % 8)) * '0'

    D = pydes.des()
    
    print("Stage1: Encrypt(E1 Stage)")
    E_Output0 = D.encrypt(Key0, plaintext)
    print("Stage1: Encrypt done. ")
    
    print("Stage2: Decrypt(D Stage)")
    E_Output1 = D.decrypt(Key1, E_Output0)
    print("Stage2: Decrypt done. ")
    
    print("Stage3: Encrypt(E2 Stage)")
    E_Output2 = D.encrypt(Key2, E_Output1)
    print("Stage3: Encrypt done. ")

    print("Complete Encryption done. ")

    ciphertext = E_Output2

    # Decryption process - DED
    #D_Output0 = D.decrypt(k2, ciphertext)
    #D_Output1 = D.encrypt(k1, D_Output0)
    #D_Output2 = D.decrypt(k0, D_Output1)

    #plaintext_1 = D_Output2

    file_object.close()

    return plaintext, ciphertext


if __name__ == '__main__' : 

    # 3 64-bit keys for Triple DES
    print("Input 3 8-byte keys: ")
    k0 = input("Key 0: ")
    k1 = input("Key 1: ")
    k2 = input("Key 2: ")

    print("Enter the path of file: ", end='')
    FilePath = input()

    plaintext, ciphertext = tripledes(FilePath, k0, k1, k2)

    print("plaintext: ", plaintext)
    print("ciphertext: ", ciphertext)



    



