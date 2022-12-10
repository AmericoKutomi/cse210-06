from constants import *
from game.scripting.action import Action


class DrawRacketAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):

        def show_racket(racket):
            body = racket.get_body()
            if racket.is_debug():
                rectangle = body.get_rectangle()
                self._video_service.draw_rectangle(rectangle, PURPLE)
         
            image = racket.get_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)

        racket_left = cast.get_first_actor(RACKET_GROUP)
        racket_right = cast.get_second_actor(RACKET_GROUP)

        show_racket(racket_left)
        show_racket(racket_right)
