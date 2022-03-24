FROM dustynv/ros:foxy-ros-base-l4t-r32.7.1

ADD install.rosinstall .
RUN mkdir -p /opt/dev_ws/src && \
    vcs import /opt/dev_ws/src < install.rosinstall

RUN apt-get update -y && \
    apt-get install -y python3-natsort && \
    pip3 install -IU --no-cache-dir -r /opt/dev_ws/src/ros2_oled/ros2_oled/requirements.txt && \  
    rosdep install --from-paths /opt/dev_ws/src --ignore-src -r -y && \
    rm -rf /var/lib/apt/lists/*

RUN . /opt/ros/foxy/install/setup.sh && \
    cd /opt/dev_ws && \
    colcon build --symlink-install

RUN sed --in-place --expression \
        '$isource "/opt/dev_ws/install/setup.bash"' \
        /ros_entrypoint.sh    
  
	
STOPSIGNAL SIGINT

WORKDIR /opt/dev_ws/src
