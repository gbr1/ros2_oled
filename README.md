# ros2_oled
A simple package to use [luma.oled](https://github.com/rm-hull/luma.oled) on Jetson Nano and other SBCs across ROS2.


## Dependencies and install

- ROS2
- Luma
    ```bash
        sudo pip3 install -IU --no-cache-dir pillow
        sudo pip3 install -IU --no-cache-dir luma.oled
    ```
- Luma emulator (?)

## Usage

`ros2 run ros2_oled oled_node`
<br>

if you want to test you can use [ros2_video_streamer](https://github.com/gbr1/ros2_video_streamer) package: <br>
`ros2 run camera_simulator camera_simulator --type video --path <path to video>`








## Build docker
`docker build -t gbr1/ros2_luma:latest .`

## Run docker
`docker run --runtime nvidia -v $HOME/dev_ws:/root/dev_ws --device /dev/i2c-1 -it --rm gbr1/ros2_luma:latest bash`<br>
for a new terminal:<br>
`docker ps -a` <br>
check name ang then:<br>
`docker exec -it <name> bash`



---
> ***Copyright 2022 © G. Bruno under MIT license***

