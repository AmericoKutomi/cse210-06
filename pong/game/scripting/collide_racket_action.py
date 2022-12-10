from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideRacketAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):

        def ball_collide_with_racket(ball, racket, ball_direction_to):
            racket_body = racket.get_body()
            ball_body = ball.get_body()

            if self._physics_service.has_collided(ball_body, racket_body):
                if self._physics_service.is_on(racket_body, ball_body, ball_direction_to):
                    ball.bounce_y()
                elif self._physics_service.is_under(racket_body, ball_body, ball_direction_to):
                    ball.bounce_y()
                else:
                    percentage_collision_position = self._physics_service.get_position_point(racket_body, ball_body)
                    acceleration_by_collision = self._physics_service.get_acceleration(racket_body, ball_body)
                    stats = cast.get_first_actor(STATS_GROUP)    
                    ball.bounce_direction_intensity(percentage_collision_position, acceleration_by_collision, stats.get_level_velocity())
                    stats.add_points(1)
                
                sound = Sound(BOUNCE_SOUND)
                self._audio_service.play_sound(sound)    

        ball = cast.get_first_actor(BALL_GROUP)
        racket_left = cast.get_first_actor(RACKET_GROUP)
        racket_right = cast.get_second_actor(RACKET_GROUP)

        ball_collide_with_racket(ball, racket_left, 'left')
        ball_collide_with_racket(ball, racket_right, 'right')
        
