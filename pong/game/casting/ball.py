import random
from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Ball(Actor):
    """A solid, spherical object that is bounced around in the game."""
    
    def __init__(self, body, image, debug = False):
        """Constructs a new Ball.

        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._image = image

    def bounce_direction_intensity(self, percentage_collision_position, acceleration, minimun_velocity):
        """Bounces the ball in the x direction."""
        velocity = self._body.get_velocity()
        # inverts x direction and apply the acceleration: range 0.7 to 1.1
        vx = velocity.get_x() * (0.4 * acceleration + 0.7) * -1
        if abs(vx) < minimun_velocity:
            if vx < 0:
                vx = minimun_velocity * -1
            else:
                vx = minimun_velocity
        vy = 2 * percentage_collision_position - 1
        if abs(vy) < minimun_velocity:
            if vy < 0:
                vy = minimun_velocity * -1
            else:
                vy = minimun_velocity
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)

    def bounce_x(self):
        """Bounces the ball in the x direction."""
        velocity = self._body.get_velocity()
        # the x direction is inverted
        vx = velocity.get_x() * -1
        vy = velocity.get_y()
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)

    def bounce_y(self):
        """Bounces the ball in the y direction."""
        velocity = self._body.get_velocity()
        vx = velocity.get_x()
        # the y direction is inverted
        vy = velocity.get_y() * -1 
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)

    def get_body(self):
        """Gets the ball's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def get_image(self):
        """Gets the ball's image.
        
        Returns:
            An instance of Image.
        """
        return self._image
        
    def release(self):
        """Release the ball in a random direction."""
        rn = random.uniform(0.9, 1.1)

        rn = 0.9
        vx = random.choice([-BALL_VELOCITY * rn, BALL_VELOCITY * rn])
        vy = -BALL_VELOCITY
        # vy = -0.9
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)