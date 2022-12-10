from constants import *
from game.scripting.action import Action


class ControlRacketAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        racket_left = cast.get_first_actor(RACKET_GROUP)
        racket_right = cast.get_second_actor(RACKET_GROUP)

        racket_left_in_movement = False
        racket_right_in_movement = False

        if self._keyboard_service.is_key_down('w'): 
            racket_left_in_movement = True
            racket_left.swing_up()
        elif self._keyboard_service.is_key_down('s'): 
            racket_left_in_movement = True
            racket_left.swing_down()  

        if not racket_left_in_movement: 
            racket_left.stop_moving()        

        if self._keyboard_service.is_key_down('i'): 
            racket_right_in_movement = True
            racket_right.swing_up()
        elif self._keyboard_service.is_key_down('k'): 
            racket_right_in_movement = True
            racket_right.swing_down()  

        if not racket_right_in_movement: 
            racket_right.stop_moving()        


