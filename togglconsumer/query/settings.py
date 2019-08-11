import json
from os.path import expanduser

from toggl.api_client import TogglClientApi


class Settings:
    def __init__(self, authdirectory=expanduser("~") + "/.creds", authfile="toggl.txt"):
        self.authdirectory = authdirectory
        self.authfile = authfile
        self.toggl_client = self.get_client()

    def get_credentials(self):
        return json.load(open(self.authdirectory + "/" + self.authfile))

    def get_client(self):
        settings = self.get_credentials()
        return TogglClientApi(settings)

    def __str__(self):
        return 'Settings(Directory={}, AuthFile={}'.format(self.authdirectory, self.authfile)

