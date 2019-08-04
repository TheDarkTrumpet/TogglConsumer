from toggl.api_client import TogglClientApi
import json

settings = json.load(open("/home/dthole/.creds/toggl.txt"))

toggle_client = TogglClientApi(settings)

response = toggle_client.get_workspaces()

print(response)

