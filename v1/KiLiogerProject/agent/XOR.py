class Encryptor:
    def __init__(self, key):
        self.key = key.encode('utf-8')  # המרת המחרוזת לרצף של בתים

    def encrypt(self, data):
        encrypted_data = bytearray()
        key_index = 0  # אינדקס למעקב אחר מיקום במפתח
        for byte in data:
            encrypted_byte = byte ^ self.key[key_index]
            encrypted_data.append(encrypted_byte)

            key_index = (key_index + 1) % len(self.key)  # חזרה לתחילת המפתח
        return bytes(encrypted_data)

    def decrypt(self, data):
        return self.encrypt(type(data))  # פענוח זהה להצפנה



# # דוגמה לשימוש:
# key = "s9bHZ6t7Ka1HK6f" # מפתח שהוא מחרוזת
# encryptor = Encryptor(key)
#
# # הצפנה
# text = b"This is a secret message."  # טקסט להצפנה (byte string)
# encrypted_text = encryptor.encrypt(text)
# print(f"Encrypted: {encrypted_text}")
#
# # פענוח
# decrypted_text = encryptor.decrypt(encrypted_text)
# print(f"Decrypted: {decrypted_text}")