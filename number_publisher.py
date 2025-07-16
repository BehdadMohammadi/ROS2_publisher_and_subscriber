#!/usr/bin/env python3
import rclpy
import random
from rclpy.node import Node
from example_interfaces.msg import Int64

class number_publisher_node(Node):
    def __init__(self):
        super().__init__("number_publisher")
        self.publishers_ = self.create_publisher(Int64, "number", 10)
        self.timers_ = self.create_timer(0.5, self.publish_number)
        self.get_logger().info("Number Publisher has been started.")
    
    
    def publish_number(self):
        msg = Int64()
        msg.data = random.randint(1, 100)
        self.publishers_.publish(msg)
        


def main(args=None):
    rclpy.init(args=args)
    node = number_publisher_node()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
