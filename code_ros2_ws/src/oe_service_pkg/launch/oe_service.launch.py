from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
def generate_launch_description():
    return LaunchDescription([
        Node(
            package='oe_service_pkg',
            executable='oe_server',
            name='oe_server_node'
        ),
        Node(
            package='oe_service_pkg',
            executable='oe_client',
            name='oe_client_node'
        ),
        ExecuteProcess(
            cmd=['ros2', 'topic', 'list'],
            output='screen'
        )
    ])