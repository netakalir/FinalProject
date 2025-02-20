from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for messages
messages = {}

message_id = 1

@app.route('/message', methods=['GET'])
def get_first_message():
    if messages:
        return jsonify({'id': 1, 'message': messages[1]}),201
    else:
        return jsonify({'error': 'No messages found'}), 404

@app.route('/message', methods=['POST'])
def new_message():
    global message_id
    print("rec :",request.data)
    data = request.get_json() # {"message":"Hello Neta"}
    print(data)
    if 'message' not in data:
        return jsonify({'error': 'Message content is required'}), 400


    messages[message_id] = data['message']
    message_id += 1

    return jsonify({'id': message_id, 'message': data['message']}), 201


@app.route('/message/<int:msg_id>', methods=['GET'])
def get_message(msg_id):
    if msg_id in messages:
        return jsonify({'id': msg_id, 'message': messages[msg_id]}), 200
    else:
        return jsonify({'error': 'Message not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
    print(messages)
