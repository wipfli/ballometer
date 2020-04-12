import busio
import my_adafruit_lsm303_accel
import adafruit_lsm303dlh_mag
    
i2c = busio.I2C(24, 23)

accel = my_adafruit_lsm303_accel.LSM303_Accel(i2c, address=0x18)
mag = adafruit_lsm303dlh_mag.LSM303DLH_Mag(i2c)

print("Acceleration (m/s^2): X=%0.3f Y=%0.3f Z=%0.3f"%accel.acceleration)
print("Magnetometer (micro-Teslas)): X=%0.3f Y=%0.3f Z=%0.3f"%mag.magnetic)