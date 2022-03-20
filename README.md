# ros2_oled
A simple package to use [luma.oled](https://github.com/rm-hull/luma.oled) on Jetson Nano and other SBCs across ROS2.

## Build docker
`docker build -t gbr1/ros2_luma:latest .`

## Run docker
`docker run -v $HOME/dev_ws:/root/dev_ws --device /dev/i2c-1 -it --rm gbr1/ros2_luma:latest bash`

