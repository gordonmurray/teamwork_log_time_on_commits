from github import Github
from teamwork import create_task_list
from teamwork import create_task
from teamwork import create_time_entry
from config import base_url
import time

# Replace with your Github personal access token
g = Github("ghp_xxxxx")

user = g.get_user("gordonmurray")
repos = user.get_repos()

non_forks = []
for repo in repos:
    if not repo.fork:
        non_forks.append(repo.name)

        #print(repo.name)

        # Create a task list named after the repo
        tasklist_id = create_task_list(repo.name, "twp_xxxxx")

        print(tasklist_id)

        # loop over the commits in this repo
        for commit in repo.get_commits():
            print(commit.commit.message)
            print(commit.commit.author.date)

            # create a task for each commit
            task_id = create_task(tasklist_id, "twp_xxxxx", commit.commit.message)

            print(task_id)

            # create a time entry for this task
            time_entry_response = create_time_entry(task_id, "twp_xxxxx", "15", commit.commit.author.date)

            print(time_entry_response)

            # sleep to avoid hitting the API rate limit
            time.sleep(2)

print(non_forks)
