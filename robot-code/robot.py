#!/usr/bin/env python3
#######################################
# Romi Base
# Par Martin Rioux, Team 3996
#######################################

import sys
import os
if sys.platform == "linux":
    import pwd
    os.getlogin = lambda: pwd.getpwuid(os.getuid())[0]

import wpilib
import ntcore  # Outils pour les NetworkTables
from magicbot import MagicRobot
# from robotpy_ext.autonomous.selector import AutonomousModeSelector
from common import gamepad_helper as gh
from components import tankdrive
import romi



class MyRobot(MagicRobot):
    """
    Create components
    """

    tank_drive: tankdrive.TankDrive

    def createObjects(self):
        """
        Création des composantes, les nom du type 'shooter_' seront injectés
        """

        # Moteurs
        self.tank_drive_left_motor = romi.RomiMotor(0)
        self.tank_drive_right_motor = romi.RomiMotor(1)

        # General
        self.gamepad1 = wpilib.Joystick(0)
        self.gyro = romi.RomiGyro()

        # NetworkTable
        self.nt = ntcore.NetworkTableInstance.getDefault().getTable("robotpy")
        self.nt.putNumber("test/romi", 1)

        # Variables

    def disabledPeriodic(self):
        self.update_sd()

    def autonomousInit(self):
        pass

    def autonomous(self):
        # For auto, use MagicBot's auto mode.
        # This will load the ./autonomous folder.
        super().autonomous()

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        self.update_sd()

        left = self.gamepad1.getRawAxis(gh.AXIS_LEFT_Y)
        right = self.gamepad1.getRawAxis(gh.AXIS_RIGHT_Y)

        self.tank_drive.drive(-left, right)

    def update_sd(self):
        """
        Puts data to the smartdashboard.
        """
        self.nt.putNumber('romi/gyro/angle', self.gyro.getAngle())
        self.nt.putNumber('romi/gyro/angle_x', self.gyro.getAngleX())
        self.nt.putNumber('romi/gyro/angle_y', self.gyro.getAngleY())
        self.nt.putNumber('romi/gyro/angle_z', self.gyro.getAngleZ())


if __name__ == "__main__":
    import os
    os.environ["HALSIMWS_HOST"] = "10.0.0.2"
    wpilib.run(MyRobot)
