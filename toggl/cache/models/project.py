from sqlalchemy import Column, Integer, String
from toggl.cache.models.base import Base


class Project(Base):
    __tablename__ = 'Projects'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

    def __repr__(self):
        return "<Project(id='%i' name='%s)>" % (self.id, self.name)