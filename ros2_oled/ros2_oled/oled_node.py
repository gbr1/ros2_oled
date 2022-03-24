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
        if self.display_type=='pygame':
            from luma.emulator.device import pygame
            self.device=pygame()

        elif self.display_type=='asciiart':
            from luma.emulator.device import asciiart
            self.device=asciiart()

        elif self.display_type=='asciiblock':
            from luma.emulator.device import asciiblock
            self.device=asciiblock()

        elif self.display_type=='gifanim':
            from luma.emulator.device import gifanim
            self.device=gifanim()

        elif self.display_type=='capture':
            from luma.emulator.device import captures
            self.device=capture()

        elif self.display_type=='ssd1306':
            from luma.oled.device import ssd1306
            self.device=ssd1306()

        else:
            self.get_logger().error('wrong display: %s' % self.display_type)

        # init subscriber
        self.subscription = self.create_subscription(Image,'/image/image_raw',self.listener_callback,10)
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
        self.declare_parameter('display.type','ssd1306')
        self.display_type = self.get_parameter('display.type').get_parameter_value().string_value
        self.get_logger().info('paramtro %s' % self.display_type)
        



def main():
    rclpy.init()
    node = OledNode()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()