import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

RPM = 10

class RpmPublisher(Node):
    
    def __init__(self):
        super().__init__('rpm_pub_node')
        self.pub = self.create_publisher(Float32, 'rpm_topic', 10)
        self.timer = self.create_timer(2, self.rpm_pub_cb)
        self.get_logger().info('RPM Publisher Node Running...')

    def rpm_pub_cb(self):
        msg = Float32()
        msg.data = float(RPM)
        self.pub.publish(msg)
        self.get_logger().info('Published message: ' + str(msg.data))

    
def main(args=None):
    rclpy.init(args=args)
    node = RpmPublisher()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrup')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
