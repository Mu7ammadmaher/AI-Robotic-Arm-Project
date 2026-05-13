import math

class ArmKinematics:
    """
    Handles the mathematical calculations for the 4-DOF robotic arm.
    Translates (X, Y, Z) coordinates into joint angles.
    """
    def __init__(self, link1_len, link2_len):
        self.L1 = link1_len
        self.L2 = link2_len

    def calculate_angles(self, target_x, target_y):
        # Calculate distance to target
        dist = math.sqrt(target_x**2 + target_y**2)
        
        # Check if target is within reach to prevent crashes
        if dist > (self.L1 + self.L2):
            return None, "Target out of reach"

        # Inverse Kinematics logic using Law of Cosines
        cos_angle2 = (target_x**2 + target_y**2 - self.L1**2 - self.L2**2) / (2 * self.L1 * self.L2)
        angle2 = math.acos(cos_angle2)
        
        angle1 = math.atan2(target_y, target_x) - math.atan2(
            (self.L2 * math.sin(angle2)), (self.L1 + self.L2 * math.cos(angle2))
        )

        return [math.degrees(angle1), math.degrees(angle2)], "Success"