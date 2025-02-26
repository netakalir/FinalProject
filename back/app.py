from flask import Flask, request, jsonify,send_file
from flask_cors import CORS
import os
import json
from dotenv import load_dotenv



def xor_encrypt_decrypt( data: str, key: str) -> str:
    key_length = len(key)
    return ''.join(chr(ord(data[i]) ^ ord(key[i % key_length])) for i in range(len(data)))



class Server:
    load_dotenv()
    def __init__(self):
        self.app = Flask(__name__)
        CORS(self.app)
        self.logs_dict={}
        self.logs_list=[]
        self.data_file={}
        self.name_file=[]
        self.file_path=None
        self.key =  os.getenv('SECRET_KEY')
        self.path = os.path.abspath(os.getcwd())

        # stores the received data
        @self.app.route('/save_data', methods=['POST'])# מקבל מהלקוח מידע
        def receive_data():
            return self.receive_data()

        # temporary storage of data
        @self.app.route('/logs_list', methods=['GET'])   # שולח את המידע בכל זמן נתון
        def get_logs():
            return self.get_logs()

        # stores list of file names
        @self.app.route('/get_file_name', methods=['GET']) # מחזיר את שמות הקבצים שנוצרו
        def get_file_name():
            return jsonify(self.name_file)

        # returns file name with data inside
        @self.app.route('/get_all_data',methods=['GET'])  # שולח את המידע שנשמר בקובץ
        def get_all_data():
            return self.data_file

        # return data through file name
        @self.app.route('/get_by_name/<string:filename>', methods=['GET']) # שולח מידע לפי בקשת UI
        def get_file(filename):
            return self.get_by_name(filename)


    def receive_data(self):
        try:

            json_data = request.get_json()
            data_enc = json_data.get('data')
            time = json_data.get('time')
            system = json_data.get('system')
            # print(data_enc)
            data = xor_encrypt_decrypt(data_enc, self.key)
            # print(data)
            if not data:
                return jsonify({"error": "מחכה לשליחת מידע..."}), 400

            self.logs_dict = {"dencrypted_data": data,"time": time,"system": system}
            self.logs_list.append(self.logs_dict)

            name_for_file = str(self.logs_dict['system']['mac']).replace(":", "-")

            folder_path = os.path.join(self.path, 'data')
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            if not name_for_file in self.name_file:
                 self.name_file.append(name_for_file)

            file_path = os.path.join(folder_path, name_for_file + ".txt")

            with open(file_path, "a", encoding="utf-8") as file:
                file.write(f"Time: {self.logs_dict['time']}\n")
                file.write(f"Decrypted Data: {self.logs_dict['dencrypted_data']}\n")
                file.write(f"System Info: {json.dumps(self.logs_dict['system'])}\n")
                file.write("\n")


            return jsonify({"הודעה ": "המידע התקבל בהצלחה!!"}), 200


        except Exception as e:
            print(f"שגיאה בשרת: {e} ")
            return jsonify({"error": str(e)}), 500

    def get_logs(self):
        return jsonify({"logs": self.logs_list})

    def get_file_name(self):
        return jsonify(self.name_file)

    def get_all_data(self):
        with open(self.path,"r") as file:
            file_content = file.read()
        self.data_file = {"filename": "data.txt", "content": file_content}
        return jsonify(self.data_file)

    def get_by_name(self, filename):
        folder_path =  os.path.abspath(os.getcwd())
        self.file_path = os.path.join(folder_path, filename)

        if os.path.exists(self.file_path):
            return send_file(self.file_path, as_attachment=True)  # שולח את הקובץ להורדה
        else:
            return jsonify({"error": "הקובץ לא נמצא"}), 404


    def run(self):
        self.app.run(host='0.0.0.0', port=5000, debug=True)


if __name__ == '__main__':
    server = Server()
    server.run()


