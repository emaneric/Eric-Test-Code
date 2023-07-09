from smbus2 import SMBus

with SMBus(1) as bus:
    b = bus.read_byte_data(04h, 0)
    print(b)