# TogglConsumer

This is a library, and execution of a cached version of what I have in Toggl.  The data from this is used in other libraries

# Important Note

As of this note, this library is highly in development/beta.  The code isn't very clean, there's few/no tests, and isn't ready for prime time. Part of this project is in an attempt to also relearn Python 3, for other projects.

# Installation and Setup

This project was built using virtualenv, for the most part.  You'll likely want to reinit the environment when setting this up.

The libraries used are currently in source/requirements.txt  You can reinstall these by using pip.

Right now, one external file is required, and that's in "~/.creds/toggl.txt", this is a dictionary of the following format:

```json
{"token": "<YOUR_TOGGL_API", "user_agent": togglconsumer, "workspace_id": <WORKSPACE_ID> }
```
