import json
from togglconsumer.cache.models.project import Project
from .base import Base, Elements

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
