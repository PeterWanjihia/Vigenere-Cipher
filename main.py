# import string
# alphabet = list(string.ascii_lowercase)


# def  text_indices(text):
#     text_index = []
#     for char in text:
#         char_indices = [i for i,x in enumerate(alphabet) if x== char]
#         text_index.append(char_indices)
#     return text_index
    
    
# def  key_indices(key,text):
#     key_indices = []
#     while len(key) < len(text):
#         key +=key
#     key = key[:len(text)]
#     for char in key:
#         char_indices = [i for i,x in enumerate(alphabet) if x==char]
#         key_indices.append(char_indices)
#     return key_indices

# p_indices = [item[0]  for item in text_indices('javatpoint')]
# k_indices = [item[0] for item in key_indices('best','javatpoint')]
# def V_encryption(p_indices,k_indices):
#     e_indices = []   
#     z_indices = list(zip(p_indices,k_indices))
#     for i in z_indices:
#         e_indices.append(sum(list(i))%26)
#     e_letter = []
#     for index in e_indices:
#         c_letter = [x for i,x in enumerate(alphabet) if index == i]
#         e_letter.append(c_letter)
#     return e_letter
    

# e_letters = ''.join(map(str,[item[0] for item in V_encryption(p_indices,k_indices)]))
# e_indices = [item[0] for item in text_indices(e_letters)]

# def V_decryption(e_indices,k_indices):
#     d_indices = []
#     z_indices = list(zip(e_indices,k_indices))
#     for i in z_indices:
#         d_indices.append((i[0]-i[1])%26)
#     d_letters = [alphabet[index] for index in d_indices]
#     return d_letters
        
# p_letters = ''.join(map(str,[item[0] for item in V_decryption(e_indices,k_indices)]))        
    
import string

def text_indices(text, alphabet):
    return [alphabet.index(char) for char in text]

def key_indices(key, text, alphabet):
    key = (key * (len(text) // len(key))) + key[:len(text) % len(key)]
    return [alphabet.index(char) for char in key]

def V_encryption(p_indices, k_indices, alphabet):
    e_indices = [(p + k) % 26 for p, k in zip(p_indices, k_indices)]
    return [alphabet[index] for index in e_indices]

def V_decryption(e_indices, k_indices, alphabet):
    d_indices = [(e - k) % 26 for e, k in zip(e_indices, k_indices)]
    return [alphabet[index] for index in d_indices]

def main():
    alphabet = list(string.ascii_lowercase)
    plaintext = input('Enter the text:')
    key = input('Enter the key:')
    
    p_indices = text_indices(plaintext, alphabet)
    k_indices = key_indices(key, plaintext, alphabet)
    
    encrypted_letters = V_encryption(p_indices, k_indices, alphabet)
    encrypted_text = ''.join(encrypted_letters)
    
    e_indices = text_indices(encrypted_text, alphabet)
    
    decrypted_letters = V_decryption(e_indices, k_indices, alphabet)
    decrypted_text = ''.join(decrypted_letters)
    
    print("Original Text:", plaintext)
    print("Encrypted Text:", encrypted_text)
    print("Decrypted Text:", decrypted_text)

if __name__ == "__main__":
    main()

