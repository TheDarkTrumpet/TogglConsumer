import json
from togglconsumer.query.base import Base
from togglconsumer.query.settings import Settings


def GetWorkspaces():
    client = Settings().toggl_client
    responseText = client.get_workspaces()
    return json.loads(responseText.text)
