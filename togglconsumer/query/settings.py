import json
from os.path import expanduser

from toggl.api_client import TogglClientApi


def GetCredentials():
    homeDirectory = expanduser("~")
    return json.load(open(homeDirectory + "/.creds/toggl.txt"))


def GetClient():
    settings = GetCredentials()
    return TogglClientApi(settings)


Client = GetClient()
