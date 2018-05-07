import requests

base_url = 'http://127.0.0.1:5000/'

if __name__ == '__main__':
    #Check (a): reading
    task_list = requests.get(base_url + 'tasks').json()
    print("Checking the reading of the tasks: ")
    print(task_list)


    #Check (b): insertion of new task
    new_task = {'description': "Check of the insertion", 'urgent': 1}
    print("\n")
    print(new_task)
    requests.post(base_url + 'tasks', json=new_task)
    #task_list.append(new_task)
    #print(task_list)

    #Check (c): Search task given the id
    search_id=str(task_list[0]['id'])
    getting=requests.get(base_url+"tasks/"+search_id)
    response=getting.json()
    print("\n"+"Checking the search for a task given the id: ")
    print(response)