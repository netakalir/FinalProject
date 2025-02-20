

class Encryption:




    def xor_encrypt_decrypt(self, data: str, key: str) -> str:
        key_length = len(key)
        return ''.join(chr(ord(data[i]) ^ ord(key[i % key_length])) for i in range(len(data)))





