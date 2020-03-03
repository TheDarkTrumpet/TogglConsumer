from togglconsumer.query.projects import *
from togglconsumer.query.workspaces import *
from datetime import date


p = Projects()
p.load()

w = Workspaces()
w.load()


start_date =  date.fromisoformat('2020-01-01')
stop_date = date.fromisoformat('2020-02-03')
client = Settings().toggl_client
responseText = client.get_project_times(155621750, start_date, stop_date)



#def GetWorkspaces():
#    client = Settings().toggl_client
#    responseText = client.get_workspaces()
#    return json.loads(responseText.text)
