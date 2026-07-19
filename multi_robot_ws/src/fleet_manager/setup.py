from setuptools import setup

package_name = 'fleet_manager'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name],
        ),
        (
            'share/' + package_name,
            ['package.xml'],
        ),
        (
            'share/' + package_name + '/launch',
            ['launch/multi_robot.launch.py',
             'launch/fleet.launch.py',
             'launch/navigation.launch.py'],
        ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Harshvardhan Nayakal',
    maintainer_email='your_email@example.com',
    description='Multi Robot Fleet Management System using ROS2',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
    'console_scripts': [
        'fleet_manager = fleet_manager.fleet_manager:main',
        'robot_status = fleet_manager.robot_status:main',
        'robot2_status = fleet_manager.robot2_status:main',
    ],
},
)
