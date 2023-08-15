from flask import Flask,jsonify
from flask import request
app = Flask(__name__)

todos = [
    {"label": "My first task", "done": False}
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text= jsonify(todos)
    return json_text

@app.route("/todos", methods=["POST"])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)

    todos.append(request_body)
    return jsonify(todos)
    
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if 0 <= position < len(todos):
        del todos[position]
        return jsonify(todos), 200
    else:
        return jsonify({"error": "Invalid position"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)