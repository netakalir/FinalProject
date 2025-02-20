from flask import Flask, request, jsonify
from flask_cors import CORS

class Server:
    def __init__(self):
        self.app = Flask(__name__)
        CORS(self.app)
        self.logs = []
        self.key = "abc"

        # הגדרת הראוטים של Flask
        self.app.add_url_rule('/', methods=['POST'], view_func=self.receive_data)
        self.app.add_url_rule('/logs', methods=['GET'], view_func=self.get_logs)

    def xor_encrypt_decrypt(self, text: str) -> str:
        return ''.join(chr(ord(char) ^ ord(self.key[i % len(self.key)])) for i, char in enumerate(text))

    def receive_data(self):

        try:
            data_with_xor = request.get_json().get('data')
            print(f"Received encrypted data: {data_with_xor}")
            if not data_with_xor:
                return jsonify({"error": "No data received"}), 400


            decrypted_data = self.xor_encrypt_decrypt(data_with_xor)
            self.logs.append(decrypted_data)  # שמירת הנתון ברשימה
            print(f"נתונים שהתקבלו: {decrypted_data}")

            return jsonify({"status": "success"}), 200

        except Exception as e:
            print(f"שגיאה בשרת: {e}")
            return jsonify({"error": str(e)}), 500

    def get_logs(self):
        """ החזרת הנתונים השמורים """
        return jsonify({"logs": self.logs})

    def run(self):
        """ הפעלת השרת Flask """
        self.app.run(host='0.0.0.0', port=5000, debug=True)


if __name__ == '__main__':
    server = Server()
    server.run()
