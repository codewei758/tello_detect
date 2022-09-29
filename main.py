from subprocess import call
from typing_extensions import Self
import robomaster
from robomaster import robot


class Main():

    def __init__(self):
        # 本机地址
        robomaster.config.LOCAL_IP_STR = "192.168.31.107"
        self.tl_drone = robot.Drone()
        # 无人机组网模式 “sta”
        self.tl_drone.initialize(conn_type="sta")
        self.tl_camera = self.tl_drone.camera
        self.tl_flight = self.tl_drone.flight
        self.tl_flight.set_speed(20).wait_for_completed()

    def sub_tof_info_handler(self, tof_info):
        # 订阅TOF信息并根据TOF调整飞行方向
        tof = tof_info
        if tof > 50:
            self.tl_flight.stop().wait_for_completed()
            self.tl_flight.rotate(angle=90).wait_for_completed()
            

    def sub_drone_info_handler(self, drone_info):
        # 订阅飞行器信息
        high, baro, motor_time = drone_info
        
        if high < 60:
            self.tl_flight.up(30).wait_for_completed()
        

    def begin(self):
        '''
        检测开始函数
        '''
        self.tl_drone.sub_tof(freq=10, callback=self.sub_tof_info_handler)
        self.tl_drone.sub_drone_info(
            freq=5, callback=self.sub_drone_info_handler)
        
        self.tl_flight.takeoff().wait_for_completed()
        
        self.tl_flight.forward(distance=500).wait_for_completed()
        self.tl_flight.rotate(angle=90).wait_for_completed()
        self.tl_flight.forward(distance=500).wait_for_completed()
        self.tl_flight.rotate(angle=90).wait_for_completed()
        self.tl_flight.forward(distance=500).wait_for_completed()
        self.tl_flight.rotate(angle=90).wait_for_completed()
        self.tl_flight.forward(distance=500).wait_for_completed()
        self.tl_flight.rotate(angle=90).wait_for_completed()
        
        self.tl_flight.land()
        
        self.tl_drone.close()
        
        
        


if __name__ == '__main__':
    m = Main()
    m.begin()
   
