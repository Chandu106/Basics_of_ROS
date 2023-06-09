#!/usr/bin/env python3

import rclpy #callback functionality
from rclpy.node import Node

def main(args = None):
    rclpy.init(args=args) #initializing ros2 communications
    node = Node("py_test") #creating the node with name py_test
    node.get_logger().info("Hello ROOT") #for displaying/showing the information
    rclpy.spin(node)#in simple terms it is like a loop where the node gets spinned when we provide this functionality
    rclpy.shutdown() #lastline of the program to stop the communicatioon

if __name__ == "__main__":
    main()