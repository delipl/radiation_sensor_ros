#  Copyright 2024 Jakub Delicat
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    serial_port = LaunchConfiguration("serial_port", default="/dev/ttyACM0")

    declare_serial_port_cmd = DeclareLaunchArgument(
        "serial_port",
        default_value="/dev/ttyACM0",
        description="Serial port for the radiation sensor",
    )

    radiation_sensor_driver = Node(
        package="radiation_sensor_driver",
        executable="radiation_sensor_driver",
        name="radiation_sensor_driver",
        output="screen",
        parameters=[{"serial_port": serial_port}],
    )

    return LaunchDescription([declare_serial_port_cmd, radiation_sensor_driver])
