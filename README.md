# ros2_oled
A simple package to use [luma.oled](https://github.com/rm-hull/luma.oled) on Jetson Nano and other SBCs across ROS2.


## Dependencies and install

- ROS2
- Luma
    ```bash
        sudo pip3 install -IU --no-cache-dir pillow
        sudo pip3 install -IU --no-cache-dir luma.oled
    ```
- Luma emulator (if you need on desktop)
    ```bash
        sudo apt install python3-dev python3-pip build-essential
        sudo apt install libsdl-dev libportmidi-dev libsdl-ttf2.0-dev libsdl-mixer1.2-dev libsdl-image1.2-dev
        sudo -H pip3 install --upgrade --ignore-installed pip3 setuptools
        sudo -H pip3 install --upgrade luma.emulator
    ```


## Usage

`ros2 run ros2_oled oled_node`
<br>

if you want to test you can use `image_publisher` package: <br>
`ros2 run image_publisher image_publisher_node --ros-args -p filename:=<path to video> -p publish_rate:=<fps>`

<br>

## Topics
`/image_raw`, _sensor_msgs::image_ topic subscriptio

## Parameters
- display.emulation, _bool_, default: false
- display.type, _string_, default: ssd1306, others: pygame, asciiblock, asciiart, gifanim, capture
- display.i2c.port, _int_, defalut: 0, it is the physical i2c port used
- display.i2c.address, _int_, default: 0x3c, it is display's address

<br>
<br>





## Build docker on Jetson SBCs

**Note:** You need to edit `/etc/docker/daemon.json` as following: <br>

```json
{
    "runtimes": {
        "nvidia": {
            "path": "nvidia-container-runtime",
            "runtimeArgs": []
        }
    },
    "default-runtime": "nvidia"	
}
```
and then: `sudo systemctl restart docker.service` <br>
<br>
To build your docker:<br>
`docker build -t gbr1/ros2_luma:latest .`
<br>
To remove rubbish files:<br>
`docker system prune`

## Run docker on Jetson SBCs

`docker run --runtime nvidia -v $HOME/dev_ws/src:/opt/dev_ws/src --device /dev/i2c-0 --device /dev/i2c-1 -it --rm gbr1/ros2_luma:latest bash`<br>
for a new terminal:<br>
`docker ps -a` <br>
check name and then:<br>
`docker exec -it <name> bash`<br>
You need to `source /opt/dev_ws/install/setup.bash` in every new terminal.

<br>
<br>

## [Nanosaur.ai](https://nanosaur.ai)

To use on nanosaur, start the docker and then launch: <br>
`ros2 launch ros2_oled nanosaur_demo.launch.py` <br>
after that open other two terminals, exec the docker bash, source ros2 in each docker bash and then: <br>
`ros2 run image_publisher image_publisher_node --ros-args -p filename:=<your video.mp4> -p publish_rate:=30.0  -r __ns:=/left_video -r /left_video/image_raw:=/display/left` <br>
and in the other terminal: <br>
`ros2 run image_publisher image_publisher_node --ros-args -p filename:=<your video.mp4> -p publish_rate:=30.0 -r __ns:=/right_video -r /right_video/image_raw:=/display/right` <br>




---
> ***Copyright 2022 © G. Bruno under MIT license***

