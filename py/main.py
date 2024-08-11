import serial
import tkinter as tk
from tkinter import simpledialog

# Configure serial communication
COM_PORT = 'COM3'  
BAUDRATE = 9600
ser = serial.Serial(COM_PORT, baudrate=BAUDRATE, timeout=1)

def send_command(command):
    """Sends a command to the connected device via serial."""
    ser.write(f"{command}\n".encode())

def move_forward():
    """Moves the robot forward."""
    distance = simpledialog.askinteger("Input", "Enter distance (cm):")
    if distance is not None:
        send_command(f"MOVE_FORWARD {distance}")

def move_backward():
    """Moves the robot backward."""
    distance = simpledialog.askinteger("Input", "Enter distance (cm):")
    if distance is not None:
        send_command(f"MOVE_BACKWARD {distance}")

def turn_left():
    """Turns the robot left."""
    angle = simpledialog.askinteger("Input", "Enter angle (degrees):")
    if angle is not None:
        send_command(f"TURN_LEFT {angle}")

def turn_right():
    """Turns the robot right."""
    angle = simpledialog.askinteger("Input", "Enter angle (degrees):")
    if angle is not None:
        send_command(f"TURN_RIGHT {angle}")

def stop():
    """Stops the robot's movement immediately."""
    send_command("STOP")

def set_color():
    """Changes the lighting color."""
    color = simpledialog.askstring("Input", "Enter color (hex format #RRGGBB):")
    if color:
        send_command(f"SET_COLOR {color}")

def fade_color():
    """Fades to a new color gradually."""
    color = simpledialog.askstring("Input", "Enter target color (hex format #RRGGBB):")
    duration = simpledialog.askinteger("Input", "Enter duration (ms):")
    if color and duration is not None:
        send_command(f"FADE_COLOR {color} {duration}")

def blink():
    """Makes the light blink."""
    frequency = simpledialog.askinteger("Input", "Enter frequency (Hz):")
    duration = simpledialog.askinteger("Input", "Enter duration (ms):")
    if frequency is not None and duration is not None:
        send_command(f"BLINK {frequency} {duration}")

def set_brightness():
    """Sets the light brightness level."""
    brightness = simpledialog.askinteger("Input", "Enter brightness (0-100):")
    if brightness is not None:
        send_command(f"SET_BRIGHTNESS {brightness}")

def start_sequence():
    """Starts a predefined sequence of movements and lights."""
    sequence_name = simpledialog.askstring("Input", "Enter sequence name:")
    if sequence_name:
        send_command(f"START_SEQUENCE {sequence_name}")

def stop_sequence():
    """Stops the ongoing sequence."""
    send_command("STOP_SEQUENCE")

def sync_movement_light():
    """Synchronizes robot movement with light changes."""
    movement_type = simpledialog.askstring("Input", "Enter movement type:")
    color = simpledialog.askstring("Input", "Enter color (hex format #RRGGBB):")
    if movement_type and color:
        send_command(f"SYNCH_MOVEMENT_LIGHT {movement_type} {color}")

def play_sound():
    """Plays a specific sound."""
    file_path = simpledialog.askstring("Input", "Enter sound file path:")
    if file_path:
        send_command(f"PLAY_SOUND {file_path}")

def set_speed():
    """Adjusts the robot's movement speed."""
    speed = simpledialog.askinteger("Input", "Enter speed (0-100):")
    if speed is not None:
        send_command(f"SET_SPEED {speed}")

def rotate_arm():
    """Rotates a robotic arm to a specific position."""
    angle = simpledialog.askinteger("Input", "Enter angle (degrees):")
    if angle is not None:
        send_command(f"ROTATE_ARM {angle}")

def toggle_light():
    """Turns the light on or off."""
    state = simpledialog.askstring("Input", "Enter state (ON or OFF):")
    if state in ["ON", "OFF"]:
        send_command(f"TOGGLE_LIGHT {state}")

def set_mode():
    """Sets the system's operating mode."""
    mode = simpledialog.askstring("Input", "Enter mode (AUTO, MANUAL, etc.):")
    if mode:
        send_command(f"SET_MODE {mode}")

def calibrate():
    """Calibrates sensors and the robot's initial position."""
    send_command("CALIBRATE")

def setup_gui():
    """Sets up the graphical user interface."""
    root = tk.Tk()
    root.title("Robot and Lighting Control")

    # Buttons for control
    tk.Button(root, text="Move Forward", command=move_forward).pack(pady=10)
    tk.Button(root, text="Move Backward", command=move_backward).pack(pady=10)
    tk.Button(root, text="Turn Left", command=turn_left).pack(pady=10)
    tk.Button(root, text="Turn Right", command=turn_right).pack(pady=10)
    tk.Button(root, text="Stop", command=stop).pack(pady=10)
    tk.Button(root, text="Set Color", command=set_color).pack(pady=10)
    tk.Button(root, text="Fade Color", command=fade_color).pack(pady=10)
    tk.Button(root, text="Blink", command=blink).pack(pady=10)
    tk.Button(root, text="Set Brightness", command=set_brightness).pack(pady=10)
    tk.Button(root, text="Start Sequence", command=start_sequence).pack(pady=10)
    tk.Button(root, text="Stop Sequence", command=stop_sequence).pack(pady=10)
    tk.Button(root, text="Sync Movement with Light", command=sync_movement_light).pack(pady=10)
    tk.Button(root, text="Play Sound", command=play_sound).pack(pady=10)
    tk.Button(root, text="Set Speed", command=set_speed).pack(pady=10)
    tk.Button(root, text="Rotate Arm", command=rotate_arm).pack(pady=10)
    tk.Button(root, text="Toggle Light", command=toggle_light).pack(pady=10)
    tk.Button(root, text="Set Mode", command=set_mode).pack(pady=10)
    tk.Button(root, text="Calibrate", command=calibrate).pack(pady=10)

    # Start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    setup_gui()
