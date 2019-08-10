import json
import settings


def GetProjects():
    client = settings.Client
    responseText = client.get_projects()
    return json.loads(responseText.text)


print(GetProjects())
