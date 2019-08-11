from sqlalchemy import Column, Integer, String
from togglconsumer.cache.models.base import Base


class Project(Base):
    __tablename__ = 'Projects'

    id = Column(Integer, primary_key=True, autoincrement=True)
    workspace_id = Column(Integer)

    name = Column(String)

    def __repr__(self):
        return "<Project(id='%i' name='%s)>" % (self.id, self.name)