#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

class number_counter_node(Node):
    def __init__(self):
        self.count = 0
        super().__init__("number_counter")
        self.subscriber_ = self.create_subscription(Int64, "number", self.callback_number, 10)
        self.get_logger().info("Number Counter has been started")

        self.publishers_ = self.create_publisher(Int64, "number_count", 10)


    def callback_number(self, msg: Int64):
        self.get_logger().info(str(msg.data))
        self.publish_number_count()

    
    def publish_number_count(self):
        self.count = self.count + 1
        
        msg = Int64()
        msg.data = self.count

        self.publishers_.publish(msg)





def main(args=None):
    rclpy.init(args=args)
    node = number_counter_node()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
