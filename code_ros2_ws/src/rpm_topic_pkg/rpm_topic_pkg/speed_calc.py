import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

WHEEL_RADIUS = 12.5 / 100


class SpeedCalculator(Node):

    def __init__(self):
        super().__init__('speed_calc_node')
        self.sub = self.create_subscription(Float32, 'rpm_topic', self.speed_calc_cb, 10)
        self.pub = self.create_publisher(Float32, 'speed_tpic', 10)
        self.get_logger().info('Speed Calculator Node Started...')


    def speed_calc_cb(self, rpm_msg):
        self.get_logger().info('Received rpm message: ' + str(rpm_msg.data))
        speed = rpm_msg.data * WHEEL_RADIUS * 2 * 3.14159 / 60 # speed in m/s
        speed_msg = Float32()
        speed_msg.data = float(speed)
        self.pub.publish(speed_msg)
        self.get_logger().info('Published speed message: ' + str(speed_msg.data))
        

def main(args=None):
    rclpy.init(args=args)
    node = SpeedCalculator()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()