from sqlalchemy import Column, Integer, String, Boolean, DateTime, DECIMAL
from togglconsumer.cache.models.base import Base


class TimeTags(Base):
    __tablename__ = 'TimesTags'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))

    def __init__(self, input_dictionary=None):
        if input_dictionary is not None:
            self.set_attributes(input_dictionary)

    def __repr__(self):
        return "<TimeTag(id='%i' name='%s)>" % (self.id, self.name)

    def set_attributes(self, input_dictionary):
        for key, value in input_dictionary.items():
            setattr(self, key, value)