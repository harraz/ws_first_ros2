
# 🚀 ROS 2 Iron Dev Environment (Ubuntu + Docker + VS Code)

**Maintainer:** Mohamed Farouk Harraz
**Docker Hub:** `harraztendo/ros2-iron-dev`
**ROS Distribution:** Iron Irwini
**Base OS:** Ubuntu 22.04 (Jammy)

This repository provides a **ready-to-use ROS 2 Iron development environment** with:

✅ Docker image
✅ X11 / GUI support (`rviz2`, `xeyes`)
✅ VS Code Dev Container support
✅ Python3 + pip
✅ Networking preconfigured for ROS2
✅ Zero local ROS install needed

---

## 📦 What’s included

* ROS 2 Iron (desktop)
* `rviz2`, `ros2`, `xeyes`
* Python 3 + pip + venv
* iputils, git, curl
* X11 GUI support
* VS Code + Dev Container ready

---

## 🖥️ System Requirements

* Ubuntu / Debian (recommended)
* Docker installed
* VS Code + **Dev Containers** extension installed
* X11 running on host (`:0`)

---

## 🚀 Quick Start (VS Code – Recommended)

### 1. Clone this repo

```bash
git clone https://github.com/harraz/ws_first_ros2.git
cd ws_first_ros2
```

### 2. Allow X11 access

```bash
xhost +local:docker
```

### 3. Open in VS Code

```bash
code .
```

When VS Code asks:

> **"Folder contains a Dev Container configuration. Reopen in container?"**

✅ Click **Yes**

You’ll be inside the ROS2 container in ~1 minute.

---

## 🧪 Test it

In the VS Code container terminal:

```bash
ros2 topic list
rviz2
xeyes
```

You should see:

* ROS topics
* RViz GUI open
* X11 test window (eyes)

---

## 🐳 Docker — Manual Run (without VS Code)

```bash
xhost +local:docker

docker run -it --rm \
  --net=host \
  -e DISPLAY=$DISPLAY \
  -e ROS_DOMAIN_ID=42 \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v $(pwd):/projects/ws_first_ros2 \
  harraztendo/ros2-iron-dev:latest \
  /bin/bash
```

Then inside the container:

```bash
source /opt/ros/iron/setup.bash
rviz2
```

---

## 📁 Repository Structure

```
ws_first_ros2/
├── .devcontainer/
│   └── devcontainer.json
├── src/
├── build/
├── install/
└── README.md
```

---

## 🧩 VS Code Extensions Used

Only essential extensions are included:

* `ms-iot.vscode-ros`
* `ms-python.python`
* `ms-vscode.cpptools`
* `twxs.cmake`

No bloat. No deprecated extensions.

---

## 🐋 Docker Image

**Name:** `harraztendo/ros2-iron-dev:latest`

The image includes:

* ROS2 Iron (desktop)
* X11 GUI support
* Python + essentials
* User: `harraz`

Pull it:

```bash
docker pull harraztendo/ros2-iron-dev:latest
```

---

## 🧠 Notes

* `ROS_DOMAIN_ID=42` is preconfigured
* `--net=host` is used for discovery
* Autocomplete is enabled
* Alias: `ws` → sources the workspace

---

## 👤 Author

**Mohamed Farouk Harraz**
📧 [harraz@gmail.com](mailto:harraz@gmail.com)
🌐 [https://github.com/harraz](https://github.com/harraz)

