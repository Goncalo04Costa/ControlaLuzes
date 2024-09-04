# main.py
from robot import Robot, connect_all_robots, disconnect_all_robots, send_command_to_all

# Create instances for each robot with their respective COM ports
robot1 = Robot(name="Robot1", com_port="COM3")
robot2 = Robot(name="Robot2", com_port="COM4")
robot3 = Robot(name="Robot3", com_port="COM5")

# Create a list of robots
robots = [robot1, robot2, robot3]

# Connect to all robots
connect_all_robots(robots)

# Send a command to all robots
send_command_to_all(robots, "MOVE_FORWARD 100")

# Disconnect from all robots
disconnect_all_robots(robots)
