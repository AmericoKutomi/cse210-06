# cse210-06
CSE210 Week 6 Assignment - Final Project - Pong

The Pong game is used to exemplify the main principles of programming with classes and maintainability. The game Pong was developed from the game Batter. The Batter game has one horizontal racket used to hit the ball against bricks. The Pong game has two vertical rackets that hit a ball against the other player's field. 

Each player has 3 lives. The player loses a life when he lets the ball pass. The player wins the game when his opponent loses all lives.
The game starts with level 0. The level is changed every time the score turns to 20. One point is added to the score each time one player hits the ball.
The racket has the ability to change the ball direction. When the ball hits the bottom of the racket, the ball is directed downwards. The further down, the greater the angle of rebound. The same reasoning applies when the ball hits the top.
The greater the contact area between the ball and the racket, the greater the intensity of the return of the ball.

The main changes from Batter to Pong are listed more below.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- pong                (source code for game)
  +-- assets            (resources used by the game: images, sounds, etc.)
  +-- game              (specific game classes)
    +--- casting
    +--- directing
    +--- scripting
    +--- services
  +-- __main__.py       (entry point for program)
  +-- constants.py
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.8.0

## Authors
---
* AMERICO SADAO KUTOMI (kut22001@byui.edu)

## Main Changes
```
ball.py: new method bounce_direction_intensity - the way the racket collides to the ball changes the ball direction and ball acceleration
cast.py: new method get_second_actor - as the game works with two players, several actors work in pairs; this method returns the second actor of each group
racket.py: new attributes and methods - attribute lives; new methods swing_down, swing_up, add_life, get_lives, and lose_life
stats.py: the attributes were changed to accomodate the game score and points
collide_borders_action: as the game works in the horizontal direction, this class was dramatically changed to have balls bouncing on top and bottom, and to make the players lose lives when the ball reaches the right and left edges
collide_racket_action: the execute method has an internal function ball_collide_with_racket that will determine which behaviour the ball will have according to the way it collides to the racket
control_racket_action: it considers two players, so the keys w and s, and i and k, work for players 1 and 2 respectively
scene_manager: the class that controls the game; see all the changes in the souce code especially in _prepare_new_game, _prepare_try_again, and _prepare_game_over.

```
