from github import Github
from teamwork import create_task_list, create_task, create_time_entry
from config import teamwork_api_key, github_username, github_personal_access_token, default_minutes, api_rate_limit_sleep
import time

def main():

    # Replace with your Github personal access token
    g = Github(github_personal_access_token)

    user = g.get_user(github_username)
    repos = user.get_repos()

    non_forks = []

    for repo in repos:
        if not repo.fork:
            non_forks.append(repo.name)

            print(repo.name)

            # Create a task list named after the repo
            tasklist_id = create_task_list(repo.name, teamwork_api_key)

            # loop over the commits in this repo
            for commit in repo.get_commits():
                print(commit.commit.message)
                print(commit.commit.author.date)

                # create a task for each commit
                task_id = create_task(tasklist_id, teamwork_api_key, commit.commit.message)

                # create a time entry for this task
                time_entry_response = create_time_entry(task_id, teamwork_api_key, default_minutes, commit.commit.author.date)

                print(time_entry_response)

                # sleep to avoid hitting the API rate limit
                time.sleep(api_rate_limit_sleep)

    print(non_forks)

if __name__ == "__main__":
    main()
