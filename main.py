from togglconsumer.query.projects import *
from togglconsumer.query.workspaces import *

p = Projects()
p.load()

w = Workspaces()
w.load()






#def GetWorkspaces():
#    client = Settings().toggl_client
#    responseText = client.get_workspaces()
#    return json.loads(responseText.text)
