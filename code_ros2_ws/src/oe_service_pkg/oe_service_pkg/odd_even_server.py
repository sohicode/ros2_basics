import rclpy
from rclpy.node import Node
from interface_pkg.srv import OddEvenCheck

class OddEvenCheckServer(Node):
    def __init__(self):
        super().__init__('odd_even_server_node')
        self.srv = self.create_service(OddEvenCheck, 'odd_even_check', self.odd_even_cb)
        self.get_logger().info('Odd Even Check Service Server Running...')
    
    def odd_even_cb(self, request, response):
        self.get_logger().info('Request Received... ')

        if request.number % 2 == 0:
            response.decision = 'Even'
        elif request.number % 2 == 1:
            response.decision = 'Odd'
        else:
            response.decision = 'Error'
        
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