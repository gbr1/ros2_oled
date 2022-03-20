FROM dustynv/ros:foxy-ros-base-l4t-r32.7.1
ADD requirements.txt .
ENV ROS_DISTRO=foxy
RUN apt-get update -y && \
    apt-get install -y python3-natsort
RUN pip3 install -IU --no-cache-dir -r requirements.txt && \  
    rm -rf /var/lib/apt/lists/*
	
STOPSIGNAL SIGINT

WORKDIR /root
