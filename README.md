

# **Robot and Lighting Control Project for Shows**

This project provides a complete solution for synchronized control of robots and lighting systems in shows and events. Using Python as the main programming language, it enables sending commands to robots and lighting systems via serial communication (by cable) from a Windows PC, allowing precise and coordinated execution of movements and light effects.

## **Key Features**

- **Robot Movement Control:** Ability to send commands to move robots in various directions, with adjustable parameters like speed, distance, and rotation angle.

- **Lighting Synchronization:** Full control over lighting systems, including color changes, brightness adjustment, and the creation of effects like blinking and smooth transitions.

- **Automated Sequence Execution:** Create and execute predefined sequences that synchronize robot movements with lighting effects, ideal for complex performances.

- **Support for Multiple Devices:** Manage multiple devices connected via cable to the PC, with automatic COM port detection.

- **Simple Graphical Interface:** A basic graphical interface allows users to control robots and lighting intuitively, with options to send commands and view real-time responses.

## **How It Works**

This system uses serial communication to send commands from the PC to robots and lighting systems. Each command is defined in a simple structure, which can include parameters like speed, color, or duration. The Python code processes these commands and sends them through the COM ports to the connected devices.

### **Command Examples**

- `MOVE_FORWARD 100` - Moves the robot forward by 100 cm.
- `SET_COLOR #FF0000` - Changes the light color to red.
- `BLINK 2 5000` - Makes the light blink at 2 Hz for 5 seconds.

### **Technologies Used**

- **Python:** Main language for developing the control software.
- **pySerial:** Library used for serial communication with the devices.
- **Tkinter:** Used to create a simple graphical interface.
