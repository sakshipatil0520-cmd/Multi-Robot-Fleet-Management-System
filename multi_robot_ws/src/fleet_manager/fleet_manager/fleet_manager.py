#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from fleet_manager.tasks import TASK_QUEUE


class FleetManager(Node):

    def __init__(self):

        super().__init__('fleet_manager')

        self.subscription = self.create_subscription(
            String,
            '/fleet_status',
            self.status_callback,
            10
        )

        self.robot_status = {}

        self.task_queue = TASK_QUEUE.copy()

        self.get_logger().info("Fleet Manager Started")

    def status_callback(self, msg):

        data = msg.data.split(",")

        robot = data[0]
        status = data[1]
        battery = data[2]

        self.robot_status[robot] = {
            "status": status,
            "battery": battery
        }

        self.display_status()

        self.assign_task()

    def display_status(self):

    print("\n==============================")
    print(" Fleet Status Dashboard")
    print("==============================")

    for robot in self.robot_status:

        print(f"Robot   : {robot}")
        print(f"Status  : {self.robot_status[robot]['status']}")
        print(f"Battery : {self.robot_status[robot]['battery']}%")

        if "task" in self.robot_status[robot]:
            print(f"Task    : {self.robot_status[robot]['task']}")

        print("------------------------------")
            
            

    def assign_task(self):

    if not self.task_queue:
        return

    for robot in self.robot_status:

        if self.robot_status[robot]["status"] == "IDLE":

            # Skip if this robot already has a task
            if "task" in self.robot_status[robot]:
                continue

            task = self.task_queue.pop(0)

            self.robot_status[robot]["task"] = task
            self.robot_status[robot]["status"] = "BUSY"

            print("\n====================================")
            print("Task Assigned")
            print("------------------------------------")
            print(f"Robot : {robot}")
            print(f"Task  : {task}")
            print("====================================")

            break

def main(args=None):

    rclpy.init(args=args)

    node = FleetManager()

    try:

        rclpy.spin(node)

    except KeyboardInterrupt:

        node.get_logger().info("Fleet Manager Stopped")

    finally:

        node.destroy_node()

        if rclpy.ok():
            rclpy.shutdown()


if __name__ == "__main__":
    main()
