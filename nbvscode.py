import os

def setup_nbvscode():
    os.makedirs("/home/jovyan/repos", exist_ok=True)
    return {
        "command": ["code-server", "--port", "{port}",
                    "--auth", "none", "--disable-telemetry",
                    "--extensions-dir", "/home/jovyan/.vscode_extensions/",
                    "--user-data-dir", "/home/jovyan/.vscode_data/",
                    "/home/jovyan/repos"],
        "absolute_url": False,
        "launcher_entry": {
            "title": "Code Server",
        }
    }
