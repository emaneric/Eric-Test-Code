from smbus2 import SMBus, i2c_msg

with SMBus(1) as bus:
    # Read 1 bytes from address 68
    #msg = i2c_msg.read(68, 1)
    #bus.i2c_rdwr(msg)
    print(read_byte(68rce=None))