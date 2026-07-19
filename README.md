# Multi-Robot Fleet Management System (ROS2)

## Overview

This project demonstrates a ROS2-based Multi-Robot Fleet Management System designed for warehouse automation. The system coordinates multiple autonomous robots, monitors their operational status, and performs task allocation through ROS2 communication.

This project focuses on scalable fleet management concepts used in modern industrial automation.

## Features

- Multi-robot communication
- Fleet monitoring
- Robot status updates
- Task allocation
- ROS2 topic communication
- Modular architecture
- Warehouse automation simulation

## Technologies Used

- ROS2 Humble
- Python
- Gazebo
- RViz2
- Ubuntu 22.04

## Project Structure

```
multi_robot_ws/
│
├── src/
│   └── fleet_manager/
├── launch/
├── config/
├── screenshots/
├── logs/
└── README.md
```

## How to Run

```bash
cd ~/multi_robot_ws

colcon build

source install/setup.bash

Terminal 1
ros2 run fleet_manager fleet_manager

Terminal 2
ros2 run fleet_manager robot_status

Terminal 3
ros2 run fleet_manager robot2_status
```

## Output

- Robot status monitoring
- Fleet dashboard
- Multi-robot communication
- Task allocation simulation

## Learning Outcomes

- Multi-robot coordination
- ROS2 publisher/subscriber communication
- Fleet management
- Distributed robotic systems
- Warehouse automation

## Future Improvements

- Dynamic task scheduling
- Battery management
- Gazebo multi-robot simulation
- Navigation2 integration
- AI-based route optimization

## Contributors

- Harshvardhan Nayakal
- Sakshi Patil

Developed as a collaborative robotics learning project.
