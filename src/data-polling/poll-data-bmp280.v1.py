import time
from bmp280 import BMP280

# Create sensor object (defaults to I2C bus 1, address 0x76 or 0x77)
bmp = BMP280(i2c_dev=1)

while True:
    temperature = bmp.get_temperature()
    pressure = bmp.get_pressure()
    altitude = bmp.get_altitude()

    print(f"Temp: {temperature:.2f} °C")
    print(f"Pressure: {pressure:.2f} hPa")
    print(f"Altitude: {altitude:.2f} m")
    print("---")

    time.sleep(2)  # poll every 2 seconds


#using pip install bmp280 
