import os
import getpass

username = getpass.getuser()

def setup_nbvscode():

    return {
        "command": ["code-server", "--port", "{port}",
                    "--auth", "none", "--disable-telemetry",
                    "/home/{}".format(username)],
        "absolute_url": False,
        "launcher_entry": {
            "title": "Code Server",
        }
    }
