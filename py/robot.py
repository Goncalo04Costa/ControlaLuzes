# robot.py
import serial

class Robot:
    def __init__(self, name, com_port, baudrate=9600):
        """Initializes a robot with its name, COM port, and baud rate."""
        self.name = name
        self.com_port = com_port
        self.baudrate = baudrate
        self.serial_connection = None
    
    def connect(self):
        """Establishes a serial connection to the robot."""
        try:
            self.serial_connection = serial.Serial(self.com_port, baudrate=self.baudrate, timeout=1)
            print(f"Connected to {self.name} on {self.com_port}")
        except serial.SerialException as e:
            print(f"Error connecting to {self.name}: {e}")

    def disconnect(self):
        """Closes the serial connection."""
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()
            print(f"Disconnected from {self.name}")

    def send_command(self, command):
        """Sends a command to the robot via serial."""
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.write(f"{command}\n".encode())
            print(f"Sent command to {self.name}: {command}")
        else:
            print(f"Connection to {self.name} is not open.")

# Functions to manage multiple robots
def connect_all_robots(robots):
    """Connects all robots in the list."""
    for robot in robots:
        robot.connect()

def disconnect_all_robots(robots):
    """Disconnects all robots in the list."""
    for robot in robots:
        robot.disconnect()

def send_command_to_all(robots, command):
    """Sends a command to all robots in the list."""
    for robot in robots:
        robot.send_command(command)
