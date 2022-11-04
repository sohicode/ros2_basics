import rclpy
from rclpy.node import Node
from interface_pkg.srv import OddEvenCheck

class OddEvenCheckClient(Node):
    def __init__(self):
        super().__init__('odd_even_client_node')
        # pass
        self.get_logger().info('Service Client Start')
    
    def send_request(self, num):
        # pass
        self.client.wait_for_service()
        self.future = self.client.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        self.result = self.future.result()
        return self.result
 

def main(args=None):
    rclpy.init(args=args)
    node = OddEvenCheckClient()
    try:
        # pass
        node.get_logger().info('Server returned: ' + res.decision)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()