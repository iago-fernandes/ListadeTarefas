from flask import jsonify, request
from app import app, db
from models import Todo

@app.route('/todo', methods=['GET'])
def allTodos():
    todos = []
    all_todos = Todo.query.all()

    for todo in all_todos:
        todo_data = {}
        todo_data['id'] = todo.id
        todo_data['text'] = todo.text
        todo_data['complete'] = todo.complete
        todos.append(todo_data)
    
    return jsonify({'Todos' : todos})


@app.route('/todo', methods=['POST'])
def newTodo():
    data = request.get_json()
    new_todo = Todo(text=data['text'], complete=False)

    db.session.add(new_todo)
    db.session.commit()

    return jsonify({'message': '[200] Todo created !'})


@app.route('/todo/<todo_id>', methods=['PUT'])
def completeTodo(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()

    if not todo:
        return jsonify({'Message' : '[404] Todo not found !'})

    todo.complete = True
    db.session.commit()

    return jsonify({'Message' : '[200] Todo completed !'})

    

@app.route('/todo/<todo_id>', methods=['DELETE'])
def deleteTodo(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()

    if not todo:
        return jsonify({'Message' : '[404] Todo not found !'})

    db.session.delete(todo)
    db.session.commit()

    return jsonify({'Message' : '[200] Todo deleted !'})