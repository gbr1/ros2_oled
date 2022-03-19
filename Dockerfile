FROM dustynv/ros:foxy-ros-base-l4t-r32.7.1
ADD requirements.txt .
RUN pip3 install -IU --no-cache-dir -r requirements.txt
WORKDIR /root
