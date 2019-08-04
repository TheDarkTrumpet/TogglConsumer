import settings

def GetWorkspaces():
    client = settings.Client
    responseText = client.get_workspaces()
    json.loads(responseText.text)

print(GetWorkspaces())


