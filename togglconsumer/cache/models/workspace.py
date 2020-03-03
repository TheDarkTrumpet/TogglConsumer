from sqlalchemy import Column, Integer, String, Boolean, DateTime, DECIMAL
from togglconsumer.cache.models.base import Base


class Workspace(Base):
    __tablename__ = 'Workspaces'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    profile = Column(Integer)
    premium = Column(Boolean)
    admin = Column(Boolean)
    default_hourly_rate = Column(Integer)
    default_currency = Column(String(20))
    only_admins_may_create_projects = Column(Boolean)
    only_admins_see_billable_rates = Column(Boolean)
    only_admins_ee_team_dashboard = Column(Boolean)
    project_bllable_by_default = Column(Boolean)
    rounding = Column(Integer)
    rounding_minutes = Column(Integer)
    api_token = Column(String(50))
    at = Column(DateTime)
    logo_url = Column(String(500))
    ical_url = Column(String(500))
    ical_enabled = Column(Boolean)

    def __init__(self, input_dictionary=None):
        if input_dictionary is not None:
            self.set_attributes(input_dictionary)

    def __repr__(self):
        return "<Project(id='%i' name='%s)>" % (self.id, self.name)

    def set_attributes(self, input_dictionary):
        for key, value in input_dictionary.items():
            setattr(self, key, value)
            #if self.__getattribute__(key) is not None:
            #    setattr(self, key, value)