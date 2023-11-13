import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class ScanInfo(Node):

    def __init__(self):
        super().__init__('scan_info_node')
        self.sub = self.create_subscription(LaserScan, 'scan', self.sub_cb, 10)
        self.get_logger().info('ScanInfo Node Running...')

    def sub_cb(self, msg):
        self.get_logger().info('Received message: ')

        print('time stamp = ' + str(msg.header.stamp))
        print('angle_min = ' + str(msg.angle_min) + ' rad')
        print('angle_max = ' + str(msg.angle_max) + ' rad')
        print('angle_increment = ' + str(msg.angle_increment) + ' rad')
        
        print('time_increment = ' + str(msg.time_increment) + ' seconds')
        print('scan_time = ' + str(msg.scan_time) + ' seconds')

        # Distance Range(120 ~ 3,500mm)
        print('range_min = ' + str(msg.range_min) + ' m')
        print('range_max = ' + str(msg.range_max) + ' m')

        # Angular Range(360 degrees), Angular Resolution(1 degree)
        print('ranges len = ' + str(len(msg.ranges)))
        print('intensities len = ' + str(len(msg.intensities)))

        print('ranges - 0 degree = ' + str(msg.ranges[0]))
        print('ranges - 90 degree = ' + str(msg.ranges[90]))
        print('ranges - 180 degree = ' + str(msg.ranges[180]))
        print('ranges - 270 degree = ' + str(msg.ranges[270]))
        

def main(args=None):
    rclpy.init(args=args)
    node = ScanInfo()

    try:
        rclpy.spin_once(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()