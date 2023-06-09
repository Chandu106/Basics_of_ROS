#!/usr/bin/env python3

#creating a node using classes (oop)
import rclpy #callback functionality
from rclpy.node import Node

class MyNode(Node):

    def __init__(self):
        super().__init__("py_test")
        self.get_logger().info("Hello ROOT")

def main(args = None):
    rclpy.init(args=args) #initializing ros2 communications
    node = MyNode()
    rclpy.spin(node)#in simple terms it is like a loop where the node gets spinned when we provide this functionality
    rclpy.shutdown() #lastline of the program to stop the communicatioon

if __name__ == "__main__":
    main()