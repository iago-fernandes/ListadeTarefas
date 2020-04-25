from app import app

@app.route('/todo', methods=['GET'])
def allTodos():
    pass


@app.route('/todo/<id>', methods=['GET'])
def oneTodo():
    pass


@app.route('/todo', methods=['POST'])
def newTodo():
    pass


@app.route('/todo/<id>', methods=['PUT'])
def completeTodo():
    pass


@app.route('/todo/<id>', methods=['DELETE'])
def deleteTodo():
    pass