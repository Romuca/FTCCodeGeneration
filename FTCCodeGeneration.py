from Blocks import *


class FTCCodeGeneration:
    name = "FTCCodeGeneration"
    version = "0.1.6a"
    repo = "https://github.com/Romuca/FTCCodeGeneration"
    data = "Development began on 21st March"
    blocks = [MoveStraight, MoveToPoint, Rotate, ControlServo, ControlCRServo, Sleep, GetDistance, TelemetryAddData,
              Loop]
    units = [Centimeter, Ticks, Degrees, Radians]
