# gui_control.py
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

# Implement your GUI functions like move_forward, move_backward, etc. here...

def setup_gui():
    """Sets up the graphical user interface."""
    root = tk.Tk()
    root.title("Robot and Lighting Control")

    # Buttons for control
    tk.Button(root, text="Move Forward", command=move_forward).pack(pady=10)
    # Repeat for other buttons...

    # Start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    setup_gui()
