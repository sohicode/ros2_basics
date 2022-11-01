from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='topic_pkg',
            executable='rpm_pub',
            name='rpm_pub_node'
        ),
        Node(
            package='topic_pkg',
            executable='speed_calc',
            name='speed_calc_node',
            parameters=[
                {'wheel_radius': 0.5}
            ]
        ),
        Node(
            package='topic_pkg',
            executable='speed_sub',
            name='speed_sub_node'
        ),        
        ExecuteProcess(
            cmd=['ros2', 'topic', 'list'],
            output='screen'
        )
    ])