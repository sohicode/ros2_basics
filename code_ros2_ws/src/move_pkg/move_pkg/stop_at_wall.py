import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
#https://github.com/ros2/common_interfaces/blob/foxy/geometry_msgs/msg/Twist.msg
#https://github.com/ros2/common_interfaces/blob/rolling/sensor_msgs/msg/LaserScan.msg

class StopAtWall(Node):

    def __init__(self):
        super().__init__('stop_at_wall_node')
        self.counter = 0
        self.pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self.sub = self.create_subscription(LaserScan, 'scan', self.sub_cb, 10)
        self.get_logger().info('StopAtWall Node Running...')

    def sub_cb(self, msg):
        
        # stop
        if msg.ranges[0] < 0.5:
            self.pub_cb(0.0)
        else:
            self.pub_cb(0.2)

        self.get_logger().info('Received message: ')

    def pub_cb(self, x):
        msg = Twist() 
        msg.linear.x = x

        self.pub.publish(msg)
        self.get_logger().info('Published message: ' + str(msg.linear.x))


def main(args=None):
    rclpy.init(args=args)
    node = StopAtWall()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()