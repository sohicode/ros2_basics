import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MyPublisher(Node):
    
    def __init__(self):
        super().__init__('pub_node')
        self.counter = 0
        self.pub = self.create_publisher(String, 'my_topic', 10)
        self.timer = self.create_timer(1, self.pub_cb)
        self.get_logger().info('Publisher Node Running...')

    def pub_cb(self):
        self.counter += 1
        msg = String()
        msg.data = 'hi: ' + str(self.counter)
        self.pub.publish(msg)
        self.get_logger().info('Published message: ' + msg.data)

    
def main(args=None):
    rclpy.init(args=args)
    node = MyPublisher()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
