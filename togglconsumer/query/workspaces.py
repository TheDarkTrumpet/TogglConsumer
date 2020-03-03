import json
from togglconsumer.query.base import Base
from togglconsumer.cache.models.workspace import Workspace
from togglconsumer.query.settings import Settings


class Workspaces (Base):
    def __init__(self):
        self.workspaces = []
        Base.__init__(self)

    def load(self):
        projectsj = self._getprojects()
        for p in projectsj:
            project = Workspace(p)
            self.workspaces.append(project)

    def _getprojects(self):
        responseText = self.client.get_projects()
        return json.loads(responseText.text)