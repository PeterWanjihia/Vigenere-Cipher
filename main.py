

import string

def text_indices(text, alphabet):
    return [alphabet.index(char) for char in text if char!=' ']

def key_indices(key, text, alphabet):
    key = (key * (len(text) // len(key))) + key[:len(text) % len(key)]
    return [alphabet.index(char) for char in key if char!= ' ']

def V_encryption(p_indices, k_indices, alphabet):
    e_indices = [(p + k) % 26 if isinstance(p, int) else p for p, k in zip(p_indices, k_indices)]
    return [alphabet[index] if isinstance(index, int) else ' '  for index in e_indices]


def V_decryption(e_indices, k_indices, alphabet):
    d_indices = [(e - k) % 26 if isinstance(e, int) else e for e, k in zip(e_indices, k_indices)]
    return [alphabet[index] if isinstance(index, int) else index for index in d_indices]

def main():
    alphabet = list(string.ascii_lowercase)
    plaintext = input('Enter the text:').lower()
    key = input('Enter the key:')
    # encrypted_letters = input('Enter the encrypted letters:')
    
    p_indices = text_indices(plaintext, alphabet)
    k_indices = key_indices(key, plaintext, alphabet)
    
    encrypted_letters = V_encryption(p_indices, k_indices, alphabet)
    encrypted_text = ''.join(encrypted_letters)
    
    e_indices = text_indices(encrypted_text, alphabet)
    
    decrypted_letters = V_decryption(e_indices, k_indices, alphabet)
    decrypted_text = ''.join(decrypted_letters)
    
    def insert_spaces(p_text, e_text):
        for i,x in enumerate(p_text):
            if x == ' ':
                e_text.insert(i, ' ')
            result = "".join(str(element) for element in e_text)
        return result
    
    enc_text = insert_spaces(list(plaintext),list(encrypted_text))    
    
    print("Original Text:", plaintext)
    print("Encrypted Text:",enc_text)
    print("Decrypted Text:", decrypted_text)

if __name__ == "__main__":
    main()


