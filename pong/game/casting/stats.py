from constants import *
from game.casting.actor import Actor


class Stats(Actor):
    """The game stats."""

    def __init__(self, debug = False):
        """Constructs a new Stats."""
        super().__init__(debug)
        self._level = 0
        self._score = 0
        self._minimun_velocity = 0.7

    def add_points(self, points):
        """Adds the given points to the score.
        
        Args:
            points: A number representing the points to add.
        """
        self._score += points

    def get_level(self):
        """Gets the level.

        Returns:
            A number representing the level.
        """
        return self._level

    def get_score(self):
        """Gets the score.

        Returns:
            A number representing the score.
        """
        return self._score

    def next_level(self):
        """Adds one level."""
        self._level += 1
        self._score = 0
        self._minimun_velocity = 0.7 + self._level * 0.2

    def reset(self):
        """Resets the stats back to their default values."""
        self._level = 0
        self._score = 0
        self._minimun_velocity = 0.7

    def get_level_velocity(self):
        """Gets the minimun level velocity

        Returns:
            A number representing the velocity.
        """
        return self._minimun_velocity

    def reset_score(self):
        """Resets the score to 0."""
        self._score = 0
