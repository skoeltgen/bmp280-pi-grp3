import time
import board
import adafruit_bmp280

i2c = board.I2C()  # uses board.SCL and board.SDA
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)

# Set sea-level pressure for altitude calculation (hPa)
bmp280.sea_level_pressure = 1013.25

while True:
    print(f"Temperature: {bmp280.temperature:.1f} °C")
    print(f"Pressure: {bmp280.pressure:.1f} hPa")
    print(f"Altitude: {bmp280.altitude:.2f} m")
    print("---")
    time.sleep(2)

#Using pip3 install adafruit-circuitpython-bmp280
