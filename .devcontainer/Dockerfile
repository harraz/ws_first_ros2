FROM osrf/ros:iron-desktop

LABEL maintainer="Mohamed Farouk Harraz <harraz@gmail.com>"
LABEL description="ROS2 Iron + X11 + Python + DevContainer support"
LABEL org.opencontainers.image.source="https://github.com/harraz"
LABEL org.opencontainers.image.authors="Mohamed Farouk Harraz"

ENV DEBIAN_FRONTEND=noninteractive

# -------------------------------
# Tools + Python + X11
# -------------------------------
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        bash-completion \
        python3 \
        python3-pip \
        python3-venv \
        git \
        curl \
        wget \
        nano \
        iputils-ping \
        net-tools \
        x11-apps \
        xauth \
    && rm -rf /var/lib/apt/lists/*

# -------------------------------
# ROS2 shell setup (root)
# -------------------------------
RUN echo "if [ -f /opt/ros/iron/setup.bash ]; then source /opt/ros/iron/setup.bash; fi" >> /root/.bashrc \
 && echo "alias ws='cd /projects/ws_first_ros2 && [ -f install/setup.bash ] && source install/setup.bash'" >> /root/.bashrc \
 && echo "alias py='python3'" >> /root/.bashrc

WORKDIR /projects/ws_first_ros2
CMD ["/bin/bash"]
