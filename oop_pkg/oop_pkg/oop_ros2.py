#! /usr/bin/env python3
import rclpy
from rclpy.node import Node

class OopNode(Node):

    def __init__(self):
        super().__init__('oop_node')
        self.counter_ = 0
        self.get_logger().info('Hello World!')
        self.create_timer(0.5, self.timer_cb)

    def timer_cb(self):
        self.counter_ += 1
        self.get_logger().info('Hello ' + str(self.counter_))


def main(args = None):
    rclpy.init(args=args)
    node = OopNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
