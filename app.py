from flask import Flask, jsonify
import subprocess
import os
import shutil

app = Flask(__name__)

# =====================================================
# SAFE APP LAUNCHER (Windows-friendly)
# Use full paths or reliable system commands
# =====================================================

def is_exe(cmd):
    return shutil.which(cmd) is not None


APPS = {
    "code": "code",  # VS Code (must be in PATH)
    "notepad": "notepad.exe",
    "calc": "calc.exe",
    "explorer": "explorer.exe",

    # Chrome safer handling (fallback included below)
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe"
}


# =====================================================
# WORKSPACES
# =====================================================

WORKSPACES = {
    "coding": ["code", "chrome", "notepad"],
    "study": ["chrome", "notepad", "calc"],
    "content": ["chrome", "notepad"]
}


# =====================================================
# CORE LAUNCH FUNCTION
# =====================================================

def open_app(app_name):
    if app_name not in APPS:
        return False, "App not registered"

    command = APPS[app_name]

    try:
        # Special handling for chrome fallback
        if app_name == "chrome" and not os.path.exists(command):
            if is_exe("chrome"):
                subprocess.Popen("chrome", shell=True)
                return True, "Launched via PATH"
            return False, "Chrome not found"

        # If executable exists as file path
        if os.path.exists(command):
            subprocess.Popen([command], shell=False)
            return True, "Launched via path"

        # If it's a system command (notepad, calc, code)
        if is_exe(command):
            subprocess.Popen(command, shell=True)
            return True, "Launched via system PATH"

        return False, "Executable not found"

    except Exception as e:
        return False, str(e)


# =====================================================
# WORKSPACE LAUNCHER
# =====================================================

def open_workspace(workspace_name):
    if workspace_name not in WORKSPACES:
        return False, "Workspace not found"

    results = []

    for app in WORKSPACES[workspace_name]:
        success, msg = open_app(app)
        results.append({
            "app": app,
            "success": success,
            "message": msg
        })

    return True, results


# =====================================================
# ROUTES
# =====================================================

@app.route("/")
def home():
    return """
    <h1>Auto Dock</h1>

    <h2>Apps</h2>
    /app/code<br>
    /app/chrome<br>
    /app/notepad<br>
    /app/calc<br>

    <h2>Workspaces</h2>
    /workspace/coding<br>
    /workspace/study<br>
    /workspace/content<br>
    """


@app.route("/app/<app_name>")
def launch_app(app_name):
    success, msg = open_app(app_name)

    if success:
        return jsonify({
            "status": "SUCCESS",
            "app": app_name,
            "info": msg
        })

    return jsonify({
        "status": "ERROR",
        "app": app_name,
        "message": msg
    }), 404


@app.route("/workspace/<workspace_name>")
def launch_workspace(workspace_name):
    success, result = open_workspace(workspace_name)

    if success:
        return jsonify({
            "status": "SUCCESS",
            "workspace": workspace_name,
            "results": result
        })

    return jsonify({
        "status": "ERROR",
        "message": result
    }), 404


# =====================================================
# START SERVER
# =====================================================

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)