# Auto Dock

Auto Dock is an automation system that prepares your workspace before you start working.

Instead of manually opening applications every day, Auto Dock launches predefined workspaces with a single trigger.

Current version:
- Python + Flask automation server
- VS Code integration
- Workspace profiles
- ESP32 simulation using Wokwi

Future versions will add physical hardware and AI-assisted workspace preparation.

## Why I Built Auto Dock

Every day, developers repeat the same actions:

- Open VS Code
- Launch Chrome
- Open notes
- Prepare their environment

These repetitive tasks waste time and interrupt focus.

I created Auto Dock to automate workspace preparation so that the environment is ready before work begins. The long-term goal is to create a hardware device that prepares a computer workspace automatically.

## Features

Current Features

- Workspace automation
- Multiple workspace profiles
- Open individual applications
- Flask API endpoints
- VS Code integration
- ESP32 simulation using Wokwi

Planned Features

- Hardware trigger using ESP32
- Voice commands
- Mobile application
- AI recommendations
- Scheduled automation
- Wake-on-LAN support

User Trigger
     │
     ▼
Python Server
     │
     ▼
Workspace Profile
     │
     ▼
Launch Applications
     │
     ▼
Ready Workspace

## Workspace Profiles

| Workspace | Applications                |
| --------- | --------------------------- |
| Coding    | VS Code, Chrome, Notepad    |
| Study     | Chrome, Notepad, Calculator |
| Content   | Chrome, Notepad             |

VS Code
Google Chrome
Notepad
Calculator
File Explorer

## Screenshots


### Software Dashboard

(image)

### Wokwi ESP32 Simulation

(image)

### Full System Architecture

(image)

### Hardware Prototype (when available)

(image)

### Wiring Diagram

(image)

~~~
git clone https://github.com/Labrez-2010/Auto-Dock.git
~~~
~~~
cd Auto-Dock
~~~
~~~
pip install -r requirements.txt
~~~
~~~
py app.py
~~~
