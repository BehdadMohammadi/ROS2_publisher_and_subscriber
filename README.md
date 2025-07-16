# ROS 2 Number Publisher and Counter Package

This ROS 2 package contains two Python nodes built with `rclpy`. Together, they demonstrate basic publishing and subscribing using standard message types from `example_interfaces`.

## Nodes

### 1. `number_publisher`

- **File:** `number_publisher.py`
- **Description:**  
  This node publishes a random integer between 1 and 100 every 0.5 seconds on the `/number` topic.
- **Published Topic:**
  - `/number` (`example_interfaces/msg/Int64`)

#### Behavior:
Upon starting, the node logs that it has been launched, and continuously publishes random integers to the topic `/number`.

---

### 2. `number_counter`

- **File:** `number_counter.py`
- **Description:**  
  This node subscribes to the `/number` topic and counts how many messages it has received. It publishes the current count to a new topic called `/number_count`.
- **Subscribed Topic:**
  - `/number` (`example_interfaces/msg/Int64`)
- **Published Topic:**
  - `/number_count` (`example_interfaces/msg/Int64`)

#### Behavior:
Every time a message is received on `/number`, the node logs the number, increments an internal counter, and publishes the updated count to `/number_count`.

---

## How to Run

Make sure you have a ROS 2 workspace set up. To run these nodes:

```bash
# Source ROS 2 and your workspace
source /opt/ros/<ros_distro>/setup.bash
source install/setup.bash

# Run number_publisher
ros2 run <your_package_name> number_publisher

# In another terminal, run number_counter
ros2 run <your_package_name> number_counter
