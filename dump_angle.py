
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


if __name__ == "__main__":
    dump_all()