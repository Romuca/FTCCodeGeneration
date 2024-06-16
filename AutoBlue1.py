from Blocks import *


class AutoBlue1:  # example class
    name = "AutoBlue1"
    data = "16.06.24_12:26"
    ticks_per_rotation = 560
    blocks = [
        Loop(  # move in a square
            Countable(4),
            [
                MoveStraight(Centimeter, 60, 0.7),
                Rotate(Degrees, 90, 0.2),
                Sleep(0.5)
            ]  # returns to start point
        ),
        If(  # simple condition, outputs the position during randomization
            class_type=Condition(GetDistance("distance_left", Centimeter), Less, 20),
            actions=[
                TelemetryAddData("Left:", GetDistance("distance_left", Centimeter))
            ],
            else_actions=[
                If(
                    class_type=Condition(GetDistance("distance_right", Centimeter), Less, 20),
                    actions=[
                        TelemetryAddData("Right:", GetDistance("distance_right", Centimeter))
                    ],
                    else_actions=[
                        TelemetryAddData("Position:", "Center")
                    ]
                )
            ]
        )
    ]
