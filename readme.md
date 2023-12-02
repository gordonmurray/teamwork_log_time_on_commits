# Log time on Commits in Teamwork

A Python script to import your Github projects in to Teamwork as Task Lists and then log time for each of the commits in the project. This allows you to see how long you spent on open source projects.

![Some logged time in Teamwork]({{ site.url }}/images/logged_time.png)

![A list of Github projects in Teamwork]({{ site.url }}/images/screenshot.png)

Set up

First create a config file with your Githib and Teamwork defaults:

```python
# config.py

teamwork_url = "https://xxxxx.teamwork.com"
teamwork_api_key = "twp_xxxxxx"
github_username = "gordonmurray"
github_personal_access_token = "ghp_xxxxxx"
teamwork_user_id = xxxxxx
teamwork_project_id = "xxxxxx"
default_minutes = 15
api_rate_limit_sleep = 3
```

Then install Python requirements and run the file:


```bash
sudo apt install python3.11-venv -y

python3 -m venv commits

source commits/bin/activate

pip install -r requirements.txt

python3 commits.py
```


This uses the following Teamwork API calls:

Create a Task list in a project

```bash
curl -X POST 'https://[YOUR_ACCOUNT].teamwork.com/projects/10000/tasklists.json' \
-H 'Authorization: Basic YOUR_TOKEN' \
-H 'Content-Type: application/json' \
-d '{"todo-list":{"name":"A task list","description":"Boo!"}}'
```

Create a task in a list:


```bash
curl -X POST 'https://[YOUR_ACCOUNT].teamwork.com/tasklists/10000/tasks.json' \
-H 'Authorization: Basic YOUR_TOKEN' \
-H 'Content-Type: application/json' \
-d '{"todo-item":{"content":"A new task ","tasklistId":10000,"description":""}}'
```

Log time on a task:

```bash
curl -X POST 'https://[YOUR_ACCOUNT].teamwork.com/projects/api/v3/tasks/10000/time.json' \
-H 'Authorization: Basic YOUR_TOKEN' \
-H 'Content-Type: application/json' \
-d '{"timelog":{"hours":0,"minutes":30,"date":"2023-11-29","time":"20:40:00","description":"Some Description","isBillable":false,"taskId":10000,"userId":10000}}'
```