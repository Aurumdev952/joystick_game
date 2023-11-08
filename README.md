<div align="center">
    <h1>Joystick game - Pong🏓</h1>
</div>

---

## description

this is a simple game made using pygame that is controlled by a joystick that is connected to arduino uno micro-controller.

## gameplay

In this game, you are controlling a player that is moving up and down across the screen, then you have to move the player so that a moving ball hits the player, that causes the ball to bounce back.

The objective is prevent the ball from getting past your player.

## Getting started

to get started, make sure you have python installed in your system and then clone this repository
```bash
git clone https://github.com/Aurumdev952/joystick_game
```
install dependencies
```bash
cd joystick_game
pip install pygame
```
after that, make sure you have arduino uno micro-controller and a joystick module
connect them according to this scheme

![scheme](/assets/scheme.png)

after that, upload the code in `joystick_game.ino` and make sure to modify the `PORT` constant in `PONG-GAME.py` according to the serial port you have connected to.

to run the game, use:
```bash
python PONG_GAME.py
```

# Known issues
different joysticks may give different values for resting positions which may lead to wierd behaviours, to fix this
open the Serial monitor and check the values being outputed, then check the second value when the joystick is in resting position, then go into `PONG_GAME.py` and modify the `BASE` constant to the value you found. That should fix that issue.


# about
this game was developed by Crash Devs.
