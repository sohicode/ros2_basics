import rclpy
from rclpy.node import Node
from example_interfaces.srv import SetBool

class DeliveryCheckService(Node):

    def __init__(self):
        super().__init__('delivery_check_service')
        
        # 'check_delivery' 서비스 서버 생성
        self.srv = self.create_service(SetBool, 'check_delivery', self.check_delivery_callback)
        
        # 배달 완료 상태를 저장하는 변수
        self.delivery_complete = False
    
    # 배달 완료 여부를 처리하는 콜백 함수
    def check_delivery_callback(self, request, response):
        print("-start-")
        print("배달 중입니다. 계속하려면 엔터 키를 누르세요...")
        user_input = input("배달이 끝났으면 'y'를 입력하세요...")  # 사용자 입력을 대기

        # 'y' 입력 시 배달 완료 상태로 설정
        if user_input == 'y':
            self.delivery_complete = True
            print('complete 설정')

        if self.delivery_complete:
            response.success = True
            response.message = "배달이 완료되었습니다."
        else:
            response.success = False
            response.message = "배달이 아직 완료되지 않았습니다."

        print(response.message)
        print("-end-")
        return response


    
    # 임의로 배달 완료 상태를 변경하는 함수 (테스트 용도)
    def set_delivery_complete(self, status: bool):
        self.delivery_complete = status
        print(f"배달 완료 상태 설정됨: {status}")

def main(args=None):
    rclpy.init(args=args)

    delivery_check_service = DeliveryCheckService()

    print("배달 확인 서비스가 실행 중입니다.")
    
    try:
        # 노드를 실행하여 서비스 요청을 처리
        rclpy.spin(delivery_check_service)
    except KeyboardInterrupt:
        pass
    finally:
        # 노드 종료
        delivery_check_service.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
