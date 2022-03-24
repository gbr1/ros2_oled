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
            ('/image_raw', '/display/right'),
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

    ld.add_action(declare_filename_cmd)
    ld.add_action(declare_publish_rate_cmd)
    ld.add_action(oled_node_left)
    ld.add_action(oled_node_right)

    return ld
