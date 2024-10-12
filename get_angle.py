"""
This example attempt to retrieve the current angle from the encoder
"""

COM_PORT='COM5'

import can

def send_read_request():
    with can.Bus(interface='slcan', channel=COM_PORT, bitrate=250000) as bus:
        msg = can.Message(arbitration_id=0x50,
                          data=[0x55, 0x55, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff],
                          is_extended_id=False)

        try:
            bus.send(msg)
            print(f"Message sent on {bus.channel_info}")
        except can.CanError:
            print("Error sending CAN message")

if __name__ == "__main__":
    send_read_request()
