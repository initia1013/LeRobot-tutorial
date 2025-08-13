import time
from lerobot.motors.motors_bus import Motor, MotorNormMode
from lerobot.motors.feetech import FeetechMotorsBus
#################초기 상태로 시작하는 코드##############################
def final():
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
										
    target_positions = {
        "motor_1": 2047.00,
        "motor_2": 880.00,
        "motor_3": 3113.00,
        "motor_4": 2782.00,
        "motor_5": 2047.00,
        "motor_6": 2050.00,
    }

    # 동기식 위치 명령 전송
	#바로 밑 코드의 900 이 부분이 속도 조절부임
    for name in motors:
    	bus.write("Goal_Velocity", name, 1200) 

    for name, pos in target_positions.items():
        bus.write("Goal_Position", name, int(pos), normalize=False)
    #time.sleep도 중요하니까 지우면 안됨!! (모터 작동시간 보장)
    time.sleep(2)
#################여기부터 좌표 지정 수행 코드 부분(순차적으로 수행동작 나눌 필요있음)##############################

#########  1번 동작
    target_positions = {
        "motor_1": 1750.00,
        "motor_2": 1578.00,
        "motor_3": 2317.00,
        "motor_4": 2797.00,
        "motor_5": 2086.00,
        "motor_6": 2060.00,
    }

    # 동기식 위치 명령 전송
	#바로 밑 코드의 900 이 부분이 속도 조절부임
    for name in motors:
    	bus.write("Goal_Velocity", name, 900) 

    for name, pos in target_positions.items():
        bus.write("Goal_Position", name, int(pos), normalize=False)
    #time.sleep도 중요하니까 지우면 안됨!! (모터 작동시간 보장)
    time.sleep(2)

##########   2번 동작
    target_positions = {
        "motor_1": 1668.00,
	"motor_2": 2012.00,
        "motor_3": 2049.00,
        "motor_4": 2797.00,
        "motor_5": 2086.00,
        "motor_6": 2060.00,
    }
    # 동기식 위치 명령 전송
	#바로 밑 코드의 900 이 부분이 속도 조절부임
    for name in motors:
    	bus.write("Goal_Velocity", name, 900) 

    for name, pos in target_positions.items():
        bus.write("Goal_Position", name, int(pos), normalize=False)
    #time.sleep도 중요하니까 지우면 안됨!!
    time.sleep(2)

##########  3번 동작
    target_positions = {
        "motor_1": 1690.00,
	"motor_2": 2376.00,
        "motor_3": 1636.00,
        "motor_4": 3074.00,
        "motor_5": 2051.00,
        "motor_6": 2360.00,
    }
    # 동기식 위치 명령 전송
	#바로 밑 코드의 900 이 부분이 속도 조절부임
    for name in motors:
    	bus.write("Goal_Velocity", name, 900) 

    for name, pos in target_positions.items():
        bus.write("Goal_Position", name, int(pos), normalize=False)
    #time.sleep도 중요하니까 지우면 안됨!!
    time.sleep(2)

##########   4번 동작
    target_positions = {
        "motor_1": 1684.00,
        "motor_2": 2497.00,
        "motor_3": 1596.00,
        "motor_4": 2989.00,
        "motor_5": 2093.00,
        "motor_6": 2323.00,
    }
    # 동기식 위치 명령 전송
	#바로 밑 코드의 900 이 부분이 속도 조절부임
    for name in motors:
    	bus.write("Goal_Velocity", name, 900) 

    for name, pos in target_positions.items():
        bus.write("Goal_Position", name, int(pos), normalize=False)
    #time.sleep도 중요하니까 지우면 안됨!!
    time.sleep(2)



######### 5번 동작 (잡기)
    target_positions = {
        "motor_1": 1684.00,
        "motor_2": 2497.00,
        "motor_3": 1596.00,
        "motor_4": 2989.00,
        "motor_5": 2093.00,
        "motor_6": 2230.00,

    }
    # 동기식 위치 명령 전송
	#바로 밑 코드의 900 이 부분이 속도 조절부임
    for name in motors:
    	bus.write("Goal_Velocity", name, 900) 

    for name, pos in target_positions.items():
        bus.write("Goal_Position", name, int(pos), normalize=False)
    #time.sleep도 중요하니까 지우면 안됨!!
    time.sleep(2)



###############잡고 돌리는 부분######################

    target_positions = {
        "motor_1": 1684.00,
        "motor_2": 2497.00,
        "motor_3": 1596.00,
        "motor_4": 2989.00,
        "motor_5": 2093.00+2047.00,
        "motor_6": 2230.00,

    }
    # 동기식 위치 명령 전송
	#바로 밑 코드의 900 이 부분이 속도 조절부임
    for name in motors:
    	bus.write("Goal_Velocity", name, 900) 

    for name, pos in target_positions.items():
        bus.write("Goal_Position", name, int(pos), normalize=False)
    #time.sleep도 중요하니까 지우면 안됨!!
    time.sleep(3)


    target_positions = {
        "motor_1": 1684.00,
        "motor_2": 2497.00,
        "motor_3": 1596.00,
        "motor_4": 2989.00,
        "motor_5": 2093.00,
        "motor_6": 2230.00,

    }
    # 동기식 위치 명령 전송
	#바로 밑 코드의 900 이 부분이 속도 조절부임
    for name in motors:
    	bus.write("Goal_Velocity", name, 900) 

    for name, pos in target_positions.items():
        bus.write("Goal_Position", name, int(pos), normalize=False)
    #time.sleep도 중요하니까 지우면 안됨!!
    time.sleep(3)

######### 5번 역동작 (놓기)
    target_positions = {
        "motor_1": 1684.00,
        "motor_2": 2497.00,
        "motor_3": 1596.00,
        "motor_4": 2989.00,
        "motor_5": 2093.00,
        "motor_6": 2323.00,

    }
    # 동기식 위치 명령 전송
	#바로 밑 코드의 900 이 부분이 속도 조절부임
    for name in motors:
    	bus.write("Goal_Velocity", name, 900) 

    for name, pos in target_positions.items():
        bus.write("Goal_Position", name, int(pos), normalize=False)
    #time.sleep도 중요하니까 지우면 안됨!!
    time.sleep(1)


########################복귀 후 종료 코드(동작 세분화 할 필요 있음 )



######### 4번 동작
    target_positions = {
        "motor_1": 1684.00,
        "motor_2": 2497.00,
        "motor_3": 1596.00,
        "motor_4": 2989.00,
        "motor_5": 2093.00,
        "motor_6": 2323.00,
    }
    # 동기식 위치 명령 전송
	#바로 밑 코드의 900 이 부분이 속도 조절부임
    for name in motors:
    	bus.write("Goal_Velocity", name, 900) 

    for name, pos in target_positions.items():
        bus.write("Goal_Position", name, int(pos), normalize=False)
    #time.sleep도 중요하니까 지우면 안됨!!
    time.sleep(2)


##########   2번 동작
    target_positions = {
        "motor_1": 1668.00,
	"motor_2": 2012.00,
        "motor_3": 2049.00,
        "motor_4": 2797.00,
        "motor_5": 2086.00,
        "motor_6": 2323.00,
    }
    # 동기식 위치 명령 전송
	#바로 밑 코드의 900 이 부분이 속도 조절부임
    for name in motors:
    	bus.write("Goal_Velocity", name, 900) 

    for name, pos in target_positions.items():
        bus.write("Goal_Position", name, int(pos), normalize=False)
    #time.sleep도 중요하니까 지우면 안됨!!
    time.sleep(2)
#########  1번 동작
    target_positions = {
        "motor_1": 1750.00,
        "motor_2": 1578.00,
        "motor_3": 2317.00,
        "motor_4": 2797.00,
        "motor_5": 2086.00,
        "motor_6": 2060.00,
    }

    # 동기식 위치 명령 전송
	#바로 밑 코드의 900 이 부분이 속도 조절부임
    for name in motors:
    	bus.write("Goal_Velocity", name, 900) 

    for name, pos in target_positions.items():
        bus.write("Goal_Position", name, int(pos), normalize=False)
    #time.sleep도 중요하니까 지우면 안됨!! (모터 작동시간 보장)
    time.sleep(2)

#############초기 상태로 복귀

    target_positions = {
        "motor_1": 2047.00,
        "motor_2": 880.00,
        "motor_3": 3113.00,
        "motor_4": 2782.00,
        "motor_5": 2047.00,
        "motor_6": 2050.00, }

    # 동기식 위치 명령 전송
	#바로 밑 코드의 900 이 부분이 속도 조절부임
    for name in motors:
    	bus.write("Goal_Velocity", name, 900) 

    for name, pos in target_positions.items():
        bus.write("Goal_Position", name, int(pos), normalize=False)
    #time.sleep도 중요하니까 지우면 안됨!! (모터 작동시간 보장)
    time.sleep(2)




    for name in motors:
       bus.disable_torque(name)

    bus.disconnect()





















if __name__ == "__main__":
    final()