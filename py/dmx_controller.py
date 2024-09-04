# dmx_controller.py

import pyudmx

class DMXController:
    def __init__(self):
        """Initializes the DMX controller with a USB-DMX interface."""
        self.usb_dmx = pyudmx.uDMXDevice()
        self.usb_dmx.open()

    def set_dmx_channel(self, channel, value):
        """
        Sets a specific DMX channel to a value.
        
        Parameters:
        - channel: DMX channel number (1-512).
        - value: DMX value (0-255).
        """
        if 1 <= channel <= 512 and 0 <= value <= 255:
            self.usb_dmx.send_single_value(channel - 1, value)  # DMX channels start at 1, array at 0
        else:
            print("Invalid channel or value.")

    def close(self):
        """Closes the DMX connection."""
        self.usb_dmx.close()

# Example usage (if run directly):
if __name__ == "__main__":
    dmx = DMXController()

    # Example: Set Pan (channel 1) to 127 (middle position)
    dmx.set_dmx_channel(1, 127)

    # Example: Set Tilt (channel 2) to 200
    dmx.set_dmx_channel(2, 200)

    # Close DMX connection
    dmx.close()
