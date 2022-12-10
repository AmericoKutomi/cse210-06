from constants import *
from game.scripting.action import Action


class CheckOverAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        stats = cast.get_first_actor(STATS_GROUP)
        points = stats.get_score()        
        if points > LEVEL_POINTS:
            stats.next_level()
            callback.on_next(NEXT_LEVEL)