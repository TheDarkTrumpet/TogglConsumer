from collections import Sequence

from .settings import Settings


class Base:
    def __init__(self):
        self.client = Settings().toggl_client

    def from_list(self, jsonlist):
        elements = []
        for a in jsonlist:
            elements.append(cls.from_dict(a))
        return elements


class Elements (Sequence):
    def __getitem__(self, i: int):
        return self.elements[i]

    def __str__(self):
        return "<{}: Collection of size: {}".format(self.__class__.__name__, len(self.elements))

    def __repr__(self):
        return self.__str__()