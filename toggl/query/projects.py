import json
from .settings import *


def GetProjects():
    client = Client
    responseText = client.get_projects()
    return json.loads(responseText.text)


print(GetProjects())
