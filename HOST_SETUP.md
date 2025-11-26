# Host Setup – Debian + Docker + X11 + ROS2 GUI

This document captures ALL host-side requirements and fixes needed to run
ROS2 Iron inside Docker with full X11 GUI (rviz2, rqt, xeyes, Gazebo, etc).

This setup was built and verified on:
- Debian (Docker from Debian repo – running as root)
- VS Code + Dev Containers
- ROS2 Iron (osrf/ros:iron-desktop based)

This file prevents you from having to rediscover the same gotchas.

--------------------------------------------------
1. Verify Docker is working
--------------------------------------------------

docker --version
docker info

Make sure Docker is running and does NOT error.


--------------------------------------------------
2. Ensure docker group exists
--------------------------------------------------

On Debian, Docker does NOT always create the docker group.

sudo groupadd docker   # if it does not exist
sudo usermod -aG docker $USER
newgrp docker

Verify:
getent group docker

You should see something like:
docker:x:994:harraz


--------------------------------------------------
3. Test Docker WITHOUT sudo
--------------------------------------------------

docker run hello-world

If this works, continue.


--------------------------------------------------
4. Enable X11 access for Docker
--------------------------------------------------

This is REQUIRED each time you reboot:

xhost +local:docker

You must see:
"local:docker being added to access control list"


--------------------------------------------------
5. Test X11 using xeyes (Docker → Host)
--------------------------------------------------

docker run -it --rm \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  x11-apps xeyes

You should see moving eyes appear.


--------------------------------------------------
6. Test ROS2 GUI directly from Docker
--------------------------------------------------

docker run -it --rm \
  --net=host \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  osrf/ros:iron-desktop \
  rviz2

If RVIZ2 opens, the system is ready ✅


--------------------------------------------------
7. Docker cleanup (when VS Code gets confused)
--------------------------------------------------

Use this when containers/images get corrupted:

docker system prune -a --volumes
docker network prune
docker volume prune

Restart Docker:

sudo systemctl restart docker


--------------------------------------------------
8. Emergency reset (nuclear option)
--------------------------------------------------

docker stop $(docker ps -aq) 2>/dev/null
docker rm -f $(docker ps -aq) 2>/dev/null
docker rmi -f $(docker images -q) 2>/dev/null


--------------------------------------------------
9. Important note about ROS Docs
--------------------------------------------------

THIS DOCUMENT IS MISLEADING for building ROS in VScode and Docker:

https://docs.ros.org/en/foxy/How-To-Guides/Setup-ROS-2-with-VSCode-and-Docker-Container.html

Problems:
- Wrong image
- No X11 GUI support
- Old VS Code extensions
- Wrong .devcontainer structure

This repo replaces that with a working setup.


--------------------------------------------------
10. Approved VS Code extensions (NOT deprecated)
--------------------------------------------------

KEEP:
- ms-vscode-remote.remote-containers
- ms-python.python
- ms-vscode.cpptools
- ms-vscode.cmake-tools
- eamodio.gitlens (optional)

REMOVE (deprecated):
- ms-iot.vscode-ros

VS Code may show:
"Develop Robot Operating System (ROS)... is deprecated"
Ignore and use the above instead.


--------------------------------------------------
11. Summary Checklist ✅
--------------------------------------------------

Docker installed: ✅
User in docker group: ✅
xhost configured: ✅
xeyes works: ✅
rviz2 works: ✅
VS Code Dev Container works: ✅


--------------------------------------------------
Maintainer
--------------------------------------------------

Mohamed Farouk Harraz
GitHub: https://github.com/harraz
Email: harraz@gmail.com
