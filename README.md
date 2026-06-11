# Auto Dock

Auto Dock is a workspace automation system that prepares a user's work environment before they start working.

Instead of manually opening applications every day, Auto Dock launches predefined workspaces with a single trigger. The current prototype uses Python and Flask for automation and includes an ESP32 simulation using Wokwi. The long-term vision is a hardware device that automatically prepares a workspace before the user reaches their desk.

---

# Problem

Every day, users repeat the same setup process before starting work:

* Opening Visual Studio Code
* Launching web browsers
* Opening notes and study materials
* Preparing development tools
* Organizing their workspace

These repetitive actions consume time and interrupt focus.

---

# Solution

Auto Dock automates workspace preparation.

With a single trigger, Auto Dock launches predefined applications and creates a ready-to-work environment automatically.

Instead of spending time preparing a workspace, users can begin working immediately.

---

# Why I Built Auto Dock

I noticed that I repeatedly opened the same applications every day before studying, coding, or creating content.

Although each action only takes a few seconds, these repeated setup tasks add unnecessary friction and break concentration.

I created Auto Dock to automate this process and explore how software automation can eventually be combined with hardware devices to prepare a workspace automatically before a user even reaches their desk.

---

# How It Works

```text
User Trigger
     │
     ▼
Python Automation Server
     │
     ▼
Workspace Profile Selected
     │
     ▼
Applications Launch Automatically
     │
     ▼
Ready Workspace
```

---

# Features

## Current Features

* Workspace automation
* Multiple workspace profiles
* Individual application launching
* Flask API endpoints
* VS Code integration
* ESP32 simulation using Wokwi
* Workspace launch simulation

## Planned Features

* ESP32 hardware trigger
* Mobile application
* Voice commands
* Smart scheduling
* Wake-on-LAN support
* Multi-device support
* AI-assisted workspace recommendations

---

# Workspace Profiles

| Workspace | Applications                |
| --------- | --------------------------- |
| Coding    | VS Code, Chrome, Notepad    |
| Study     | Chrome, Notepad, Calculator |
| Content   | Chrome, Notepad             |

---

# Supported Applications

* Visual Studio Code
* Google Chrome
* Notepad
* Calculator
* File Explorer

---

# Screenshots

## Software Dashboard

![Software Dashboard](images/dashboard.png)

---

## Wokwi ESP32 Simulation

![Wokwi Simulation]<img width="321" height="315" alt="image" src="https://github.com/user-attachments/assets/5ba47dd7-42a2-4e79-824f-da8f9f3a5a6e" />


---

## System Architecture



_soon_

## Hardware Prototype (Future Version)

_soon_

---

## Wiring Diagram

![Wiring Diagram]<img width="1244" height="1265" alt="ChatGPT Image Jun 11, 2026, 08_02_02 PM" src="https://github.com/user-attachments/assets/4c7b8c1e-7b50-4c00-b5d7-cc560eb45f05" />

Board might be differ as using wokwi 
---

# Demo Video

https://youtu.be/8TeNCQADesA

The demonstration should show:

1. Starting the Auto Dock server
2. Triggering a workspace
3. Applications launching automatically
4. The workspace becoming ready

## CAD diagram 

- front part
[front part.pdf](https://github.com/user-attachments/files/28844033/front.part.pdf)
- Base part
 [Base part.pdf](https://github.com/user-attachments/files/28844077/Base.part.pdf)



---

# Technology Stack

## Software

* Python
* Flask
* Visual Studio Code
* PlatformIO
* Wokwi Simulator

## Planned Hardware

* ESP32 Development Board
* Wi-Fi Communication
* Status LEDs
* RTC Module
* Optional Bluetooth Support

---

# Installation

Clone the repository:

```bash
git clone https://github.com/Labrez-2010/Auto-Dock.git
```

Move into the project directory:

```bash
cd Auto-Dock
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
py app.py
```

Expected output:

```text
* Running on http://127.0.0.1:5000
```

---

# Quick Start

After starting the Flask server, open one of the following endpoints in your browser.

## Coding Workspace

```text
http://127.0.0.1:5000/workspace/coding
```

Launches:

* VS Code
* Chrome
* Notepad

---

## Study Workspace

```text
http://127.0.0.1:5000/workspace/study
```

Launches:

* Chrome
* Notepad
* Calculator

---

## Content Workspace

```text
http://127.0.0.1:5000/workspace/content
```

Launches:

* Chrome
* Notepad

---

# Finding the Project Path (Optional)

If you do not know your project path:

1. Open the project in VS Code.
2. Open **Terminal → New Terminal**.
3. Look at the current directory shown in the terminal.

Example:

```text
C:\Users\hp\OneDrive\Documents\PlatformIO\Projects\Auto Dock>
```

Use the path with:

```bash
cd "C:\Users\hp\OneDrive\Documents\PlatformIO\Projects\Auto Dock"
```

---

# Future Hardware Integration

The future version of Auto Dock will integrate an ESP32-based hardware device.

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

Example workflow:

1. User leaves school or work.
2. User sends a trigger.
3. Auto Dock receives the command.
4. Development tools are launched.
5. Browser tabs are prepared.
6. Applications open automatically.
7. Workspace becomes ready before arrival.

---

# Roadmap

## Phase 1

Basic workspace automation

## Phase 2

ESP32 hardware prototype

## Phase 3

Remote triggers and smart scheduling

## Phase 4

AI-assisted workspace recommendations

## Phase 5

Fully autonomous workspace preparation

---

# Author

Labrez Shaikh

---

