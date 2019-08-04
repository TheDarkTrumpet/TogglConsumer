from toggl.api_client import TogglClientApi
import json
from os.path import expanduser

home = expanduser("~")
settings = json.load(open(home + "/.creds/toggl.txt"))

toggle_client = TogglClientApi(settings)

response = toggle_client.get_workspaces()
workspaces = json.loads(response.text)

print(workspaces)


