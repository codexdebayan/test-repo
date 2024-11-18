from flask import Flask, request, jsonify

app = Flask(__name__)

data = {
    "101": "Gyan",
    "102" : "Prince",
    "103" : "Shyam",
    "104" : "John"
}
ids = list(data.keys())

@app.route('/users', methods=['POST'])
def add_user():
    user = request.args.get('user')
    id = str(int(max(ids)) + 1)
    data[id] = user
    ids.append(id)
    return jsonify({"msg": "User Inserted Successfully!"}, 200)

@app.route('/users', methods=['GET'])
def returive_user():
    users = list(data.values())
    return jsonify(users)

@app.route('/users', methods=['DELETE'])
def del_user():
    id = request.args.get('id')
    data.pop(id)
    ids.remove(id)
    return jsonify({"msg": f"User with ID {id} deleted successfully!"}), 200

if __name__ == ('__main__'):
    app.run(host='0.0.0.0', port=5000 )
