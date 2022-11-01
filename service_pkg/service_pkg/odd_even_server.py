import rclpy
from rclpy.node import Node
from interface_pkg.srv import OddEvenCheck

class OddEvenCheckServer(Node):
    def __init__(self):
        super().__init__('odd_even_server_node')
        # pass
        self.get_logger().info('Odd Even Check Service Server Running...')
    
    def odd_even_cb(self, request, response):
        self.get_logger().info('Request Received... ')

        # pass
        
        print(request)
        print(response)

        return response


def main(args=None):
    rclpy.init(args=args)
    node = OddEvenCheckServer()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()