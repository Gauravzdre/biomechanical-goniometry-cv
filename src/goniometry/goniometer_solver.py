import math
from typing import Tuple

class GoniometerSolver:
    """
    Computes joint angles and angular velocities by projecting
    3D landmarks onto anatomical reference planes (sagittal, coronal).
    """
    @staticmethod
    def calculate_3pt_angle(p1: Tuple[float, float], p2: Tuple[float, float], p3: Tuple[float, float]) -> float:
        v1 = (p1[0] - p2[0], p1[1] - p2[1])
        v2 = (p3[0] - p2[0], p3[1] - p2[1])

        dot = v1[0] * v2[0] + v1[1] * v2[1]
        mag1 = math.hypot(v1[0], v1[1])
        mag2 = math.hypot(v2[0], v2[1])

        if mag1 * mag2 == 0:
            return 0.0

        cos_angle = max(-1.0, min(1.0, dot / (mag1 * mag2)))
        return math.degrees(math.acos(cos_angle))
