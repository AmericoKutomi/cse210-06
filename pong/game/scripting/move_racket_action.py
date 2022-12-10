from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class MoveRacketAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):

        def move_racket(racket):

            body = racket.get_body()
            velocity = body.get_velocity()
            position = body.get_position()
            x = position.get_x()
            
            position = position.add(velocity)

            if x < 0:
                position = Point(0, position.get_y())
            elif x > (SCREEN_WIDTH - RACKET_WIDTH):
                position = Point(SCREEN_WIDTH - RACKET_WIDTH, position.get_y())
                
            body.set_position(position)

        racket_left = cast.get_first_actor(RACKET_GROUP)
        racket_right = cast.get_second_actor(RACKET_GROUP)

        move_racket(racket_left)
        move_racket(racket_right)
