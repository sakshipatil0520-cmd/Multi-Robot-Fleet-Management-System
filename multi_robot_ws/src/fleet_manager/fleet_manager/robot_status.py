#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class RobotStatus(Node):

    def __init__(self):

        super().__init__('robot_status')

        self.publisher = self.create_publisher(
            String,
            '/fleet_status',
            10
        )

        self.robot_name = "Robot1"

        self.timer = self.create_timer(
            2.0,
            self.publish_status
        )

        self.get_logger().info(f"{self.robot_name} Started")

    def publish_status(self):

        msg = String()

        msg.data = f"{self.robot_name},IDLE,100"

        self.publisher.publish(msg)

        self.get_logger().info(
            f"Published : {msg.data}"
        )


def main(args=None):

    rclpy.init(args=args)

    node = RobotStatus()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        pass

    finally:
        node.destroy_node()

        if rclpy.ok():
            rclpy.shutdown()


if __name__ == "__main__":
    main()
