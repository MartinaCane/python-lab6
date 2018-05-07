from flask import Flask, jsonify, Response, request
import json
import Database

app = Flask(__name__)

task_list = Database.read_from_db()



#Point a: Read list of tasks from Database
@app.route('/tasks')
def list_tasks():
    task_list = Database.read_from_db()
    tasks = task_list
    return jsonify(tasks)


#Point b: Insert a new task
@app.route('/tasks', methods=['POST'])
def newTask():
    new_task = request.json
    print(new_task)

    creation = Database.insert_new_task(new_task['description'], new_task['urgent'])
    print(creation)
    task_list.append(creation)
    return jsonify(creation)

#Point c: Search task given id
@app.route('/tasks/<id>')
def searchTask(id):
    id_n = int(id)
    task = [task for task in task_list if task['id'] == id_n]
    print(task, len(task))
    if len(task) != 0:
        return jsonify(task[0])



if __name__ == '__main__':

    app.run()