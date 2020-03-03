from .settings import Settings


class Base:
    def __init__(self):
        self.client = Settings().toggl_client


class BaseElement:
    pass