import rclpy
from rclpy.node import Node
from std_srvs.srv import SetBool

class PowerServer(Node):
    def __init__(self):
        super().__init__('service_server_node')
        self.srv = self.create_service(SetBool, 'power_service', self.power_cb)
        self.get_logger().info("Service Server Running...")

    def power_cb(self, request, response):
        self.get_logger().info('Request Received... ')
        
        if request.data:
            response.success = True
            response.message = 'Power On'
        elif not request.data:
            response.success = True
            response.message = 'Power Off'
        else:
            response.success = False
            response.message = 'Error'
        
        print(request)
        print(response)
        
        return response


def main(args=None):
    rclpy.init(args=args)
    node = PowerServer()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
    