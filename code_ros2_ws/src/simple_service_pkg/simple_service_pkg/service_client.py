import rclpy
from rclpy.node import Node
from std_srvs.srv import SetBool

class PowerClient(Node):

    def __init__(self):
        super().__init__('service_client_node')
        self.client = self.create_client(SetBool, 'power_service')
        self.req = SetBool.Request()
        self.get_logger().info('Service Client Start')

    def send_request(self, user_input):
        self.req.data = (user_input.lower() == 'on')

        self.client.wait_for_service()
        self.future = self.client.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        self.result = self.future.result()
        return self.result


def main(args=None):
    rclpy.init(args=args)
    node = PowerClient()
    try:
        #pass
        user_input = input('Enter an power "on" or "off" : ')
        res = node.send_request(user_input)
        node.get_logger().info('Server returned: ' + res.message)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()