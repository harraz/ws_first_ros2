# ROS2 Iron + Docker + VS Code Dev Container (X11 Ready)

This repository contains a fully working ROS2 Iron development environment
using Docker + VS Code Dev Containers with full X11 GUI support.

This setup was stabilized after fixing:
- Docker permissions on Debian
- X11 forwarding issues
- Incorrect ROS official documentation
- VS Code container bugs
- Deprecated extensions

Everything here is verified working.

--------------------------------------------------
What Works
--------------------------------------------------

✅ rviz2
✅ rqt
✅ xeyes / xclock
✅ ROS2 CLI
✅ VS Code Dev Container
✅ Python3 / Pip
✅ CMake / GCC
✅ GUI from container to host


--------------------------------------------------
Docker Image Used
--------------------------------------------------

harraztendo/ros2-iron-dev:latest

Based on:
osrf/ros:iron-desktop

Includes:
- ROS2 Iron + Desktop tools
- X11 utilities
- bash-completion
- python3 + pip
- gcc / cmake / build-essentials
- sudo + network tools
- Non-root user: harraz


--------------------------------------------------
Project Structure
--------------------------------------------------

ws_first_ros2/
├── .devcontainer/
│   └── devcontainer.json
├── Dockerfile
├── HOST_SETUP.md
├── README.md
├── src/
├── install/
├── build/
└── log/


--------------------------------------------------
Dev Container Configuration
--------------------------------------------------

Key values:

- Image: harraztendo/ros2-iron-dev:latest
- Network: host
- Display forwarding: enabled
- Workspace: /projects/ws_first_ros2
- Keep-alive: sleep infinity

Main block:

"image": "harraztendo/ros2-iron-dev:latest",
"command": "sleep infinity",
"runArgs": [
  "--net=host",
  "-e", "DISPLAY=${env:DISPLAY}",
  "-v", "/tmp/.X11-unix:/tmp/.X11-unix"
]


--------------------------------------------------
How To Use
--------------------------------------------------

1. Open VS Code
2. File → Open Folder → ws_first_ros2
3. Click **Reopen in Container**
4. Open terminal in container
5. Test:

xeyes
rviz2


--------------------------------------------------
Important Notes
--------------------------------------------------

This guide is MISLEADING for ROS2 + GUI:
https://docs.ros.org/en/foxy/How-To-Guides/Setup-ROS-2-with-VSCode-and-Docker-Container.html

It uses:
- The wrong image
- No GUI -> no rviz2
- Wrong VS Code setup
- Old extensions

This repository replaces it with a working solution.


--------------------------------------------------
Maintainer
--------------------------------------------------

Mohamed Farouk Harraz
Ast: Greater Philadelphia
GitHub: https://github.com/harraz
Email: harraz@gmail.com


--------------------------------------------------
Next Phases (Planned)
--------------------------------------------------

- Robot tank integration
- Sensor fusion (MPU + ultrasonic)
- ESP32 / Camera
- AI + navigation
- ROS2 Nav stack
