from constants import *
from game.scripting.action import Action


class DrawHudAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        stats = cast.get_first_actor(STATS_GROUP)
        racket_left = cast.get_first_actor(RACKET_GROUP)
        racket_right = cast.get_second_actor(RACKET_GROUP)

        self._draw_label(cast, LEVEL_GROUP, LEVEL_FORMAT, stats.get_level())
        self._draw_label(cast, LIVES_GROUP, LIVES_FORMAT, racket_left.get_lives(), True)
        self._draw_label(cast, LIVES_GROUP, LIVES_FORMAT, racket_right.get_lives(), False)
        self._draw_label(cast, SCORE_GROUP, SCORE_FORMAT, stats.get_score())

    def _draw_label(self, cast, group, format_str, data, first = True):
        the_value_to_display = format_str.format(data)
        if first:
            label = cast.get_first_actor(group)
        else:
            label = cast.get_second_actor(group)

        text = label.get_text()
        text.set_value(the_value_to_display)
        position = label.get_position()
        self._video_service.draw_text(text, position)