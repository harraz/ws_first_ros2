FROM osrf/ros:iron-desktop

LABEL maintainer="Mohamed Farouk Harraz <harraz@gmail.com>"
LABEL description="ROS2 Iron + X11 + Python + DevContainer support (Optimized)"
LABEL org.opencontainers.image.source="https://github.com/harraz"
LABEL org.opencontainers.image.authors="Mohamed Farouk Harraz"

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=America/New_York

# ----------------------------------------------------
# Force IPv4 + Faster Ubuntu mirrors (speed + reliability)
# ----------------------------------------------------
RUN echo 'Acquire::ForceIPv4 "true";' > /etc/apt/apt.conf.d/99force-ipv4 \
 && sed -i 's|http://archive.ubuntu.com|http://us.archive.ubuntu.com|g' /etc/apt/sources.list \
 && sed -i 's|http://security.ubuntu.com|http://us.archive.ubuntu.com|g' /etc/apt/sources.list

# ----------------------------------------------------
# System + Dev Tools + Python + X11
# ----------------------------------------------------
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
        bash-completion \
        python3 \
        python3-pip \
        python3-venv \
        git \
        curl \
        wget \
        nano \
        tree \
        iputils-ping \
        net-tools \
        x11-apps \
        xauth \
        tzdata \
        locales \
    && rm -rf /var/lib/apt/lists/*

# ----------------------------------------------------
# Locale
# ----------------------------------------------------
RUN locale-gen en_US.UTF-8
ENV LANG=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8

# ----------------------------------------------------
# Python tooling
# ----------------------------------------------------
RUN pip3 install --no-cache-dir --upgrade pip setuptools wheel

# ----------------------------------------------------
# Workspace root
# ----------------------------------------------------
WORKDIR /projects/ws_first_ros2

CMD ["/bin/bash"]

