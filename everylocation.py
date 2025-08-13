import time
from lerobot.motors.motors_bus import Motor, MotorNormMode
from lerobot.motors.feetech import FeetechMotorsBus

def counterclockwise_rotate():
    port = "COM3"  # 실제 연결된 포트명

    # ID 1~6까지의 모터를 생성
    motors = {
        f"motor_{i}": Motor(id=i, model="sts3215", norm_mode=MotorNormMode.DEGREES)
        for i in range(1, 7)
    }

    bus = FeetechMotorsBus(port=port, motors=motors)
    bus.connect()

    # 모든 모터 토크 활성화
    for name in motors:
        bus.enable_torque(name)

    # 위치 읽기
    data = bus.sync_read("Present_Position", motors=list(motors.keys()), normalize=False)

    # 결과 출력
    print("모든 모터 pos")
    for name, position in data.items():
        print(f"{name}: {position:.2f}")

    time.sleep(2)
    input("모터가 유지됩니다. 종료하려면 Enter 키를 누르세요...")
    # 토크 비활성화
    for name in motors:
       bus.disable_torque(name)

    bus.disconnect()

if __name__ == "__main__":
    counterclockwise_rotate()
