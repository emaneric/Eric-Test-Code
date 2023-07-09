from smbus2 import SMBus, i2c_msg

with SMBus(1) as bus:
    # Read 1 bytes from address 68
    b = bus.read_byte_data(68, 0)
    print(b)