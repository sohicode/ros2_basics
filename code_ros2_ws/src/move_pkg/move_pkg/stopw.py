import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
#https://github.com/ros2/common_interfaces/blob/foxy/geometry_msgs/msg/Twist.msg

class StopW(Node):

    x = 0.2

    def __init__(self):
        super().__init__('stopw_node')
        self.counter = 0
        self.pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.pub_cb)
        self.sub = self.create_subscription(LaserScan, 'scan', self.sub_cb, 10)


    def pub_cb(self):
        msg = Twist() 
        msg.linear.x = self.x

        self.pub.publish(msg)
        self.get_logger().info('Published message: ' + str(msg.linear.x))

    def sub_cb(self, msg):
        self.get_logger().info('ranges - 0 degree = ' + str(msg.ranges[0]))

        if msg.ranges[0] < 0.5:
            self.x = 0.0




def main(args=None):
    rclpy.init(args=args)
    node = StopW()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()