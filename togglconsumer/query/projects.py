import json
from togglconsumer.query.settings import Settings
from . import base
from .settings import Settings

class Projects (base):
    def __init__(self):
        pass


    def GetProjects(self):
        client = Settings().toggl_client
        responseText = client.get_projects()
        return json.loads(responseText.text)


print(GetProjects())
