from flask import Flask, jsonify, Response, request
import json
import Database

app = Flask(__name__)


@app.route('/tasks')
def list_tasks():

    task_list = Database.read_from_db()
    tasks = task_list

    return jsonify(tasks)

if __name__ == '__main__':

    app.run()