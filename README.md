# radiation_sensor_ros
ROS 2 driver for BG51 Radiation Sensor


## How to Build a ROS 2 Workspace Using `colcon`

Follow the steps below to build a ROS 2 workspace containing the `radiation_msgs` and `radiation_sensor_driver` packages:

### Prerequisites
- Ensure you have ROS 2 installed (e.g., Humble, Galactic, etc.).
- Make sure `colcon` is installed:
  ```bash
  sudo apt install python3-colcon-common-extensions
  ```

### Steps

1. Create the Workspace Create a directory for your workspace:

    ```bash
        mkdir -p ~/ros2_ws/src
        cd ~/ros2_ws/src
    ```

2. Clone the repository:

    ```bash
        git clone https://github.com/delipl/radiation_sensor_ros src/
    ```

3. Install Dependencies Use `rosdep` to install dependencies:

    ```bash
        rosdep install --from-paths src --ignore-src -r -y
    ```

4. Build the Workspace Build the workspace using `colcon`:

    ```bash
        colcon build
    ```

## How to Run a ROS 2 package

### Steps

1. Source the workspace:

    ```bash
        cd ~/ros2_ws/src
        source install/setup.bash
    ```

2. Run single sensor:

    ```bash
    ros2 launch radiation_sensor_driver radiation_sensor_driver.launch.py
    ```

3. In the other terminal you can see the measurements

    ```bash
        cd ~/ros2_ws/src
        source install/setup.bash
        ros2 topic echo /radiation
    ```
