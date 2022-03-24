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
