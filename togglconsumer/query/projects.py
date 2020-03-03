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



class Project:
    def __init__(self):
        self.id = 0
        self.wid = 0
        self.cid = 0
        self.name = ""
        self.billable = ""
        self.is_private = ""
        self.active = False
        self.template = False
        self.at = 0
        self.created_at = 0
        self.color = 0
        self.auto_estimates = False
        self.actual_hours = 0
        self.hex_color = 0