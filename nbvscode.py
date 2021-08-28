import os

def setup_nbvscode():
    os.makedirs("/home/jovyan/repos", exist_ok=True)
    return {
        "command": ["code-server", "--port", "{port}",
                    "--auth", "none", "--disable-telemetry",
                    "/home/jovyan/repos"],
        "absolute_url": False,
        "launcher_entry": {
            "title": "Code Server",
        }
    }
