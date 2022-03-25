#
# The MIT License
#
# Copyright (c) 2022 Giovanni di Dio Bruno https://gbr1.github.io
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():

    oled_node_left = Node(
        package='ros2_oled',
        executable='oled_node',
        namespace="display_left",
        parameters=[
            {'display.emulation':False},
            {'display.type':'ssd1306'},
            {'display.i2c.port':1},
        ],
        remappings=[
            ('/image_raw', '/display/left'),
        ]
    )

    oled_node_right = Node(
        package='ros2_oled',
        executable='oled_node',
        namespace="display_right",
        parameters=[
            {'display.emulation':False},
            {'display.type':'ssd1306'},
            {'display.i2c.port':0},
        ],
        remappings=[
            ('/image_raw', '/display/right'),
        ]
    )



    ld = LaunchDescription()

    ld.add_action(oled_node_left)
    ld.add_action(oled_node_right)

    return ld
