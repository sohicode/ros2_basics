import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class SpeedSubscriber(Node):

    def __init__(self):
        super().__init__('speed_sub_node')
        self.sub = self.create_subscription(Float32, 'speed_topic', self.sub_cb, 10)
        self.get_logger().info ("Speed Subscriber Node Running...")

    def sub_cb(self, msg):
        self.get_logger().info('Received message: ' + str(msg.data))


def main(args=None):
    rclpy.init(args=args)
    node = SpeedSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()