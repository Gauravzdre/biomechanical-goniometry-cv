class RepCounterFsm:
    """
    Finite state machine tracking exercise range-of-motion repetitions.
    """
    def __init__(self, flexion_threshold = 85.0, extension_threshold = 160.0):
        self.flex_th = flexion_threshold
        self.ext_th = extension_threshold
        self.state = "EXTENDED"
        self.rep_count = 0

    def update(self, angle: float) -> int:
        if self.state == "EXTENDED" and angle <= self.flex_th:
            self.state = "FLEXED"
        elif self.state == "FLEXED" and angle >= self.ext_th:
            self.state = "EXTENDED"
            self.rep_count += 1
        return self.rep_count
