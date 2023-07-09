from smbus2 import SMBus
import time

# Open i2c bus 1 and read one byte from address 80, offset 0
bus = SMBus(1)

while (True):
    b = bus.read_byte_data(0x68, 0)
    print(b)
    time.sleep(1);

bus.close()