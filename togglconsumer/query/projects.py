import json
from togglconsumer.query.settings import Settings


def GetProjects():
    client = Settings().toggl_client
    responseText = client.get_projects()
    return json.loads(responseText.text)


print(GetProjects())
