# Host Setup for ROS2 Iron + Docker + VS Code (X11 Enabled)

This document records everything required on the **host system** to run ROS2 Iron + GUI tools (rviz2, rqt, xeyes) successfully inside Docker and VS Code Dev Containers.

This setup has been validated on:

- Debian Linux host
- Docker running as root
- ROS2 Iron containers based on `osrf/ros:iron-desktop`
- VS Code Dev Containers extension
- X11 applications forwarding correctly


------------------------------------------------------------
1. Docker Install (Debian)
------------------------------------------------------------

If Docker was installed using the Debian package, it may **not** create a `docker` group automatically.

Check group:

    getent group docker

If missing, create it:

    sudo groupadd docker
    sudo usermod -aG docker $USER

Confirm membership:

    getent group docker

Expected output:

    docker:x:994:harraz

Logout/login after this step.


------------------------------------------------------------
2. X11 Host Configuration
------------------------------------------------------------

Allow Docker containers to access your display:

    xhost +local:

Verify socket:

    ls /tmp/.X11-unix

Expected:

    X0  X1


------------------------------------------------------------
3. Required Test Packages
------------------------------------------------------------

Install on host:

    sudo apt install -y x11-apps

Test:

    xeyes

You should see eyes pop up.


------------------------------------------------------------
4. Docker X11 Test
------------------------------------------------------------

Verify container-to-display access:

    docker run -it --rm \
      --net=host \
      -e DISPLAY=$DISPLAY \
      -v /tmp/.X11-unix:/tmp/.X11-unix \
      ubuntu:22.04 bash

Inside container:

    apt update
    apt install -y x11-apps
    xeyes

If it works → X11 is correct ✔️


------------------------------------------------------------
5. ROS2 Image Used (IMPORTANT)
------------------------------------------------------------

Official ROS Docker guide is misleading for GUI.

Correct base:

    osrf/ros:iron-desktop

Your published image:

    harraztendo/ros2-iron-dev:latest

Includes:
- rviz2
- rqt
- ROS2 CLI
- Python3 / pip
- X11/OpenGL


------------------------------------------------------------
6. Required Runtime Variables
------------------------------------------------------------

    export ROS_DOMAIN_ID=42
    export QT_X11_NO_MITSHM=1


------------------------------------------------------------
7. Correct DevContainer Flags
------------------------------------------------------------

Must include:

    "--net=host"
    "-e DISPLAY=${env:DISPLAY}"
    "-v /tmp/.X11-unix:/tmp/.X11-unix"


------------------------------------------------------------
8. Final Test Command
------------------------------------------------------------

    docker run -it --rm \
     --net=host \
     -e DISPLAY=$DISPLAY \
     -e ROS_DOMAIN_ID=42 \
     -e QT_X11_NO_MITSHM=1 \
     -v /tmp/.X11-unix:/tmp/.X11-unix \
     harraztendo/ros2-iron-dev:latest bash

Inside:

    xeyes
    rviz2
    ros2 topic list


------------------------------------------------------------
WARNING ABOUT OFFICIAL GUIDE
------------------------------------------------------------

This is misleading for Iron + GUI:

https://docs.ros.org/en/foxy/How-To-Guides/Setup-ROS-2-with-VSCode-and-Docker-Container.html

Problems:
- Minimal image (no GUI)
- No X11 forwarding
- Wrong .devcontainer placement
- Outdated extensions

Use YOUR image instead.

