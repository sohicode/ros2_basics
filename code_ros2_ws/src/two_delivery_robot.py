import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from example_interfaces.srv import SetBool

class DeliveryRobot(Node):

    def __init__(self, name):
        super().__init__(name)
        self.client = self.create_client(SetBool, 'check_delivery')
        self.delivery_complete = False  # 배달 완료 상태 초기화
        self.robot_name = name  # 로봇의 이름 설정

    # 배달 완료 여부 확인 (비동기 방식)
    def check_delivery_status_async(self):
        request = SetBool.Request()

        if self.client.wait_for_service(timeout_sec=1.0):
            print(f"{self.robot_name} 배달 요청 (비동기)...")
            future = self.client.call_async(request)
            future.add_done_callback(self.delivery_response_callback)
            print(f"{self.robot_name} 배달 완료 여부 확인 중 (비동기)...")
        else:
            print(f"{self.robot_name} 서비스를 찾을 수 없습니다.")
    
    # 서비스 응답을 처리하는 콜백 함수 (비동기 방식)
    def delivery_response_callback(self, future):
        try:
            print(f"---{self.robot_name} delivery_response_callback start---")
            response = future.result()
            if response.success:
                self.delivery_complete = True
                print(f"{self.robot_name} 배달 완료: {response.message}")
            else:
                self.delivery_complete = False
                print(f"{self.robot_name} 배달 미완료: {response.message}")
        except Exception as e:
            print(f"{self.robot_name} 서비스 호출 실패: {e}")
        print(f"---{self.robot_name} delivery_response_callback end---")


def main(args=None):
    rclpy.init(args=args)

    # 두 대의 배달 로봇 생성
    robot1 = DeliveryRobot('delivery_robot_1')
    robot2 = DeliveryRobot('delivery_robot_2')

    # MultiThreadedExecutor 사용하여 두 대의 로봇을 동시에 실행
    executor = MultiThreadedExecutor()
    executor.add_node(robot1)
    executor.add_node(robot2)

    try:
        # 두 로봇 모두 비동기 방식으로 배달 완료 여부 확인
        robot1.check_delivery_status_async()
        robot2.check_delivery_status_async()

        # MultiThreadedExecutor로 두 로봇이 동시에 실행되도록 함
        executor.spin()

    except KeyboardInterrupt:
        print("사용자가 실행을 중단했습니다.")

    finally:
        # 노드 및 실행기 종료
        executor.shutdown()
        robot1.destroy_node()
        robot2.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
