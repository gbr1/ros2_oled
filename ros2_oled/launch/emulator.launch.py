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
    filename=LaunchConfiguration('filename')
    publish_rate=LaunchConfiguration('publish_rate')
    declare_filename_cmd = DeclareLaunchArgument('filename', description='Filename used for video')
    declare_publish_rate_cmd = DeclareLaunchArgument('publish_rate', default_value='25.0', description='Publish rate')



    oled_node = Node(
        package='ros2_oled',
        executable='oled_node',
        namespace="display_1",
        parameters=[
            {'display.emulation':True},
            {'display.type':'pygame'},
        ]

    )

    video_node = Node(
        package='image_publisher',
        executable='image_publisher_node',
        parameters=[
            {'filename':filename},
            {'publish_rate':publish_rate},
        ]
    )

    ld = LaunchDescription()

    ld.add_action(declare_filename_cmd)
    ld.add_action(declare_publish_rate_cmd)
    ld.add_action(oled_node)
    ld.add_action(video_node)


    return ld
