import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MySubscriber(Node):

    def __init__(self):
        super().__init__('sub_node')
        self.sub = self.create_subscription(String, 'sohi_topic', self.sub_cb, 10)
        self.get_logger().info ("Subscriber Node Running...")

    def sub_cb(self, msg):
        self.get_logger().info('Received message: ' + msg.data)


def main(args=None):
    rclpy.init(args=args)
    node = MySubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()