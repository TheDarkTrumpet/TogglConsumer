import json
from togglconsumer.cache.models.project import Project
from togglconsumer.query.settings import Settings
from .base import Base, Elements
from .settings import Settings

class Projects (Base):
    def __init__(self):
        self.projects = []
        Base.__init__(self)

    def load(self):
        projectsj = self._getprojects()
        for p in projectsj:
            project = Project(p)
            self.projects.append(project)

    def _getprojects(self):
        responseText = self.client.get_projects()
        return json.loads(responseText.text)



class Project (Elements):
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

    @classmethod
    def from_dict(cls, items):
        c = cls()
        incorrect_headers = []
        for k, v in items.items():
            if hasattr(c, k):
                setattr(c, k, v)
            else:
                incorrect_headers.append(k)

        if len(incorrect_headers) > 0:
            pass
            # Debug.print_debug(F"Incorrect headers detected: {set(incorrect_headers)}")
        return c