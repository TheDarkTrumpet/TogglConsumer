from sqlalchemy import Column, Integer, String, Boolean, DateTime, DECIMAL

from togglconsumer.cache.models.base import Base


class Project(Base):
    __tablename__ = 'Projects'

    id = Column(Integer, primary_key=True, autoincrement=True)
    workspace_id = Column(Integer)
    cid = Column(Integer)
    name = Column(String)
    billable = Column(Boolean)
    is_private = Column(Boolean)
    active = Column(Boolean)
    template = Column(Boolean)
    at = Column(DateTime)
    created_at = Column(DateTime)
    color = Column(Integer)
    auto_estimates = Column(Boolean)
    actual_hours = Column(Integer)
    hex_color = Column(String)
    rate = Column(DECIMAL)
    guid = Column(String)
    currency = Column(String)

    _mapping_override = {
        "wid": "workspace_id",
        "cid": "cid",
    }

    def __init__(self, input_dictionary=None):
        if input_dictionary is not None:
            self.set_attributes(input_dictionary)

    def __repr__(self):
        return "<Project(id='%i' name='%s)>" % (self.id, self.name)

    def set_attributes(self, input_dictionary):
        for key, value in input_dictionary.items():
            if key in self._mapping_override.keys():
                key = self._mapping_override[key]

            setattr(self, key, value)
            #if self.__getattribute__(key) is not None:
            #    setattr(self, key, value)