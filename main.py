import robomaster
from robomaster import robot

def sub_tof_info_handler(tof_info):
    tof = tof_info
    print("drone tof: {0}".format(tof))

def sub_drone_info_handler(drone_info):
    high, baro, motor_time = drone_info
    print("drone info: high:{0}, baro:{1}, motor_time:{2}".format(high, baro, motor_time))
    
if __name__ == '__main__':
    # 本机地址
    robomaster.config.LOCAL_IP_STR = "192.168.31.107"
    tl_drone = robot.Drone()
    # 无人机组网模式 “sta”
    tl_drone.initialize(conn_type="sta")
    
    
    tl_camera = tl_drone.camera
    # 订阅TOF和飞行器信息
    tl_drone.sub_tof(freq=10, callback=sub_tof_info_handler)
    tl_drone.sub_drone_info(freq=1,callback=sub_drone_info_handler)
    
    
    