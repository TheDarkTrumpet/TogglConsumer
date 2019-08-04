import json
# from Toggl import settings
import settings


def GetWorkspaces():
    client = settings.Client
    responseText = client.get_workspaces()
    return json.loads(responseText.text)


print(GetWorkspaces())

