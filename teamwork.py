import requests
import base64
from datetime import datetime
from urllib.parse import urljoin
from config import base_url

def create_task_list(task_list_name, auth_code, project_id="693059"):

    full_url = urljoin(base_url, "/projects/")

    # Encoding the auth_code for basic authentication
    encoded_auth = base64.b64encode(auth_code.encode()).decode()

    # Headers
    headers = {
        "Authorization": f"Basic {encoded_auth}",
        "Content-Type": "application/json"
    }

    # Data payload
    data = {
        "todo-list": {
            "name": task_list_name,
            "description": ""
        }
    }

    # API Endpoint
    endpoint = f"{full_url}{project_id}/tasklists.json"

    # Making the POST request
    response = requests.post(endpoint, headers=headers, json=data)

    # Checking if the request was successful and extracting TASKLISTID
    if response.status_code == 201:
        response_data = response.json()
        if "TASKLISTID" in response_data:
            return response_data["TASKLISTID"]
        else:
            return "Error: TASKLISTID not found in response"
    else:
        return f"Error: {response.status_code} - {response.text}"



def create_task(task_list_id, auth_code, content):

    full_url = urljoin(base_url, "/tasklists/")

    # Encoding the auth_code for basic authentication
    encoded_auth = base64.b64encode(auth_code.encode()).decode()

    # Headers
    headers = {
        "Authorization": f"Basic {encoded_auth}",
        "Content-Type": "application/json"
    }

    # Data payload
    data = {
        "todo-item": {
            "content": content,
            "tasklistId": task_list_id,
            "description": ""
        }
    }

    # API Endpoint
    endpoint = f"{full_url}{task_list_id}/tasks.json"

    # Making the POST request
    response = requests.post(endpoint, headers=headers, json=data)

    # Checking if the request was successful and extracting the task ID
    if response.status_code == 201:
        response_data = response.json()
        if "id" in response_data:
            return response_data["id"]
        else:
            return "Error: 'id' not found in response"
    else:
        return f"Error: {response.status_code} - {response.text}"


def create_time_entry(task_id, auth_code, minutes, datetime_obj):

    full_url = urljoin(base_url, "/projects/api/v3/tasks/")

    # Encoding the auth_code for basic authentication
    encoded_auth = base64.b64encode(auth_code.encode()).decode()

    # Headers
    headers = {
        "Authorization": f"Basic {encoded_auth}",
        "Content-Type": "application/json"
    }

    # Check if datetime_obj is a datetime object, if not, attempt to parse it
    if not isinstance(datetime_obj, datetime):
        try:
            datetime_obj = datetime.strptime(datetime_obj, "%Y-%m-%d %H:%M:%S")
        except ValueError as e:
            return f"Error parsing date and time: {e}"

    current_date = datetime_obj.strftime("%Y-%m-%d")
    current_time = datetime_obj.strftime("%H:%M:%S")

    # Data payload
    data = {
        "timelog": {
            "hours": 0,
            "minutes": int(minutes),
            "date": current_date,
            "time": current_time,
            "description": "Time logged",
            "isBillable": False,
            "taskId": int(task_id),
            "userId": 154258  # Replace with your user ID
        }
    }

    # API Endpoint
    endpoint = f"{full_url}{task_id}/time.json"

    # Making the POST request
    response = requests.post(endpoint, headers=headers, json=data)

    # Checking if the request was successful and extracting the relevant information
    if response.status_code == 201:
        return response.json()
    else:
        return f"Error: {response.status_code} - {response.text}"
