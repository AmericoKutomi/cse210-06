from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Racket(Actor):
    """A implement used to hit and bounce the ball in the game."""
    
    def __init__(self, body, image, debug = False):
        """Constructs a new Bat.
        
        Args:Args:
            body: A new instance of Body.
            animation: A new instance of Animation.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._image = image
        self._lives = DEFAULT_LIVES

    def get_image(self):
        """Gets the bat's image.
        
        Returns:
            An instance of Image.
        """
        return self._image

    def get_body(self):
        """Gets the bat's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def move_next(self):
        """Moves the bat using its velocity."""
        position = self._body.get_position()
        velocity = self._body.get_velocity()
        new_position = position.add(velocity)
        self._body.set_position(new_position)

    def swing_left(self):
        """Steers the bat to the left."""
        velocity = Point(-RACKET_VELOCITY, 0)
        self._body.set_velocity(velocity)
        
    def swing_right(self):
        """Steers the bat to the right."""
        velocity = Point(RACKET_VELOCITY, 0)
        self._body.set_velocity(velocity)

    def swing_up(self):
        """Steers the bat to the top."""
        position = self._body.get_position()
        #size = self._body.get_size()
        self.stop_moving()
        if position.get_y() > FIELD_TOP:
            velocity = Point(0, -RACKET_VELOCITY)
            self._body.set_velocity(velocity)
        
    def swing_down(self):
        """Steers the bat to the bottom."""
        position = self._body.get_position()
        size = self._body.get_size()
        self.stop_moving()
        if position.get_y() < (SCREEN_HEIGHT - size.get_y()):
            velocity = Point(0, RACKET_VELOCITY)
            self._body.set_velocity(velocity)

    def stop_moving(self):
        """Stops the bat from moving."""
        velocity = Point(0, 0)
        self._body.set_velocity(velocity)

    def add_life(self):
        """Adds one life."""
        if self._lives < MAXIMUM_LIVES:
            self._lives += 1 

    def get_lives(self):
        """Gets the lives.

        Returns:
            A number representing the lives.
        """
        return self._lives
  
    def lose_life(self):
        """Removes one life."""
        if self._lives > 0:
            self._lives -= 1
        pass
    
    # def reset(self):
        """Resets the stats back to their default values."""
        # self._lives = DEFAULT_LIVES