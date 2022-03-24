from errno import EMULTIHOP
import rclpy
from rclpy.node import Node

import cv2
from cv_bridge import CvBridge
from PIL import Image as PilImg


from sensor_msgs.msg import Image
from sensor_msgs.msg import CameraInfo

from luma.core.interface.serial import i2c


class OledNode(Node):

    def __init__(self):

        self.cv_bridge = CvBridge()
        super().__init__('oled_node')
        self.init_parameters()

        #init device
        if self.emulation and self.display_type=='pygame':
            from luma.emulator.device import pygame
            self.device=pygame()

        elif self.emulation and self.display_type=='asciiart':
            from luma.emulator.device import asciiart
            self.device=asciiart()

        elif self.emulation and self.display_type=='asciiblock':
            from luma.emulator.device import asciiblock
            self.device=asciiblock()

        elif self.emulation and self.display_type=='gifanim':
            from luma.emulator.device import gifanim
            self.device=gifanim()

        elif self.emulation and self.display_type=='capture':
            from luma.emulator.device import capture
            self.device=capture()

        elif self.emulation == False and self.display_type=='ssd1306':
            from luma.oled.device import ssd1306
            serial = i2c(port=self.i2c_port, address=self.i2c_address)
            self.device=ssd1306(serial)

        else:
            self.get_logger().error('wrong display: %s' % self.display_type)

        # init subscriber
        self.subscription = self.create_subscription(Image,'/image_raw',self.listener_callback,10)
        self.subscription 
        



    def listener_callback(self, msg):
        current_frame = self.cv_bridge.imgmsg_to_cv2(msg)

        #this part is to convert in pillow to be displayed using luma
        current_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2RGB)
        image = PilImg.fromarray(current_frame)
        device_size = self.device.width, self.device.height
        image = image.resize(device_size, PilImg.ANTIALIAS)
        self.device.display(image.convert(self.device.mode))

    def init_parameters(self):
        self.declare_parameter('display.emulation',False)
        self.emulation = self.get_parameter('display.emulation').get_parameter_value().bool_value
        
        self.declare_parameter('display.type','ssd1306')
        self.display_type = self.get_parameter('display.type').get_parameter_value().string_value

        if self.emulation==False:
            self.declare_parameter('display.i2c.port',0)
            self.i2c_port = self.get_parameter('display.i2c.port').get_parameter_value().integer_value
            self.declare_parameter('display.i2c.address',0x3C)
            self.i2c_address = self.get_parameter('display.i2c.address').get_parameter_value().integer_value
            
        



def main():
    rclpy.init()
    node = OledNode()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()