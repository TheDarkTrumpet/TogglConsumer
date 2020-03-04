from sqlalchemy import Column, Integer, String, Boolean, DateTime, DECIMAL
from togglconsumer.cache.models.base import Base


class Time(Base):
    __tablename__ = 'Times'

    id = Column(Integer, primary_key=True)
    pid = Column(Integer)
    tid = Column(Integer)
    uid = Column(Integer)
    description = Column(String(500))
    start = Column(DateTime)
    end = Column(DateTime)
    updated = Column(DateTime)
    dur = Column(Integer)
    user = Column(String(60))
    use_stop = Column(Boolean)
    client = Column(String(100))
    project = Column(String(100))
    project_color = Column(String(5))
    project_hex_color = Column(String(20))
    task = Column(String(500))
    billable = Column(DECIMAL)
    is_billable = Column(Boolean)
    cur = Column(String(30))
    # Tags

    def __init__(self, input_dictionary=None):
        if input_dictionary is not None:
            self.set_attributes(input_dictionary)

    def __repr__(self):
        return "<Time(id='%i' name='%s)>" % (self.id, self.name)

    def set_attributes(self, input_dictionary):
        for key, value in input_dictionary.items():
            setattr(self, key, value)
            #if self.__getattribute__(key) is not None:
            #    setattr(self, key, value)