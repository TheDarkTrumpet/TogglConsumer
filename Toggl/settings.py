from toggl.api_client import TogglClientApi
from os.path import expanduser
import json


def GetCredentials():
    homeDirectory = expanduser("~")
    json.load(open(homeDirectory + "/.creds/toggl.txt"))


def GetClient():
    settings = GetCredentials()
    TogglClientApi(settings)


Client = GetClient()
