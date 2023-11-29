# Log time on Commits in to Teamwork


```
sudo apt install python3.11-venv -y

python3 -m venv commits

source commits/bin/activate

pip install -r requirements.txt

python3 commits.py
```


This uses the following Teamwork API calls:

Create a Task list in a project

```
curl -X POST 'https://[YOUR_ACCOUNT].teamwork.com/projects/693059/tasklists.json' \
-H 'Authorization: Basic YOUR_TOKEN' \
-H 'Content-Type: application/json' \
-d '{"todo-list":{"name":"fourth task list","description":"blaah"}}'
```

Create a task in a list:


```
curl -X POST 'https://[YOUR_ACCOUNT].teamwork.com/tasklists/2924348/tasks.json' \
-H 'Authorization: Basic YOUR_TOKEN' \
-H 'Content-Type: application/json' \
-d '{"todo-item":{"content":"a new task ","tasklistId":2924348,"description":""}}'
```

Log time on a task:

```
curl -X POST 'https://[YOUR_ACCOUNT].teamwork.com/projects/api/v3/tasks/39564562/time.json' \
-H 'Authorization: Basic YOUR_TOKEN' \
-H 'Content-Type: application/json' \
-d '{"timelog":{"hours":0,"minutes":30,"date":"2023-11-29","time":"20:40:00","description":"asdasdasdsa","isBillable":false,"taskId":39564562,"userId":154258}}'
```
