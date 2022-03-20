import rclpy
from rclpy.node import Node

import cv2
from cv_bridge import CvBridge


from sensor_msgs.msg import Image
from sensor_msgs.msg import CameraInfo


class OledNode(Node):

    def __init__(self):
        super().__init__('oled_node')
        self.subscription = self.create_subscription(Image,'/image/image_raw',self.listener_callback,10)
        self.subscription 
        self.cv_bridge = CvBridge()



    def listener_callback(self, msg):
        #msg.width
        #msg.height
        current_frame = self.cv_bridge.imgmsg_to_cv2(msg)
        cv2.imshow("image", current_frame)
        cv2.waitKey(1)



def main(args=None):
    rclpy.init(args=args)

    node = OledNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()