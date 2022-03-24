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
`ros2 run image_publisher image_publisher --ros-args -p filename:=<path to video> -p publish_rate:=<fps>`


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
`docker run --runtime nvidia -v $HOME/dev_ws/src:/opt/dev_ws/src --device /dev/i2c-1 -it --rm gbr1/ros2_luma:latest bash`<br>
for a new terminal:<br>
`docker ps -a` <br>
check name and then:<br>
`docker exec -it <name> bash`<br>
You need to `source /opt/dev_ws/install/setup.bash` in every new terminal.



---
> ***Copyright 2022 © G. Bruno under MIT license***

