import datetime
from flask import Flask, request, jsonify

class Server:

    def __init__(self):
        self.app = Flask(__name__)
        self.data = {}
        self.enc_key = 'abcde'

        @self.app.route('/', methods = ['POST'])
        def stor_data():
            return self.stor_in_server()


    def stor_in_server(self):
        receive = request.get_json()
        return jsonify(receive)


    def run(self):
        self.app.run(host='0.0.0.0', port= 5000, debug= True)



if __name__ == "__main__":
    app = Server()
    app.run()

