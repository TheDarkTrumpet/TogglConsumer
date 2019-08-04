import json
import settings


def GetWorkspaces():
    client = settings.Client
    responseText = client.get_workspaces()
    return json.loads(responseText.text)
