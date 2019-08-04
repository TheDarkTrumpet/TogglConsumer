import json
import settings
from toggl.api_client import TogglClientApi


def GetProjects():
    client = settings.Client
    responseText = client.get_projects()
    return json.loads(responseText.text)


print(GetProjects())
