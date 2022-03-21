import rclpy
from rclpy.node import Node

import sys
from luma.core import cmdline, error


import cv2
from cv_bridge import CvBridge
from PIL import Image as PilImg


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
        #cv2.imshow("image", current_frame)
        #cv2.waitKey(1)
        #
        #this part is to convert in pillow to be displayed using luma
        current_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2RGB)
        image = PilImg.fromarray(current_frame)
        #image.show()
        #image = image.resize((128,64),PilImg.ANTIALIAS).transform(device.size,PilImg.AFFINE, (1,0,0,0,1,0), PilImg.BILINEAR).convert(device.mode)
        device_size = device.width, device.height
        image = image.resize(device_size, PilImg.ANTIALIAS)
        device.display(image.convert(device.mode))
        

def display_settings(device, args):
    """
    Display a short summary of the settings.
    :rtype: str
    """
    iface = ''
    display_types = cmdline.get_display_types()
    if args.display not in display_types['emulator']:
        iface = 'Interface: {}\n'.format(args.interface)

    lib_name = cmdline.get_library_for_display_type(args.display)
    if lib_name is not None:
        lib_version = cmdline.get_library_version(lib_name)
    else:
        lib_name = lib_version = 'unknown'

    import luma.core
    version = 'luma.{} {} (luma.core {})'.format(
        lib_name, lib_version, luma.core.__version__)

    return 'Version: {}\nDisplay: {}\n{}Dimensions: {} x {}\n{}'.format(
        version, args.display, iface, device.width, device.height, '-' * 60)


def get_device(actual_args=None):
    """
    Create device from command-line arguments and return it.
    """
    if actual_args is None:
        actual_args = sys.argv[1:]
    parser = cmdline.create_parser(description='luma.examples arguments')
    args = parser.parse_args(actual_args)

    if args.config:
        # load config from file
        config = cmdline.load_config(args.config)
        args = parser.parse_args(config + actual_args)

    # create device
    try:
        device = cmdline.create_device(args)
        print(display_settings(device, args))
        return device

    except error.Error as e:
        parser.error(e)
        return None





def main(args=None):
    rclpy.init(args=args)
    
    node = OledNode()
    

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()



device=get_device()

if __name__ == '__main__':
    main()