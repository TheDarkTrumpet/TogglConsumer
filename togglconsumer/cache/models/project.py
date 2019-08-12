from sqlalchemy import Column, Integer, String, Boolean
from togglconsumer.cache.models.base import Base


class Project(Base):
    __tablename__ = 'Projects'

    id = Column(Integer, primary_key=True, autoincrement=True)
    workspace_id = Column(Integer)
    name = Column(String)
    billable = Column(Boolean)
    is_private = Column(Boolean)
    active = Column(Boolean)
    actual_hours = Column(Integer)

    def __repr__(self):
        return "<Project(id='%i' name='%s)>" % (self.id, self.name)