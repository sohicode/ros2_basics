import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
#https://github.com/ros2/common_interfaces/blob/foxy/geometry_msgs/msg/Twist.msg

class Stop(Node):

    def __init__(self):
        super().__init__('stop_node')
        self.counter = 0
        self.pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.pub_cb)
        
    def pub_cb(self):
        msg = Twist() 
        msg.linear.x = 0.0

        self.pub.publish(msg)
        self.get_logger().info('Published message: ' + str(msg.linear.x))


def main(args=None):
    rclpy.init(args=args)
    node = Stop()

    try:
        rclpy.spin_once(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()