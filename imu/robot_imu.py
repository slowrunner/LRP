from ros_safe_inertial_measurement_unit import SafeIMUSensor

from vpython import vector
import time

VERBOSITY = True


class RobotImu:
    """Define a common interface to an inertial measurement unit with temperature"""
    def __init__(self):
        self._imu = SafeIMUSensor(port="AD1", use_mutex=True, init=False, verbose=VERBOSITY)
        time.sleep(1.0)

    def read_temperature(self):
        """Read a temperature in degrees C."""
        return self._imu.safe_read_temperature()

    def read_gyroscope(self):
        """Return prescaled gyro data"""
        # _, _, _, x, y, z = self._imu.read_accelerometer_gyro_data()
        x, y, z = self._imu.safe_read_gyroscope()
        return vector(x, y, z)

    def read_accelerometer(self):
        """Return accelerometer data"""
        # accel_x, accel_y, accel_z, _, _, _ = self._imu.read_accelerometer_gyro_data()
        accel_x, accel_y, accel_z = self._imu.safe_read_accelerometer()
        return vector(accel_x, accel_y, accel_z)

    def read_magnetometer(self):
        """Return magnetometer data"""
        mag_x, mag_y, mag_z = self._imu.safe_read_magnetometer()
        return vector(mag_x, -mag_y, -mag_z)

