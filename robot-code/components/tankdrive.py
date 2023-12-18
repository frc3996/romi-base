
import romi

def square_input(input):
    if input == 0:
        return 0
    return (input**2) * (input / abs(input))

class TankDrive:
    tank_drive_left_motor: romi.RomiMotor
    tank_drive_right_motor: romi.RomiMotor

    def setup(self):
        self.left_command = 0
        self.right_command = 0

    def drive(self, left, right):
        self.left_command = square_input(left)
        self.right_command = square_input(right)

    def execute(self):
        self.left_motor.set(self.left_command)
        self.right_motor.set(self.right_command)
        self.left_command = 0
        self.right_command = 0
