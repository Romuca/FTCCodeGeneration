# bruh
class Device:
    port = 0
    device = ""
    name = ""

    def __init__(self, port, dev, name):
        self.port = port


class DeviceList:
    devices = [Device, Device, Device, Device]

    def __init__(self, port0, port1, port2, port3):
        self.devices[0] = port0
        self.devices[1] = port1
        self.devices[2] = port2
        self.devices[3] = port3
