
"""
Shows how to receive messages via polling.
"""

import can
from can.bus import BusState


def dump_all():
    """Receives all messages and prints them to the console until Ctrl+C is pressed."""

    # this uses the default configuration (for example from environment variables, or a
    # config file) see https://python-can.readthedocs.io/en/stable/configuration.html
    with can.Bus(interface='slcan', channel='COM5', bitrate=250000) as bus:
        # set to read-only, only supported on some interfaces
        try:
            bus.state = BusState.PASSIVE
        except NotImplementedError:
            pass

        try:
            while True:
                msg = bus.recv(1)
                if msg is not None and len(msg.data) >= 2:
                    if msg.data[0] == 0x55 and msg.data[1] == 0x55:
                        print(msg)

        except KeyboardInterrupt:
            pass  # exit normally

def dump_delta():
    """Receives all messages and prints the difference from the last to the console until Ctrl+C is pressed."""

    # this uses the default configuration (for example from environment variables, or a
    # config file) see https://python-can.readthedocs.io/en/stable/configuration.html
    with can.Bus(interface='slcan', channel='COM5', bitrate=250000) as bus:
        # set to read-only, only supported on some interfaces
        try:
            bus.state = BusState.PASSIVE
        except NotImplementedError:
            pass

        try:
            last_msg = bytearray([0x55, 0x55, 0x3c, 0x00, 0x00, 0x00, 0xf2, 0xff])
            while True:
                msg = bus.recv(1)
                if msg is not None and len(msg.data) == 8:
                    if msg.data[0] == 0x55 and msg.data[1] == 0x55:
                        output_msg = []
                        for i in range(2, 4):
                            output_msg.append(msg.data[i] - last_msg[i])
                        last_msg = msg.data
                        print(output_msg)

        except KeyboardInterrupt:
            pass  # exit normally

def dump_just_angle():
    """Receives all messages and prints the angle portion of each message to the console until Ctrl+C is pressed."""

    # this uses the default configuration (for example from environment variables, or a
    # config file) see https://python-can.readthedocs.io/en/stable/configuration.html
    with can.Bus(interface='slcan', channel='COM5', bitrate=250000) as bus:
        # set to read-only, only supported on some interfaces
        try:
            bus.state = BusState.PASSIVE
        except NotImplementedError:
            pass

        try:
            last_msg = bytearray([0x55, 0x55, 0x3c, 0x00, 0x00, 0x00, 0xf2, 0xff])
            while True:
                msg = bus.recv(1)
                if msg is not None and len(msg.data) == 8:
                    if msg.data[0] == 0x55 and msg.data[1] == 0x55:
                        # From translated manual:
                        # Take the encoder reply "55 55 aa bb cc dd ee ff" data as an example to calculate
                        # Angle calculation method: Angle register value = (0xbb << 8) | 0xaa
                        #                           Angle (°) = Angle register value * 360 / 32768
                        angle_register = msg.data[3] << 8 | msg.data[2]
                        angle = angle_register * 360 / 32768
                        print(f"{angle_register} = {angle}°")

        except KeyboardInterrupt:
            pass  # exit normally


if __name__ == "__main__":
    dump_just_angle()