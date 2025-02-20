class EncryptedXor:
    def __init__(self):
        self.text=""
        self.key=""

    def xor_encrypt_decrypt(self,text,key):
       self.text = text
       self.key = key
       result=[]
       for i,char in enumerate(text):
           key_char=key[i % len(key)]
           encrypted_char=chr( ord(char)^ ord(key_char))
           result.append(encrypted_char)

       return ''.join(result)

