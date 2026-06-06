## Auto Dock 
 A device that automate your app opening task me a device prepare your workspace before you

 ---

## Overview
Auto Dock is a automation device that automatically prepare a user environment, it ready your workspace before your touch a laptop, your system is ready for you to do work.instead of opening manually opening application.

**Example** - you send a command open vs code ,it automatically open it   
       ( _In future it have beautiful app to get best exprence_ )

**The Hardware version it communicates with a computer and prepare a workspace before you reaches a desk.** 

---

## Problem
**Every day user spent time :**

- opening a a applications
- Launching ides
- opening browser tabs 
- organizing Workspaces

#### These Repetative actions waste time and break focus

---


## Solution
#### Auto Dock automates workspace preperation.
 
 **The system recevies triggers and automatically launches predefined workflows , allowing user to start working i immediately** .

 ---
 
 ## degital version
 **Current implementation includes :**
 
- ESP32 Simulation using Wokwi 
- PlatformIO development Environment
- Vs code intregration
- workplace Launch Simulation 

---
---

# Functioning flow
## Current Digital Prototype Flow

```text
User
  │
  ▼
Terminal Command
  │
  ▼
Python Automation Script
  │
  ▼
Predefined Tasks Executed
  │
  ▼
Applications Launch Automatically
  │
  ▼
Workspace Ready

```
## How the Current System Works

Just like typing:

```bash
code
```

opens Visual Studio Code,

Auto Dock uses terminal commands and Python scripts to automatically launch and prepare your workspace.




### Similar Examples

```bash
code
```
Opens Visual Studio Code.

---------------------------

```bash
calc
```

Opens Calculator.

------------------------------------------
```bash
notepad
```

Opens Notepad.

--------------------------------------
```bash
start chrome
```

Opens Google Chrome.

---------------------------

Auto Dock automates these actions so that multiple applications and workflows can be prepared with a single trigger.

### For Workspace
# Workspace Profiles

Auto Dock supports multiple workspace profiles. Each workspace launches a predefined set of applications to prepare the environment for a specific task.

---

## Coding Workspace

Launches:

* Visual Studio Code
* Google Chrome
* Notepad

Endpoint:

```text
http://127.0.0.1:5000/workspace/coding
```

Workflow:

```text
User
 │
 ▼
Coding Workspace Trigger
 │
 ▼
VS Code Opens
Chrome Opens
Notepad Opens
 │
 ▼
Ready-to-Code Environment
```

---

## Study Workspace

Launches:

* Google Chrome
* Notepad
* Calculator

Endpoint:

```text
http://127.0.0.1:5000/workspace/study
```

Workflow:

```text
User
 │
 ▼
Study Workspace Trigger
 │
 ▼
Chrome Opens
Notepad Opens
Calculator Opens
 │
 ▼
Ready-to-Study Environment
```

---

## Content Workspace

Launches:

* Google Chrome
* Notepad

Endpoint:

```text
http://127.0.0.1:5000/workspace/content
```

Workflow:

```text
User
 │
 ▼
Content Workspace Trigger
 │
 ▼
Chrome Opens
Notepad Opens
 │
 ▼
Ready-to-Create Environment
```

---

# Single Application Mode

Open a specific application without launching a complete workspace.

## Visual Studio Code

```text
http://127.0.0.1:5000/app/code
```

## Google Chrome

```text
http://127.0.0.1:5000/app/chrome
```

## Notepad

```text
http://127.0.0.1:5000/app/notepad
```

## Calculator

```text
http://127.0.0.1:5000/app/calc
```

---

# Custom Workspaces

Users can create additional workspaces by modifying the configuration.

Example:

```python
"gaming": [
    "chrome",
    "discord",
    "spotify"
]
```

Example Endpoint:

```text
http://127.0.0.1:5000/workspace/gaming
```

---

# Future Improvements

* JSON-based workspace configuration
* Web dashboard
* Voice commands
* ESP32 hardware trigger
* AI workspace recommendations
* Scheduled workspace automation
* Multi-device support

### Future Hardware Integration

```text
User Command / Presence Detection / Advance feature 
            │
            ▼
ESP32 Device
            │
            ▼
Automation Server
            │
            ▼
Python Scripts
            │
            ▼
Applications Launch
            │
            ▼
Ready-to-Work Environment
```

### Example

1. User leaves school.
2. User sends a trigger.
3. Auto Dock receives the command.
4. Development environment is prepared.
5. Browser tabs are opened.
6. VS Code launches.
7. Workspace becomes ready before arrival.


## AI Features

- Predict next task
- Suggest priorities
- Recommend applications
- Auto-create work sessions

_After hardware intregration_



# Tech Stack


### Current Prototype

* Laptop/Desktop
* Internet Connection
* VS Code
* Python 3.x
* PlatformIO
* Wokwi Simulator
---

### Hardware Requirements

| Component                       | Purpose                 |
| ------------------------------- | ----------------------- |
| ESP32 Development Board         | Main controller         |
| Wi-Fi Module (built into ESP32) | Network communication   |
| Relay Module                    | Power control           |
| USB-C Power Supply              | Device power            |
| Bluetooth Module (optional)     | Nearby device detection |
| LEDs (optional)                 | Status indication       |
| Buzzer (optional)               | Notifications           |
| RTC Module (optional)           | Scheduling              |
| Enclosure                       | Physical dock housing   |

###  Hardware Setup

```text
User Command / Presence Detection
            │
            ▼
ESP32 Controller
            │
            ▼
Wi-Fi Communication
            │
            ▼
Automation Server
            │
            ▼
Python Scripts
            │
            ▼
Applications Launch
            │
            ▼
Ready Workspace
```

### Future Improvements

* Wake-on-LAN support
* Bluetooth proximity detection
* AI task recommendations
* Voice commands
* Mobile companion app
* Multi-device support
* Smart scheduling
# Installation

## Prerequisites

Make sure the following are installed:

* Python 3.x
* Visual Studio Code
* Google Chrome
* Git

---

## Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/auto-dock.git
```

Move into the project directory:

```bash
cd auto-dock
```

---

## Install Dependencies

Install Flask:

```bash
pip install flask
```

Or install all dependencies:

```bash
pip install -r requirements.txt
```

---

## Verify VS Code Command Line Support

Make sure the following command opens Visual Studio Code:

```bash
code
```

If not, enable the `code` command from VS Code.

---

## Run the Application

Start the Flask server:

```bash
py app.py
```

Output:

```text
* Running on http://127.0.0.1:5000
```

---

## Open the Dashboard

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

---

# Quick Start

Start Coding Workspace:

```text
http://127.0.0.1:5000/workspace/coding
```

Start Study Workspace:

```text
http://127.0.0.1:5000/workspace/study
```

Start Content Workspace:

```text
http://127.0.0.1:5000/workspace/content
```

---

# Single Application Mode

Open VS Code:

```text
http://127.0.0.1:5000/app/code
```

Open Chrome:

```text
http://127.0.0.1:5000/app/chrome
```

Open Notepad:

```text
http://127.0.0.1:5000/app/notepad
```

Open Calculator:

```text
http://127.0.0.1:5000/app/calc
```

---

# Stop the Server

Press:

```text
Ctrl + C
```

in the terminal.

## Or no need go on url just open terminal example write code and vs code open same for other app 

APPS 
```
    "code":                # VS Code
    "chrome":              # Google Chrome
    "notepad":             # Notepad
    "calc":                # Calculator
    "explorer":            # File Explorer
```


#  My Roadmap

Phase 1:
- Basic automation

Phase 2:
- Hardware prototype

Phase 3:
- AI recommendations

Phase 4:
- Fully autonomous workspace setup

---

# Author

Labrez Shaikh












