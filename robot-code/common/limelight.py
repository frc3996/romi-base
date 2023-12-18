
import ntcore
import math

class Limelight:
    def __init__(self, limelight_name="limelight"):
        self.nt = ntcore.NetworkTableInstance.getDefault().getTable(limelight_name)
        self.zero = 0

    def set_zero(self, zero):
        self.zero = zero

    def get_target_valid(self):
        return self.nt.getNumber('tv', 0) == 1

    def get_ta(self):
        return self.nt.getNumber('ta', 0)

    def get_target_x_offset(self, for_april_tag):
        ta = self.get_ta()
        if ta == 0:
            return 0
        if for_april_tag is True:
            distance = math.sqrt(2.665) * 34 / math.sqrt(ta)  
        else: 
            distance = math.sqrt(0.49) * 28 / math.sqrt(ta)  
            
        real_offset = math.atan(self.zero / distance)
        print(ta, distance, real_offset, self.zero, self.nt.getNumber('tx', 0) - real_offset)
        return (self.nt.getNumber('tx', 0) - real_offset)

    def set_reflective_mode(self):
        return self.nt.putNumber('pipeline', 0)

    def set_april_tag_mode(self):
        return self.nt.putNumber('pipeline', 1)

    def set_cone_mode(self):
        return self.nt.putNumber('pipeline', 2)

    def light_on(self):
        self.nt.putNumber('ledMode', 0)

    def light_off(self):
        self.nt.putNumber('ledMode', 1)

    def targetReady(self, for_april_tag, acceptable_offset=2):
        if self.get_target_valid() is False:
            return False
        
        if abs(self.get_target_x_offset(for_april_tag)) < acceptable_offset:
            return True
        return False
