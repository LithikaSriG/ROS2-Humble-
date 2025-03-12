import rclpy
from rclpy.node import Node
from std_msgs.msg import String
class PublisherNode(Node):
    def __init__(self):
         super().__init__('Publisher')
         self.publisher_=self.create_publisher(String,'topic',10)
         self.timer = self.create_timer(0.5,self.publisher_msg)
         self.i= 'lithika sri'
    def publisher_msg(self):
         msg = String()
         msg.data = self.i 
         
         self.publisher_.publish(msg)
def main():
   rclpy.init(args=None)
   node = PublisherNode()
   rclpy.spin(node)
if __name__ == '__main__':
   main()
