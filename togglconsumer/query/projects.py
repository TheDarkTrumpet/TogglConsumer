import json
from datetime import date, datetime, timedelta
from togglconsumer.cache.models.project import Project
from .base import Base, Elements

class Projects (Base):
    def __init__(self):
        self.projects = []
        self.time_entries = []
        self.with_times = False
        Base.__init__(self)

    def load(self):
        projectsj = self._getprojects()
        for p in projectsj:
            project = Project(p)
            if self.with_times:
                pass
            self.projects.append(project)

    def _getprojects(self):
        responseText = self.client.get_projects()
        return json.loads(responseText.text)

    @classmethod
    def with_time(cls, start, end):
        c = cls()
        return c

    @classmethod
    def with_time(cls, days_before):
        stop_date = date.now()
        start_date = stop_date - timedelta(days=days_before)
        return cls.with_time(start_date, stop_date)