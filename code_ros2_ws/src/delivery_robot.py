import rclpy 
from rclpy.node import Node
from example_interfaces.srv import SetBool

class DeliveryRobot(Node):

    def __init__(self):
        super().__init__('delivery_robot')
        
        # 배달 목적지 도착 확인을 위한 비동기 서비스 클라이언트
        self.client = self.create_client(SetBool, 'check_delivery')
        
    # 배달 완료 여부 확인 (비동기 방식)
    def check_delivery_status_async(self):
        # 서비스 요청 생성
        request = SetBool.Request()
        
        # 서비스가 준비되었는지 확인 후 비동기 호출
        # - 서비스가 준비되면 call_async로 비동기 요청을 보낸다.
        # - 요청을 보내고 나면 즉시 반환되며, 응답이 완료되면 콜백 함수 delivery_response_callback이 호출된다.
        # - 이 방식은 요청을 보낸 후 바로 다음 작업을 수행할 수 있다.

        # (참고)서비스가 준비되었는지 확인 후 동기 호출
        # - 서비스가 준비되면 call로 동기 요청을 보낸다.
        # - 요청이 완료될 때까지 기다리며, 응답을 받으면 그 결과를 처리한다.
        # - 동기 방식은 요청을 보내고 결과를 기다리기 때문에, 그 사이 다른 작업을 수행할 수 없다.

        if self.client.wait_for_service(timeout_sec=1.0):
            print("배달 요청 (비동기)...")
            future = self.client.call_async(request)  # 비동기 서비스 호출
            future.add_done_callback(self.delivery_response_callback)  # 응답 완료 시 호출할 콜백 추가
            print("배달 완료 여부 확인 중 (비동기)...")
            # 비동기 처리가 끝날 때까지 스핀 처리하여 기다림
            while not future.done():
                print("ing")
                rclpy.spin_once(self, timeout_sec=1)

            # 비동기 호출 끝난 후에도 spin_once 실행하여 콜백 처리 유지
            print("비동기 호출 끝남. 응답 대기 중...")
            rclpy.spin_once(self, timeout_sec=1)  # 추가적인 spin 호출

            print("비동기 호출 끝남")
        else:
            print("서비스를 찾을 수 없습니다.")
    
    # 서비스 응답을 처리하는 콜백 함수 (비동기 방식)
    def delivery_response_callback(self, future):
        print("---delivery_response_callback start---")
        try:
            response = future.result()
            if response.success:
                self.delivery_complete = True  # 배달 완료 상태 설정
                print("배달 완료: ", response.message)
            else:
                self.delivery_complete = False  # 배달 미완료 상태 설정
                print("배달 미완료: ", response.message)
        except Exception as e:
            print(f"서비스 호출 실패: {e}")
        print("---delivery_response_callback end---")

    
def main(args=None):
    rclpy.init(args=args)
    
    delivery_robot = DeliveryRobot()

    try:
        # 비동기 방식으로 배달 완료 여부 확인
        print("비동기 방식으로 배달 완료 여부 확인")
        delivery_robot.check_delivery_status_async()


    except KeyboardInterrupt:
        print("사용자가 실행을 중단했습니다.")

    finally:
        rclpy.shutdown()

if __name__ == '__main__':
    main()
