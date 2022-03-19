# ros2_luma
A simple package to use Luma.oled on jetson nano and other sbc across ROS2

## Build docker
`docker build -t gbr1/ros2_luma:latest .`

## Run docker
`docker run -v $HOME/dev_ws:/root/dev_ws --device /dev/i2c-1 -it --rm gbr1/ros2_luma:latest bash`

